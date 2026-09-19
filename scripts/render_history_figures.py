"""Render original, accessible SVG teaching diagrams for the history series.

Conceptual diagrams, not structural coordinates or experimental data.
Source papers and scope are cited in the accompanying Markdown captions.
No third-party runtime dependency is required.
"""
from pathlib import Path
from html import escape
import math

OUT = Path(__file__).resolve().parents[1] / 'docs/assets/images/textbook'
INK, MUTED, GREEN, BLUE, GOLD = '#19372f', '#50655e', '#18755e', '#315d97', '#a56820'


class Figure:
    def __init__(self, title, subtitle, height, desc):
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{height}" viewBox="0 0 720 {height}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
                      '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9" fill="#627e72"/></marker></defs>',
                      '<style>text{font-family:"Microsoft YaHei","Noto Sans CJK SC",sans-serif} .heading{font-weight:700}</style>',
                      f'<rect width="720" height="{height}" fill="#f7faf7"/>']
        self.text(36, 53, title, 31, INK, True)
        self.text(36, 90, subtitle, 22, MUTED)

    def text(self, x, y, value, size=24, color=INK, bold=False, anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" class="{"heading" if bold else "body"}">{escape(value)}</text>')

    def lines(self, x, y, values, size=24, color=INK, gap=35):
        for i, value in enumerate(values):
            self.text(x, y+i*gap, value, size, color)

    def rect(self, x, y, w, h, fill='#ffffff', stroke='#d6e3da', radius=16):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

    def circle(self, x, y, r, fill=GREEN):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')

    def arrow(self, x1, y1, x2, y2):
        self.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="#627e72" stroke-width="3" marker-end="url(#arrow)"/>')

    def footer(self, lines):
        self.lines(36, self.height-57, lines, 20, MUTED, 29)

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / name).write_text('\n'.join(self.parts+['</svg>'])+'\n', encoding='utf-8')


def fls2():
    f = Figure('FLS2：受体身份怎样逐层建立', '四类证据，各自回答一个不同问题', 1010,
               '2000年遗传必要性，2006年直接结合与识别特征，2007年共同受体组装，2013年胞外复合体结构。箭头表示认识接续。')
    cards = [
        ('2000', '这个基因是否必要？', ['响应缺陷 → 定位与克隆', 'FLS2具有受体样结构', '还需区分：感知者，还是感知的助手？']),
        ('2006', '它是否承担配体识别？', ['配体结合 + 识别特征随FLS2转移', '支持FLS2决定主要识别选择性', '还需解释：识别怎样连接激活？']),
        ('2007', '刺激以后怎样组成信号单位？', ['FLS2与BAK1出现配体相关关联', '从单个受体，走向共同受体复合体', '关联证据尚未显示每个分子的接触。']),
        ('2013', '共同受体为什么能被招募？', ['flg22与FLS2结合，也参与BAK1接触', '胞外结构解释联合识别与组装', '并未独自排定全部胞内磷酸化次序。'])]
    for i, (year, title, lines) in enumerate(cards):
        y = 120 + i*202
        f.rect(30, y, 660, 178)
        f.rect(48, y+17, 87, 40, '#e2f0e8', '#e2f0e8', 9)
        f.text(91, y+46, year, 24, GREEN, True, 'middle')
        f.text(152, y+46, title, 25, INK, True)
        f.lines(51, y+87, lines, 23, MUTED, 32)
        if i<3: f.arrow(360, y+179, 360, y+196)
    f.footer(['原创概念图；箭头表示证据推进，不是细胞内反应时序。', '完整分子机制、来源与适用范围见本篇正文。'])
    f.save('history-fls2-evidence.svg')


def zar1():
    f=Figure('ZAR1：从结构到通道，差了哪一步', '形状提出假说，功能证据决定怎样解释形状', 1020,
             '2015年宿主状态识别，2019年活化五聚体，2021年离子通道证据。示意圆圈不代表原子结构。')
    f.rect(30, 121, 660, 218)
    f.text(51, 162, '2015  输入与伙伴分工', 26, GREEN, True)
    f.lines(51, 205, ['PBL2的特定状态：被读取的宿主信息', 'RKS1：连接状态读取与受体变化', 'ZAR1：受体活化与执行装配'], 24, INK, 36)
    f.arrow(360, 340, 360, 364)
    f.rect(30, 376, 660, 250)
    f.text(51, 418, '2019  活化后形成五聚体', 26, GREEN, True)
    for i in range(5):
        a=-math.pi/2+i*2*math.pi/5
        f.circle(136+59*math.cos(a), 511+59*math.sin(a), 25, GREEN)
    f.text(136, 606, '五聚体示意', 21, MUTED, False, 'middle')
    f.lines(248, 476, ['氨基端重排，出现漏斗状组织', '提供可能作用于膜的结构依据', '但尚未直接测到离子电流。'], 23, INK, 39)
    f.arrow(360, 628, 360, 652)
    f.rect(30, 664, 660, 243)
    f.text(51, 707, '2021  通道功能获得独立证据', 26, GREEN, True)
    f.lines(51, 752, ['膜中组织 + 电生理 + 植物功能相互支持', '活化ZAR1五聚体：钙通透的阳离子通道', '“钙通透”不表示只能让钙离子通过。', '一个ZAR1范例不决定全部NLR的工作方式。'], 23, INK, 36)
    f.footer(['原创概念图；圆圈仅表示亚基数目，不是实验结构。', '分别对应2015、2019与2021年原始研究。'])
    f.save('history-zar1-evidence.svg')


def eds1():
    f=Figure('EDS1：先分清两种异二聚体', '以2022年两类TIR来源信号研究为主线', 880,
             'TIR相关酶活动产生不同核苷酸信号。pRib-AMP或pRib-ADP联系EDS1-PAD4和ADR1；ADPr-ATP或di-ADPR联系EDS1-SAG101和NRG1。分支并非绝对独立。')
    f.rect(104, 126, 512, 86, '#e2f0e8')
    f.text(360, 162, 'TIR相关酶活动', 27, GREEN, True, 'middle')
    f.text(360, 193, '产生可被下游读取的小分子信号', 22, INK, False, 'middle')
    f.arrow(275, 215, 192, 263); f.arrow(445, 215, 528, 263)
    for x, label, ligand, helper, color in [
        (30,'EDS1–PAD4',['pRib-AMP','pRib-ADP'],'ADR1家族', GREEN),
        (374,'EDS1–SAG101',['ADPr-ATP','di-ADPR'],'NRG1家族', BLUE)]:
        f.rect(x, 280, 316, 291)
        f.text(x+158, 326, '配体类别', 24, MUTED, False, 'middle')
        f.text(x+158, 362, ' / '.join(ligand) if x==374 else ligand[0]+' /', 23, color, True, 'middle')
        if x==30: f.text(x+158, 393, ligand[1], 23, color, True, 'middle')
        f.arrow(x+158, 414, x+158, 443)
        f.text(x+158, 482, label, 26, color, True, 'middle')
        f.text(x+158, 526, '一个EDS1 + 一个伙伴', 21, MUTED, False, 'middle')
        f.arrow(x+158, 573, x+158, 609)
        f.rect(x, 625, 316, 76, '#edf2f8' if x==374 else '#e2f0e8')
        f.text(x+158, 674, helper, 27, color, True, 'middle')
    f.lines(36, 746, ['分工有偏向，但不能简化为“一个只管抗性，另一个只管死亡”。', '具体家族成员、植物背景及其他输入，需要回到原论文判断。'], 20, MUTED, 31)
    f.footer(['原创概念图；EDS1–PAD4与EDS1–SAG101是不同复合体。', '本图未将三种EDS1家族蛋白画成一个固定三聚体。'])
    f.save('history-eds1-branches.svg')


def npr1():
    f=Figure('NPR1：位置、伙伴与状态共同决定功能', '核内与胞质是不同工作背景，不是一条固定转换路线', 1050,
             '核内NPR1与TGA转录因子共同调节表达；2022年结构显示NPR1二聚体连接两个TGA3二聚体。胞质SINCs联系蛋白稳态和细胞存活。')
    f.rect(30, 122, 660, 374, '#edf2f8')
    f.text(52, 167, '核内：转录共调控', 29, BLUE, True)
    f.lines(52, 208, ['2022年结构：NPR1二聚体连接两个TGA3二聚体。', 'NPR1提供协作组织，TGA承担DNA识别相关任务。'], 22, INK, 34)
    for cx, label, color in [(123,'TGA3×2',BLUE),(360,'NPR1×2',GREEN),(597,'TGA3×2',BLUE)]:
        f.rect(cx-76, 279, 152, 84, '#ffffff')
        f.circle(cx-20, 306, 14, color);f.circle(cx+20, 306, 14, color)
        f.text(cx, 348, label, 22, color, True, 'middle')
    f.parts.append('<path d="M199,321 L284,321 M436,321 L521,321" stroke="#627e72" stroke-width="4"/>')
    f.lines(52, 409, ['核定位与伙伴关系，仍需与SA响应和周转相结合。', '功能性二聚体不能被“活化后永远是单体”概括。'], 22, INK, 35)
    f.rect(30, 525, 660, 252, '#e2f0e8')
    f.text(52, 570, '胞质：SINCs与蛋白稳态', 29, GREEN, True)
    f.lines(52, 614, ['2020年研究将SA诱导的NPR1凝聚体', '与Cullin3相关底物调控和细胞存活联系。', '看见斑点只是起点，还要解释组成和生理功能。', '这一角色扩展了以核内转录为中心的早期模型。'], 23, INK, 37)
    f.rect(30, 807, 660, 127, '#fff6e8', '#ead7b8')
    f.text(52, 849, '阅读历史模型时，先确认所测的“状态”', 25, GOLD, True)
    f.lines(52, 889, ['提取后的高分子条带、功能性二聚体和凝聚体，', '是不同证据对象，不能仅按“聚集”一词合并。'], 22, INK, 32)
    f.footer(['原创概念图；未表达所有复合体、转录步骤或SA依赖关系。', '2026年MED15A相关进展及不同团队贡献见正文。'])
    f.save('history-npr1-contexts.svg')


if __name__ == '__main__':
    for render in (fls2, zar1, eds1, npr1):
        render()
    print('Rendered 4 original history teaching diagrams.')
