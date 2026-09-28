"""Espectro de aireación pulmonar: de líneas A a consolidación (esquema docente).

Basado en Demi L et al., J Ultrasound Med 2023 (PMID 35993596) y Gargani L et al.,
Eur Heart J Cardiovasc Imaging 2023 (PMID 37450604). Dibujo propio, no son imágenes reales.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

import _eco  # noqa: E402
from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
fig, axes = plt.subplots(1, 4, figsize=(12, 6.75))
fig.subplots_adjust(left=0.02, right=0.98, top=0.78, bottom=0.2, wspace=0.08)
paneles = [
    ("Pulmón aireado", "Líneas A", lambda ax: _eco.lineas_a(ax)),
    ("Síndrome intersticial", "Líneas B", lambda ax: _eco.lineas_b(ax, [0.38, 0.62])),
    ("Pulmón blanco", "Líneas B confluentes", lambda ax: _eco.confluentes(ax)),
    ("Sin aire", "Consolidación", lambda ax: _eco.consolidacion(ax)),
]
for ax, (arriba, abajo, dibujar) in zip(axes, paneles):
    _eco._base(ax)
    dibujar(ax)
    ax.text(0.5, 1.42, abajo, ha="center", va="top", fontsize=17, color=PALETA["primario"])
    ax.text(0.5, 1.56, arriba, ha="center", va="top", fontsize=14, color=PALETA["suave"])

fig.add_artist(FancyArrowPatch((0.05, 0.88), (0.95, 0.88), transform=fig.transFigure,
                               arrowstyle="-|>", mutation_scale=22, color=PALETA["acento"], lw=2))
fig.text(0.05, 0.93, "Más aire", fontsize=14, color=PALETA["suave"], ha="left")
fig.text(0.95, 0.93, "Más agua, menos aire", fontsize=14, color=PALETA["acento"], ha="right")
fig.text(0.02, 0.04, "Esquema docente, no son imágenes reales · Basado en Demi 2023 y Gargani 2023",
         fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-espectro-aireacion")
