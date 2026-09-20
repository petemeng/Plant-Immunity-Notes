"""Render seven original teaching figures for the worked examples in chapters 21–23.

All numerical values are fictional. No figure reproduces an experimental image.
Uses the book's SVG layout helper and matplotlib for the standalone ROS plot.
"""
from pathlib import Path
from render_microbiome_figures import Diagram, GREEN, BLUE, INK, MUTED

OUT=Path(__file__).resolve().parents[1]/'docs/assets/images/textbook'


def table(d, headers, rows, widths, height=76):
    """Readable boxed values, deliberately distinct from experimental photographs."""
    x0=26; y=d.y
    for i,row in enumerate([headers]+rows):
        x=x0
        for j,(value,width) in enumerate(zip(row,widths)):
            fill=GREEN if i==0 else ('#edf4ef' if i%2 else '#fff')
            d.rect(x,y,width,height,fill,'#d4e3d9',1,0)
            lines=str(value).split('|')
            size=21 if i==0 else 23
            yy=y+(height-len(lines)*29)/2+23
            for line in lines:
                d.text(x+width/2,yy,line,size,'white' if i==0 else INK,i==0)
                # The shared primitive is left-aligned by default.
                d.parts[-1]=d.parts[-1].replace('<text ', '<text text-anchor="middle" ',1)
                yy+=29
            x+=width
        y+=height
    d.y=y+28


def coip():
    d=Diagram('21.2 Co-IP：逐泳道检查输入与捕获','虚构教学读数；各行仅在同行内比较','五泳道分别为基准、甲、乙、丙和GFP标签对照；甲伙伴富集增加，乙诱饵捕获增加，丙伙伴输入增加。')
    d.note('捕获：anti-GFP；检测：A-GFP或B-HA。表中数字是任意单位，非免疫印迹照片。')
    table(d,['检测项目','1|基准','2|甲','3|乙','4|丙','5|标签'],[
        ['Input|A-GFP',100,100,100,100,'—'],
        ['Input|B-HA',100,100,100,200,100],
        ['IP|A-GFP',20,20,40,20,'—'],
        ['IP|B-HA',10,30,20,20,1],
    ],[168,92,92,92,92,92])
    d.card('甲：输入与捕获近似，B共沉淀更多',['支持关联读数发生变化，仍不能从条带确定亲和力。'])
    d.card('乙与丙：另有同步变化',['乙捕获到更多A；丙起始样本中的B更多。','二者的IP B增量都不能单独归于结合增强。'],color=BLUE)
    d.note('第5泳道只有游离GFP，没有A-GFP；游离GFP在Input和IP中均可检出。“—”不是零值。不能用跨行原始信号换算分子比例。')
    d.save('ch21-case-coip.svg')


def y2h():
    d=Diagram('21.3 Y2H：同一候选读数，不同背景','两套独立的虚构教学记录；并非真实重复','候选配对报告均为80；记录一诱饵加空AD为75，记录二为2，因此两套结果的背景解释不同。')
    d.note('两套记录的各组合均通过基础生长/构件保留检查。下表仅列报告任意单位。')
    table(d,['组合','记录Ⅰ','记录Ⅱ'],[
        ['BD-A＋AD-B',80,80],['BD-A＋空AD',75,2],
        ['空BD＋AD-B',2,2],['空BD＋空AD',1,1],['已知阳性配对',90,90],
    ],[300,164,164])
    d.card('记录Ⅰ：伙伴缺席，报告仍很高',['候选信号不能直接归因于A与B的特异关系。','不可只从80减去75，就宣称排除了自激活。'])
    d.card('记录Ⅱ：候选配对高于所列背景',['支持该体系中的候选关联，仍需表达等前提。','已知阳性90不代表A与B的亲和力刻度。'],color=BLUE)
    d.note('基本生长正常不等于已确认完整融合蛋白表达。两记录用于比较逻辑，不能从真实重复中挑选“好看”的一套。')
    d.save('ch21-case-y2h.svg')


def qpcr():
    d=Diagram('22.2 RT-qPCR：先计算，再解释倍数','虚构算术例；效率及参照假设见正文','目标Cq提前并不自动等于相对丰度升高；基准和A均为一倍，B四倍，C四分之一。')
    d.card('统一计算关系',['ΔCq = 目标Cq − 参照Cq','ΔΔCq = 比较组ΔCq − 基准组ΔCq','相对倍数 = 2的负ΔΔCq次方'])
    table(d,['组别','目标/|参照Cq','ΔCq','ΔΔCq','相对|倍数'],[
        ['基准','26 / 20',6,0,1],['A','24 / 18',6,0,1],
        ['B','23 / 19',4,'−2',4],['C','25 / 17',8,'+2',0.25],
    ],[90,166,112,130,130])
    d.card('C组：目标较早，却相对下降',['目标提前1个循环，参照提前3个循环。','归一化后为基准的0.25倍，而不是升高。'],color=BLUE)
    d.note('结果依赖扩增效率、参照稳定性及可比背景等假设。表中没有生物学重复，不能用于显著性检验或推断蛋白与抗性倍数。')
    d.save('ch22-case-qpcr.svg')


def dual_luc():
    d=Diagram('22.3 Dual-LUC：把比值拆回原始读数','虚构算术例；LUC与REN均为任意单位','A至D的比值都为四，是基准二的两倍；但LUC分别增加、不变、增加和减少。')
    table(d,['组别','LUC','REN','LUC/REN','相对|基准'],[
        ['基准',1000,500,2,1],['A',2000,500,4,2],['B',1000,250,4,2],
        ['C',4000,1000,4,2],['D',500,125,4,2],
    ],[88,135,135,150,120])
    d.card('A与B：比值相同，变化来源不同',['A的LUC增加、REN不变；B的LUC不变、REN下降。'])
    d.card('C与D：不能忽略两种报告都在变化',['C两者均升高；D两者均降低。','D的LUC已低于基准，比值却仍为基准的2倍。'],color=BLUE)
    d.note('这说明要检查报告背景与参照适用性，不是说某一行自动证明或否定转录调控。Dual-LUC的比值不是split-LUC互补信号。')
    d.save('ch22-case-dual-luc.svg')


def ros():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','Noto Sans CJK SC','SimHei','DejaVu Sans'],
                         'svg.fonttype':'none','svg.hashsalt':'plant-immunity-method-cases-v1','axes.unicode_minus':False,'font.size':19})
    x=list(range(7)); a=[0,3,12,6,1,0,0]; b=[0,2,6,7,6,3,0]
    areas=[sum((v[i]+v[i+1])/2 for i in range(6)) for v in [a,b]]
    assert areas==[22,24]
    fig,ax=plt.subplots(figsize=(9,8),facecolor='#f8faf6')
    fig.subplots_adjust(left=.15,right=.96,bottom=.34,top=.77)
    ax.set_facecolor('#f8faf6')
    ax.plot(x,a,'o-',color=GREEN,lw=3,ms=8,label='R1：峰值12；面积22')
    ax.plot(x,b,'s--',color=BLUE,lw=3,ms=8,label='R2：峰值7；面积24')
    ax.set(xticks=x,yticks=[0,3,6,9,12],ylim=(-.5,14),xlim=(-.2,6.2),xlabel='教学相对时序（非分钟）',ylabel='相对发光信号（任意单位）')
    ax.xaxis.labelpad=18
    ax.spines[['right','top']].set_visible(False)
    ax.grid(axis='y',color='#d6e2d9',alpha=.8)
    ax.legend(frameon=False,fontsize=17,loc='upper right')
    ax.annotate('较高、较早的峰',(2,12),xytext=(.3,13.25),fontsize=17,color=GREEN)
    ax.annotate('较低的峰，较长的尾部',(4,6),xytext=(3.25,9),fontsize=17,color=BLUE)
    fig.text(.055,.94,'23.2 ROS：峰值与整体曲线各说明什么',fontsize=25,color=INK,weight='bold')
    fig.text(.055,.885,'虚构教学曲线；R1、R2不是实际材料或实验结果',fontsize=19,color=MUTED)
    fig.text(.055,.165,'相邻点代表相等的抽象时间间隔；点间按直线连接。\n面积单位为“信号 × 相对时间”，仅展示曲线形状差异。\n图中没有误差或生物学重复，不能比较显著性与抗病性。',fontsize=18,color=MUTED,linespacing=1.6,va='top')
    path=OUT/'ch23-case-ros.svg'
    fig.savefig(path,format='svg',metadata={'Date':None});plt.close(fig)
    svg=path.read_text(encoding='utf-8')
    pos=svg.index('>',svg.index('<svg'))+1
    svg=svg[:pos]+'<title>23.2 虚构ROS曲线的峰值与面积</title><desc>R1峰值12面积22，R2峰值7面积24；仅比较教学曲线，不能推断实际抗病性。</desc>'+svg[pos:]
    path.write_text('\n'.join(line.rstrip() for line in svg.splitlines())+'\n',encoding='utf-8')


def complementation():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','Noto Sans CJK SC','SimHei','DejaVu Sans'],
                         'svg.fonttype':'none','svg.hashsalt':'plant-immunity-method-cases-v1','axes.unicode_minus':False,'font.size':19})
    rows=[[96,101,103],[28,32,30],[35,31,33],[29,31,30],[91,95,99]]
    means=[sum(v)/3 for v in rows]
    assert means==[100,30,33,30,95]
    names=['野生型','a1','a2','a1对照','恢复A功能']
    fig,ax=plt.subplots(figsize=(9,7),facecolor='#f8faf6')
    fig.subplots_adjust(left=.24,right=.94,bottom=.32,top=.76)
    ax.set_facecolor('#f8faf6')
    for i,(values,mean) in enumerate(zip(rows,means)):
        ax.scatter(values,[i-.09,i,i+.09],s=65,color=GREEN,zorder=3)
        ax.plot([mean,mean],[i-.28,i+.28],color=BLUE,lw=3,zorder=2)
        ax.text(113,i,f'{mean:g}',ha='left',va='center',fontsize=19,color=BLUE)
    ax.set(yticks=range(5),yticklabels=names,xticks=[0,25,50,75,100],xlim=(0,126),ylim=(4.55,-.7),xlabel='某项早期氧化响应（任意单位）')
    ax.xaxis.labelpad=18
    ax.spines[['right','top','left']].set_visible(False)
    ax.tick_params(axis='y',length=0,pad=12)
    ax.grid(axis='x',color='#d6e2d9')
    ax.text(110,-.58,'均值',fontsize=18,color=BLUE)
    fig.text(.055,.94,'23.1 遗传互补：先看每个样本，再看均值',fontsize=24,color=INK,weight='bold')
    fig.text(.055,.865,'全部为虚构数据；每组3株；未附显著性检验',fontsize=19,color=MUTED)
    fig.text(.055,.17,'圆点：单株读数；蓝色短线：三株均值。\n这里只比较一种响应，不能推出整体抗病能力。\n材料背景、恢复表达和生长状态等前提见正文。',fontsize=18,color=MUTED,linespacing=1.5,va='top')
    path=OUT/'ch23-case-complementation.svg'
    fig.savefig(path,format='svg',metadata={'Date':None});plt.close(fig)
    svg=path.read_text(encoding='utf-8');pos=svg.index('>',svg.index('<svg'))+1
    svg=svg[:pos]+'<title>23.1 遗传互补的虚构单株读数与均值</title><desc>野生型、a1、a2、a1对照、恢复A功能的均值为100、30、33、30、95；每组3个虚构单株值。</desc>'+svg[pos:]
    path.write_text('\n'.join(line.rstrip() for line in svg.splitlines())+'\n',encoding='utf-8')


def replicates():
    d=Diagram('23.3 重复层级：植物不等于细胞','虚构取样情境；比较单位需要与问题对应','条件甲乙各三株独立植物，每株一百个细胞；每组独立植物数为三，而非三百。')
    for title,color in [('条件甲',GREEN),('条件乙',BLUE)]:
        d.text(32,d.y+25,title,27,color,True); d.y+=48
        for i,x in enumerate([26,240,454],1):
            d.rect(x,d.y,200,165,'#edf4ef' if color==GREEN else '#eef3f9')
            d.text(x+24,d.y+40,f'独立植株 {i}',24,color,True)
            d.text(x+24,d.y+88,'100个细胞',23)
            d.text(x+24,d.y+126,'共享一个来源',22,MUTED)
        d.y+=193
    d.card('用于植株层面的组间比较',['每组n = 3株；每组共观察300个细胞。','全部样本：6株植物，600个细胞。'])
    d.card('细胞提供另一层信息',['更多细胞帮助描述同一植株内部差异。','不能把同株细胞当作300份独立植株来源。'],color=BLUE)
    d.note('需要保留嵌套关系；若土壤、批次或其他处理单位另有共享因素，还应按实际设计解释独立性。')
    d.save('ch23-case-replicates.svg')


if __name__=='__main__':
    for render in (coip,y2h,qpcr,dual_luc,complementation,ros,replicates):render()
    print('Rendered seven original worked-example figures (fictional data).')
