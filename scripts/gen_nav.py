#!/usr/bin/env python3
"""从 index.md 解析论文列表，扫描 readings/ 目录，更新 mkdocs.yml 的 nav 配置。
不依赖 pyyaml——直接用字符串操作替换 mkdocs.yml 中 nav: 以下的内容。
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.md"
READINGS = ROOT / "readings"
MKDOCS = ROOT / "mkdocs.yml"

FILE_ORDER = ["总纲.md", "故事版.md", "图表版.md"]
FILE_LABELS = {"总纲.md": "总纲", "故事版.md": "故事版", "图表版.md": "图表版"}


def parse_index():
    papers = []
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|") or "arXiv" in line or "---" in line:
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) >= 4 and cols[0] and cols[1]:
            papers.append({"id": cols[0], "title": cols[1]})
    return papers


def build_nav_yaml(papers):
    lines = ["nav:"]
    lines.append("  - 首页: index.md")
    lines.append("  - 论文笔记:")

    for paper in papers:
        pid = paper["id"]
        dir_id = pid.replace("/", ".")
        paper_dir = READINGS / dir_id
        if not paper_dir.is_dir():
            continue

        title = paper["title"]
        if len(title) > 55:
            title = title[:52] + "..."
        label = f"{pid} — {title}"
        lines.append(f'    - "{label}":')

        for fname in FILE_ORDER:
            if (paper_dir / fname).exists():
                lines.append(f"      - {FILE_LABELS[fname]}: readings/{dir_id}/{fname}")

        for f in sorted(paper_dir.glob("§*.md")):
            lines.append(f"      - 精读 {f.stem}: readings/{dir_id}/{f.name}")

    return "\n".join(lines) + "\n"


def update_mkdocs(nav_yaml):
    content = MKDOCS.read_text(encoding="utf-8")
    nav_pattern = re.compile(r"^nav:.*", re.MULTILINE | re.DOTALL)
    if nav_pattern.search(content):
        before_nav = content[:content.index("nav:")]
        content = before_nav + nav_yaml
    else:
        content = content.rstrip() + "\n\n" + nav_yaml

    MKDOCS.write_text(content, encoding="utf-8")


def main():
    papers = parse_index()
    nav_yaml = build_nav_yaml(papers)
    update_mkdocs(nav_yaml)
    count = sum(1 for p in papers if (READINGS / p["id"]).is_dir())
    print(f"Generated nav: {count} papers with readings")
    print(nav_yaml)


if __name__ == "__main__":
    main()
