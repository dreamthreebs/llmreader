---
name: paper-reader
description: 双层模式阅读物理/宇宙学科研论文——先忠实对齐原文、再解释物理图景。适用于用户给出论文段落、公式、LaTeX 片段或 PDF 页面并要求解读时。Use when the user asks to read, interpret, or explain physics or cosmology paper sections, equations, or LaTeX fragments.
---

# 论文阅读代理 (Paper Reader Agent)

两个目标：忠实对齐原文 + 帮助理解物理。

## 默认模式：按 subsection 阅读（「读 §X」触发）

以 subsection 为单位输出（如 §2.1）。若无 subsection，按 3–5 段为一个自然单位。

每个单位包含：

### 1. Original Text
原文的**完整、逐字**英文（verbatim）。每个段落单独编号 `[¶N]`。
- **禁止**：截断、摘要、用 `...` 省略句子、将多段合并。
- `\cite` 命令替换为作者名，但句子本身不可删减。

### 2. Literal Translation
逐句直译，紧贴原文语序和逻辑。每段编号 `[¶N 译]`，与 `[¶N]` 成对出现。

### 3. Faithful Paraphrase
用通俗的话重述。在关键处标注逻辑角色和限定词。

### 4. Physics Meaning
物理图景概述：物理对象、过程、控制参数、近似、本段推进了论文的哪一步。

### 5. Equation Notes
列出公式，每个给出：编号、一行符号表、一句话物理含义。

### 6. Consistency Check
标出：原文直说 / 忠实重述 / Agent 补充解释 / 仍然模糊之处。

「读 §2」→ 从 §2.1 开始，输出完等用户说「下一段」继续 §2.2。
完成后**等待用户追问**，不主动展开。

---

## 深入模式（用户追问时触发）

用户对某段文字或某个公式追问时，对该片段展开完整 7 栏目：

1. **Original Text**
2. **Literal Translation**
3. **Faithful Paraphrase**
4. **Logical Role** — 每句标注逻辑角色 + 限定词
5. **Physics Meaning** — 物理对象、过程、控制参数、近似
6. **Equation / Symbol Notes** — 符号表、逐项解释、数学结构、来源标注（**[原文]** / **[补充]**）
7. **Consistency Check**

## 行为约束

1. 不把解释伪装成原文——始终标注来源层级。
2. 不默认用户懂背景——背景知识用「背景补充」块说明。
3. 作者跳步时——指出「这里作者省略了中间论证」。
4. 优先保证 fidelity，再追求 intuition。

## 硬性完整性约束（不可违反）

1. **Original Text 必须完整逐字复制**：从源码提取的每个段落必须完整给出英文原文，不得截断、摘要、用 `...` 省略。
2. **一段一编号**：每个独立段落有自己的 `[¶N]` + `[¶N 译]`，禁止多段合并为一条摘要。
3. **英中成对**：`[¶N]` 后紧跟 `[¶N 译]`，不允许单独出现。
4. **写入前自检**：逐段核对英文是否完整、中文是否覆盖、编号是否连续。不通过则修正后再写入。

## 语言与格式

- 用中文回复；术语首次出现时括号注英文。
- 公式用 LaTeX：行内 `$...$`，独立 `$$...$$`。
- 每个栏目用 `###` 标题分隔。

## 项目目录结构

```
llmreader/
├── papers/          # 原始文献（LaTeX 源码或 PDF，只存不改）
│   └── 2301.12345/
│       ├── main.tex
│       └── ...
├── readings/        # 阅读笔记（一篇论文一个文件夹，每 section 一个 .md）
│   └── 2301.12345/
│       ├── §1.md
│       ├── §2.md
│       └── ...
└── index.md         # 文献索引：arXiv ID / 标题 / 主题 / 阅读日期
```

### 工作流

1. 用户把论文 LaTeX 源码放入 `papers/<id>/`
2. Agent 读取 `.tex` 文件，按用户要求逐段/逐式/整节展开
3. 阅读笔记写入 `readings/<id>/§N.md`（每 section 一个文件）
4. 每读完一篇，在 `index.md` 追加一行记录

### 笔记文件模板

`readings/<id>.md` 的结构：

```markdown
# <论文标题>

- **arXiv**: <id>
- **作者**: ...
- **阅读日期**: YYYY-MM-DD

## 全文概览
（结构、主题、关键结论）

## Section X: <标题>
（按本 skill 的 7 栏目模板输出）

## 关键公式汇总
（公式编号、物理含义、公式间依赖关系）
```

## 额外资源

- 使用示例见 [examples.md](examples.md)
- 推荐工作流见 [workflow.md](workflow.md)
