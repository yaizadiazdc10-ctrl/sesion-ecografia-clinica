"""Esquemas de imagen ecográfica pulmonar (no son imágenes reales, son dibujos docentes).

Cada función dibuja en un eje un recuadro oscuro que imita la pantalla del ecógrafo
con la línea pleural arriba y el artefacto correspondiente debajo.
"""

import numpy as np
from matplotlib.patches import Ellipse, Rectangle

FONDO = "#141414"
BLANCO = "#F2F2F2"
GRIS = "#8A8A8A"


def _base(ax, ancho=1.0, alto=1.3):
    ax.set_xlim(0, ancho)
    ax.set_ylim(alto, 0)  # y crece hacia abajo, como en la pantalla
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), ancho, alto, facecolor=FONDO, edgecolor="none"))
    # costillas con sombra acústica a los lados
    for x0 in (0.0, ancho - 0.18):
        ax.add_patch(Ellipse((x0 + 0.09, 0.16), 0.2, 0.09, facecolor=GRIS, edgecolor="none"))
        ax.add_patch(Rectangle((x0, 0.2), 0.18, alto - 0.2, facecolor="#0A0A0A", edgecolor="none"))
    # tejido de pared (grano fino)
    rng = np.random.default_rng(3)
    xs = rng.uniform(0.2, ancho - 0.2, 260)
    ys = rng.uniform(0.02, 0.22, 260)
    ax.scatter(xs, ys, s=2, color="#5A5A5A", linewidths=0)


def pleura(ax, y=0.26, ancho=1.0, irregular=False):
    x = np.linspace(0.18, ancho - 0.18, 200)
    if irregular:
        rng = np.random.default_rng(7)
        yy = y + 0.015 * np.sin(x * 60) + rng.normal(0, 0.006, x.size)
        for i in range(0, x.size - 10, 22):  # pleura fragmentada
            ax.plot(x[i:i + 16], yy[i:i + 16], color=BLANCO, lw=3.2, solid_capstyle="round")
    else:
        ax.plot(x, np.full_like(x, y), color=BLANCO, lw=2.2)


def lineas_a(ax, ancho=1.0, alto=1.3, y0=0.26):
    pleura(ax, y0, ancho)
    for k in range(1, 5):
        y = y0 * (k + 1)
        if y > alto - 0.05:
            break
        ax.plot([0.22, ancho - 0.22], [y, y], color=BLANCO, lw=2.0, alpha=max(0.15, 0.75 - 0.18 * k))


def lineas_b(ax, xs, ancho=1.0, alto=1.3, y0=0.26, grosor=5, irregular=False):
    pleura(ax, y0, ancho, irregular=irregular)
    for x in xs:
        ax.plot([x, x], [y0, alto], color=BLANCO, lw=grosor, alpha=0.9, solid_capstyle="butt")
        ax.plot([x, x], [y0, alto], color=BLANCO, lw=grosor * 2.6, alpha=0.12)


def confluentes(ax, ancho=1.0, alto=1.3, y0=0.26):
    pleura(ax, y0, ancho)
    ax.add_patch(Rectangle((0.24, y0), ancho - 0.48, alto - y0, facecolor=BLANCO, alpha=0.55, edgecolor="none"))
    for x in np.linspace(0.27, ancho - 0.27, 7):
        ax.plot([x, x], [y0, alto], color=BLANCO, lw=6, alpha=0.5)


def consolidacion(ax, ancho=1.0, alto=1.3, y0=0.26, pequena=False):
    rng = np.random.default_rng(11)
    if pequena:
        pleura(ax, y0, ancho, irregular=True)
        cx, cy, w, h = ancho / 2 + 0.1, y0 + 0.12, 0.26, 0.2
    else:
        pleura(ax, y0, ancho)
        cx, cy, w, h = ancho / 2, (alto + y0) / 2 + 0.03, ancho - 0.42, alto - y0 - 0.12
    n = 1400 if not pequena else 250
    xs = rng.uniform(cx - w / 2, cx + w / 2, n)
    ys = rng.uniform(cy - h / 2, cy + h / 2, n)
    dentro = ((xs - cx) / (w / 2)) ** 2 + ((ys - cy) / (h / 2)) ** 2 <= 1
    ax.scatter(xs[dentro], ys[dentro], s=5, color="#9A9A9A", linewidths=0)
    if not pequena:  # broncograma aéreo: puntos y trazos brillantes
        for _ in range(9):
            x, y = rng.uniform(cx - w / 3, cx + w / 3), rng.uniform(cy - h / 3, cy + h / 3)
            ax.plot([x, x + rng.uniform(-0.08, 0.08)], [y, y + rng.uniform(0.02, 0.07)],
                    color=BLANCO, lw=2.6, solid_capstyle="round")
