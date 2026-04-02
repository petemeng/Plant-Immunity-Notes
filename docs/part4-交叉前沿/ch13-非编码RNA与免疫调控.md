<div class="page-wrapper">

  <div class="breadcrumb"><a href="#">首页</a><span>›</span><a href="#">第四部分 · 交叉前沿</a><span>›</span>第13章</div>

  <header class="chapter-header"><div class="chapter-header-inner">
      <div class="chapter-number">13</div>
      <div class="chapter-part">第四部分 · 交叉前沿</div>
      <h1 class="chapter-title">非编码 RNA 与免疫调控</h1>
      <p class="chapter-subtitle">超越经典的"基因→蛋白"框架，非编码 RNA 是免疫调控中日益重要的一层</p>
    </div></header>

  <nav class="chapter-toc"><h3>本章目录</h3><ol>
      <li>RNA 沉默作为抗病毒免疫的核心机制</li>
      <li>miRNA 在免疫调控中的角色</li>
      <li>lncRNA 与免疫的新关联</li>
      <li>跨界 RNA 转移（cross-kingdom RNAi）</li>
      <li>表观遗传学与免疫记忆</li>
      <li>里程碑研究思路拆解</li><li>当前争论与未解问题</li><li>关键实验方法</li><li>推荐阅读</li>
    </ol></nav>

  <!-- ======== 引言 ======== -->
  <div class="chapter-intro">
  <p>前面各章描述的免疫信号通路——从 PRR 和 NLR 的识别，到激酶级联和激素网络的信号传递，再到转录因子驱动的基因表达——遵循的是经典的"蛋白质中心"逻辑。但在这个蛋白质构成的信号骨架之下，还潜伏着一个庞大而精密的调控层：<strong>非编码 RNA（non-coding RNA, ncRNA）</strong>。</p>

  <p>这个调控层的重要性最初在抗病毒免疫中被认识——RNA 沉默是植物对抗 RNA 病毒的最核心防线 <span class="cross-ref">→ 第1章 1.1节</span>。但随着研究的深入，ncRNA 的角色已远远超出了抗病毒：<strong>内源 miRNA 通过精确调节免疫受体和信号蛋白的表达水平来微调免疫系统的"灵敏度"，lncRNA 通过影响染色质状态参与免疫记忆的建立，而跨界 RNA 转移更将植物-病原的信息战从蛋白质层面扩展到了 RNA 层面</strong>。</p>

  <p>理解 ncRNA 在免疫中的角色，不仅补全了免疫调控的分子图景，还为开发新一代抗病策略（如 RNAi 介导的抗病和 HIGS）提供了全新的工具箱。本章将从 RNA 沉默的抗病毒核心功能出发，依次展开内源小 RNA、lncRNA 和跨界 RNA 转移的免疫调控逻辑，最后讨论表观遗传学与免疫记忆的 RNA 维度。</p>
  </div>

  <!-- ======== 13.1 RNA 沉默与抗病毒 ======== -->
  <h2><span class="section-num">13.1</span>RNA 沉默作为抗病毒免疫的核心机制</h2>

  <h3>认知演变</h3>
  <div class="box box-cognition"><div class="box-title">认知修正</div>
  <p><strong>过去：</strong>RNA 沉默最初被视为实验室中的基因工具或转座子控制机制，与免疫关系不大。<br><strong>转折：</strong>2000年代初，多项研究证明 RNA 沉默是植物抗病毒免疫的主要机制——几乎所有植物病毒都编码 RNA 沉默抑制子（VSR）这一事实，从反面证明了沉默路径的防御重要性。<br><strong>现在：</strong>RNA 沉默被认为是与 PTI/ETI 平行的第三大免疫层——尤其对 RNA 病毒，它比 NLR 介导的免疫更为普遍和基础。</p></div>

  <h3>抗病毒 RNA 沉默的分子机制</h3>
  <p>当 RNA 病毒在宿主细胞中复制时，其 RNA 依赖的 RNA 聚合酶（RdRP）产生的双链 RNA（dsRNA）复制中间体被宿主 Dicer-like（DCL）蛋白识别并切割为21-24 nt 的小干扰 RNA（virus-derived siRNA, vsiRNA）。这些 vsiRNA 被装载入 Argonaute（AGO）蛋白，形成 RNA 诱导沉默复合体（RISC），通过碱基互补配对靶向降解病毒 RNA (Ding & Voinnet, 2007)。</p>

  <p>这个系统的精妙之处在于其<strong>自放大特性</strong>：宿主的 RDR（RNA-Dependent RNA Polymerase，如 RDR6）以初级 siRNA 引导的切割产物为模板，合成新的 dsRNA，产生"次级 siRNA"——形成正反馈环路，大幅放大沉默信号。更重要的是，沉默信号可以通过胞间连丝在细胞间移动，并通过韧皮部实现全株性传播——为病毒还未到达的远端组织预先建立防御 (Melnyk et al., 2011)。</p>

  <h3>病毒的反制：RNA 沉默抑制子（VSR）</h3>
  <p>面对如此强力的沉默防线，病毒的进化回应是"以牙还牙"——<strong>几乎所有已知的植物病毒都编码至少一种 VSR</strong>。不同病毒的 VSR 在结构上高度多样（暗示独立进化起源），但在功能上趋同——它们靶向沉默通路的不同步骤：</p>
  <ul>
    <li><strong>dsRNA 结合：</strong>如番茄丛矮病毒（TBSV）的 P19 形成同源二聚体，以尺寸特异性方式结合21 nt 的 siRNA 双链体，阻止其装载入 AGO (Vargason et al., 2003)。P19 是第一个被解析晶体结构的 VSR，其与 siRNA 的共结晶是理解 VSR 作用机制的里程碑。</li>
    <li><strong>AGO 降解：</strong>如豇豆花叶病毒（CMV）的 2b 蛋白直接与 AGO1 互作并抑制其切割活性。</li>
    <li><strong>甲基化抑制：</strong>如马铃薯 Y 病毒（PVY）的 HcPro 干扰 HEN1 对 siRNA 3' 端的甲基化修饰，导致 siRNA 不稳定而降解。</li>
  </ul>

  <p>VSR 的存在创造了一种持续的分子军备竞赛——与效应子-NLR 的博弈遥相呼应 <span class="cross-ref">→ 第7章</span>。值得注意的是，一些 NLR 蛋白已被证明能直接识别 VSR（如烟草的 N 蛋白识别 TMV 的解旋酶/VSR 功能域），将 RNA 沉默防线与 ETI 防线在分子层面连接起来 <span class="cross-ref">→ 第4章</span>。</p>

  [图 13.1 抗病毒 RNA 沉默通路与 VSR 靶点示意图]

  <!-- ======== 13.2 miRNA 与免疫 ======== -->
  <h2><span class="section-num">13.2</span>miRNA 在免疫调控中的角色</h2>

  <h3>miRNA 介导的免疫增益控制</h3>
  <p>与外源 siRNA 不同，miRNA 是植物基因组自身编码的调控分子。MIR 基因转录产生前体 RNA，经 DCL1 加工为成熟 miRNA（通常21 nt），装载入 AGO1 后以碱基互补方式切割或翻译抑制靶标 mRNA。关键在于：<strong>多个 miRNA 家族的靶标恰好是免疫信号通路的核心组分</strong>——这使得 miRNA 成为免疫系统"增益"（gain）的精密调节器。</p>

  <p>最具代表性的免疫相关 miRNA 包括：</p>
  <ul>
    <li><strong>miR393——最早被鉴定的"免疫 miRNA"：</strong>Navarro et al. (2006) 在 <em>Science</em> 上报道，flg22 处理诱导 miR393 的积累，miR393 靶向降解生长素受体 TIR1/AFB 的 mRNA。由于生长素信号促进易感性（生长素促进细菌毒力基因表达），miR393 通过抑制生长素信号来间接增强免疫——这是<strong>第一个将 miRNA 与植物免疫直接连接的发现</strong>，也是生长素-免疫拮抗的重要分子机制 <span class="cross-ref">→ 第5章 5.4节</span>。</li>
    <li><strong>miR482/miR2118——NLR 表达的"刹车"：</strong>这两个 miRNA 家族靶向多种 NLR 基因的 mRNA，在非胁迫条件下维持 NLR 的低水平表达。当病原入侵触发免疫后，miR482/2118 的表达被下调，从而"释放"NLR 的表达上限——实现NLR 库的动态调控 (Shivaprasad et al., 2012; Zhai et al., 2011)。这种设计逻辑精妙而合理：NLR 的组成性高表达会导致自身免疫代价 <span class="cross-ref">→ 第11章</span>，miRNA 提供了一种低成本的"按需激活"机制。</li>
    <li><strong>miR160/miR167——生长素响应因子的调控：</strong>这两个 miRNA 家族靶向 ARF（Auxin Response Factor）家族成员，通过调节生长素信号通路间接影响免疫-生长平衡。</li>
    <li><strong>miR472——NLR 的精确制导：</strong>在拟南芥中，miR472 靶向 CC-NLR 亚家族的多个成员，参与 RDR6 依赖的次级 siRNA（phasiRNA）产生，形成"miRNA-phasiRNA"级联，对 NLR 转录本进行分层调控 (Boccara et al., 2014)。</li>
  </ul>

  <h3>miRNA 调控的系统逻辑</h3>
  <p>从系统生物学的角度看，miRNA 对免疫的调控不是简单的"开关"，而是一种<strong>网络级的"增益控制"（gain control）</strong>：</p>
  <ol class="mechanism-steps">
    <li><strong>基线设定：</strong>在非胁迫条件下，免疫相关 miRNA 维持靶标基因的低表达水平，避免不必要的免疫激活和生长代价。</li>
    <li><strong>快速解除抑制：</strong>病原信号（如 PAMP 识别）触发特定 miRNA 的下调，释放靶标基因的表达——这种"去抑制"比从头转录更快，能在分钟至小时级别改变蛋白质组。</li>
    <li><strong>时序精度：</strong>不同 miRNA 对病原信号的响应时序不同，使得免疫通路的各个节点按照特定的时间序列被依次"解锁"——先激活早期识别组分，再释放下游效应模块。</li>
    <li><strong>恢复抑制：</strong>病原被清除后，miRNA 表达恢复，重新建立靶标基因的低表达基线——完成免疫应答的"关闭"。</li>
  </ol>

  <p>这种设计的核心优势在于<strong>可逆性和低代价</strong>——与表观遗传修饰或蛋白质降解相比，miRNA 介导的 mRNA 切割提供了一种快速、可逆、且能量消耗较低的调控方式。这可能解释了为什么进化选择了 miRNA 而非转录因子来承担免疫系统"增益旋钮"的角色——当需要频繁的上下调节时，miRNA 通路的效率优势尤为明显。</p>

  <!-- ======== 13.3 lncRNA ======== -->
  <h2><span class="section-num">13.3</span>lncRNA 与免疫的新关联</h2>

  <p>长链非编码 RNA（lncRNA，>200 nt）是一个庞大但功能大部分未知的 RNA 类别。在动物免疫学中，lncRNA 的角色已被广泛研究（如 NEAT1、MALAT1 等），但在植物免疫中，这一领域仍处于早期阶段。</p>

  <h3>已知的免疫相关 lncRNA</h3>
  <p>尽管功能验证的案例有限，已有若干 lncRNA 被证明参与植物免疫调控：</p>
  <ul>
    <li><strong>ELENA1（ELF18-INDUCED LONG-NONCODING RNA 1）：</strong>这是拟南芥中研究最深入的免疫 lncRNA。ELENA1 被 elf18（EF-Tu 受体 EFR 的配体）诱导，与 MED19a（Mediator 复合体亚基）互作，增强 PR1 等防御基因的转录。<em>elena1</em> 敲除突变体对 <em>Pst</em> DC3000 更敏感 (Seo et al., 2017)。</li>
    <li><strong>ALEX1：</strong>在水稻中鉴定的一个 lncRNA，参与 JA 信号通路的调节，影响对稻瘟菌的抗性 (Yu et al., 2020)。</li>
    <li><strong>天然反义转录本（NAT）：</strong>多个免疫相关基因座被发现有反义 lncRNA 的转录。这些 NAT 可以通过 RNA-RNA 互作调节正义链的稳定性或翻译效率，为免疫基因的表达增加了一层精细调控。</li>
  </ul>

  <h3>lncRNA 与免疫记忆</h3>
  <p>lncRNA 在免疫中可能最重要的角色不是急性防御反应，而是<strong>免疫记忆的建立和维持</strong>。多条线索将 lncRNA 与 priming 和跨代免疫联系起来：</p>
  <ul>
    <li>lncRNA 可以作为"导引"将染色质修饰复合体（如 PRC2 或 COMPASS）引导到特定基因组位点，建立特异性的组蛋白修饰标记。在免疫 priming 中，防御基因启动子区域的 H3K4me3 修饰被增强但基因不被完全激活——lncRNA 可能参与这种"预设"标记的建立 <span class="cross-ref">→ 第11章</span>。</li>
    <li>在拟南芥中，SA 处理后某些基因座的 lncRNA 表达与 DNA 甲基化变化相关联——暗示 lncRNA 可能参与 RNA 指导的 DNA 甲基化（RdDM）通路与免疫信号的交叉 (Huang et al., 2021)。</li>
  </ul>

  <p>然而，必须坦率承认：<strong>目前 lncRNA 在植物免疫中的因果性证据仍然薄弱</strong>。大多数研究停留在"转录组中鉴定到差异表达的 lncRNA"的相关性层面，缺乏系统的功能验证。将 lncRNA 从"相关因子"提升为"因果调控者"，需要结合基因编辑（CRISPR 敲除/敲入 lncRNA 基因座）、结构域缺失分析和蛋白质互作组学等多种手段——这是当前研究的主要瓶颈。</p>

  <!-- ======== 13.4 跨界 RNA ======== -->
  <h2><span class="section-num">13.4</span>跨界 RNA 转移（cross-kingdom RNAi）</h2>

  <p>如果说 miRNA 和 lncRNA 代表了免疫调控的"内部事务"，那么跨界 RNA 转移（cross-kingdom RNAi）则将 RNA 的角色扩展到了<strong>植物-病原之间的"信息战"</strong>。</p>

  <h3>病原→宿主方向：RNA 劫持</h3>
  <p>2013年，Weiberg et al. 在 <em>Science</em> 上发表了一项改变认知的发现：灰霉菌 <em>Botrytis cinerea</em> 产生的小 RNA（Bc-siRNA）可以进入拟南芥和番茄细胞，<strong>劫持宿主的 AGO1</strong>，靶向沉默宿主的免疫基因（包括 MAPK 通路的成员）。这一发现意味着：</p>
  <ul>
    <li>病原的"武器库"不仅包括效应蛋白，还包括小 RNA——后者可以精准、低成本地压制宿主防御。</li>
    <li>宿主的 RNA 沉默机器（特别是 AGO 蛋白）既是防御工具，也可能成为被病原利用的"后门"。</li>
  </ul>

  <p>Wang et al. (2017) 进一步鉴定了一个具体的 <em>B. cinerea</em> 小 RNA——Bc-siR37，它靶向拟南芥的 WRKY7、PMR6 和 FEI2 等多个防御基因。在 <em>ago1</em> 突变体中，Bc-siR37 的免疫抑制效应消失，证实了 AGO1 在跨界沉默中的必要角色。</p>

  <h3>宿主→病原方向：RNA 反击</h3>
  <p>如果病原能用小 RNA 攻击宿主，植物是否也能"以其人之道还治其人之身"？2016年和2018年的两项关键研究给出了肯定答案：</p>
  <ul>
    <li><strong>Zhang et al. (2016)：</strong>发现棉花产生的 miRNA（miR166 和 miR159）可以被转运到寄生的 <em>Verticillium dahliae</em> 真菌中，靶向沉默其毒力相关基因（如 Ca²⁺ 依赖的 cysteine protease 基因 Clp-1），降低病原的致病力。</li>
    <li><strong>Cai et al. (2018)：</strong>更进一步揭示了传递机制——拟南芥通过分泌<strong>胞外囊泡（extracellular vesicles, EVs）</strong>将含有 siRNA 的货物运送到 <em>B. cinerea</em> 感染位点。这些囊泡富含 TET8（一种四跨膜蛋白）和多种靶向 <em>B. cinerea</em> 毒力基因的 siRNA。<em>tet8</em> 突变体的囊泡分泌减少，对 <em>B. cinerea</em> 也更敏感。</li>
  </ul>

  <p>这些发现开辟了一个全新的应用方向：<strong>宿主诱导基因沉默（Host-Induced Gene Silencing, HIGS）</strong>——在转基因植物中表达靶向病原关键基因的 dsRNA/miRNA，使植物成为持续的 RNA "武器工厂"。HIGS 已在多种病理系统中展示了原理验证，包括抗真菌、抗卵菌和抗线虫 <span class="cross-ref">→ 第14章</span>。</p>

  [图 13.2 跨界 RNA 转移的双向机制——病原 RNA 劫持 vs 宿主 RNA 反击]

  <!-- ======== 13.5 表观遗传学 ======== -->
  <h2><span class="section-num">13.5</span>表观遗传学与免疫记忆</h2>

  <p>ncRNA 与免疫的交叉不止于急性调控——<strong>RNA 指导的表观遗传修饰可能是免疫记忆（priming）的分子基础之一</strong>。</p>

  <h3>RNA 指导的 DNA 甲基化（RdDM）与免疫</h3>
  <p>植物特有的 RdDM 通路通过24 nt siRNA-AGO4 复合体引导 DRM2 甲基转移酶到特定基因组位点进行 DNA 甲基化。越来越多的证据表明，RdDM 通路与免疫存在交叉：</p>
  <ul>
    <li><strong>转座子去抑制与防御基因激活：</strong>SA 信号和病原侵染可以局部降低某些转座子和重复序列的 DNA 甲基化水平。由于许多防御基因（尤其是 NLR 基因）位于富含转座子的基因组区域，转座子的去甲基化可能通过"顺式"效应增强邻近防御基因的表达 (Dowen et al., 2012)。</li>
    <li><strong>跨代免疫记忆：</strong>某些表观遗传变化（包括 DNA 甲基化和组蛋白修饰的改变）可以在有限的代际间传递。Luna et al. (2012) 报道，拟南芥经 <em>Pst</em> DC3000 处理后，其子代在没有再次接触病原的情况下表现出增强的 SA 依赖性防御——这种跨代效应与特定基因组位点的 DNA 甲基化变化相关。</li>
  </ul>

  <h3>组蛋白修饰与免疫 priming</h3>
  <p>免疫 priming 的表观遗传基础不限于 DNA 甲基化。Jaskiewicz et al. (2011) 发现，经 SA 或病原处理的拟南芥在防御基因启动子区域出现持久的 H3K4me3（激活标记）和 H3 乙酰化增加，即使在 SA 水平恢复正常后这些标记仍然存在。这种"表观遗传疤痕"可能解释了 priming 的分子基础：防御基因虽然未被完全激活，但其染色质状态已经被"预设"为更容易被再次激活的状态 <span class="cross-ref">→ 第11章</span>。</p>

  <p>ncRNA 在这个过程中扮演什么角色？一种可能的模型是：免疫信号诱导特定的 lncRNA 或 siRNA 产生 → 这些 ncRNA 引导染色质修饰酶到防御基因座 → 建立持久的表观遗传标记 → 后续的免疫刺激可以更快速地在这些"预标记"的位点启动全面的转录激活。这一模型的各个环节已有间接证据支持，但<strong>完整的因果链条尚未在任何单一系统中被验证</strong>。</p>

  <!-- ======== Key Question ======== -->
  <div class="box box-cognition"><div class="box-title">Key Question</div>
  <p><strong>ncRNA 介导的免疫调控是进化的"锦上添花"还是"不可或缺"？</strong></p>
  <p>一个根本性的问题是：如果去除所有已知的免疫相关 miRNA 和 lncRNA，植物的免疫系统是否会崩溃？还是仅仅变得"不那么精确"？目前的证据倾向于后者——单个 miRNA 突变体的免疫表型通常是定量的（抗性降低30-50%）而非定性的（完全丧失抗性）。但 miRNA 家族之间可能存在大量的功能冗余，需要多基因突变体才能揭示全局效应。如果 ncRNA 主要承担"微调"功能而非"开关"功能，那么它们的进化优势在于：<strong>以极低的成本（几百个碱基的 RNA，无需翻译为蛋白质）实现对复杂网络的精密调节</strong>——这是蛋白质调控因子难以匹敌的效率。</p>
  </div>

  <!-- ======== 里程碑 ======== -->
  <h2><span class="section-num">13.6</span>里程碑研究思路拆解</h2>

  <h3>里程碑 1：Navarro et al. (2006) — 第一个免疫 miRNA 的鉴定</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>miRNA 是否参与 PTI 信号的调控？</p>
  <p><strong>关键思路：</strong>用 flg22 处理拟南芥后进行 small RNA 组学分析，鉴定差异表达的 miRNA，并追踪其靶标基因的生物学功能。</p>
  <p><strong>关键证据链：</strong>（1）flg22 处理诱导 miR393 积累；（2）miR393 的靶标是生长素受体 TIR1/AFB；（3）miR393 过表达增强对 <em>Pst</em> DC3000 的抗性；（4）外源生长素处理增加细菌易感性。</p>
  <p><strong>影响：</strong>首次建立 miRNA-免疫的因果连接，揭示了生长素-免疫拮抗的分子机制。同时为后续大量免疫 miRNA 的鉴定开辟了方法学范式。</p></div>

  <h3>里程碑 2：Weiberg et al. (2013) — 真菌小 RNA 劫持宿主沉默机器</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>病原是否可以通过小 RNA 实现跨界的基因沉默来压制宿主免疫？</p>
  <p><strong>关键思路：</strong>对 <em>B. cinerea</em> 感染的拟南芥和番茄进行小 RNA 测序，区分宿主来源和病原来源的小 RNA，然后通过 AGO 免疫沉淀（AGO-IP）确认病原小 RNA 是否被宿主 AGO 蛋白装载。</p>
  <p><strong>关键证据链：</strong>（1）<em>B. cinerea</em> 小 RNA 在宿主组织中大量积累；（2）Bc-siRNA 与宿主 AGO1 物理互作（AGO1-IP-seq）；（3）Bc-siRNA 的靶标预测并实验验证命中宿主 MAPK 基因；（4）在 <em>ago1</em> 突变体中，Bc-siRNA 的免疫抑制效应消失。</p>
  <p><strong>影响：</strong>开创性地证明病原可以利用小 RNA 作为"跨界效应子"，将植物-病原互作的信息战从蛋白质层面扩展到 RNA 层面。</p></div>

  <h3>里程碑 3：Cai et al. (2018) — 植物胞外囊泡输出小 RNA 反击病原</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>植物是否可主动用 RNA 跨界压制病原？如果可以，传递介质是什么？</p>
  <p><strong>关键思路：</strong>从拟南芥感染位点的质外体液中分离胞外囊泡，分析其 RNA 货物和蛋白质组成，通过荧光标记追踪囊泡的跨界转运。</p>
  <p><strong>关键证据链：</strong>（1）拟南芥在 <em>B. cinerea</em> 感染位点分泌富含 TET8 蛋白的胞外囊泡；（2）囊泡中含有靶向 <em>B. cinerea</em> 毒力基因的 siRNA；（3）荧光标记的囊泡可被 <em>B. cinerea</em> 菌丝吸收；（4）<em>tet8</em> 突变体的囊泡分泌减少且对 <em>B. cinerea</em> 更敏感；（5）植物来源小 RNA 进入病原后可降低靶基因表达和毒力。</p>
  <p><strong>影响：</strong>不仅证明了跨界 RNA 传递的双向性，还鉴定了传递介质（胞外囊泡），为 HIGS 和 SIGS（Spray-Induced Gene Silencing，喷雾诱导基因沉默）等应用策略提供了机制基础。</p></div>

  <!-- ======== 争论 ======== -->
  <h2><span class="section-num">13.7</span>当前争论与未解问题</h2>
  <ul class="questions-list">
    <li><strong>跨界 RNA 传递的效率由哪些因素决定？</strong>在自然感染条件下，有多少小 RNA 能成功跨越细胞壁-质膜双重屏障被病原吸收？传递效率是否足以在田间条件下产生有意义的保护效果？胞外囊泡的稳定性和靶向性如何？</li>
    <li><strong>田间环境中 RNA 防御如何保持稳定？</strong>dsRNA 在土壤和叶表环境中容易被核酸酶降解。SIGS 策略（直接喷洒 dsRNA）的田间持效期通常只有数天——如何延长 RNA 的环境稳定性？纳米载体或细菌表达系统是否能解决这一问题？</li>
    <li><strong>lncRNA 在免疫记忆中的因果证据还缺什么？</strong>目前大多数 lncRNA-免疫关联是相关性的。需要：（1）CRISPR 精确删除 lncRNA 基因座（而不影响邻近基因）的突变体；（2）lncRNA 域缺失/嵌合体实验区分 RNA 序列功能和转录行为功能；（3）lncRNA-蛋白质互作组学确认具体的效应分子。</li>
    <li><strong>如何构建低脱靶 RNA 抗病工程体系？</strong>HIGS 和 SIGS 的一个核心安全关切是脱靶效应——设计的 dsRNA 是否会意外沉默宿主或非靶标微生物的基因？如何在设计阶段进行全面的脱靶预测？</li>
    <li><strong>ncRNA 调控是否在作物中保守？</strong>大多数机制发现来自拟南芥。miR393-生长素受体轴在作物中是否以相同方式运作？跨界 RNA 转移在不同病理系统中的普遍性和效率是否一致？</li>
  </ul>

  <!-- ======== 实验方法 ======== -->
  <h2><span class="section-num">13.8</span>关键实验方法</h2>
  <table><thead><tr><th>实验方法</th><th>用途</th><th>经典文献</th></tr></thead><tbody>
  <tr><td>small RNA-seq + AGO-IP</td><td>鉴定与特定 AGO 蛋白结合的功能性小 RNA，区分宿主和病原来源</td><td class="ref">Weiberg et al., 2013, Science</td></tr>
  <tr><td>胞外囊泡分离与示踪</td><td>纯化植物分泌的胞外囊泡，分析其 RNA 货物，荧光标记追踪跨界转运</td><td class="ref">Cai et al., 2018, Science</td></tr>
  <tr><td>靶基因报告系统（5'RACE/GFP sensor）</td><td>验证特定 miRNA/siRNA 对靶标 mRNA 的切割，确认沉默因果关系</td><td class="ref">Zhang et al., 2016, Nat Plants</td></tr>
  <tr><td>CRISPR 敲除 ncRNA 基因座</td><td>建立 lncRNA/miRNA 与免疫表型的因果关系</td><td class="ref">Seo et al., 2017, Plant Cell</td></tr>
  <tr><td>ChIP-seq 与 ATAC-seq</td><td>解析免疫相关基因座的组蛋白修饰和染色质可及性变化</td><td class="ref">Jaskiewicz et al., 2011, Plant Cell</td></tr>
  </tbody></table>

  <div class="reading-section">
    <h2><span class="section-num">13.9</span>推荐阅读</h2>
    <div class="reading-level level-essential"><h4>🔴 必读</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Weiberg A, Wang M, Lin FM, et al.</span><span class="title"><em>Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways.</em></span><span class="journal"><em>Science</em>, 2013.</span></div><div class="reading-reason">跨界 RNA 抑制的经典发现。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Cai Q, Qiao L, Wang M, et al.</span><span class="title"><em>Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes.</em></span><span class="journal"><em>Science</em>, 2018.</span></div><div class="reading-reason">植物反向跨界防御里程碑。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Navarro L, Dunoyer P, Jay F, et al.</span><span class="title"><em>A plant miRNA contributes to antibacterial resistance by repressing auxin signaling.</em></span><span class="journal"><em>Science</em>, 2006.</span></div><div class="reading-reason">第一个免疫 miRNA，miRNA-激素-免疫的三方连接。</div></div>
    </div>
    <div class="reading-level level-important"><h4>🟡 重要</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Borges F, Martienssen RA.</span><span class="title"><em>The expanding world of small RNAs in plants.</em></span><span class="journal"><em>Nat Rev Mol Cell Biol</em>, 2015.</span></div><div class="reading-reason">小 RNA 机制的全面综述。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Huang CY, Wang H, Hu P, et al.</span><span class="title"><em>Long noncoding RNAs and their roles in plant immune responses.</em></span><span class="journal"><em>Plant Commun</em>, 2021.</span></div><div class="reading-reason">lncRNA 免疫综述，定义了当前知识边界。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Shivaprasad PV, Chen HM, Patel K, et al.</span><span class="title"><em>A microRNA superfamily regulates nucleotide binding site–leucine-rich repeats and other mRNAs.</em></span><span class="journal"><em>Plant Cell</em>, 2012.</span></div><div class="reading-reason">miRNA-NLR 调控轴的系统解析。</div></div>
    </div>
    <div class="reading-level level-extended"><h4>🟢 拓展</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Wang M, Weiberg A, Dellota E Jr, Yamane D, Jin H.</span><span class="title"><em>Botrytis small RNA Bc-siR37 suppresses plant defense genes by cross-kingdom RNAi.</em></span><span class="journal"><em>Nat Plants</em>, 2017.</span></div><div class="reading-reason">跨界 RNA 的具体分子个案。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Gaffar FY, Koch A.</span><span class="title"><em>Catch me if you can! RNA silencing-based improvement of antiviral plant immunity.</em></span><span class="journal"><em>Viruses</em>, 2019.</span></div><div class="reading-reason">RNA 沉默的应用前景。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Zhang T, Zhao YL, Zhao JH, et al.</span><span class="title"><em>Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen.</em></span><span class="journal"><em>Nat Plants</em>, 2016.</span></div><div class="reading-reason">跨界 RNA 功能扩展实证。</div></div>
    </div>
  </div>

  <!-- ======== 参考文献 ======== -->
  <h2><span class="section-num">13.10</span>参考文献</h2>
  <ol class="references">
    <li>Boccara M, Sarazin A, Thiébeauld O, et al. The <em>Arabidopsis</em> miR472-RDR6 silencing pathway modulates PAMP- and effector-triggered immunity through the post-transcriptional control of disease resistance genes. <em>PLoS Pathog</em>, 2014, 10: e1003883.</li>
    <li>Borges F, Martienssen RA. The expanding world of small RNAs in plants. <em>Nat Rev Mol Cell Biol</em>, 2015, 16: 727–741.</li>
    <li>Cai Q, Qiao L, Wang M, et al. Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. <em>Science</em>, 2018, 360: 1126–1129.</li>
    <li>Ding SW, Voinnet O. Antiviral immunity directed by small RNAs. <em>Cell</em>, 2007, 130: 209–222.</li>
    <li>Dowen RH, Pelizzola M, Schmitz RJ, et al. Widespread dynamic DNA methylation in response to biotic stress. <em>Proc Natl Acad Sci USA</em>, 2012, 109: E2183–E2191.</li>
    <li>Huang CY, Wang H, Hu P, et al. Long noncoding RNAs and their roles in plant immune responses. <em>Plant Commun</em>, 2021, 2: 100228.</li>
    <li>Jaskiewicz M, Conrath U, Peterhänsel C. Chromatin modification acts as a memory for systemic acquired resistance in the plant stress response. <em>EMBO Rep</em>, 2011, 12: 50–55.</li>
    <li>Luna E, Bruce TJA, Roberts MR, et al. Next-generation systemic acquired resistance. <em>Plant Physiol</em>, 2012, 158: 844–853.</li>
    <li>Melnyk CW, Molnar A, Baulcombe DC. Intercellular and systemic movement of RNA silencing signals. <em>EMBO J</em>, 2011, 30: 3553–3563.</li>
    <li>Navarro L, Dunoyer P, Jay F, et al. A plant miRNA contributes to antibacterial resistance by repressing auxin signaling. <em>Science</em>, 2006, 312: 436–439.</li>
    <li>Seo JS, Sun HX, Park BS, et al. ELF18-INDUCED LONG-NONCODING RNA associates with Mediator to enhance expression of innate immune response genes in <em>Arabidopsis</em>. <em>Plant Cell</em>, 2017, 29: 1024–1038.</li>
    <li>Shivaprasad PV, Chen HM, Patel K, et al. A microRNA superfamily regulates nucleotide binding site–leucine-rich repeats and other mRNAs. <em>Plant Cell</em>, 2012, 24: 859–874.</li>
    <li>Vargason JM, Szittya G, Burgyán J, Hall TMT. Size selective recognition of siRNA by an RNA silencing suppressor. <em>Cell</em>, 2003, 115: 799–811.</li>
    <li>Wang M, Weiberg A, Dellota E Jr, Yamane D, Jin H. <em>Botrytis</em> small RNA Bc-siR37 suppresses plant defense genes by cross-kingdom RNAi. <em>Nat Plants</em>, 2017, 3: 16231.</li>
    <li>Weiberg A, Wang M, Lin FM, et al. Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. <em>Science</em>, 2013, 342: 118–123.</li>
    <li>Yu Y, Zhou YF, Feng YZ, et al. Transcriptional landscape of pathogen-responsive lncRNAs in rice unveils the role of ALEX1 in jasmonate pathway and disease resistance. <em>Plant Biotechnol J</em>, 2020, 18: 679–690.</li>
    <li>Zhai J, Jeong DH, De Paoli E, et al. MicroRNAs as master regulators of the plant NB-LRR defense gene family via the production of phased, trans-acting siRNAs. <em>Genes Dev</em>, 2011, 25: 2540–2553.</li>
    <li>Zhang T, Zhao YL, Zhao JH, et al. Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen. <em>Nat Plants</em>, 2016, 2: 16153.</li>
  </ol>

  <nav class="chapter-nav"><a href="#"><div><span class="nav-label">上一章</span>← 第12章 环境因子与免疫</div></a><a href="#"><div style="text-align:right;"><span class="nav-label">下一章</span>第14章 从基础到抗病育种 →</div></a></nav>
</div>
