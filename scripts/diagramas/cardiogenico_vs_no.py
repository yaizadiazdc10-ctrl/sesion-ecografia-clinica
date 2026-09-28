"""Líneas B cardiogénicas frente a no cardiogénicas (esquema docente).

Criterios: pleura fina y distribución homogénea bilateral en el edema cardiogénico; pleura
irregular, áreas respetadas y consolidaciones subpleurales en SDRA/neumonía.
Copetti R et al., Cardiovasc Ultrasound 2008 (PMID 18442425); Gargani L et al. 2023 (PMID 37450604).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402

import _eco  # noqa: E402
from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
fig, axes = plt.subplots(1, 2, figsize=(10, 6.75))
fig.subplots_adjust(left=0.03, right=0.97, top=0.9, bottom=0.26, wspace=0.12)

ax = axes[0]
_eco._base(ax)
_eco.lineas_b(ax, [0.3, 0.44, 0.58, 0.72], grosor=4)
ax = axes[1]
_eco._base(ax)
_eco.lineas_b(ax, [0.34, 0.42], grosor=4, irregular=True)
_eco.consolidacion(ax, pequena=True)

titulos = [("Cardiogénico", ["Pleura fina y regular", "Líneas B homogéneas", "Bilateral y gravitacional"]),
           ("No cardiogénico", ["Pleura irregular, fragmentada", "Parcheado, áreas respetadas", "Consolidaciones subpleurales"])]
for ax, (t, pts), col in zip(axes, titulos, [PALETA["acento"], PALETA["primario"]]):
    ax.set_title(t, fontsize=18, color=col, loc="center")
    for i, p in enumerate(pts):
        ax.text(0.5, 1.4 + i * 0.13, p, ha="center", va="top", fontsize=14, color=PALETA["texto"])
fig.text(0.03, 0.02, "Esquema docente · Copetti 2008; Gargani 2023", fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-cardiogenico-vs-no")
