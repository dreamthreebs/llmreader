# Paper Reader — Cursor AI Skill for Reading Research Papers

一个 [Cursor](https://cursor.com) Agent Skill，让 AI 帮你**逐段精读**科研论文。

核心理念：**Fidelity first, intuition second** —— 先忠实对齐原文，再解释物理图景。不跳步、不瞎编、不把 AI 的猜测伪装成原文意思。

## 解决什么问题

读论文时 AI 最常见的毛病：

- 直接给你一段"总结"，跳过了原文到底说了什么
- 把自己补充的背景知识和原文说的东西混在一起
- 公式只给符号表，不解释"作者为什么要这么写"
- 翻译把 "suggests" 译成 "证明"，悄悄加强了语气

Paper Reader 用**结构化的双层阅读**解决这些问题——每一段都强制输出原文、直译、重述、物理含义、公式笔记、一致性检查，并且每句解释都标注来源（`[原文]` / `[重述]` / `[补充]`）。

## 安装

把 `.cursor/skills/paper-reader/` 文件夹复制到你的项目中，就能用了。

```bash
# 方法 1：直接 clone 然后复制
git clone https://github.com/<your-username>/llmreader.git
cp -r llmreader/.cursor/skills/paper-reader your-project/.cursor/skills/

# 方法 2：只复制 skill 文件夹到全局（所有项目可用）
cp -r llmreader/.cursor/skills/paper-reader ~/.cursor/skills/
```

首次使用时，Agent 会问你两件事：

1. **输入格式** — LaTeX 源码（推荐）还是 PDF？
2. **文件存放在哪** — 论文和笔记放哪个目录？

回答完就开始工作。

## 30 秒上手

```
1. 把论文 LaTeX 源码放进项目（或直接给 arXiv 链接）
2. 说「先读」→ Agent 自动生成 总纲 + 故事版 + 图表版
3. 对感兴趣的章节说「读 §2」→ 逐段精读
4. 不懂就追问 → Agent 把解答写进笔记
```

## 口令速查

### 拿到新论文时

| 口令 | 做什么 |
|------|--------|
| **先读** / **新论文** | 一次性生成：总纲 → 故事版 → 图表版 |
| **写总纲** | 只写五问总纲 |
| **写故事版** | 只写通俗叙事版 |
| **写图表版** | 只写逐图解读版 |

### 深入精读时

| 口令 | 做什么 |
|------|--------|
| **读 §X** | 按 subsection 精读，每次一个 subsection |
| **下一段** | 继续读当前 section 的下一个 subsection |
| **读公式 (X)** | 精读某个公式：动机 + 符号表 + 逐项解释 |
| **鸟瞰 §X** | 快速概览某节的结构、假设、结论（不逐句） |

### 理解和思考时

| 口令 | 做什么 |
|------|--------|
| **追问** | 对刚读的内容追问，Agent 把解答写进笔记 |
| **串联公式** | 把关键公式串联，梳理推导依赖链 |
| **回顾** | 总结最近读过内容的逻辑推进线 |
| **批判** | 审视假设和近似，找作者跳步的地方 |

### 质量控制

| 口令 | 做什么 |
|------|--------|
| **检查 §X** | 回到源文件逐段核对：原文完整性、翻译忠实度、物理正确性、来源标注 |
| **检查总纲** | 校验总纲中的物理陈述和关键数字 |
| **检查图表版** | 校验图表版中的图片描述和物理解释 |

## 输出示例

### 精读笔记（`读 §2` 输出的内容）

> **[¶2]** The optical depth to Thomson scattering along a direction $\hat{\boldsymbol{\gamma}}$ in the sky is given by
>
> $$\tau(\hat{\boldsymbol{\gamma}}) = \int d\chi\, g(z)\left[1 + \delta_e(\chi\hat{\boldsymbol{\gamma}})\right]$$
>
> where $\delta_e$ is the electron density contrast...
>
> **[¶2 译]** 沿天空方向 $\hat{\boldsymbol{\gamma}}$ 的 Thomson 散射光学深度由下式给出：
>
> $$\tau(\hat{\boldsymbol{\gamma}}) = \int d\chi\, g(z)\left[1 + \delta_e(\chi\hat{\boldsymbol{\gamma}})\right]$$
>
> 其中 $\delta_e$ 是电子密度对比度（density contrast）...
>
> **Faithful Paraphrase**: 这个积分做的事情是：沿一条视线，把每个位置"那里有多少自由电子"乘以"光子路过时被散射的概率"加起来。
>
> **Equation Notes**:
> - **动机**：把光子沿视线经过的所有 Thomson 散射事件累积起来，得到总光学深度
> - **符号**: $g(z)$ = 可见度函数，$\delta_e$ = 电子密度对比度，$\chi$ = 共动距离
>
> **Consistency Check**: 公式 [原文]；"把散射事件累积"的直觉解释 [补充]

### 总纲（`写总纲` 输出的内容）

> **一句话版**：什么星系驱动了宇宙再电离，再电离过程持续了多久？
>
> **核心想法**：联合使用三种互补数据集（21-cm 功率谱上限、Lyman 线观测、CMB 功率谱），在完全边缘化 $f_\mathrm{esc}$ 的贝叶斯框架下进行推断，消除了以往因 $f_\mathrm{esc}$ 假设差异导致的系统偏差。

实际产出的完整笔记见 [`readings/`](readings/) 目录。

## 四层笔记体系

每篇论文产生四层文件，从 5 分钟快速回忆到按需深入：

| 文件 | 定位 | 阅读时间 | 适合场景 |
|------|------|---------|---------|
| **总纲.md** | 问题 → 想法 → 结论 | 5 min | 快速回忆、给别人讲论文 |
| **故事版.md** | 物理图景 | 20 min | 从零建立直觉 |
| **图表版.md** | 证据链条 | 30 min | 对着图理解论证 |
| **§N.md** | 公式推导 + 追问 | 按需 | 深入某节细节 |

## 推荐工作流

### 快速通读（1 小时了解一篇论文）

```
给链接 → 「先读」
  ↓
读 总纲.md（5 min）→ 知道论文在解决什么、核心想法是什么
  ↓
读 故事版.md（20 min）→ 建立物理直觉
  ↓
读 图表版.md（30 min）→ 对着图理解每个论证
  ↓
哪里不懂 → 追问 / 读 §X 深入
```

### 深入精读

```
快速通读之后 →
  ↓
读 §2（核心方法和公式）→ 读 §3（数值结果）→ ...
  ↓
串联公式 → 梳理推导链
  ↓
批判 → 审视假设和近似
  ↓
检查 → 确保笔记准确
```

## 默认目录结构

```
your-project/
├── papers/<id>/              # 原始文献（建议 gitignore）
│   ├── main.tex / paper.pdf
│   └── figures/
├── readings/<id>/            # 阅读笔记
│   ├── 总纲.md
│   ├── 故事版.md
│   ├── 图表版.md
│   ├── §1.md, §2.md, ...
│   └── ...
├── index.md                  # 文献索引
└── .cursor/skills/
    └── paper-reader/         # ← 就是这个 skill
        ├── SKILL.md
        ├── workflow.md
        └── examples.md
```

目录名可自定义——首次使用时 Agent 会问你。

## 自定义

如果你想为特定项目固定目录配置（不用每次被问），在 `.cursor/rules/` 下创建一个 workspace rule：

```markdown
---
description: 本项目的论文阅读目录约定
alwaysApply: false
---

## 输入源
本项目以 LaTeX 源码为主要输入。论文源码已存放在 `papers/<id>/` 中。

## 目录结构
- 原始文献：`papers/<id>/`
- 阅读笔记：`readings/<id>/`
- 文献索引：`index.md`
```

## FAQ

**Q: 只能读物理/宇宙学论文吗？**

A: 不是。skill 的核心方法论（双层阅读、来源标注、公式处理）适用于任何有公式的科研论文。物理/宇宙学的示例只是因为作者本人的研究方向。

**Q: 必须要 LaTeX 源码吗？**

A: 推荐但不强制。PDF 也能用，但公式提取质量会下降。大多数 arXiv 论文可在页面点 "Other formats → Download source" 获取源码。

**Q: 图表版的图片显示不了？**

A: `papers/` 目录建议加入 `.gitignore`（文件太大）。图表版的文字解说是自包含的，没有图也能看懂。想看图的话，下载论文源码，把 PDF 图转成 PNG 即可：

```bash
cd papers/<id>/figures
for f in *.pdf; do magick "$f" -resize '800x800>' -quality 85 "${f%.pdf}.png"; done
```

**Q: 笔记语言可以改吗？**

A: 目前默认中文输出。如果需要改为英文或其他语言，修改 `SKILL.md` 中「格式约定」部分的语言设置即可。

## GitHub Pages（MkDocs 站点）

仓库根目录的 `readings/*.md` 里常有 LaTeX 的 `{{ ... }}`，**不能**让 GitHub Pages 用 Jekyll 去「从 main 根目录构建站点」，否则会报 Liquid 语法错误。

正确做法：

1. 推送 `main` 后，等待 **Actions** 里 **Deploy to GitHub Pages** 跑完；它会用 MkDocs 生成静态站并推到 **`gh-pages`** 分支。
2. 打开 **Settings → Pages → Build and deployment**：
   - **Source** 选 **Deploy from a branch**（不要用 main 当站点根）。
   - **Branch** 选 **`gh-pages`**，目录选 **`/ (root)`**。

若仍看到 `jekyll-theme-primer`、`Rendering: readings/...` 的日志，说明 Pages 仍在从 **main** 跑 Jekyll；请按上面把分支改成 **`gh-pages`**。

## License

MIT
