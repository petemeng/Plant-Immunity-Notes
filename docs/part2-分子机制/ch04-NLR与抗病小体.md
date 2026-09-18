<div class="page-wrapper">

  <!-- Breadcrumb -->
  <div class="breadcrumb">
    <a href="../../">首页</a><span>›</span>
    <span>第二部分 分子机制</span><span>›</span>
    第4章
  </div>

  <!-- Chapter Header -->
  <header class="chapter-header">
    <div class="chapter-header-inner">
      <div class="chapter-number">04</div>
      <div class="chapter-part">第二部分 · 分子机制</div>
      <h1 class="chapter-title">NLR 与抗病小体</h1>
      <p class="chapter-subtitle">
        从细胞内识别到抗病小体：理解免疫信号、离子通道与细胞死亡
      </p>
    </div>
  </header>
  <section class="box box-experiment learning-guide" aria-label="初学者学习导引">
  <h2>学习导引</h2>
  <p><strong>学完本章，你应能：</strong></p><ul><li>区分按结构域命名的 CNL/TNL/RNL 与按任务命名的 sensor/helper。</li><li>理解结构、通道活性和整株抗性属于不同证据层次。</li><li>追踪 TNL 小分子信号如何经 EDS1 复合体连接辅助 NLR。</li></ul>
  <p><strong>必备概念：</strong>结构域是蛋白中具有相对独立结构或功能的部分；寡聚化是多个亚基组装；变构是某处状态变化影响另一处功能。NLR 的识别、激活和最终抗病结果需要分开讨论。</p>
  <p><strong>建议路线：</strong>先读4.2分类表，再分别读4.4与4.5两种信号实现方式。4.6以后讨论配对和网络时，始终标注谁负责感知、谁负责传递、谁执行输出。 基础补课可见<a href="../../learning/ch00-细胞与分子基础/">第0章：细胞与分子基础</a>。</p>
  </section>


  <!-- Chapter TOC -->
  <nav class="chapter-toc">
    <h3>本章目录</h3>
    <ol>
      <li>引言</li>
      <li>NLR 的分类与域架构</li>
      <li>Resistosome 的发现与结构革命</li>
      <li>Helper NLR 网络与信号汇聚</li>
      <li>细胞死亡与免疫的解耦</li>
      <li>Integrated decoy 与感知多样性的扩展</li>
      <li>NLR 网络：sensor 与 helper 的分工协作</li>
      <li>过敏性坏死反应 (HR) 的分子基础</li>
      <li>里程碑研究思路拆解</li>
      <li>当前争论与未解问题</li>
      <li>关键实验方法</li>
      <li>推荐阅读</li>
    </ol>
  </nav>
  <div class="box box-cognition"><div class="box-title">概念桥梁：两套分类坐标不要混用</div><p>CNL、TNL、RNL 描述结构与系统发育类别；sensor（感知者）、helper（辅助者）和 executor（执行者）描述在一个受体系统中的功能角色。RNL 常承担辅助功能，但“helper NLR”不等同于“RNL”：NRC 类辅助 NLR 属于 CNL。某些 CNL 能兼顾感知和输出，另一些需要配对或网络伙伴。<br>同理，“抗病小体”是组装后的信号复合体，不是所有 NLR 静息时都存在的细胞器。看见环状或漏斗状结构，首先说明亚基怎样排列；若要断言能通离子，仍需功能性通道证据；若要断言提高抗病性，还需宿主—病原互作中的结果。</p></div>


  <!-- 4.1 Introduction -->
  <h2><span class="section-num">4.1</span>引言</h2>

  <p>
    当病原体成功突破植物表面的 <span class="keyword">PTI</span> <span class="english-term">(Pattern-Triggered Immunity)</span> 防线后，它们分泌的效应子 <span class="english-term">(effector)</span> 进入植物细胞内部，试图抑制免疫信号并劫持宿主代谢。面对这一威胁，植物演化出一类细胞内免疫受体——<span class="keyword">NLR 蛋白</span> <span class="english-term">(Nucleotide-binding Leucine-rich Repeat)</span>，它们能够直接或间接识别效应子的活动，并触发强烈的防御响应。
  </p>

  <p>NLR 介导的免疫有时伴随<strong>超敏反应（hypersensitive response, HR）</strong>，但细胞死亡与限制病原的抗性并不完全等价。2019年 ZAR1 抗病小体结构揭示了激活态五聚体及漏斗状 N 端构象 (Wang et al., 2019a, b)；2021年研究才通过成像与电生理等证据支持 ZAR1 是<strong>可透 Ca²⁺ 的阳离子通道</strong> (Bi et al., 2021)。这一前后衔接展示了结构提出机制线索、功能研究进一步检验的过程。</p>

  <!-- 4.2 -->
  <h2><span class="section-num">4.2</span>NLR 蛋白的分类与结构域组织</h2>

  <p>
    植物 NLR 蛋白属于 STAND 超家族 <span class="english-term">(Signal Transduction ATPases with Numerous Domains)</span>，与动物某些免疫与细胞死亡蛋白共享更广泛的 STAND 家族背景；植物 NLR 的 NB-ARC 与动物典型 NLR 的 NACHT 不能当作同一结构域，而炎性小体是复合体名称。根据 N 端效应结构域的差异，植物 NLR 分为三大类：
  </p>

  <table>
    <thead>
      <tr>
        <th>类型</th>
        <th>N 端结构域</th>
        <th>代表成员</th>
        <th>功能特征</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>CNL</strong></td>
        <td>CC <span class="english-term">(Coiled-Coil)</span></td>
        <td><span class="gene">ZAR1</span>, <span class="gene">RPM1</span>, <span class="gene">Rx</span></td>
        <td>部分已解析成员如 ZAR1 形成可透 Ca²⁺ 的寡聚通道；不能把同一聚合数推广到全部 CNL</td>
      </tr>
      <tr>
        <td><strong>TNL</strong></td>
        <td>TIR <span class="english-term">(Toll/Interleukin-1 Receptor)</span></td>
        <td><span class="gene">RPP1</span>, <span class="gene">ROQ1</span>, <span class="gene">SNC1</span></td>
        <td>激活后 TIR 结构域获得 NADase 酶活性，通过 EDS1 传递信号</td>
      </tr>
      <tr>
        <td><strong>RNL</strong></td>
        <td>RPW8 <span class="english-term">(CC<sub>R</sub>)</span></td>
        <td><span class="gene">NRG1</span>, <span class="gene">ADR1</span></td>
        <td>ADR1 与 NRG1 家族常承担辅助信号功能，参与防御与细胞死亡；也可连接部分表面免疫过程</td>
      </tr>
    </tbody>
  </table>

  <p>
    三类 NLR 均共享保守的中央 <span class="keyword">NB-ARC 结构域</span> <span class="english-term">(Nucleotide-Binding domain shared with Apaf-1, R proteins, and CED-4)</span> 和 C 端 <span class="keyword">LRR 结构域</span> <span class="english-term">(Leucine-Rich Repeat)</span>。NB-ARC 结构域是分子开关的核心：静息状态下结合 ADP，维持蛋白的自抑制构象；激活后 ADP 被交换为 ATP，触发构象变化并驱动寡聚化。
  </p>

  <!-- 4.3 -->
  <h2><span class="section-num">4.3</span>NLR 的激活机制：从自抑制到寡聚化</h2>

  <p>
    NLR 在未被激活时以<span class="keyword">自抑制构象</span> <span class="english-term">(autoinhibited conformation)</span> 存在。LRR 结构域折叠回来包裹 NB-ARC 结构域，阻止其核苷酸交换和寡聚化。这种精密的自抑制机制确保 NLR 不会在没有病原体的情况下被意外激活——因为 NLR 的激活通常意味着细胞死亡，误激活将对植物自身造成严重损害。
  </p>

  <p>
    当效应子被识别后（无论是直接结合还是通过感知宿主蛋白的修饰），LRR 结构域的构象发生改变，释放对 NB-ARC 的抑制。随后发生以下关键事件：
  </p>

  <ol class="mechanism-steps">
    <li>
      <strong>核苷酸交换</strong>：NB-ARC 结构域释放 ADP，结合 ATP。这是激活的关键分子开关。
    </li>
    <li>
      <strong>构象开放</strong>：ATP 结合诱导 NB-ARC 结构域的大幅构象变化，暴露出此前被掩埋的寡聚化界面。
    </li>
    <li>
      <strong>寡聚化组装</strong>：多个激活态 NLR 单体通过 NB-ARC 结构域的相互作用组装成轮状寡聚体。ZAR1 的已解析激活复合体为五聚体，RPP1 和 ROQ1 等 TNL 的已解析复合体为四聚体；这是具体体系的结构结果。
    </li>
    <li>
      <strong>N 端效应结构域暴露</strong>：寡聚化将 N 端 CC 或 TIR 结构域聚集在一起，执行下游功能——部分执行型 CNL/RNL 可形成离子通道，若干 TNL 的 TIR 结构域则产生免疫相关小分子信号。
    </li>
  </ol>

  <!-- 4.4 ZAR1 -->
  <h2><span class="section-num">4.4</span>ZAR1 抗病小体——里程碑式的结构突破</h2>

  <p>
    2019 年，柴继杰团队与周俭民团队合作，在 <em>Science</em> 杂志连发两篇论文，报道了拟南芥 <span class="gene">ZAR1</span> 蛋白在静息态、中间态和激活态三种构象下的冷冻电镜结构 (Wang <em>et al.</em>, 2019a, b)。这是首个完整的植物 NLR 激活态结构，也标志着<span class="keyword">抗病小体 (resistosome)</span> 概念的正式确立。
  </p>

  <div class="figure">
    <svg viewBox="0 0 760 210" role="img" aria-label="ZAR1 抗病小体三态转换示意图">
      <defs>
        <marker id="arrow-ch4a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
          <path d="M0,0 L8,3 L0,6 Z" fill="#6b7f8f"></path>
        </marker>
      </defs>
      <rect x="30" y="38" width="170" height="96" rx="6" fill="#eef5ee" stroke="#78917d"></rect>
      <text x="115" y="62" text-anchor="middle" font-size="15" fill="#233426">静息态</text>
      <circle cx="92" cy="94" r="24" fill="#d6e8db" stroke="#64826d"></circle>
      <rect x="116" y="78" width="50" height="32" rx="4" fill="#fff6dd" stroke="#a68b53"></rect>
      <text x="115" y="144" text-anchor="middle" font-size="12" fill="#4b5a50">ZAR1-RKS1 + ADP</text>

      <rect x="294" y="38" width="170" height="96" rx="6" fill="#f6f0e6" stroke="#aa8d66"></rect>
      <text x="379" y="62" text-anchor="middle" font-size="15" fill="#4b3523">中间态</text>
      <circle cx="346" cy="94" r="24" fill="#e8dcc6" stroke="#a68b53"></circle>
      <rect x="370" y="78" width="58" height="32" rx="4" fill="#f0e2cc" stroke="#a06c45"></rect>
      <text x="379" y="144" text-anchor="middle" font-size="12" fill="#6b563f">PBL2-UMP 捕获</text>

      <rect x="558" y="38" width="170" height="96" rx="6" fill="#eef1fb" stroke="#7789af"></rect>
      <text x="643" y="62" text-anchor="middle" font-size="15" fill="#263451">激活态</text>
      <circle cx="623" cy="96" r="16" fill="#d7dff4" stroke="#667aa5"></circle>
      <circle cx="663" cy="96" r="16" fill="#d7dff4" stroke="#667aa5"></circle>
      <circle cx="643" cy="76" r="16" fill="#d7dff4" stroke="#667aa5"></circle>
      <circle cx="625" cy="116" r="16" fill="#d7dff4" stroke="#667aa5"></circle>
      <circle cx="661" cy="116" r="16" fill="#d7dff4" stroke="#667aa5"></circle>
      <path d="M615 152 Q643 176 671 152" fill="none" stroke="#53698f" stroke-width="5"></path>
      <text x="643" y="144" text-anchor="middle" font-size="12" fill="#3f4d68">五聚体孔道</text>

      <path d="M200 86 L294 86" stroke="#6b7f8f" stroke-width="2.5" marker-end="url(#arrow-ch4a)"></path>
      <path d="M464 86 L558 86" stroke="#6b7f8f" stroke-width="2.5" marker-end="url(#arrow-ch4a)"></path>
      <text x="247" y="75" text-anchor="middle" font-size="12" fill="#667280">AvrAC 修饰</text>
      <text x="511" y="75" text-anchor="middle" font-size="12" fill="#667280">ADP→ATP / 寡聚化</text>
    </svg>
    <p class="figure-caption">
      <strong>图 4.1 ZAR1 抗病小体的组装过程。</strong>
      (A) 静息态：ZAR1<sup>LRR</sup>-RKS1 二元复合体，NB-ARC 结合 ADP，蛋白处于自抑制构象。
      (B) 中间态：效应子 AvrAC 修饰 PBL2 后，PBL2<sup>UMP</sup> 被 RKS1 捕获，触发 ZAR1 的 ADP→ATP 交换。
      (C) 激活态：五个 ZAR1 单体组装为轮状五聚体，N 端 CC 结构域形成漏斗状结构，插入质膜形成钙离子通道。
      结构依据 Wang <em>et al.</em>, 2019, <em>Science</em>；通道功能依据 Bi <em>et al.</em>, 2021, <em>Cell</em>。
    </p>
  </div>

  <p>ZAR1 的激活过程清晰地展示了从效应子识别到细胞死亡的完整分子逻辑：</p>

  <ol class="mechanism-steps">
    <li>
      <strong>效应子活动的间接感知</strong>：丁香假单胞菌 <span class="english-term">(<em>Pseudomonas syringae</em>)</span> 的 III 型效应子 AvrAC 将 UMP 基团转移到宿主激酶 PBL2 上，干扰其在 PTI 中的信号功能。
    </li>
    <li>
      <strong>诱饵蛋白的捕获</strong>：被修饰的 PBL2<sup>UMP</sup> 被 ZAR1 复合体中的假激酶 RKS1 识别和结合。PBL2 在此充当"诱饵" <span class="english-term">(decoy)</span>，其被效应子修饰本身就是危险信号。
    </li>
    <li>
      <strong>核苷酸交换与寡聚化</strong>：PBL2<sup>UMP</sup> 的结合触发 ZAR1 的 ADP→dATP/ATP 交换，诱导构象开放，五个 ZAR1-RKS1-PBL2<sup>UMP</sup> 三元复合体组装为轮状五聚体。
    </li>
    <li>
      <strong>膜孔形成</strong>：五聚体的 N 端 CC (α1 螺旋) 结构域聚集形成漏斗状结构，插入质膜，形成可透 Ca²⁺ 的阳离子通道。
    </li>
    <li>
      <strong>钙内流与细胞死亡</strong>：胞外 Ca²⁺ 大量内流，触发下游 HR 相关的信号通路，最终导致细胞程序性死亡。
    </li>
  </ol>

  <div class="box box-cognition">
    <div class="box-title">认知修正</div>
    <p>ZAR1 的结构与通道研究证明：至少某些植物 NLR 可以直接承担离子通道功能，而不只是上游感知器。这没有排除其他受体依赖中间信号伙伴，也不能推广为所有 CNL 都独立执行细胞死亡。ZAR1 与动物成孔蛋白可作功能比较，但功能相似不等于它们是同一种蛋白或使用同一死亡程序。</p>
  </div>

  <!-- 4.5 TNL -->
  <h2><span class="section-num">4.5</span>TNL 的信号转导：NADase 活性与 EDS1 枢纽</h2>

  <p>在已解析的 TNL 体系中，RPP1、ROQ1 等激活后形成寡聚复合体，使 TIR 结构域产生酶活。与 ZAR1 通道机制不同，这里的关键是生成能被下游感知的小分子信号，而不是将 NAD⁺ 水解简单理解为耗尽代谢底物。不同 TIR 蛋白的产物谱也不完全相同。</p>

  <p>2022年的研究鉴定了与下游受体机制直接相关的产物：pRib-AMP/pRib-ADP 与 EDS1–PAD4 分支相关，ADPr-ATP/di-ADPR 与 EDS1–SAG101 分支相关，分别促进其与 ADR1 或 NRG1 类辅助 NLR 耦合 (Huang et al., 2022; Jia et al., 2022)。EDS1 及其伙伴是具有脂酶样折叠的免疫调节蛋白，不能因此认定其作用就是水解脂质。早期 v-cADPR 的检测是 TIR 酶活的重要线索，但不应将其直接写成已经确立的 EDS1 通用配体。</p>

  <div class="box box-cognition">
    <div class="box-title">认知修正</div>
    <p>
      TIR 结构域的 NADase 酶活性是 2019 年前后由多个团队独立发现的 (Horsefield <em>et al.</em>, 2019; Wan <em>et al.</em>, 2019)。此前，TIR 结构域被认为仅作为蛋白-蛋白互作的支架结构域发挥功能。酶活性的发现揭示了 TNL 信号转导的全新生化机制，也解释了为什么 TNL 和 CNL 的下游通路如此不同——部分 CNL 直接形成通道，TNL 则可通过酶产物、EDS1 复合体和辅助 NLR 连接到防御与死亡输出。
    </p>
  </div>

  <!-- 4.6 Integrated Decoy -->
  <h2><span class="section-num">4.6</span>Integrated Decoy 与感知多样性的扩展</h2>

  <p>NLR 如何识别效应蛋白？最初的"基因对基因"假说暗示直接的受体-配体结合，但保卫假说已经表明间接识别可能更为普遍 <span class="cross-ref">→ 第1章 1.3节</span>。"整合诱饵"（Integrated Decoy / Integrated Domain, ID）模型将这一概念推向了新的高度。</p>

  <h3>从保卫到整合：概念的进化</h3>
  <p>保卫假说（Guard Model）认为 NLR 监测效应蛋白的靶标蛋白——当靶标被修饰时，NLR 被激活。但如果被监测的蛋白逐渐丧失其原始功能，专门演化为"诱饵"（Decoy），我们就得到了诱饵模型 (van der Hoorn &amp; Kamoun, 2008)。整合诱饵模型更进一步：<strong>将诱饵结构域直接整合到 NLR 蛋白自身中</strong>，形成一个"受体-诱饵"的融合蛋白 (Cesari et al., 2014)。</p>

  <p>具体而言，许多 NLR 蛋白在经典的 NB-ARC-LRR 结构之外，还包含一个"非典型"结构域——即整合域（ID）。这些 ID 往往是效应蛋白在宿主中的真实靶标的同源序列。例如：</p>
  <ul>
    <li><strong>水稻 RGA5：</strong>其 C 端整合了一个重金属相关域（HMA），是<em>M. oryzae</em>效应蛋白 AVR-Pia 的直接结合靶标。AVR-Pia 结合 HMA 域后，RGA5 与其配对 NLR RGA4 协同激活免疫 (Cesari et al., 2013)。</li>
    <li><strong>拟南芥 RRS1：</strong>整合了一个 WRKY 转录因子域。<em>Ralstonia solanacearum</em>的效应蛋白 PopP2 是一种乙酰转移酶，靶向 WRKY 蛋白进行乙酰化修饰以抑制免疫。当 PopP2 修饰 RRS1 中的 WRKY 域时，RRS1 与配对 NLR RPS4 协同激活 ETI (Le Roux et al., 2015; Sarris et al., 2015)。</li>
    <li><strong>水稻 Pik-1：</strong>整合了一个 HMA 域，直接结合<em>M. oryzae</em>效应蛋白 AVR-PikD，与配对 NLR Pik-2 协同工作 (Maqbool et al., 2015)。</li>
  </ul>

  <div class="figure">
    <svg viewBox="0 0 760 220" role="img" aria-label="整合诱饵模型与 helper NLR 信号汇聚">
      <defs>
        <marker id="arrow-ch4b" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
          <path d="M0,0 L8,3 L0,6 Z" fill="#6b7f8f"></path>
        </marker>
      </defs>
      <rect x="28" y="42" width="132" height="48" rx="4" fill="#fff0e3" stroke="#b18056"></rect>
      <text x="94" y="70" text-anchor="middle" font-size="14" fill="#5a3b25">效应蛋白</text>
      <rect x="212" y="34" width="162" height="64" rx="5" fill="#eef5ee" stroke="#74907b"></rect>
      <text x="293" y="58" text-anchor="middle" font-size="14" fill="#24382b">sensor NLR</text>
      <rect x="248" y="68" width="90" height="20" rx="3" fill="#d9eadf" stroke="#74907b"></rect>
      <text x="293" y="82" text-anchor="middle" font-size="11" fill="#395645">integrated domain</text>
      <rect x="426" y="42" width="132" height="48" rx="4" fill="#eef1fb" stroke="#7789af"></rect>
      <text x="492" y="70" text-anchor="middle" font-size="14" fill="#263451">helper NLR</text>
      <rect x="610" y="32" width="118" height="68" rx="5" fill="#f6f0e6" stroke="#aa8d66"></rect>
      <text x="669" y="58" text-anchor="middle" font-size="14" fill="#4d3928">输出</text>
      <text x="669" y="78" text-anchor="middle" font-size="12" fill="#6b563f">Ca²⁺ / HR / 防御基因</text>

      <path d="M160 66 L212 66" stroke="#6b7f8f" stroke-width="2.5" marker-end="url(#arrow-ch4b)"></path>
      <path d="M374 66 L426 66" stroke="#6b7f8f" stroke-width="2.5" marker-end="url(#arrow-ch4b)"></path>
      <path d="M558 66 L610 66" stroke="#6b7f8f" stroke-width="2.5" marker-end="url(#arrow-ch4b)"></path>

      <rect x="190" y="142" width="130" height="40" rx="4" fill="#f7faf7" stroke="#8aa28e"></rect>
      <text x="255" y="166" text-anchor="middle" font-size="13" fill="#2f4636">识别可快速变异</text>
      <rect x="430" y="142" width="130" height="40" rx="4" fill="#f7faf7" stroke="#8aa28e"></rect>
      <text x="495" y="166" text-anchor="middle" font-size="13" fill="#2f4636">输出保持保守</text>
      <path d="M293 98 L255 142" stroke="#8aa28e" stroke-width="2" marker-end="url(#arrow-ch4b)"></path>
      <path d="M492 90 L495 142" stroke="#8aa28e" stroke-width="2" marker-end="url(#arrow-ch4b)"></path>
    </svg>
    <p class="figure-caption"><strong>图 4.2 整合诱饵与 sensor-helper 分工。</strong>携带整合域的 sensor NLR 负责捕获效应蛋白活动，helper NLR 负责稳定输出。识别端可以快速进化，输出端保持保守，这使 NLR 网络既能追踪病原变化，又能维持可靠的信号执行。</p>
  </div>

  <h3>NLR 配对：sensor-executor 的最小单元</h3>
  <p>一个引人注目的规律是：携带 ID 的 NLR 几乎总是成对出现——一个 sensor NLR（携带 ID，负责识别）和一个 executor/helper NLR（负责信号输出），两者基因在基因组上通常头对头或尾对尾排列 (Cesari et al., 2014)。这种配对架构赋予了极大的进化灵活性：sensor NLR 的 ID 可以快速变异以追踪效应蛋白的进化，而 executor NLR 保持保守以维持可靠的信号输出。</p>

  <p>生物信息学分析显示，植物 NLR 组中整合的域类型极为多样——包括激酶域、WRKY 域、HMA 域、BED 锌指域等，总计超过50种不同的整合域类型 (Kroj et al., 2016; Sarris et al., 2016)。这些整合域的多样性可能反映了效应蛋白靶标的多样性，暗示 ID-NLR 是植物应对效应蛋白多样化的一种高效进化策略。</p>

  <div class="figure">
    <img src="../../assets/images/papers/nature-2026-helper-nlr-clusters-fig4.png" alt="Ge et al. 2026 图4：SUMM2 激活后形成 EDS1-PAD4-ADR1-L1 helper NLR 抗病小体簇">
    <p class="figure-caption"><strong>图 4.P1 论文原图：helper NLR 抗病小体簇把 NLR 输出从线性通路推向高阶组装。</strong>原图为 Ge et al. (2026) <em>Nature</em> Fig. 4，DOI: 10.1038/s41586-026-10215-1。该图展示 SUMM2 激活后 EDS1-PAD4 与 ADR1-L1 的空间组织和簇状组装，直接对应本章关于 sensor-helper 分工和 NLR 输出阈值的讨论。依据 CC BY-NC-ND 4.0 原样复用；图片未作裁剪、改色或内容改动。</p>
  </div>

  <div class="box box-cognition">
    <div class="box-title">认知升级</div>
    <p>整合诱饵模型揭示了植物免疫的一个深刻的进化智慧：<strong>把效应蛋白的攻击靶标变成识别陷阱</strong>。效应蛋白进化来修饰宿主蛋白 X → 植物把 X 的结构域整合进 NLR → 效应蛋白"上钩"修饰整合域 → NLR 激活。这种策略的精妙之处在于，效应蛋白越是精准地攻击其靶标，就越容易被"整合了靶标的 NLR"所识别。这为合理设计新型抗病 NLR 提供了明确的工程思路 <span class="cross-ref">→ 第14章</span>。</p>
  </div>

  <!-- 4.7 NLR Network -->
  <h2><span class="section-num">4.7</span>NLR 网络：sensor 与 helper 的分工协作</h2>

  <p>
    随着越来越多 NLR 的功能被揭示，领域认识到植物体内的 NLR 并非各自为战，而是组成了一个<span class="keyword">功能网络</span>。根据功能分工，NLR 可分为：
  </p>

  <p>
    <strong>Sensor NLR</strong>：负责识别特定的效应子或效应子活动。它们的 LRR 或整合结构域 <span class="english-term">(Integrated Domain, ID)</span> 提供识别特异性，但自身可能不直接执行免疫信号输出。
  </p>

  <p>
    <strong>Helper NLR</strong>：接收 sensor NLR 的信号，执行下游功能（如成孔、激活防御基因）。典型的 helper NLR 包括 <span class="gene">NRG1</span>、<span class="gene">ADR1</span>（RNL 类）和 <span class="gene">NRC</span> 家族（CNL 类）。
  </p>

  <p>
    这种 sensor-helper 的分工模式具有重要的进化意义：sensor NLR 可以快速多样化以应对不断变化的效应子，而 helper NLR 保持相对保守，维持可靠的信号输出。这类似于适应性免疫中"识别"与"效应"功能的分离，是进化效率的体现。
  </p>

  <p>
    2026 年的结构研究进一步把 helper NLR 从“下游执行器”推进到“可聚合的信号平台”。Ge et al. (2026) 发现，CNL 型 sensor NLR SUMM2 激活后，可以诱导 EDS1-PAD4 与 ADR1-L1 组装成 helper NLR 抗病小体簇，而不是一条简单的线性通路。这个结果提示：helper NLR 的寡聚状态可能决定输出阈值、细胞死亡强度和防御基因激活比例，是未来解耦“有效防御”与“组织损伤”的关键调控层。
  </p>

  <!-- 4.7 HR -->
  <h2><span class="section-num">4.8</span>过敏性坏死反应 (HR) 的分子基础</h2>

  <p>
    HR 是 ETI 最显著的表型输出——受感染的细胞及其周围少量细胞迅速死亡，在叶片上形成可见的坏死斑点，将病原体（尤其是活体营养型病原体）封锁在死亡组织中。HR 的核心分子执行者现在被认为是 NLR 抗病小体形成的膜孔本身，以及其导致的 Ca²⁺ 内流。
  </p>

  <p>
    值得注意的是，细胞死亡与免疫信号是否可以解耦 <span class="english-term">(uncoupling)</span>，是领域内的重要争论之一。部分证据表明，NLR 可以在不引发明显 HR 的情况下激活免疫基因表达和抗病性，提示 NLR 的功能输出可能比"全有或全无"的细胞死亡更为精细。
  </p>

  <!-- ======== Key Question ======== -->
  <div class="box box-cognition"><div class="box-title">Key Question</div>
  <p><strong>NLR 介导的细胞死亡与免疫信号输出能否被彻底解耦？</strong></p>
  <p>如果可以解耦——即保留 NLR 的免疫信号输出（防御基因激活、SA 积累等）同时消除细胞死亡——那将在育种上具有巨大价值：抗性增强但没有 HR 带来的组织损伤代价。初步证据暗示 CNL 的成孔和信号输出可能有部分独立性（低水平的 Ca²⁺ 内流足以激活信号，但不足以杀死细胞），但这一假说的普遍适用性尚待验证。对 TNL 来说，由于信号通过酶产物传递给 helper NLR，理论上可以通过工程化 helper NLR 的活性来调控输出水平 <span class="cross-ref">→ 第14章</span>。</p>
  </div>

  <!-- ======== 里程碑研究 ======== -->
  <h2><span class="section-num">4.9</span>里程碑研究思路拆解</h2>

  <h3>里程碑 1：Wang et al. (2019a, 2019b) — ZAR1 抗病小体的结构解析</h3>

  <div class="box box-experiment">
    <div class="box-title">思路拆解</div>
    <p>
      <strong>面对的问题：</strong>NLR 蛋白激活后如何触发细胞死亡？尽管遗传学证据已积累数十年，但缺乏直接的结构和生化证据解释 NLR 从"感知效应子"到"执行死亡"的跨越。
    </p>
    <p style="margin-top:0.8rem;">
      <strong>关键思路：</strong>团队选择 ZAR1 作为研究对象，因为其生化性质较好且已有较完善的遗传背景。核心策略是<strong>在体外重建完整的激活复合体</strong>，然后用冷冻电镜逐步解析从静息态到激活态的构象变化。这一思路的关键创新在于：不是只解析一个终态结构，而是捕捉了<strong>三个连续状态</strong>（静息态、中间态、激活态），使得整个激活过程的动态机制一览无遗。
    </p>
    <p style="margin-top:0.8rem;">
      <strong>关键证据链：</strong>
    </p>
    <p>① 2019年冷冻电镜给出 ZAR1 五聚体及 N 端漏斗状结构；② 蛋白定位与功能分析支持这一结构与膜关联和免疫相关；③ 2021年的独立研究通过膜中组装及电生理等证据，支持该复合体具有可透 Ca²⁺ 的阳离子通道活性 (Bi et al., 2021)。第三步不能倒填为2019年已完成的证据。</p>
    <p style="margin-top:0.8rem;">
      <strong>影响：</strong>该工作将 NLR 从"信号感受器"重新定义为"信号执行器"，彻底改变了对植物 ETI 分子机制的理解，并被迅速写入教科书。
    </p>
  </div>

  <h3>里程碑 2：Horsefield et al. (2019) & Wan et al. (2019) — TIR 域的 NADase 活性</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>TNL 类 NLR 的 TIR 结构域如何传递信号？此前认为 TIR 仅作蛋白互作支架，但遗传证据表明其自身的某种酶活性对信号传递是必需的。</p>
  <p><strong>关键思路：</strong>两个独立团队通过结构和生化分析发现，TIR 域在寡聚化后获得 NAD⁺ 水解酶（NADase）活性，将 NAD⁺ 切割为烟酰胺和变体环化 ADP-核糖（v-cADPR）等产物。</p>
  <p><strong>关键证据链：</strong>体外酶学支持 TIR 的 NAD⁺ 转化活性，相关遗传功能支持酶活与免疫的联系。2019年酶活研究并未完成2022年才进一步明确的下游小分子配体—EDS1受体机制。v-cADPR 不能在这里直接替代后续鉴定的信号分子。</p>
  <p><strong>影响：</strong>揭示了 TNL 信号转导的全新生化机制，解释了 TNL 和 CNL 下游通路分歧的分子基础。也建立了植物 TIR 与动物 SARM1（一种同样具有 NADase 活性的 TIR 域蛋白）之间的功能平行关系。</p></div>

  <h3>里程碑 3：Cesari et al. (2014) & Le Roux et al. (2015) — 整合诱饵模型</h3>
  <div class="box box-experiment"><div class="box-title">思路拆解</div>
  <p><strong>面对的问题：</strong>NLR 如何应对效应蛋白靶标的多样性？如果效应蛋白靶向不同的宿主蛋白，植物是否需要为每个靶标单独演化一个 NLR？</p>
  <p><strong>关键思路：</strong>通过比较基因组学分析发现，许多 NLR 在经典结构域之外整合了额外的"非典型域"（ID），这些 ID 的序列与已知效应蛋白靶标同源。由此提出：NLR 通过将效应蛋白靶标整合为自身的一部分，以"钓鱼"方式捕获效应蛋白。</p>
  <p><strong>关键证据链：</strong>（1）水稻 RGA5 的 HMA 域直接结合 AVR-Pia；（2）拟南芥 RRS1 的 WRKY 域被 PopP2 乙酰化后触发 RPS4 激活；（3）全基因组分析揭示超过50种不同的 ID 类型。</p>
  <p><strong>影响：</strong>为合理设计新型 NLR 提供了清晰的策略框架：鉴定效应蛋白靶标 → 将靶标域工程整合进 NLR sensor → 配对 executor NLR。这一策略已在水稻抗稻瘟病中初步验证。</p></div>

  <!-- 4.10 Open Questions -->
  <h2><span class="section-num">4.10</span>当前争论与未解问题</h2>

  <ul class="questions-list">
    <li>
      <strong>抗病小体的通道选择性和调控机制尚不清楚。</strong>ZAR1 的阳离子通透性及不同离子的相对贡献如何影响免疫？是否存在内源性调控因子控制孔道的开闭？
    </li>
    <li>
      <strong>NLR 是否存在非细胞死亡依赖的免疫输出？</strong>部分实验表明 NLR 可以在不引发 HR 的情况下激活转录重编程，但分子机制不明。如何解耦"死亡"与"免疫"？
    </li>
    <li>
      <strong>不同 NLR 的寡聚化是否遵循统一机制？</strong>已经解析的 NLR 复合体具有不同聚合数，哪些结构约束决定这些差异？寡聚数目是否影响功能输出的强度和类型？
    </li>
    <li>
      <strong>NLR 的亚细胞定位如何影响其功能？</strong>部分 NLR 在激活前定位于细胞核，激活后是否需要重新定位到质膜才能成孔？核定位的 NLR 执行什么功能？
    </li>
    <li>
      <strong>NLR 网络的涌现性质。</strong>多个 sensor NLR 是否可以同时激活同一个 helper NLR？信号如何整合？是否存在阈值效应？
    </li>
  </ul>

  <p>2025 年的可激活 NLR 工程研究进一步把这个问题推向应用层面。Wang et al. (2025) 将天然自激活 NLR 改造成“病原蛋白酶激活”的免疫开关：只有当目标病原的特异性蛋白酶切割设计好的连接肽时，NLR 才解除抑制并触发广谱免疫。这一策略的重要性不只在于获得抗性，而在于它提供了一个新的设计原则——不是直接改变 NLR 的效应子识别界面，而是把病原体的保守酶活转化为免疫触发信号。结合 Ge et al. (2026) 对 helper NLR 抗病小体簇的解析，未来工程化的关键不只是“让 NLR 开启”，而是控制它开启后的聚合状态和输出强度。</p>

  <!-- 4.10 Methods -->
  <h2><span class="section-num">4.11</span>关键实验方法</h2>

  <table>
    <thead>
      <tr>
        <th>实验方法</th>
        <th>用途</th>
        <th>经典文献</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>冷冻电镜 <span class="english-term">(Cryo-EM)</span></td>
        <td>解析 NLR/抗病小体的三维结构</td>
        <td class="ref">Wang et al., 2019, Science</td>
      </tr>
      <tr>
        <td>电解质渗漏 <span class="english-term">(Electrolyte Leakage)</span></td>
        <td>检测组织膜完整性变化；需与其他死亡证据结合，不能把渗漏单独等同于 HR</td>
        <td class="ref">标准免疫表型方法</td>
      </tr>
      <tr>
        <td>脂质体重建 <span class="english-term">(Liposome Reconstitution)</span></td>
        <td>体外验证 NLR 的成孔活性和离子选择性</td>
        <td class="ref">Bi et al., 2021, Cell</td>
      </tr>
      <tr>
        <td>Co-IP / 免疫共沉淀</td>
        <td>验证 NLR 复合体的蛋白互作</td>
        <td class="ref">广泛使用</td>
      </tr>
      <tr>
        <td>体外 NADase 活性测定</td>
        <td>检测 TNL 的 TIR 结构域酶活性</td>
        <td class="ref">Horsefield et al., 2019, Science</td>
      </tr>
      <tr>
        <td>自激活突变体 <span class="english-term">(Autoactive mutant)</span></td>
        <td>模拟 NLR 持续激活状态，验证功能</td>
        <td class="ref">广泛使用</td>
      </tr>
    </tbody>
  </table>

  <!-- 4.11 Recommended Reading -->
  <div class="reading-section">
    <h2><span class="section-num">4.12</span>推荐阅读</h2>

    <div class="reading-level level-essential">
      <h4>🔴 必读</h4>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Wang J, Hu M, Wang J, <em>et al.</em></span>
          Reconstitution and structure of a plant NLR resistosome conferring immunity.
          <span class="journal"><em>Science</em>, 2019, 364(6435): eaav5870.</span>
        </div>
        <div class="reading-reason">首个完整的植物 NLR 激活态结构，确立了抗病小体概念，揭示 CNL 作为钙离子通道的机制。不读此文无法理解本章核心内容。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Wang J, Wang J, Hu M, <em>et al.</em></span>
          Ligand-triggered allosteric ADP release primes a plant NLR complex.
          <span class="journal"><em>Science</em>, 2019, 364(6435): eaav5868.</span>
        </div>
        <div class="reading-reason">ZAR1 静息态和中间态结构，完整展示了 NLR 从自抑制到激活的构象变化全过程。与上文为姊妹篇。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Dongus JA, Parker JE.</span>
          EDS1 signalling: At the nexus of intracellular and surface receptor immunity.
          <span class="journal"><em>Curr Opin Plant Biol</em>, 2021, 62: 102039.</span>
        </div>
        <div class="reading-reason">EDS1 枢纽与 TNL 信号通路的权威综述，系统梳理了 TNL-EDS1-helper NLR 轴的最新认知。</div>
      </div>
    </div>

    <div class="reading-level level-important">
      <h4>🟡 重要</h4>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Horsefield S, Burdett H, Zhang X, <em>et al.</em></span>
          NAD⁺ cleavage activity by animal and plant TIR domains in cell death pathways.
          <span class="journal"><em>Science</em>, 2019, 365(6455): 793-799.</span>
        </div>
        <div class="reading-reason">发现 TIR 结构域的 NADase 酶活性，改写了对 TNL 信号机制的理解。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Wang X, et al.</span>
          Remodelling autoactive NLRs for broad-spectrum immunity in plants.
          <span class="journal"><em>Nature</em>, 2025, 645: 737–745.</span>
        </div>
        <div class="reading-reason">把 NLR 的高风险自激活特性改造成病原蛋白酶依赖的可控免疫开关，是 NLR 工程从“改识别”走向“改激活逻辑”的代表。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Ge D, Ortiz-Morea FA, Xie Y, et al.</span>
          Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR.
          <span class="journal"><em>Nature</em>, 2026, 652: 251–258.</span>
        </div>
        <div class="reading-reason">把 helper NLR 从线性下游执行器推进为可聚合的抗病小体簇。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Adachi H, Derevnina L, Kamoun S.</span>
          NLR singletons, pairs, and networks: evolution, assembly, and regulation of the intracellular immunoreceptor circuitry of plants.
          <span class="journal"><em>Curr Opin Plant Biol</em>, 2019, 50: 121-131.</span>
        </div>
        <div class="reading-reason">NLR 网络概念的系统阐述，清晰梳理了 sensor-helper 分工与进化逻辑。</div>
      </div>
    </div>

    <div class="reading-level level-extended">
      <h4>🟢 拓展</h4>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Bi G, Su M, Li N, <em>et al.</em></span>
          The ZAR1 resistosome is a calcium-permeable channel triggering plant immune signaling.
          <span class="journal"><em>Cell</em>, 2021, 184(13): 3528-3541.</span>
        </div>
        <div class="reading-reason">直接证明 ZAR1 抗病小体是可透 Ca²⁺ 的阳离子通道，从电生理层面补全了机制拼图。</div>
      </div>

      <div class="reading-item">
        <div class="reading-ref">
          <span class="authors">Kourelis J, van der Hoorn RAL.</span>
          Defended to the nines: 25 years of resistance gene cloning identifies nine mechanisms for R protein function.
          <span class="journal"><em>Plant Cell</em>, 2018, 30(2): 285-299.</span>
        </div>
        <div class="reading-reason">从进化角度总结 R 蛋白的九种工作机制，有助于在更大的框架下理解 NLR 的多样化策略。</div>
      </div>
    </div>
  </div>

  <!-- ======== 参考文献 ======== -->
  <h2><span class="section-num">4.13</span>参考文献</h2>
  <ol class="references">
    <li>Adachi H, Derevnina L, Kamoun S. NLR singletons, pairs, and networks: evolution, assembly, and regulation of the intracellular immunoreceptor circuitry of plants. <em>Curr Opin Plant Biol</em>, 2019, 50: 121–131.</li>
    <li>Bi G, Su M, Li N, et al. The ZAR1 resistosome is a calcium-permeable channel triggering plant immune signaling. <em>Cell</em>, 2021, 184: 3528–3541.e12. <a href="https://doi.org/10.1016/j.cell.2021.05.003">DOI</a>.</li>
    <li>Cesari S, Bernoux M, Moncuquet P, et al. A novel conserved mechanism for plant NLR protein pairs: the "integrated decoy" hypothesis. <em>Front Plant Sci</em>, 2014, 5: 606.</li>
    <li>Cesari S, Thouri M, Broz P, et al. The rice resistance protein pair RGA4/RGA5 recognizes the <em>Magnaporthe oryzae</em> effectors AVR-Pia and AVR1-CO39 by direct binding. <em>Plant Cell</em>, 2013, 25: 1463–1481.</li>
    <li>Dongus JA, Parker JE. EDS1 signalling: at the nexus of intracellular and surface receptor immunity. <em>Curr Opin Plant Biol</em>, 2021, 62: 102039.</li>
    <li>Ge D, Ortiz-Morea FA, Xie Y, et al. Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. <em>Nature</em>, 2026, 652: 251–258. DOI: 10.1038/s41586-026-10215-1.</li>
    <li>Horsefield S, Burdett H, Zhang X, et al. NAD⁺ cleavage activity by animal and plant TIR domains in cell death pathways. <em>Science</em>, 2019, 365: 793–799.</li>
    <li>Huang S, Jia A, Song W, et al. Identification and receptor mechanism of TIR-catalyzed small molecules in plant immunity. <em>Science</em>, 2022, 377: eabq3297. <a href="https://doi.org/10.1126/science.abq3297">DOI</a>.</li>
    <li>Jia A, Huang S, Song W, et al. TIR-catalyzed ADP-ribosylation reactions produce signaling molecules for plant immunity. <em>Science</em>, 2022, 377: eabq8180. <a href="https://doi.org/10.1126/science.abq8180">DOI</a>.</li>
    <li>Kourelis J, van der Hoorn RAL. Defended to the nines: 25 years of resistance gene cloning identifies nine mechanisms for R protein function. <em>Plant Cell</em>, 2018, 30: 285–299.</li>
    <li>Kroj T, Chanclud E, Michel-Romiti C, et al. Integration of decoy domains derived from protein targets of pathogen effectors into plant immune receptors is widespread. <em>New Phytol</em>, 2016, 210: 618–626.</li>
    <li>Lapin D, Bhandari DD, Parker JE. Origins and immunity networking functions of EDS1 family proteins. <em>Annu Rev Phytopathol</em>, 2022, 60: 253–276.</li>
    <li>Le Roux C, Huet G, Jauneau A, et al. A receptor pair with an integrated decoy converts pathogen disabling of transcription factors to immunity. <em>Cell</em>, 2015, 161: 1074–1088.</li>
    <li>Maqbool A, Saitoh H, Franceschetti M, et al. Structural basis of pathogen recognition by an integrated HMA domain in a plant NLR immune receptor. <em>eLife</em>, 2015, 4: e08709.</li>
    <li>Sarris PF, Cevik V, Dagdas G, et al. Comparative analysis of plant immune receptor architectures uncovers host proteins likely targeted by pathogens. <em>BMC Biol</em>, 2016, 14: 8.</li>
    <li>Sarris PF, Duxbury Z, Huh SU, et al. A plant immune receptor detects pathogen effectors that target WRKY transcription factors. <em>Cell</em>, 2015, 161: 1089–1100.</li>
    <li>van der Hoorn RAL, Kamoun S. From guard to decoy: a new model for perception of plant pathogen effectors. <em>Plant Cell</em>, 2008, 20: 2009–2017.</li>
    <li>Wan L, Essuman K, Anderson RG, et al. TIR domains of plant immune receptors are NAD⁺-cleaving enzymes that promote cell death. <em>Science</em>, 2019, 365: 799–803.</li>
    <li>Wang J, Hu M, Wang J, et al. Reconstitution and structure of a plant NLR resistosome conferring immunity. <em>Science</em>, 2019a, 364: eaav5870.</li>
    <li>Wang J, Wang J, Hu M, et al. Ligand-triggered allosteric ADP release primes a plant NLR complex. <em>Science</em>, 2019b, 364: eaav5868.</li>
    <li>Wang X, Ji C, Wang L, et al. Remodelling autoactive NLRs for broad-spectrum immunity in plants. <em>Nature</em>, 2025, 645: 737–745. DOI: 10.1038/s41586-025-09252-z.</li>
  </ol>

  <!-- Chapter Navigation -->

  <section class="chapter-review"><h2>本章小结与自测</h2><p>先遮住解析，用自己的话作答。能说明“为什么”，比复述缩写更能检验理解。</p>
  <h3>理解题 4.1：为什么不能把“所有 CNL 都是五聚体钙通道”当作定义？</h3><details><summary>查看解析</summary><p>CNL 依据 N 端 CC 域及相关谱系特征分类，不由聚合数定义。ZAR1 是明确实例，其他 CNL 的组装、伙伴需求和执行方式有差异；代表性机制不能替代整个类别的定义。</p></details>
  <h3>理解题 4.2：2019年与2021年的 ZAR1 论文分别回答了什么问题？</h3><details><summary>查看解析</summary><p>2019年的结构研究解释激活态五聚体的构象及与膜关联相关的漏斗状结构。2021年的成像和电生理等证据支持其为可透 Ca²⁺ 的阳离子通道，并联系到植物细胞的信号与死亡。结构线索与通道功能证明应分开归功。</p></details>
  <h3>理解题 4.3：TNL 产生小分子信号，为何仍需要辅助 NLR？</h3><details><summary>查看解析</summary><p>产生信号和执行输出是不同任务。在已解析体系中，TIR 酶活产生的特定小分子由 EDS1 异源二聚体感知，促进其与 ADR1 或 NRG1 类伙伴耦合，进而推动下游免疫。不能把 TIR 消耗 NAD⁺ 简化为直接耗尽细胞能量致死。</p></details>
  <p><strong>复习任务：</strong>画一张不超过六个节点的本章概念图，并在每条箭头旁写出关系：直接作用、间接依赖、相关性或待验证假说。若无法确定，应保留问号。</p></section>
<nav class="chapter-nav">
    <a href="../ch03-受体与信号转导/"><div><span class="nav-label">上一章</span>← 第3章 受体与信号转导</div></a>
    <a href="../ch05-激素信号网络/"><div style="text-align:right;"><span class="nav-label">下一章</span>第5章 激素信号网络 →</div></a>
  </nav>
</div>
