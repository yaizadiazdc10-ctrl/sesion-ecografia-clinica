"""Genera los gráficos de identidad de la web (SVG) en docs/assets/brand/.

- hero-sector.svg: sector ecográfico con patrón pulmonar normal (línea pleural + líneas A)
- logo.svg:        marca pequeña (sector con línea pleural), también usada como favicon

Uso: .venv/bin/python scripts/web/graficos_web.py
"""

import math
import random
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "docs" / "assets" / "brand"

# Paleta "blush / rose gold" (misma que docs/stylesheets/extra.css)
BLUSH_50 = "#FBF3F0"
BLUSH_100 = "#F7E6E0"
BLUSH_300 = "#E6B4A8"
ROSE_400 = "#D9A396"
ROSE_500 = "#C98F80"
ROSE_600 = "#9A5B52"
ROSE_700 = "#8A4F47"
TINTA_OSCURA = "#241C1B"
TINTA_NEGRA = "#130E0D"


def polar(cx, cy, r, grados):
    t = math.radians(grados)
    return cx + r * math.cos(t), cy + r * math.sin(t)


def sector_path(cx, cy, rin, rout, a0, a1):
    x0, y0 = polar(cx, cy, rin, a0)
    x1, y1 = polar(cx, cy, rout, a0)
    x2, y2 = polar(cx, cy, rout, a1)
    x3, y3 = polar(cx, cy, rin, a1)
    return (f"M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f} A{rout},{rout} 0 0 1 {x2:.1f},{y2:.1f} "
            f"L{x3:.1f},{y3:.1f} A{rin},{rin} 0 0 0 {x0:.1f},{y0:.1f} Z")


def arco(cx, cy, r, a0, a1):
    x0, y0 = polar(cx, cy, r, a0)
    x1, y1 = polar(cx, cy, r, a1)
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f}"


def hero():
    rnd = random.Random(7)
    W, H = 600, 540
    cx, cy = 300, 34
    rin, rout = 26, 480
    a0, a1 = 90 - 37, 90 + 37
    pleura = 150

    def intensidad(r):
        atenuacion = 1 - 0.55 * (r / rout)
        if r < 48:
            base = 0.28
        elif r < pleura - 8:  # partes blandas y músculo intercostal: bandas
            base = 0.42 + 0.18 * math.sin(r / 6.5)
        else:  # pulmón aireado: artefacto, poca señal
            base = 0.16
        return max(0.05, base * atenuacion)

    motas = []
    for _ in range(1900):
        # más densidad en el campo cercano
        r = rin + (rout - rin) * (rnd.random() ** 1.25)
        a = rnd.uniform(a0 + 0.5, a1 - 0.5)
        x, y = polar(cx, cy, r, a)
        rx = rnd.uniform(1.4, 3.6) * (0.8 + r / rout)  # la mota se alarga lateralmente en profundidad
        ry = rnd.uniform(0.6, 1.2)
        op = min(0.95, intensidad(r) * rnd.uniform(0.5, 1.6))
        color = rnd.choice([BLUSH_100, BLUSH_300, ROSE_400, BLUSH_100])
        motas.append(
            f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'transform="rotate({a - 90:.0f} {x:.1f} {y:.1f})" fill="{color}" opacity="{op:.2f}"/>'
        )

    escala = []
    for cm in range(0, 11):
        y = cy + rin + cm * (rout - rin) / 10
        r_px = 2.4 if cm % 5 == 0 else 1.4
        escala.append(f'<circle cx="{W - 14}" cy="{y:.1f}" r="{r_px}" fill="{ROSE_500}"/>')
        if cm % 5 == 0:
            escala.append(f'<text x="{W - 24}" y="{y + 4:.1f}" text-anchor="end" '
                          f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
                          f'font-size="11" fill="{ROSE_500}">{cm}</text>')
    foco_y = cy + pleura + 6
    escala.append(f'<path d="M{W - 30},{foco_y} l-9,-5 v10 z" fill="{ROSE_500}"/>')

    sector = sector_path(cx, cy, rin, rout, a0, a1)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Sector ecográfico con patrón pulmonar normal: línea pleural y líneas A">
  <defs>
    <linearGradient id="fondo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{TINTA_OSCURA}"/>
      <stop offset="1" stop-color="{TINTA_NEGRA}"/>
    </linearGradient>
    <radialGradient id="brillo" cx="{cx}" cy="{cy + 120}" r="260" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{ROSE_500}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{ROSE_500}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="recorte"><path d="{sector}"/></clipPath>
    <filter id="suave" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="1.6"/></filter>
    <filter id="halo" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="5"/></filter>
  </defs>
  <path d="{sector}" fill="url(#fondo)"/>
  <g clip-path="url(#recorte)">
    <path d="{sector}" fill="url(#brillo)"/>
    <g>{"".join(motas)}</g>
    <path d="{arco(cx, cy, pleura, a0, a1)}" stroke="{BLUSH_100}" stroke-width="9" fill="none" opacity="0.35" filter="url(#halo)"/>
    <path d="{arco(cx, cy, pleura, a0, a1)}" stroke="{BLUSH_50}" stroke-width="3.2" fill="none" opacity="0.95" filter="url(#suave)"/>
    <path d="{arco(cx, cy, pleura * 2, a0, a1)}" stroke="{BLUSH_300}" stroke-width="3" fill="none" opacity="0.45" filter="url(#suave)"/>
    <path d="{arco(cx, cy, pleura * 3, a0, a1)}" stroke="{BLUSH_300}" stroke-width="3" fill="none" opacity="0.22" filter="url(#suave)"/>
  </g>
  <path d="{sector}" fill="none" stroke="{ROSE_600}" stroke-opacity="0.35" stroke-width="1"/>
  {"".join(escala)}
</svg>
'''
    return svg


def logo():
    cx, cy = 16, 3
    a0, a1 = 90 - 34, 90 + 34
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{ROSE_500}"/>
      <stop offset="1" stop-color="{ROSE_700}"/>
    </linearGradient>
  </defs>
  <path d="{sector_path(cx, cy, 3, 26, a0, a1)}" fill="url(#g)"/>
  <path d="{arco(cx, cy, 12, a0 + 3, a1 - 3)}" stroke="{BLUSH_50}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
  <path d="{arco(cx, cy, 21, a0 + 4, a1 - 4)}" stroke="{BLUSH_300}" stroke-width="1.2" fill="none" stroke-linecap="round" opacity="0.7"/>
</svg>
'''


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, contenido in [("hero-sector.svg", hero()), ("logo.svg", logo())]:
        ruta = SALIDA / nombre
        ruta.write_text(contenido, encoding="utf-8")
        print(f"Guardado {ruta.relative_to(RAIZ)} ({ruta.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
