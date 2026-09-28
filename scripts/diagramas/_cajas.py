"""Utilidades para diagramas de flujo sobrios (cajas, flechas y etiquetas)."""

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from estilo import PALETA


def caja(ax, x, y, w, h, texto, destacada=False, pregunta=False, size=14, negrita=False):
    """Caja centrada en (x, y). Las preguntas llevan borde fino; los destinos, relleno gris
    o, si están destacados, relleno morado tenue con borde morado."""
    if destacada:
        fc, ec, lw = PALETA["acento_suave"], PALETA["acento"], 1.6
    elif pregunta:
        fc, ec, lw = "white", PALETA["primario"], 1.1
    else:
        fc, ec, lw = PALETA["fondo_alt"], PALETA["linea"], 1.0
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=fc, edgecolor=ec, linewidth=lw))
    ax.text(x, y, texto, ha="center", va="center", fontsize=size,
            color=PALETA["acento"] if destacada else PALETA["texto"],
            fontweight="bold" if negrita else "normal", linespacing=1.3)


def flecha(ax, xy0, xy1, etiqueta=None, destacada=False, lado="derecha", size=13, curva=0.0):
    color = PALETA["acento"] if destacada else PALETA["suave"]
    ax.add_patch(FancyArrowPatch(xy0, xy1, arrowstyle="-|>", mutation_scale=16,
                                 color=color, linewidth=2.0 if destacada else 1.2,
                                 connectionstyle=f"arc3,rad={curva}", shrinkA=2, shrinkB=2))
    if etiqueta:
        mx, my = (xy0[0] + xy1[0]) / 2, (xy0[1] + xy1[1]) / 2
        dx = 0.12 if lado == "derecha" else -0.12
        ax.text(mx + dx, my, etiqueta, ha="left" if lado == "derecha" else "right", va="center",
                fontsize=size, color=color, fontweight="bold" if destacada else "normal")
