"""Sensibilidad y especificidad para la ICA: ecografía pulmonar frente a radiografía de tórax.

Fuente: Maw AM et al., JAMA Netw Open 2019;2:e190703 (PMID 30874784): LUS S 0,88 E 0,90;
Rx S 0,73 E 0,90.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
fig, ax = plt.subplots(figsize=(8, 6.75))
grupos = ["Sensibilidad", "Especificidad"]
lus, rx = [88, 90], [73, 90]
x = np.arange(2)
w = 0.36
b1 = ax.bar(x - w / 2, lus, w, color=PALETA["acento"])
b2 = ax.bar(x + w / 2, rx, w, color=PALETA["linea"])
for barras, vals, col in ((b1, lus, PALETA["acento"]), (b2, rx, PALETA["suave"])):
    for b, v in zip(barras, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v} %", ha="center", fontsize=20, color=col)
ax.text(x[0] - w / 2, 4, "Ecografía", ha="center", fontsize=14, color="white", rotation=90, va="bottom")
ax.text(x[0] + w / 2, 4, "Radiografía", ha="center", fontsize=14, color=PALETA["texto"], rotation=90, va="bottom")
ax.set_xticks(x, grupos, fontsize=16)
ax.set_ylim(0, 105)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_title("Diagnóstico de ICA en urgencias", fontsize=18)
fig.text(0.02, 0.01, "Metaanálisis de Maw 2019 (6 estudios, 1827 pacientes)", fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-rendimiento-lus-vs-rx")
