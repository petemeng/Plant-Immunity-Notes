"""Render original, conceptual textbook figures; no experimental data are used."""
from pathlib import Path
from html import escape
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/assets/images/textbook"
OUT.mkdir(parents=True, exist_ok=True)

def svg_start(title, desc, width, height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
            '<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#456b58"/></marker></defs>',
            '<style>text{font-family:"Microsoft YaHei","Noto Sans SC",sans-serif;fill:#243b30} .small{font-size:16px}.label{font-size:19px;font-weight:600}</style>',
            f'<rect width="{width}" height="{height}" fill="#faf9f6" rx="12"/>']

def box(parts, x, y, w, h, lines, fill="#e8f0e9"):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#789580"/>')
    for i, line in enumerate(lines):
        parts.append(f'<text x="{x+w/2}" y="{y+30+i*26}" text-anchor="middle" class="{ "label" if i==0 else "small" }">{escape(line)}</text>')

def arrow(parts, path, dashed=False):
    dash_attr = ' stroke-dasharray="7 5"' if dashed else ''
    parts.append(f'<path d="{path}" fill="none" stroke="#456b58" stroke-width="2.5" marker-end="url(#arr)"{dash_attr}/>')

parts = svg_start("从识别到防御结果", "识别、传递、执行形成过程，反馈调节识别与信号；环境、组织和时间影响全部层次。", 920, 340)
parts.append('<text x="460" y="37" text-anchor="middle" class="label">组织身份 · 环境条件 · 时间状态</text>')
for x, lines, fill in [(30,["识别", "微生物与宿主线索"],"#edf3f8"),(255,["信号传递","离子、激酶与调控"],"#e8f0e9"),(480,["防御执行","结构、代谢与表达"],"#fff2d9"),(705,["功能结果","保护效果与生理代价"],"#eee9f4")]:
    box(parts,x,80,185,90,lines,fill)
for x in [215,440,665]:
    arrow(parts,f"M{x} 125 H{x+37}")
arrow(parts,"M572 170 V220 H347 V174")
parts.append('<text x="460" y="247" text-anchor="middle" class="small">反馈可增强、限制或重置响应</text>')
parts.append('<text x="460" y="295" text-anchor="middle" class="small">注意：信号指标变化，需要额外证据才能与最终保护建立联系。</text></svg>')
(OUT / "immune-cycle.svg").write_text("\n".join(parts), encoding="utf-8")

parts = svg_start("根部免疫的三个坐标", "纵向发育区域、径向组织身份和当前细胞状态共同决定对根免疫的解释。", 920, 480)
parts.append('<text x="460" y="37" text-anchor="middle" class="label">同一个“根部响应”，需要三个坐标</text>')
box(parts,25,70,250,58,["纵向：发育区域"],"#edf3f8")
box(parts,335,70,250,58,["径向：组织身份"],"#e8f0e9")
box(parts,645,70,250,58,["状态：当前活动"],"#fff2d9")
for i, text in enumerate(["较成熟的分化区域", "伸长区域", "分生区域与根冠"]):
    box(parts,45,155+i*77,210,58,[text],"#edf3f8")
for r, fill in [(113,"#dae8db"),(87,"#eaf0de"),(60,"#f4e5be"),(34,"#e4dbef")]:
    parts.append(f'<circle cx="460" cy="266" r="{r}" fill="{fill}" stroke="#789580"/>')
for y, text in [(169,"表皮"),(199,"皮层"),(226,"内皮层"),(275,"中柱")]:
    parts.append(f'<text x="460" y="{y}" text-anchor="middle" font-size="16">{text}</text>')
for i, text in enumerate(["未出现特定应答", "局部感知与应答", "恢复、重塑或持续变化"]):
    box(parts,665,155+i*77,210,58,[text],"#fff2d9")
parts.append('<text x="460" y="435" text-anchor="middle" class="small">组织示意不按比例；不同植物根的层数、结构与区域划分可以不同。</text></svg>')
(OUT / "root-context.svg").write_text("\n".join(parts), encoding="utf-8")

font_path = Path("C:/Windows/Fonts/msyh.ttc")
font = FontProperties(fname=str(font_path)) if font_path.exists() else FontProperties(family="DejaVu Sans")
plt.rcParams.update({"svg.fonttype": "path", "axes.spines.top":False,"axes.spines.right":False})
x = [i/50 for i in range(501)]
a = [1+5*math.exp(-((t-2.7)/0.8)**2) for t in x]
b = [1+3*math.exp(-((t-4.6)/2.0)**2) for t in x]
fig, ax = plt.subplots(figsize=(9,5.2))
fig.subplots_adjust(left=.10, right=.97, bottom=.22, top=.85)
fig.set_facecolor("#faf9f6")
ax.set_facecolor("#faf9f6")
ax.plot(x,a,color="#276447",linewidth=2.7,label="示意 A：峰值较高、持续较短")
ax.plot(x,b,color="#9c671d",linewidth=2.7,linestyle="--",label="示意 B：峰值较低、持续较长")
ax.set_xlabel("时间（任意单位）",fontproperties=font)
ax.set_ylabel("报告信号（任意单位）",fontproperties=font)
ax.set_title("同一过程可以从不同时间特征描述",fontproperties=font,pad=14)
ax.legend(prop=font,frameon=False,loc="upper right")
ax.set_ylim(0,7.5)
ax.grid(axis="y",alpha=.2)
fig.text(.51,.035,"纯教学示意：曲线由函数生成，不代表真实实验或抗病效果。",ha="center",fontproperties=font,fontsize=10)
fig.savefig(OUT/"response-curves.svg",bbox_inches="tight")
plt.close(fig)
curve_path = OUT / "response-curves.svg"
curve_path.write_text("\n".join(line.rstrip() for line in curve_path.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
print("Rendered 3 original teaching figures.")
