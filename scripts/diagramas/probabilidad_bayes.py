"""Cómo cambia la probabilidad de ICA con el patrón B (teorema de Bayes, cálculo propio).

LR+ 7,4 y LR− 0,16 del patrón B para ICA en urgencias: Martindale JL et al.,
Acad Emerg Med 2016;23:223-42 (PMID 26910112). Probabilidad pretest ilustrativa del 40 %.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402

from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402


def post(p, lr):
    o = p / (1 - p) * lr
    return o / (1 + o)


pre = 0.40
pos, neg = post(pre, 7.4), post(pre, 0.16)
aplicar_estilo()
fig, ax = plt.subplots(figsize=(8, 6.75))
ax.set_xlim(-0.2, 3.2)
ax.set_ylim(0, 100)
ax.axis("off")
for y in (0, 25, 50, 75, 100):
    ax.plot([0.3, 2.9], [y, y], color=PALETA["linea"], lw=0.8)
    ax.text(0.2, y, f"{y} %", ha="right", va="center", fontsize=13, color=PALETA["suave"])
ax.scatter([0.8], [pre * 100], s=260, color=PALETA["primario"], zorder=3)
ax.text(0.8, pre * 100 - 8, "Antes\n40 %", ha="center", va="top", fontsize=16, color=PALETA["primario"])
ax.annotate("", xy=(2.3, pos * 100), xytext=(0.9, pre * 100),
            arrowprops=dict(arrowstyle="-|>", color=PALETA["acento"], lw=2.4, mutation_scale=18))
ax.annotate("", xy=(2.3, neg * 100), xytext=(0.9, pre * 100),
            arrowprops=dict(arrowstyle="-|>", color=PALETA["suave"], lw=1.6, mutation_scale=16))
ax.scatter([2.3], [pos * 100], s=260, color=PALETA["acento"], zorder=3)
ax.scatter([2.3], [neg * 100], s=200, color=PALETA["suave"], zorder=3)
ax.text(2.45, pos * 100, f"Patrón B\n≈ {pos*100:.0f} %", va="center", fontsize=17, color=PALETA["acento"])
ax.text(2.45, neg * 100, f"Sin patrón B\n≈ {neg*100:.0f} %", va="center", fontsize=15, color=PALETA["suave"])
ax.set_title("Probabilidad de ICA con la ecografía pulmonar", fontsize=18)
fig.text(0.02, 0.01, "LR+ 7,4 y LR− 0,16 (Martindale 2016) · Cálculo propio con el teorema de Bayes",
         fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-probabilidad-bayes")
