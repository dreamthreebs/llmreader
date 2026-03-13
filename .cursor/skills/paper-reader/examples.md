# 使用示例

## 示例 1：逐段阅读 — 普通文本段落

### 用户输入

> 请帮我阅读这段：
>
> "The matter power spectrum P(k) describes the amplitude of density fluctuations as a function of wavenumber k. On large scales, the spectrum is nearly scale-invariant, as predicted by inflationary models. On small scales, the spectrum is suppressed due to free-streaming of neutrinos, which erases structure below the free-streaming scale."

### Agent 输出

---

#### 1. Original Text

> "The matter power spectrum P(k) describes the amplitude of density fluctuations as a function of wavenumber k. On large scales, the spectrum is nearly scale-invariant, as predicted by inflationary models. On small scales, the spectrum is suppressed due to free-streaming of neutrinos, which erases structure below the free-streaming scale."

#### 2. Literal Translation

- 物质功率谱 $P(k)$ 描述了密度涨落的振幅作为波数 $k$ 的函数。
- 在大尺度上，该谱近似标度不变（scale-invariant），正如暴胀模型（inflationary models）所预言的那样。
- 在小尺度上，由于中微子的自由流（free-streaming），该谱被抑制——自由流抹除了自由流尺度以下的结构。

#### 3. Faithful Paraphrase

- $P(k)$ 告诉我们：在不同空间尺度（用波数 $k$ 表示）上，物质密度的不均匀程度有多大。
- 在大尺度上，不同尺度的密度涨落强度几乎相同——这和暴胀理论的预言一致。
- 在小尺度上，中微子因为质量极轻、速度极快，会从密度峰值中"流出去"，把那里本该形成的结构抹掉，导致 $P(k)$ 在小尺度被压低。

#### 4. Logical Role of Each Sentence

| 句子 | 逻辑角色 | 限定词 |
|------|----------|--------|
| 第 1 句 | **definition** — 定义 $P(k)$ | — |
| 第 2 句 | **result** + **inference** — 陈述大尺度行为并引用暴胀预言 | "nearly" (nearly scale-invariant) |
| 第 3 句 | **result** + **inference** — 陈述小尺度抑制并给出物理原因 | "suppressed", "erases" |

#### 5. Physics Meaning

- **在全文中的定位**：这是介绍性段落，为后续讨论中微子质量对 $P(k)$ 的影响做铺垫。
- **物理对象**：物质密度场、中微子、密度涨落
- **物理过程**：大尺度——暴胀产生的近标度不变初始谱被保留；小尺度——中微子自由流抑制结构形成
- **控制参数**：波数 $k$（对应空间尺度 $\sim 1/k$）、中微子质量（决定自由流尺度）
- **近似**：大尺度上的"近似标度不变"隐含了慢滚暴胀的假设 **[补充]**

#### 6. Equation / Symbol Notes

| 符号 | 名称 | 物理含义 |
|------|------|----------|
| $P(k)$ | 物质功率谱 (matter power spectrum) | 密度涨落在波数 $k$ 处的方差 |
| $k$ | 波数 (wavenumber) | 空间频率，$k$ 大 = 小尺度，$k$ 小 = 大尺度 |

此处没有独立公式需要展开。

#### 7. Consistency Check

- **原文明确写出**：$P(k)$ 的定义、大尺度近标度不变、小尺度被中微子自由流抑制
- **忠实重述**：$P(k)$ 衡量不同尺度上的密度不均匀程度
- **解释性说明**：中微子"质量极轻、速度极快"是补充的背景物理；"慢滚暴胀假设"是推断
- **仍然模糊**：原文未定量给出自由流尺度的表达式

---

## 示例 2：逐式阅读 — 公式处理

### 用户输入

> 请帮我理解这个公式：
>
> $$C_\ell^{TT} = \frac{2}{\pi} \int_0^\infty k^2 dk \, |\Theta_\ell(k)|^2$$
>
> 原文说："The angular power spectrum of temperature anisotropies is obtained by integrating the square of the transfer function over all wavenumbers."

### Agent 输出

---

#### 1. Original Text

> $$C_\ell^{TT} = \frac{2}{\pi} \int_0^\infty k^2 dk \, |\Theta_\ell(k)|^2$$
>
> "The angular power spectrum of temperature anisotropies is obtained by integrating the square of the transfer function over all wavenumbers."

#### 2. Literal Translation

温度各向异性（temperature anisotropies）的角功率谱（angular power spectrum）通过对转移函数（transfer function）的平方在所有波数上积分得到。

#### 3. Faithful Paraphrase

要得到 CMB 温度涨落在天空上第 $\ell$ 个多极矩的功率，需要把所有空间尺度（波数 $k$）上的温度扰动贡献 $|\Theta_\ell(k)|^2$ 加起来（积分）。

#### 4. Logical Role

| 内容 | 逻辑角色 |
|------|----------|
| 公式本身 | **definition** — 定义 $C_\ell^{TT}$ |
| 原文说明 | **definition** 的自然语言重述 |

#### 5. Physics Meaning

- **物理对象**：CMB 温度涨落场在天球上的统计量
- **物理过程**：不同波数 $k$ 的密度扰动通过辐射转移方程演化为温度扰动 $\Theta_\ell(k)$；对所有 $k$ 求积分得到可观测量 $C_\ell^{TT}$
- **控制参数**：多极矩 $\ell$（对应天空上的角尺度 $\theta \sim \pi/\ell$）
- **作用**：这是连接理论（初始功率谱 + 转移函数）与观测（CMB 角功率谱）的桥梁公式 **[补充]**

#### 6. Equation / Symbol Notes

**原公式**：

$$C_\ell^{TT} = \frac{2}{\pi} \int_0^\infty k^2 dk \, |\Theta_\ell(k)|^2$$

**符号表**：

| 符号 | 名称 | 物理含义 |
|------|------|----------|
| $C_\ell^{TT}$ | TT 角功率谱 | CMB 温度涨落在多极矩 $\ell$ 上的方差 |
| $\ell$ | 多极矩 (multipole) | 天球上球谐展开的阶数，对应角尺度 |
| $k$ | 波数 | 三维空间中扰动的空间频率 |
| $\Theta_\ell(k)$ | 温度转移函数 | 波数 $k$ 的扰动对第 $\ell$ 阶多极矩的贡献 |
| $\frac{2}{\pi}$ | 归一化因子 | 来自三维 → 二维（天球）投影的几何因子 |

**逐项解释**：
- 左边 $C_\ell^{TT}$：我们最终想要的可观测量
- 右边 $|\Theta_\ell(k)|^2$：每个波数 $k$ 对第 $\ell$ 阶的贡献强度
- $k^2 dk$：三维空间中的体积元因子（球壳体积 $\propto k^2$）
- 积分 $\int_0^\infty$：对所有尺度求和

**数学结构**：定义式——将 $C_\ell^{TT}$ 定义为 $\Theta_\ell(k)$ 的模方在 $k$ 空间上的积分。

**原文说明**：原文只说"对转移函数的平方积分" **[原文]**。

**物理解释**：这个公式把三维空间中的扰动信息（$k$ 空间）投影到二维天球上（$\ell$ 空间），是 CMB 理论预言与观测数据之间的核心桥梁 **[补充]**。$2/\pi$ 来自球 Bessel 函数的正交归一条件 **[补充]**。

#### 7. Consistency Check

- **原文明确写出**：$C_\ell^{TT}$ 的积分表达式、"integrating the square of the transfer function over all wavenumbers"
- **忠实重述**：把所有波数的温度扰动贡献加起来
- **解释性说明**："三维到二维投影的桥梁"、"$2/\pi$ 来自球 Bessel 函数归一化"
- **仍然模糊**：原文此处未说明 $\Theta_\ell(k)$ 是否包含初始功率谱 $P_{\mathcal{R}}(k)$；不同教材约定不同
