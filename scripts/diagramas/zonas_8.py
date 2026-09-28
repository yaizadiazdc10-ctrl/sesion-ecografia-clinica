"""Protocolo de 8 zonas (4 por hemitórax) del consenso EACVI 2023, con tres variantes:
mapa básico, patrón de edema (≥ 2 zonas positivas por hemitórax, bilateral) y congestión
residual al alta (≥ 1 zona positiva en cada hemitórax).

Fuente: Gargani L et al., Eur Heart J Cardiovasc Imaging 2023;24:1569-82 (PMID 37450604).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon, Rectangle  # noqa: E402

from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

TORSO = [(-2.2, 0.2), (-2.35, 3.2), (-2.1, 4.6), (-1.1, 5.2), (-0.45, 5.35), (-0.45, 5.9),
         (0.45, 5.9), (0.45, 5.35), (1.1, 5.2), (2.1, 4.6), (2.35, 3.2), (2.2, 0.2)]
# (x0, x1): anterior entre esternón y línea axilar anterior; lateral entre axilares anterior y posterior
FRANJAS = {"ant": (0.15, 1.3), "lat": (1.3, 2.12)}
FILAS = {"sup": (2.45, 4.3), "inf": (0.55, 2.45)}
# numeración EACVI: 1 anterior superior, 2 anterior inferior, 3 lateral superior, 4 lateral inferior
NUM = {("ant", "sup"): 1, ("ant", "inf"): 2, ("lat", "sup"): 3, ("lat", "inf"): 4}


def dibujar(nombre, positivas, titulo_der, lineas_der):
    aplicar_estilo()
    fig, (ax, axt) = plt.subplots(1, 2, figsize=(12, 6.75), gridspec_kw={"width_ratios": [1.15, 1]})
    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-0.4, 6.3)
    ax.set_aspect("equal")
    ax.axis("off")
    torso = Polygon(TORSO, closed=True, facecolor="white", edgecolor=PALETA["primario"], lw=1.4)
    ax.add_patch(torso)
    for lado, signo in (("D", -1), ("I", 1)):
        for (franja, fila), n in NUM.items():
            x0, x1 = FRANJAS[franja]
            y0, y1 = FILAS[fila]
            xa, xb = sorted((signo * x0, signo * x1))
            pos = (lado, n) in positivas
            r = Rectangle((xa, y0), xb - xa, y1 - y0,
                          facecolor=PALETA["acento_suave"] if pos else PALETA["fondo_alt"],
                          edgecolor=PALETA["acento"] if pos else PALETA["linea"], lw=1.6 if pos else 1)
            ax.add_patch(r)
            r.set_clip_path(torso)
            ax.text((xa + xb) / 2, (y0 + y1) / 2, str(n), ha="center", va="center", fontsize=20,
                    color=PALETA["acento"] if pos else PALETA["suave"], fontweight="bold" if pos else "normal")
    ax.plot([0, 0], [0.3, 5.3], color=PALETA["linea"], lw=1, ls="--")
    ax.text(-1.25, -0.3, "Hemitórax derecho", ha="center", fontsize=13, color=PALETA["suave"])
    ax.text(1.25, -0.3, "Hemitórax izquierdo", ha="center", fontsize=13, color=PALETA["suave"])
    ax.text(0, 6.15, "Vista anterior · zonas 1–2 anteriores, 3–4 laterales", ha="center",
            fontsize=12, color=PALETA["suave"])

    axt.axis("off")
    axt.set_xlim(0, 1)
    axt.set_ylim(0, 1)
    axt.text(0, 0.92, titulo_der, fontsize=20, color=PALETA["primario"], va="top")
    y = 0.78
    for linea, destacada in lineas_der:
        axt.text(0, y, linea, fontsize=15, va="top", linespacing=1.35,
                 color=PALETA["acento"] if destacada else PALETA["texto"])
        y -= 0.115 * (linea.count("\n") + 1) + 0.03
    axt.text(0, 0.02, "Protocolo de 8 zonas · Gargani 2023 (consenso EACVI)", fontsize=11, color=PALETA["suave"])
    guardar(fig, nombre)


dibujar("lus-8-zonas", set(), "Cómo explorar", [
    ("1–2 anteriores · 3–4 laterales, en cada lado", False),
    ("Contar en el peor espacio de cada zona", False),
    ("Clips de unos 6 s", False),
    ("Zona positiva: ≥ 3 líneas B", True),
    ("Siempre la misma sonda,\nposición y protocolo", False),
])
dibujar("lus-8-zonas-edema", {("D", 1), ("D", 3), ("D", 4), ("I", 1), ("I", 2), ("I", 3), ("I", 4)},
        "Patrón de edema", [
            ("≥ 3 líneas B por zona", False),
            ("≥ 2 zonas positivas por hemitórax", True),
            ("Bilateral y homogéneo", False),
            ("Pleura fina, deslizamiento conservado", False),
        ])
dibujar("lus-8-zonas-congestion-residual", {("D", 4), ("I", 3)}, "Congestión residual al alta", [
    ("≥ 1 zona positiva en cada hemitórax", True),
    ("Aunque la auscultación sea normal", False),
    ("Umbral propio del protocolo de 8 zonas:\nno intercambiable con 4 o 28 zonas", False),
])
