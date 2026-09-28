"""Tratamiento diurético guiado por líneas B (ambulatorio / tras el alta): forest plot simplificado.

Datos (RR, IC 95 %) tomados de los resúmenes de:
- Mhanna M et al. 2022 (PMID en bibliografía, clave mhanna2022): hospitalización 0,65 (0,34–1,22); visitas urgentes 0,32 (0,18–0,59)
- Al-Sagban A et al. J Crit Care 2026;93:155435 (PMID 41643462): hospitalización 0,65 (0,48–0,88); visitas urgentes 0,38 (0,22–0,66)
- Chotalia M et al. 2026 (clave chotalia2026): hospitalización 0,76 (0,48–1,18); visitas urgentes 0,31 (0,17–0,55)
- Bagheri et al. 2026 (clave bagheri2026): reingreso por IC 0,61 (0,38–0,96); mortalidad 0,96 (0,58–1,58)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

filas = [
    ("Visitas urgentes por IC", None),
    ("Mhanna 2022", (0.32, 0.18, 0.59)),
    ("Al-Sagban 2026", (0.38, 0.22, 0.66)),
    ("Chotalia 2026", (0.31, 0.17, 0.55)),
    ("Hospitalización / reingreso por IC", None),
    ("Mhanna 2022", (0.65, 0.34, 1.22)),
    ("Al-Sagban 2026", (0.65, 0.48, 0.88)),
    ("Chotalia 2026", (0.76, 0.48, 1.18)),
    ("Bagheri 2026", (0.61, 0.38, 0.96)),
    ("Mortalidad", None),
    ("Bagheri 2026", (0.96, 0.58, 1.58)),
]
aplicar_estilo()
fig, ax = plt.subplots(figsize=(12, 6.75))
n = len(filas)
grupo = 0
for i, (etq, val) in enumerate(filas):
    y = n - i
    if val is None:
        grupo += 1
        ax.text(0.052, y, etq, fontsize=15, fontweight="bold", va="center",
                color=PALETA["acento"] if grupo == 1 else PALETA["primario"])
        continue
    rr, lo, hi = val
    col = PALETA["acento"] if grupo == 1 else PALETA["primario"] if grupo == 2 else PALETA["suave"]
    ax.plot([lo, hi], [y, y], color=col, lw=2)
    ax.scatter([rr], [y], s=90, marker="s", color=col, zorder=3)
    ax.text(0.058, y, etq, fontsize=14, va="center", color=PALETA["texto"])
    ax.text(3.6, y, f"{rr:.2f} ({lo:.2f}–{hi:.2f})".replace(".", ","), fontsize=13, va="center",
            color=PALETA["texto"], ha="right")
ax.plot([1, 1], [0.4, n + 0.5], color=PALETA["suave"], lw=1, ls="--")
ax.set_xscale("log")
ax.set_xlim(0.05, 3.7)
ax.set_xticks([0.2, 0.5, 1, 1.5], ["0,2", "0,5", "1", "1,5"])
ax.set_xticks([], minor=True)
ax.set_ylim(-0.3, n + 0.7)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.text(0.55, -0.05, "Favorece la ecografía", fontsize=12, color=PALETA["suave"], ha="center")
ax.text(1.6, -0.05, "Favorece el control", fontsize=12, color=PALETA["suave"], ha="center")
ax.set_xlabel("Riesgo relativo (escala log.)", fontsize=13, color=PALETA["suave"])
fig.text(0.02, 0.01, "Metaanálisis de ECA, sobre todo ambulatorios o tras el alta · Mhanna 2022; Al-Sagban 2026; "
         "Chotalia 2026; Bagheri 2026", fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-forest-metaanalisis")
