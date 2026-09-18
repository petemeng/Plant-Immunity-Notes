# ADR1与NRG1研究史：NLR从识别者走向信号执行者

## 先分清“家族”与“功能角色”

ADR1和NRG1分别代表辅助型NLR的两个家族，不是同一个基因，也不意味着每种植物只有各一个成员。在拟南芥中讨论ADR1家族时，往往包括ADR1及相关旁系同源成员；NRG1也存在多个成员。它们属于具有RPW8样氨基端特征的RNL类。**RNL是结构分类，helper NLR是功能描述，二者不能在整个植物界无条件画等号。**

这段历史要回答：如果某个NLR并不主要决定识别哪个外来线索，它为什么仍然是免疫必需因子？阅读前先理解“传感受体”和“下游执行环节”的区别，以及同一家族成员之间的功能冗余。

## 关键年表

| 年份 | 关键认识 | 原始论文 |
|---|---|---|
| 2005 | N介导抗性需要另一个NLR NRG1 | [Peart等](https://pubmed.ncbi.nlm.nih.gov/15916955/) |
| 2011 | ADR1家族具有超出特异识别的免疫功能 | [Bonardi等](https://doi.org/10.1073/pnas.1113726108) |
| 2019 | 辅助NLR与EDS1伙伴形成特定功能模块 | [Lapin等](https://doi.org/10.1105/tpc.19.00118) |
| 2021 | NRG1与EDS1-SAG101的激活相关关联被观察 | [Sun等](https://pubmed.ncbi.nlm.nih.gov/34099661/) |
| 2021 | NRG1.1与ADR1的阳离子通道功能获得证据 | [Jacob等](https://pubmed.ncbi.nlm.nih.gov/34140391/) |
| 2021 | ADR1联系也进入细胞表面受体信号模型 | [Pruitt等](https://doi.org/10.1038/s41586-021-03829-0) |

## 第一阶段：一个抗性受体为什么还需要另一个NLR

Peart等2005年围绕烟草N相关抗性开展研究，发现NRG1是必要组分。它自身也具有NLR特征，却与N共同工作。这动摇了当时容易形成的直觉：每一个NLR都应对应一个独立的特异识别事件。更合理的可能是，NLR家族内部存在分工，某些成员承担多个识别系统需要的下游任务（Peart等，2005）。

但“需要”不等于已经知道怎样协作。遗传缺陷可能来自信号传递，也可能来自蛋白稳定性、定位或细胞状态。因此早期发现首先建立功能依赖，而没有直接给出完整分子传递过程。后来将NRG1称为辅助受体，是对不断积累证据的总结。

这个发现也说明围绕一个经典基因进行研究，可能意外改变整个家族的分类方式。N的故事不再局限于一个抗病毒受体，而成为理解不同NLR如何组织成系统的入口，详见[N研究史](N.md)。

## 第二阶段：ADR1家族把共享功能带到前台

2011年Bonardi等研究ADR1家族，将其与多类免疫反应中的水杨酸积累和防御功能联系起来。论文的思路不是寻找新的外来结合对象，而是比较多个家族成员及不同免疫情境，判断共同需要的过程是什么（Bonardi等，2011）。

这里的家族冗余很重要。若只改变一个成员，其他成员可能补偿，于是容易低估整个家族的作用。反过来，多成员缺失造成的广泛表型，也不能自动归因于某一单独蛋白直接参与所有反应。研究单位由单基因扩展为家族，需要更谨慎地讨论因果层次。

这篇论文还提醒读者，不同NLR的分子要求未必与一个标准模板完全相同。历史上观察到的特定成员、特定构型的性质，应按原实验条件理解，不能推广成“所有辅助NLR都不需要通常的核苷酸开关”。

## 第三阶段：从辅助标签走向可区分的模块

2019年的Lapin等研究把EDS1-SAG101与NRG1联系到共同演化的细胞死亡信号模块，并与EDS1-PAD4相关功能比较。2021年Sun等进一步将NRG1的伙伴联系与免疫激活状态连接。这让“辅助”不再只是一个位置模糊的标签，而成为可用物理关系与遗传关系同时描述的系统（Lapin等，2019；Sun等，2021）。

应注意，分支的功能偏好不等于互不相干。细胞死亡、防御转录、激素变化与实际抗性可以被部分分离，也会互相影响。观察到某分支更强地影响某个读出，不能把其他输出从其作用范围永久删除。

跨物种结果也应保留原有边界。拟南芥与本氏烟为机制比较提供了不同配置；兼容伙伴的组合很关键。但一种外源蛋白在另一个物种中失效，可能反映接口不匹配，而不是该蛋白在原物种没有功能。

## 第四阶段：辅助者本身成为离子通道

2021年Jacob等结合NRG1.1氨基端信号结构域的晶体结构、细胞定位、离子流及功能证据，支持活化NRG1.1和ADR1具有可通透钙离子的非选择性阳离子通道作用。这里解析的是NRG1.1的结构域，不能误读为当年已经获得两个完整活化通道的原子结构。由此，辅助NLR从“传感器后面还有未知的信号因子”转变成能够直接改变细胞离子状态的执行组分（Jacob等，2021）。

“非选择性阳离子通道”与“只让钙通过的专一通道”含义不同。钙是重要信号离子，不代表通道只允许钙通行。也不能因为异源细胞中观察到导通，就忽略植物细胞中是否形成同样组装及其生理调控；正需要不同体系的证据互相补充。

同年Pruitt等把EDS1-PAD4-ADR1节点与RLP23介导的表面免疫联系起来。这并不抹去表面受体与胞内受体的差别，而是说明它们可能使用共同的信号资源。识别发生在哪里，与信号最后汇入哪里，是两个不同问题（Pruitt等，2021）。

## 怎样读论文而不被箭头带着走

读2005年论文时问“缺少NRG1后哪个功能丢失”；读2011年论文时问“一个成员与整个家族的结论是否区分”；读2021年通道论文时问“结构、膜位置、离子流与免疫后果是否形成闭环”。三个时代分别解决必要性、功能范围与生化作用，不能彼此替代。

尚未完全解决的层面包括不同细胞中的激活阈值、通道关闭、辅助受体组合及组织间协调。研究史中的核心收益不是记住一张永不变化的通路图，而是理解为什么一个原本按识别功能命名的蛋白家族，能够分化出信号执行者。

贡献来自Peart、Mestre、Baulcombe等围绕N系统的工作，Bonardi、Tang、Dangl等ADR1研究，Lapin、Sun、Parker及合作者的模块分析，以及Jacob、Kim、Wu等跨学科通道研究。Pruitt等又把问题连接到表面免疫，这些路线共同改变了NLR的功能图景。

## 自测

复习时应给每个辅助受体结论加上一个范围说明，例如某成员、某物种、某种读出。这个简单习惯能够防止把家族性质强加给所有成员，也能帮助比较为什么不同论文在细胞死亡和抗性上得到不完全一致的结果。

**1. 一个ADR1单突变没有明显表型，能否否定家族作用？**

不能。家族成员可能冗余，单个缺失只检验该成员在特定背景中的不可替代性，不能代表整个家族。

**2. “辅助NLR”是不是指功能不重要的次要受体？**

不是。辅助是分工术语；它们可承担多个传感系统共同需要的信号或执行任务，缺失后可能造成广泛影响。

## 原始论文

1. Peart JR, Mestre P, Lu R, Malcuit I, Baulcombe DC. *NRG1, a CC-NB-LRR protein, together with N, a TIR-NB-LRR protein, mediates resistance against tobacco mosaic virus.* Current Biology, 2005. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15916955/)。
2. Bonardi V, Tang S, Stallmann A, Roberts M, Cherkis K, Dangl JL. *Expanded functions for a family of plant intracellular immune receptors beyond specific recognition of pathogen effectors.* PNAS, 2011. [DOI](https://doi.org/10.1073/pnas.1113726108)。阅读时同时查看期刊所附更正。
3. Lapin D, Kovacova V, Sun X, et al. *A Coevolved EDS1-SAG101-NRG1 Module Mediates Cell Death Signaling by TIR-Domain Immune Receptors.* The Plant Cell, 2019. [DOI](https://doi.org/10.1105/tpc.19.00118)。
4. Sun X, Lapin D, Feehan JM, et al. *Pathogen effector recognition-dependent association of NRG1 with EDS1 and SAG101 in TNL receptor immunity.* Nature Communications, 2021. [PubMed](https://pubmed.ncbi.nlm.nih.gov/34099661/)。
5. Jacob P, Kim NH, Wu F, et al. *Plant “helper” immune receptors are Ca2+-permeable nonselective cation channels.* Science, 2021. [PubMed](https://pubmed.ncbi.nlm.nih.gov/34140391/)。
6. Pruitt RN, Locci F, Wanke F, et al. *The EDS1–PAD4–ADR1 node mediates Arabidopsis pattern-triggered immunity.* Nature, 2021. [DOI](https://doi.org/10.1038/s41586-021-03829-0)。

<!-- HISTORY READING LINKS -->
## 配套阅读

以下按相关科学问题连接；具体发现归属以正文原始文献为准。

[Jonathan D. G. Jones](../labs/Jones.md) · [Jane E. Parker](../labs/Parker.md) · [Barbara Baker](../labs/Baker.md) · [全部课题组](../labs/index.md) · [基因目录](index.md)
