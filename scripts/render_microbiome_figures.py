"""Original teaching SVGs for chapters 24–27; no third-party dependencies.

Sources and interpretation boundaries are recorded in the chapter captions.
The abundance example is invented arithmetic, not measured biological data.
"""
from pathlib import Path
from html import escape
import unicodedata
import re

OUT = Path(__file__).resolve().parents[1] / 'docs/assets/images/textbook'
GREEN, BLUE, INK, MUTED = '#176c55', '#315f91', '#193a30', '#52685f'


def wrap(text, width, size):
    lines, current, used = [], '', 0
    # Keep Latin identifiers intact and attach closing punctuation to its word.
    tokens = []
    for token in re.findall(r'[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*|.', text):
        if token in '，。；：、！？）)]%' and tokens:
            tokens[-1] += token
        else:
            tokens.append(token)
    for token in tokens:
        step = sum(size * (1 if unicodedata.east_asian_width(char) in 'WF' else .57) for char in token)
        if used + step > width and current:
            lines.append(current); current, used = '', 0
        current += token; used += step
    if current:
        lines.append(current)
    return lines


class Diagram:
    def __init__(self, title, subtitle, desc):
        self.title, self.desc = title, desc
        self.parts = ['<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#718d7d"/></marker></defs>']
        self.y = self.paragraph(30, 45, title, 620, 30, INK, True) + 12
        self.y = self.paragraph(30, self.y, subtitle, 620, 23, MUTED) + 28

    def text(self, x, y, value, size=25, color=INK, bold=False):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{escape(value)}</text>')

    def paragraph(self, x, y, value, width, size=25, color=INK, bold=False):
        for line in wrap(value, width, size):
            self.text(x, y, line, size, color, bold)
            y += size * 1.45
        return y

    def rect(self, x, y, w, h, fill='#ffffff', stroke='#d4e3d9', weight=2, radius=15):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{weight}"/>')

    def arrow(self, x1, y1, x2, y2, dashed=False):
        dash='stroke-dasharray="8 7"' if dashed else ''
        self.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#718d7d" stroke-width="3" fill="none" {dash} marker-end="url(#arrow)"/>')

    def card(self, title, lines, color=GREEN, fill='#ffffff', arrow=False):
        if arrow:
            self.arrow(340, self.y-12, 340, self.y+9)
            self.y += 24
        title_lines=wrap(title, 570, 26)
        body_lines=[line for text in lines for line in wrap(text, 570, 24)]
        h=28+len(title_lines)*38+12+len(body_lines)*35+12
        self.rect(26, self.y, 628, h, fill)
        yy=self.y+37
        for line in title_lines:
            self.text(47, yy, line, 26, color, True); yy+=38
        yy+=5
        for line in body_lines:
            self.text(47, yy, line, 24); yy+=35
        self.y+=h+22

    def paired(self, items, gap=20):
        widths=304
        height=max(75+sum(len(wrap(s,262,23)) for s in lines)*34 for title,lines in items)
        for (title,lines),x,color in zip(items,(26,350),(GREEN,BLUE)):
            self.rect(x,self.y,widths,height,'#eef5ef' if x==26 else '#eef3f9')
            self.text(x+20,self.y+37,title,25,color,True)
            yy=self.y+79
            for value in lines:
                yy=self.paragraph(x+20,yy,value,262,23)
        self.y+=height+gap

    def note(self, text):
        self.y=self.paragraph(32,self.y+14,text,612,22,MUTED)+18

    def save(self, name):
        self.note('原创教学示意；具体来源与适用范围见本章图注。')
        height=int(self.y+12)
        head=f'<svg xmlns="http://www.w3.org/2000/svg" width="680" height="{height}" viewBox="0 0 680 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(self.title)}</title><desc id="desc">{escape(self.desc)}</desc><style>text{{font-family:"Microsoft YaHei","Noto Sans CJK SC",sans-serif}}</style><rect width="680" height="{height}" fill="#f8faf6"/>'
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/name).write_text(head+'\n'+'\n'.join(self.parts)+'\n</svg>\n',encoding='utf-8')


def habitats():
    d=Diagram('24.1 同一株植物，多种微生物环境','先定位在哪里，再讨论如何共处','根际、根表、根内与叶表、叶内是不同生态区室；空间联系不等于必经定殖流程。')
    d.card('根部：从来源环境到宿主内部',['土壤：提供潜在成员的来源库','根际：根活动改变周围资源与化学环境','根表：与植物表面接触','根内：内部组织具有不同约束'])
    d.paired([('叶表',['暴露于空气和外界输入','水分、光照等不断变化']),('叶内',['存在于组织内部的空间','受宿主生理与免疫调节'])])
    d.card('为什么区室必须分清？',['整根或整叶的平均值，会混合不同位置的信息。','在一个区室检测到成员，不等于它在所有位置都活跃。'],fill='#fff7e8')
    d.note('定殖不等于致病。这里比较空间环境，未表示所有微生物沿同一路线进入植物。')
    d.save('ch24-habitats.svg')


def host_community():
    d=Diagram('24.2 群落由多种过程共同塑造','宿主、资源与微生物之间持续相互影响','免疫、营养、宿主分泌物和跨界互作共同影响群落，群落也影响宿主营养和健康。')
    d.card('共同背景',['土壤来源库 × 宿主基因型 × 发育与环境'])
    d.paired([('宿主免疫',['模式感知','组织边界与稳态']),('资源与代谢',['铁可利用性等','根分泌物及局部化学环境'])])
    d.card('微生物之间的关系',['资源竞争、功能互补、跨界制约','某一成员的表现取决于周围伙伴。'])
    d.card('群落组成、数量与功能',['这些过程共同改变群落；群落也反馈影响宿主营养和健康。'],fill='#e6f1e9',arrow=True)
    d.note('营养收益与抗病收益需要分别评价。连线表达综合关系，并非一条已完全解析的单向通路。')
    d.save('ch24-host-community.svg')


def dysbiosis():
    d=Diagram('24.3 组成变化不等于菌群失衡','健康后果与因果关系，是判断的关键','稳态、群落组成改变和伴随宿主损伤的失衡需要区分。')
    d.card('稳态',['微生物群落存在，宿主组织保持健康。','稳定并不要求每个成员比例永远不变。'])
    d.card('组成发生变化',['可能反映组织发育、营养或环境差异。','仅凭多样性或某个类群比例，还不能判断健康。'],color=BLUE)
    d.card('与宿主损伤有关的失衡',['结合群落数量、成员构成与组织健康。','仍要区分：群落引起损伤，还是损伤改变群落？'],fill='#fff7e8')
    d.card('因果判断需要补上的证据',['时间关系、宿主背景和功能比较相互约束。','同一张群落组成图，不能独自完成这些判断。'])
    d.save('ch24-dysbiosis.svg')


def symbioses():
    d=Diagram('25.1 三类共处关系，三种判断重点','典型体系的对照，不是全部植物的统一模型','典型豆科根瘤、丛枝菌根与一般共栖的结构和收益不同。')
    d.card('典型豆科—根瘤菌共生',['形成根瘤及细胞内共生体','固定氮 → 植物；植物碳 → 微生物','有根瘤，不等于已获得有效固定氮。'])
    d.card('丛枝菌根（AM）',['根皮层细胞形成丛枝交换界面','磷等矿质营养 → 植物；植物碳/脂质 → 真菌','有定殖，不等于植物净收益一定增加。'],color=BLUE)
    d.card('一般共栖',['可存在于表面或内部，不必形成专门交换结构。','关系与功能需在具体宿主和环境中评价。'])
    d.note('“共生”一词在不同文献中有宽窄用法；本章重点讨论具有专门宿主程序的根瘤与AM互作。')
    d.save('ch25-symbioses.svg')


def recognition():
    d=Diagram('25.2 从信号识别到不同细胞程序','共享组件不等于所有输入都通向同一结果','宿主受体组合读取LCO与几丁质相关信息，共同共生信号模块与免疫响应需按背景区分。')
    d.card('输入：多种相关分子信息',['Nod-LCO、Myc-LCO及几丁质寡糖等','结构、修饰与组合影响宿主响应。'])
    d.card('宿主受体组合',['LysM受体及其伙伴，依宿主与细胞背景而变。','部分组分参与多种响应，例如水稻OsCERK1。'],arrow=True)
    d.paired([('共生相关程序',['核内/核周钙振荡','CCaMK → CYCLOPS','连接共生细胞与器官程序']),('免疫相关输出',['具有相应免疫信号连接','不同伙伴与细胞状态','不能仅按糖链长短二分'])])
    d.note('CSSP：共同共生信号通路。图省略中间组分；箭头不全表示直接结合，CSSP也不是所有共栖的必经路线。')
    d.save('ch25-recognition.svg')


def exchange():
    d=Diagram('25.3 进入细胞，不等于失去边界','宿主来源膜组织了专门的交换界面','两种胞内共生都保持宿主来源膜和微生物边界，植物细胞质与伙伴内部不直接混成一体。')
    for title,partner,membrane,transfer in [('根瘤共生体','类菌体','共生体膜','固定氮 → 植物；植物碳 → 类菌体'),('丛枝界面','丛枝','丛枝周膜','磷等 → 植物；植物糖/脂质 → 真菌')]:
        d.text(33,d.y+24,title,27,GREEN,True); d.y+=40
        y=d.y
        d.rect(28,y,624,258,'#eaf3e9')
        d.text(49,y+36,'植物细胞质',24)
        d.rect(97,y+58,504,178,'#fff7e8',GREEN,4)
        d.text(120,y+91,'绿色边框：'+membrane+'（宿主来源）',22,GREEN,True)
        d.text(120,y+125,'界面空间',22,MUTED)
        d.rect(163,y+145,386,68,'#eee9f5','#7a6492',3)
        d.text(185,y+187,partner+'（另有自身边界）',23,'#67527c')
        d.y+=286
        d.y=d.paragraph(35,d.y,transfer,605,24)+18
    d.card('关系维持还需要解释',['营养需求与实际交换影响宿主投入及界面维持。','定殖、物质转移、净收益应分别判断。'])
    d.note('紫色边框：微生物自身边界。图不按比例；箭头概括净方向，未指定全部跨膜步骤。细胞内共生并不意味着微生物裸露在宿主细胞质中。')
    d.save('ch25-exchange.svg')


def protection():
    d=Diagram('26.1 保护植物，可以经过不同路径','同一互作可能同时贡献多个过程','宿主介导免疫、直接生态抑制和营养改善不应混作一种机制。')
    d.card('宿主介导的诱导抗性',['根部互作改变宿主响应状态。','远端组织在后续挑战中出现相应保护。'])
    d.card('直接生态抑制',['资源、空间及微生物互作影响病原压力。','群落抑病本身不自动证明ISR。'],color=BLUE)
    d.card('营养或生长改善',['改善资源利用，可能增加生物量。','长得更大，不能单独证明抗病性增强。'])
    d.card('分别读取终点',['病原负荷、症状、组织功能和生长/产量','相同终点也可能来自不同作用路径。'],fill='#fff7e8')
    d.save('ch26-protection-routes.svg')


def priming():
    d=Diagram('26.2 预激改变后续响应的能力','定性阶段示意，不是实测时间或曲线','预激期可能只有部分变化，后续挑战时响应性质不同；根部启动组分不等于长距离移动信号。')
    d.card('阶段一：根部接触与局部响应',['经典WCS417模型涉及MYB72、BGLU42等根部功能。','局部营养与分泌物变化需按具体体系解释。'])
    d.card('阶段二：形成预激状态',['部分分子可先改变，防御基线也可能相近。','预激不等于所有防御基因持续高表达。'],arrow=True)
    d.card('阶段三：后续挑战与保护',['所测响应可更快、更强或呈现不同性质。','经典模型涉及JA/ET响应能力与NPR1；并非所有ISR都相同。'],arrow=True)
    d.y+=5
    d.arrow(60,d.y,620,d.y,True);d.y+=40
    d.note('根部与远端之间的移动信息仍需具体证据：不能把MYB72、BGLU42、香豆素或某种激素直接指定为通用移动信号。')
    d.save('ch26-priming.svg')


def context():
    d=Diagram('26.3 “有益”需要写清比较背景','宿主表现、侵害负荷与环境共同决定解释','同一微生物的效应取决于宿主、土壤、原有群落和环境；抵抗与耐受是不同维度。')
    d.paired([('宿主与土壤',['基因型、发育阶段','铁可利用性、pH等']),('群落与环境',['已有成员及互作','病害对象、气候等'])])
    d.card('抵抗：限制病原负荷',['需要与相应负荷证据联系。','症状减轻本身还不足以确定负荷减少。'])
    d.card('耐受：在一定负荷下减少损失',['比较同等或可比负荷下的宿主表现。','一个终点的较大生物量不能单独确定耐受。'],color=BLUE)
    d.card('从模型走向一般解释',['改变土壤、宿主或环境后，原来的关系是否还成立？','跨背景证据决定适用范围。'],fill='#fff7e8')
    d.save('ch26-context.svg')


def abundance():
    d=Diagram('27.2 同样的比例，不同的数量变化','虚拟算术例：所有数值均为教学构造','参照A20其他80，情境一A20其他180，情境二A10其他90；两个情境比例都是10%，但A数量不同。')
    d.card('参照',['A = 20；其他 = 80；总量 = 100','A的比例 = 20%'])
    d.card('情境一：A的数量没有减少',['A = 20；其他 = 180；总量 = 200','A的比例 = 10%'],color=BLUE)
    d.card('情境二：A的数量减少',['A = 10；其他 = 90；总量 = 100','A的比例 = 10%'],color=GREEN)
    d.card('为什么不能只看比例？',['两个情境都从20%变为10%。','只有补上合适的数量尺度，才能区分A是否真的减少。'],fill='#fff7e8')
    d.note('假设各样本比较单位相同；真实标记读数还受拷贝数、测量偏差和归一化方式影响。')
    d.save('ch27-abundance.svg')


def evidence():
    d=Diagram('27.1 每一类测量回答不同问题','更多数据，不会自动把相关变成因果','群落组成、编码潜力、活性与宿主功能是不同证据对象，需要分别解释。')
    d.card('组成：检测到了谁？',['标记序列、分类及相对丰度','ASV是序列变体，不自动等于一个菌株。'])
    d.card('潜力：可能具有什么能力？',['宏基因组揭示群落携带的基因。','有相关基因，不等于它正在发挥作用。'])
    d.card('活性：当时有哪些过程发生？',['RNA、蛋白、代谢物及空间证据','表达或积累仍不直接等于反应速率与因果作用。'])
    d.card('宿主功能：植物因此改变了吗？',['负荷、健康、营养、生长与对应功能比较','需要把测量对象、干预关系和适用背景接起来。'],fill='#e6f1e9')
    d.save('ch27-evidence.svg')


def causality():
    d=Diagram('27.3 同一个关联，可以有不同解释','图表示待比较的模型，并非已经证实的通路','土壤同时影响群落和宿主可形成关联；群落影响宿主以及宿主反向影响群落也需分别判断。')
    d.card('模型一：共同原因',['土壤状态 → 群落改变','土壤状态 → 宿主营养或免疫改变','两者相关，不要求群落直接导致宿主变化。'])
    d.card('模型二：群落参与宿主变化',['群落活动 → 宿主响应 → 相应功能结果','需要时间、功能与替代解释的比较。'],color=BLUE)
    d.card('还可能存在反向因果',['宿主损伤或代谢改变 → 群落随之变化','“受损植物中的富集成员”不自动就是致损原因。'])
    d.card('怎样让解释更可信？',['明确比较单位和背景，连接独立的功能证据。','一个环境中的结果，仍需判断能否迁移到其他背景。'],fill='#fff7e8')
    d.save('ch27-causality.svg')


if __name__ == '__main__':
    for render in (habitats,host_community,dysbiosis,symbioses,recognition,exchange,protection,priming,context,abundance,evidence,causality):
        render()
    print('Rendered 12 original microbiome teaching diagrams.')
