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
    <li><strong>dsRNA 结合：</strong>如番茄丛矮病毒（TBSV）的 P19 形成同源二聚体，以尺寸特异性方式结合21 nt 的 siRNA 双链体，阻止其装载入 AGO (Vargason et al., 2003)。</li>
    <li><strong>AGO 降解：</strong>如豇豆花叶病毒（CMV）的 2b 蛋白直接与 AGO1 互作并抑制其切割活性。</li>
    <li><strong>甲基化抑制：</strong>如马铃薯 Y 病毒（PVY）的 HcPro 干扰 HEN1 对 siRNA 3' 端的甲基化修饰，导致 siRNA 不稳定而降解。</li>
  </ul>
  <p>VSR 的存在创造了一种持续的分子军备竞赛——与效应子-NLR 的博弈遥相呼应 <span class="cross-ref">→ 第7章</span>。值得注意的是，一些 NLR 蛋白已被证明能直接识别 VSR（如烟草的 N 蛋白识别 TMV 的解旋酶/VSR 功能域），将 RNA 沉默防线与 ETI 防线在分子层面连接起来 <span class="cross-ref">→ 第4章</span>。</p>

  [图 13.1 抗病毒 RNA 沉默通路与 VSR 靶点示意图]

  <h2><span class="section-num">13.2</span>miRNA 在免疫调控中的角色</h2>
  <h3>miRNA 介导的免疫增益控制</h3>
  <p>与外源 siRNA 不同，miRNA 是植物基因组自身编码的调控分子。MIR 基因转录产生前体 RNA，经 DCL1 加工为成熟 miRNA（通常21 nt），装载入 AGO1 后以碱基互补方式切割或翻译抑制靶标 mRNA。关键在于：<strong>多个 miRNA 家族的靶标恰好是免疫信号通路的核心组分</strong>——这使得 miRNA 成为免疫系统"增益"（gain）的精密调节器。</p>
  <p>最具代表性的免疫相关 miRNA 包括：</p>
  <ul>
    <li><strong>miR393——最早被鉴定的"免疫 miRNA"：</strong>Navarro et al. (2006) 在 <em>Science</em> 上报道，flg22 处理诱导 miR393 的积累，miR393 靶向降解生长素受体 TIR1/AFB 的 mRNA <span class="cross-ref">→ 第5章 5.4节</span>。</li>
    <li><strong>miR482/miR2118——NLR 表达的"刹车"：</strong>这两个 miRNA 家族靶向多种 NLR 基因的 mRNA，在非胁迫条件下维持 NLR 的低水平表达 (Shivaprasad et al., 2012; Zhai et al., 2011) <span class="cross-ref">→ 第11章</span>。</li>
    <li><strong>miR160/miR167——生长素响应因子的调控。</strong></li>
    <li><strong>miR472——NLR 的精确制导：</strong>在拟南芥中，miR472 靶向 CC-NLR 亚家族的多个成员 (Boccara et al., 2014)。</li>
  </ul>
  <h3>miRNA 调控的系统逻辑</h3>
  <p>从系统生物学的角度看，miRNA 对免疫的调控不是简单的"开关"，而是一种<strong>网络级的"增益控制"（gain control）</strong>：</p>
  <ol class="mechanism-steps">
    <li><strong>基线设定：</strong>在非胁迫条件下，免疫相关 miRNA 维持靶标基因的低表达水平。</li>
    <li><strong>快速解除抑制：</strong>病原信号触发特定 miRNA 的下调，释放靶标基因的表达。</li>
    <li><strong>时序精度：</strong>不同 miRNA 对病原信号的响应时序不同。</li>
    <li><strong>恢复抑制：</strong>病原被清除后，miRNA 表达恢复，重新建立低表达基线。</li>
  </ol>
  <p>这种设计的核心优势在于<strong>可逆性和低代价</strong>。</p>

  <h2><span class="section-num">13.3</span>lncRNA 与免疫的新关联</h2>
  <p>长链非编码 RNA（lncRNA，>200 nt）是一个庞大但功能大部分未知的 RNA 类别。</p>
  <h3>已知的免疫相关 lncRNA</h3>
  <ul>
    <li><strong>ELENA1（ELF18-INDUCED LONG-NONCODING RNA 1）：</strong>拟南芥中研究最深入的免疫 lncRNA (Seo et al., 2017)。</li>
    <li><strong>ALEX1：</strong>水稻中鉴定的 lncRNA，参与 JA 信号通路 (Yu et al., 2020)。</li>
    <li><strong>天然反义转录本（NAT）。</strong></li>
  </ul>
  <h3>lncRNA 与免疫记忆</h3>
  <p>lncRNA 在免疫中可能最重要的角色是<strong>免疫记忆的建立和维持</strong> <span class="cross-ref">→ 第11章</span>。</p>
  <p>然而，<strong>目前 lncRNA 在植物免疫中的因果性证据仍然薄弱</strong>。</p>

  <h2><span class="section-num">13.4</span>跨界 RNA 转移（cross-kingdom RNAi）</h2>
  <h3>病原→宿主方向：RNA 劫持</h3>
  <p>2013年，Weiberg et al. 在 <em>Science</em> 上发表：灰霉菌 <em>Botrytis cinerea</em> 产生的小 RNA 可以<strong>劫持宿主的 AGO1</strong>。Wang et al. (2017) 进一步鉴定了 Bc-siR37。</p>
  <h3>宿主→病原方向：RNA 反击</h3>
  <ul>
    <li><strong>Zhang et al. (2016)：</strong>棉花 miRNA 转运到 <em>Verticillium dahliae</em> 中。</li>
    <li><strong>Cai et al. (2018)：</strong>拟南芥通过<strong>胞外囊泡（EVs）</strong>将 siRNA 运送到 <em>B. cinerea</em>。</li>
  </ul>
  <p>这些发现开辟了<strong>宿主诱导基因沉默（HIGS）</strong>方向 <span class="cross-ref">→ 第14章</span>。</p>

  [图 13.2 跨界 RNA 转移的双向机制]

  <h2><span class="section-num">13.5</span>表观遗传学与免疫记忆</h2>
  <h3>RNA 指导的 DNA 甲基化（RdDM）与免疫</h3>
  <ul>
    <li><strong>转座子去抑制与防御基因激活</strong> (Dowen et al., 2012)。</li>
    <li><strong>跨代免疫记忆</strong> (Luna et al., 2012)。</li>
  </ul>
  <h3>组蛋白修饰与免疫 priming</h3>
  <p>Jaskiewicz et al. (2011) 发现防御基因启动子区域出现持久的 H3K4me3 <span class="cross-ref">→ 第11章</span>。</p>

  <div class="box box-cognition"><div class="box-title">Key Question</div>
  <p><strong>ncRNA 介导的免疫调控是进化的"锦上添花"还是"不可或缺"？</strong></p>
  <p>单个 miRNA 突变体的免疫表型通常是定量的（抗性降低30-50%）而非定性的。<strong>以极低的成本实现对复杂网络的精密调节</strong>——这是蛋白质调控因子难以匹敌的效率。</p>
  </div>

  <h2><span class="section-num">13.6</span>里程碑研究思路拆解</h2>
  <h3>里程碑 1：Navarro et al. (2006)</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>miRNA 是否参与 PTI 信号的调控？</p>
  <p><strong>关键思路：</strong>flg22 处理后 small RNA 组学。</p>
  <p><strong>关键证据链：</strong>flg22→miR393↑→TIR1↓→抗性↑。</p>
  <p><strong>影响：</strong>首次建立 miRNA-免疫的因果连接。</p></div>
  <h3>里程碑 2：Weiberg et al. (2013)</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>病原是否可以通过小 RNA 跨界沉默宿主免疫？</p>
  <p><strong>关键思路：</strong>小 RNA 测序 + AGO-IP 验证。</p>
  <p><strong>关键证据链：</strong>Bc-siRNA→AGO1→宿主 MAPK↓。</p>
  <p><strong>影响：</strong>开创跨界 RNA 效应子概念。</p></div>
  <h3>里程碑 3：Cai et al. (2018)</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>植物是否可主动用 RNA 反击？传递介质？</p>
  <p><strong>关键思路：</strong>质外体液囊泡分离 + RNA 货物分析。</p>
  <p><strong>关键证据链：</strong>TET8 囊泡→siRNA→<em>B. cinerea</em> 毒力基因↓。</p>
  <p><strong>影响：</strong>鉴定传递介质，奠定 HIGS/SIGS 基础。</p></div>

  <h2><span class="section-num">13.7</span>当前争论与未解问题</h2>
  <ul class="questions-list">
    <li><strong>跨界 RNA 传递的效率由哪些因素决定？</strong></li>
    <li><strong>田间环境中 RNA 防御如何保持稳定？</strong></li>
    <li><strong>lncRNA 在免疫记忆中的因果证据还缺什么？</strong></li>
    <li><strong>如何构建低脱靶 RNA 抗病工程体系？</strong></li>
    <li><strong>ncRNA 调控是否在作物中保守？</strong></li>
  </ul>

  <h2><span class="section-num">13.8</span>关键实验方法</h2>
  <table><thead><tr><th>实验方法</th><th>用途</th><th>经典文献</th></tr></thead><tbody>
  <tr><td>small RNA-seq + AGO-IP</td><td>鉴定功能性小 RNA</td><td class="ref">Weiberg et al., 2013, Science</td></tr>
  <tr><td>胞外囊泡分离与示踪</td><td>验证跨界传递路径</td><td class="ref">Cai et al., 2018, Science</td></tr>
  <tr><td>靶基因报告系统（5'RACE/GFP sensor）</td><td>确认沉默因果关系</td><td class="ref">Zhang et al., 2016, Nat Plants</td></tr>
  <tr><td>CRISPR 敲除 ncRNA 基因座</td><td>建立因果关系</td><td class="ref">Seo et al., 2017, Plant Cell</td></tr>
  <tr><td>ChIP-seq 与 ATAC-seq</td><td>解析表观遗传变化</td><td class="ref">Jaskiewicz et al., 2011, Plant Cell</td></tr>
  </tbody></table>

  <div class="reading-section">
    <h2><span class="section-num">13.9</span>推荐阅读</h2>
    <div class="reading-level level-essential"><h4>🔴 必读</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Weiberg A, Wang M, Lin FM, et al.</span><span class="title"><em>Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways.</em></span><span class="journal"><em>Science</em>, 2013.</span></div><div class="reading-reason">跨界 RNA 抑制的经典发现。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Cai Q, Qiao L, Wang M, et al.</span><span class="title"><em>Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes.</em></span><span class="journal"><em>Science</em>, 2018.</span></div><div class="reading-reason">植物反向跨界防御里程碑。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Navarro L, Dunoyer P, Jay F, et al.</span><span class="title"><em>A plant miRNA contributes to antibacterial resistance by repressing auxin signaling.</em></span><span class="journal"><em>Science</em>, 2006.</span></div><div class="reading-reason">第一个免疫 miRNA。</div></div>
    </div>
    <div class="reading-level level-important"><h4>🟡 重要</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Borges F, Martienssen RA.</span><span class="title"><em>The expanding world of small RNAs in plants.</em></span><span class="journal"><em>Nat Rev Mol Cell Biol</em>, 2015.</span></div><div class="reading-reason">小 RNA 机制综述。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Shivaprasad PV, Chen HM, Patel K, et al.</span><span class="title"><em>A microRNA superfamily regulates NB-LRRs and other mRNAs.</em></span><span class="journal"><em>Plant Cell</em>, 2012.</span></div><div class="reading-reason">miRNA-NLR 调控轴。</div></div>
    </div>
    <div class="reading-level level-extended"><h4>🟢 拓展</h4>
<div class="reading-item"><div class="reading-ref"><span class="authors">Wang M, Weiberg A, Dellota E Jr, et al.</span><span class="title"><em>Botrytis small RNA Bc-siR37 suppresses plant defense genes.</em></span><span class="journal"><em>Nat Plants</em>, 2017.</span></div><div class="reading-reason">跨界 RNA 个案。</div></div>
<div class="reading-item"><div class="reading-ref"><span class="authors">Zhang T, Zhao YL, Zhao JH, et al.</span><span class="title"><em>Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen.</em></span><span class="journal"><em>Nat Plants</em>, 2016.</span></div><div class="reading-reason">跨界 RNA 功能扩展。</div></div>
    </div>
  </div>

  <h2><span class="section-num">13.10</span>参考文献</h2>
  <ol class="references">
    <li>Boccara M, et al. <em>PLoS Pathog</em>, 2014, 10: e1003883.</li>
    <li>Borges F, Martienssen RA. <em>Nat Rev Mol Cell Biol</em>, 2015, 16: 727–741.</li>
    <li>Cai Q, et al. <em>Science</em>, 2018, 360: 1126–1129.</li>
    <li>Ding SW, Voinnet O. <em>Cell</em>, 2007, 130: 209–222.</li>
    <li>Dowen RH, et al. <em>Proc Natl Acad Sci USA</em>, 2012, 109: E2183–E2191.</li>
    <li>Jaskiewicz M, et al. <em>EMBO Rep</em>, 2011, 12: 50–55.</li>
    <li>Luna E, et al. <em>Plant Physiol</em>, 2012, 158: 844–853.</li>
    <li>Melnyk CW, et al. <em>EMBO J</em>, 2011, 30: 3553–3563.</li>
    <li>Navarro L, et al. <em>Science</em>, 2006, 312: 436–439.</li>
    <li>Seo JS, et al. <em>Plant Cell</em>, 2017, 29: 1024–1038.</li>
    <li>Shivaprasad PV, et al. <em>Plant Cell</em>, 2012, 24: 859–874.</li>
    <li>Vargason JM, et al. <em>Cell</em>, 2003, 115: 799–811.</li>
    <li>Wang M, et al. <em>Nat Plants</em>, 2017, 3: 16231.</li>
    <li>Weiberg A, et al. <em>Science</em>, 2013, 342: 118–123.</li>
    <li>Yu Y, et al. <em>Plant Biotechnol J</em>, 2020, 18: 679–690.</li>
    <li>Zhai J, et al. <em>Genes Dev</em>, 2011, 25: 2540–2553.</li>
    <li>Zhang T, et al. <em>Nat Plants</em>, 2016, 2: 16153.</li>
  </ol>

  <nav class="chapter-nav"><a href="#"><div><span class="nav-label">上一章</span>← 第12章 环境因子与免疫</div></a><a href="#"><div style="text-align:right;"><span class="nav-label">下一章</span>第14章 从基础到抗病育种 →</div></a></nav>
</div>
