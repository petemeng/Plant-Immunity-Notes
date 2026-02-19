<div class="book-chapter" markdown="1">

<header class="book-header">
  <div class="book-part">第二部分 · 分子机制</div>
  <div class="book-no">04</div>
  <h1 class="book-title">NLR 与抗病小体</h1>
  <p class="book-subtitle">从细胞内受体到抗病小体：植物如何把效应子识别转化为强免疫输出</p>
</header>

<nav class="book-toc" markdown="1">
### 本章目录

1. 引言
2. NLR 的分类与结构逻辑
3. 从静息到激活：NLR 的开关机制
4. ZAR1 抗病小体：结构生物学里程碑
5. TNL 通路：NADase 与 EDS1 枢纽
6. NLR 网络：sensor 与 helper 的分工
7. 当前争论与未解问题
8. 关键实验方法 Box
9. 推荐阅读
</nav>

## <span class="sec-num">4.1</span>引言

当病原效应子成功进入细胞内部后，植物需要一个比 PTI 更高灵敏度的监测系统。这个系统就是 NLR（Nucleotide-binding Leucine-rich Repeat receptor）家族。NLR 的关键价值不只是“能识别效应子”，而是它把“识别事件”直接转化为“执行事件”：从分子构象变化到免疫输出，链条极短、反应极快。

在过去很长时间里，领域对 NLR 的理解停留在遗传层面：知道它重要，但不知道它如何工作。抗病小体结构被解析后，这个问题第一次有了分子级答案。

## <span class="sec-num">4.2</span>NLR 的分类与结构逻辑

按 N 端结构域，植物 NLR 常分为三类：

| 类型 | N 端结构域 | 常见角色 | 代表性特征 |
|---|---|---|---|
| CNL | CC | sensor 或 executor | 常与成孔执行相关 |
| TNL | TIR | 识别与信号放大 | TIR 结构域具 NADase 活性 |
| RNL | RPW8-like | helper/executor | 常在下游执行死亡与防御 |

三类 NLR 通常共享 NB-ARC + LRR 主体结构。可以把它理解为：

- `LRR` 提供识别与约束
- `NB-ARC` 充当 ATP/ADP 依赖的分子开关
- `N 端结构域` 决定“激活后怎么输出”

这种“识别-开关-执行”模块化架构，是 NLR 高可塑性与高风险并存的根本原因：一旦误激活，代价往往是细胞死亡。

## <span class="sec-num">4.3</span>从静息到激活：NLR 的开关机制

NLR 的激活不是线性的“开/关”，而是一系列受约束的状态转移：

<ol class="mechanism-steps">
  <li><strong>静息自抑制：</strong>LRR 与 NB-ARC 协同维持闭合构象，通常以 ADP 结合态稳定存在。</li>
  <li><strong>危险触发：</strong>效应子被直接识别，或其对宿主蛋白的修饰被间接感知。</li>
  <li><strong>核苷酸交换：</strong>NB-ARC 由 ADP 态转入 ATP 态，触发构象重排。</li>
  <li><strong>寡聚组装：</strong>激活态单体组装为抗病小体，形成新的功能界面。</li>
  <li><strong>功能输出：</strong>成孔、离子通量变化、转录放大和细胞死亡等响应被执行。</li>
</ol>

关键点在于：NLR 不只是受体，它在很多情况下是“受体 + 执行器”的一体化分子机器。

## <span class="sec-num">4.4</span>ZAR1 抗病小体：结构生物学里程碑

2019 年 ZAR1 抗病小体结构解析是领域分水岭。此前主流猜测是 NLR 激活后再招募下游执行因子；结构与功能数据表明，至少在 CNL 系统中，NLR 复合体本身就可承担关键执行功能。

<div class="box box-cognition" markdown="1">
<div class="box-title">认知修正</div>

旧认知：NLR 主要是“信号开关”，执行依赖更下游的未知蛋白。  
新认知：部分 NLR 抗病小体本身可直接形成膜相关执行结构，离子通量变化是早期关键事件。
</div>

这类工作的方法学启示也非常清晰：

- 先重构可控复合体（解决“看不见”的问题）
- 再用结构抓状态（静息、中间、激活）
- 最后用功能实验闭环（成孔/离子流/表型）

这套思路是后续 NLR 研究最值得复用的范式。

## <span class="sec-num">4.5</span>TNL 通路：NADase 与 EDS1 枢纽

TNL 的输出路线与 CNL 不同。TIR 结构域的 NADase 活性发现后，TNL 通路从“结构域推测”进入“生化可测”时代：

- TNL 激活后产生小分子信号
- EDS1 复合体（与 PAD4/SAG101）负责信号分流与放大
- NRG1/ADR1 等 helper NLR 在下游执行

这意味着 ETI 不是单一路径，而是多条执行模块的耦合系统。研究上要避免把“某个 NLR 结果”误认为“所有 NLR 共同机制”。

## <span class="sec-num">4.6</span>NLR 网络：sensor 与 helper 的分工

当前更实用的框架是网络视角：

- `sensor NLR` 负责识别特异效应子
- `helper NLR` 负责通用执行与放大

这种分工带来两个优势：

1. 识别端可快速进化，应对病原变化
2. 执行端相对保守，保证输出稳定

但它也带来复杂性：一个 helper 可能连接多个 sensor，网络交叉会显著影响表型解释。

## <span class="sec-num">4.7</span>当前争论与未解问题

<ul class="questions-list">
  <li><strong>执行机制是否统一？</strong>不同 NLR 抗病小体是否都通过相似离子机制输出，仍缺跨家族系统比较。</li>
  <li><strong>死亡与抗性是否可解耦？</strong>能否实现“高抗性、低代价”的非致死输出，是应用转化关键问题。</li>
  <li><strong>网络拓扑如何决定抗病谱？</strong>sensor-helper 连接关系是否决定抗病广谱性，仍缺定量框架。</li>
  <li><strong>环境因子如何改写 NLR 输出？</strong>温度、发育阶段、代谢状态对 ETI 强度的调制机制仍不清晰。</li>
</ul>

## <span class="sec-num">4.8</span>关键实验方法 Box

<div class="box box-experiment" markdown="1">
<div class="box-title">标准证据链（NLR 研究）</div>

1. **遗传证据**：突变体、互补、等位变体比较。  
2. **生化证据**：互作、寡聚状态、酶活或修饰状态。  
3. **结构证据**：关键状态结构（优先静息与激活对照）。  
4. **功能证据**：病原增殖、HR/电解质渗漏、离子信号读数。  
5. **边界验证**：跨背景、跨条件、跨病原验证可重复性。
</div>

常用方法组合：

- Cryo-EM（状态结构）
- Co-IP/BN-PAGE（复合体组装）
- NADase assay（TNL 通路）
- ROS/离子通量/HR 表型（功能终点）

## <span class="sec-num">4.9</span>推荐阅读

<div class="reading-level level-essential" markdown="1">
#### 必读

<div class="reading-item">
  <div>
    <strong>Wang J et al.</strong> Reconstitution and structure of a plant NLR resistosome conferring immunity. <em>Science</em> (2019). DOI: https://doi.org/10.1126/science.aav5870
  </div>
  <div class="reading-reason">首个高影响力抗病小体结构工作，奠定本章核心机制。</div>
</div>

<div class="reading-item">
  <div>
    <strong>Horsefield S et al.</strong> NAD+ cleavage activity by plant TIR domains. <em>Science</em> (2019).
  </div>
  <div class="reading-reason">TNL 通路生化机制转折点。</div>
</div>
</div>

<div class="reading-level level-important" markdown="1">
#### 重要

<div class="reading-item">
  <div>
    <strong>Adachi H et al.</strong> NLR singletons, pairs, and networks. <em>Current Opinion in Plant Biology</em> (2019).
  </div>
  <div class="reading-reason">理解 sensor-helper 网络组织的入口综述。</div>
</div>

<div class="reading-item">
  <div>
    <strong>Dongus JA, Parker JE.</strong> EDS1 signalling at the nexus of immunity. <em>Current Opinion in Plant Biology</em> (2021).
  </div>
  <div class="reading-reason">TNL-EDS1 轴系统梳理，适合和结构论文配套阅读。</div>
</div>
</div>

</div>
