"""Genera la presentación .pptx a partir de un guion en YAML.

Uso:
    .venv/bin/python scripts/build_pptx.py presentacion/diapositivas.yaml [-o presentacion/sesion.pptx]

Tipos de diapositiva admitidos (campo `tipo`):
    portada       titulo, subtitulo
    seccion       titulo, subtitulo?
    contenido     titulo, puntos[], imagen?, fuente?
    imagen        titulo, imagen, pie?, fuente?
    dos_columnas  titulo, izquierda{titulo?, puntos[]}, derecha{titulo?, puntos[]}, fuente?
    tabla         titulo, cabecera[], filas[[]], fuente?
    mensaje       texto, subtexto?          (mensaje clave a pantalla completa)
    referencias   titulo?, referencias[]

Todas admiten `notas` (notas del orador). Un punto puede ser texto o {texto, sub: [..]}.
Las rutas de imagen son relativas a la raíz del repositorio.
"""

import argparse
import sys
from pathlib import Path

import yaml
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

RAIZ = Path(__file__).resolve().parent.parent
ANCHO, ALTO = Inches(13.333), Inches(7.5)
MARGEN = Inches(0.6)

TEMA_POR_DEFECTO = {
    "primario": "0F766E",
    "acento": "06B6D4",
    "texto": "1F2937",
    "suave": "6B7280",
    "fondo": "FFFFFF",
    "fondo_alt": "F0FDFA",
    "fuente": "Calibri",
}


def rgb(hex_color):
    return RGBColor.from_string(hex_color.lstrip("#").upper())


class Constructor:
    def __init__(self, guion):
        self.guion = guion
        self.tema = {**TEMA_POR_DEFECTO, **(guion.get("tema") or {})}
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = ANCHO, ALTO
        self.blank = self.prs.slide_layouts[6]
        self.numero = 0

    # ---------- utilidades ----------
    def _fondo(self, slide, color):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = rgb(color)

    def _rect(self, slide, x, y, w, h, color):
        shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
        shp.fill.solid()
        shp.fill.fore_color.rgb = rgb(color)
        shp.line.fill.background()
        return shp

    def _texto(self, slide, x, y, w, h, texto, size=20, bold=False, color=None,
               align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False):
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        for i, linea in enumerate(str(texto).split("\n")):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            run = p.add_run()
            run.text = linea
            f = run.font
            f.size, f.bold, f.italic = Pt(size), bold, italic
            f.name = self.tema["fuente"]
            f.color.rgb = rgb(color or self.tema["texto"])
        return tb

    def _titulo(self, slide, titulo):
        self._rect(slide, 0, 0, ANCHO, Inches(0.12), self.tema["primario"])
        self._texto(slide, MARGEN, Inches(0.35), ANCHO - 2 * MARGEN, Inches(0.9),
                    titulo, size=32, bold=True, color=self.tema["primario"],
                    anchor=MSO_ANCHOR.MIDDLE)

    def _pie(self, slide, fuente=None):
        self.numero += 1
        y = ALTO - Inches(0.45)
        if fuente:
            self._texto(slide, MARGEN, y, ANCHO - Inches(2.2), Inches(0.35),
                        f"Fuente: {fuente}", size=11, color=self.tema["suave"], italic=True)
        self._texto(slide, ANCHO - Inches(1.4), y, Inches(0.8), Inches(0.35),
                    str(self.numero), size=11, color=self.tema["suave"], align=PP_ALIGN.RIGHT)

    def _puntos(self, slide, x, y, w, h, puntos, size=None):
        n = sum(1 + len(p.get("sub", [])) if isinstance(p, dict) else 1 for p in puntos)
        size = size or (24 if n <= 4 else 22 if n <= 6 else 18 if n <= 9 else 16)
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = True
        primero = True

        def add(texto, nivel):
            nonlocal primero
            p = tf.paragraphs[0] if primero else tf.add_paragraph()
            primero = False
            p.space_after = Pt(8 if nivel == 0 else 4)
            viñeta = "•  " if nivel == 0 else "–  "
            r1 = p.add_run()
            r1.text = ("      " * nivel) + viñeta
            r1.font.color.rgb = rgb(self.tema["acento"])
            r1.font.size = Pt(size - 4 * nivel)
            r1.font.bold = True
            r2 = p.add_run()
            r2.text = str(texto)
            r2.font.size = Pt(size - 4 * nivel)
            r2.font.name = self.tema["fuente"]
            r2.font.color.rgb = rgb(self.tema["texto"] if nivel == 0 else self.tema["suave"])

        for punto in puntos:
            if isinstance(punto, dict):
                add(punto["texto"], 0)
                for sub in punto.get("sub", []):
                    add(sub, 1)
            else:
                add(punto, 0)
        return tb

    def _imagen(self, slide, ruta, x, y, w, h):
        path = RAIZ / ruta
        if not path.exists():
            print(f"AVISO: imagen no encontrada: {ruta}", file=sys.stderr)
            caja = self._rect(slide, x, y, w, h, "E5E7EB")
            caja.text_frame.text = f"[Falta imagen]\n{ruta}"
            return
        with Image.open(path) as im:
            iw, ih = im.size
        escala = min(w / iw, h / ih)
        pw, ph = int(iw * escala), int(ih * escala)
        slide.shapes.add_picture(str(path), x + Emu((w - pw) // 2), y + Emu((h - ph) // 2), pw, ph)

    def _notas(self, slide, datos):
        if datos.get("notas"):
            slide.notes_slide.notes_text_frame.text = str(datos["notas"]).strip()

    # ---------- tipos de diapositiva ----------
    def portada(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["primario"])
        self._rect(s, 0, ALTO - Inches(0.25), ANCHO, Inches(0.25), self.tema["acento"])
        self._texto(s, MARGEN, Inches(2.0), ANCHO - 2 * MARGEN, Inches(2.0),
                    d.get("titulo", self.guion.get("titulo", "")), size=44, bold=True,
                    color="FFFFFF", anchor=MSO_ANCHOR.BOTTOM)
        sub = d.get("subtitulo", self.guion.get("subtitulo", ""))
        if sub:
            self._texto(s, MARGEN, Inches(4.1), ANCHO - 2 * MARGEN, Inches(1.0), sub,
                        size=24, color="E0F2F1")
        meta = " · ".join(x for x in [self.guion.get("autora"), self.guion.get("fecha")] if x)
        if meta:
            self._texto(s, MARGEN, Inches(5.6), ANCHO - 2 * MARGEN, Inches(0.6), meta,
                        size=18, color="E0F2F1")
        self._notas(s, d)
        self.numero += 1

    def seccion(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo_alt"])
        self._rect(s, MARGEN, Inches(3.0), Inches(0.15), Inches(1.5), self.tema["acento"])
        self._texto(s, MARGEN + Inches(0.4), Inches(2.8), ANCHO - 2 * MARGEN, Inches(1.2),
                    d["titulo"], size=40, bold=True, color=self.tema["primario"],
                    anchor=MSO_ANCHOR.MIDDLE)
        if d.get("subtitulo"):
            self._texto(s, MARGEN + Inches(0.4), Inches(4.0), ANCHO - 2 * MARGEN, Inches(0.8),
                        d["subtitulo"], size=22, color=self.tema["suave"])
        self._notas(s, d)
        self.numero += 1

    def contenido(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo"])
        self._titulo(s, d["titulo"])
        top, alto = Inches(1.5), ALTO - Inches(2.2)
        if d.get("imagen"):
            ancho_txt = (ANCHO - 2 * MARGEN) * 0.52
            self._puntos(s, MARGEN, top, ancho_txt, alto, d.get("puntos", []))
            xi = MARGEN + ancho_txt + Inches(0.3)
            self._imagen(s, d["imagen"], xi, top, ANCHO - MARGEN - xi, alto)
        else:
            self._puntos(s, MARGEN, top, ANCHO - 2 * MARGEN, alto, d.get("puntos", []))
        self._pie(s, d.get("fuente"))
        self._notas(s, d)

    def imagen(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo"])
        self._titulo(s, d["titulo"])
        alto = ALTO - Inches(2.3) - (Inches(0.5) if d.get("pie") else 0)
        self._imagen(s, d["imagen"], MARGEN, Inches(1.45), ANCHO - 2 * MARGEN, alto)
        if d.get("pie"):
            self._texto(s, MARGEN, Inches(1.45) + alto + Inches(0.05), ANCHO - 2 * MARGEN,
                        Inches(0.5), d["pie"], size=16, color=self.tema["suave"],
                        align=PP_ALIGN.CENTER)
        self._pie(s, d.get("fuente"))
        self._notas(s, d)

    def dos_columnas(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo"])
        self._titulo(s, d["titulo"])
        ancho = (ANCHO - 2 * MARGEN - Inches(0.4)) / 2
        for i, lado in enumerate(["izquierda", "derecha"]):
            col = d.get(lado, {})
            x = MARGEN + i * (ancho + Inches(0.4))
            y = Inches(1.5)
            if col.get("titulo"):
                self._rect(s, x, y, ancho, Inches(0.6), self.tema["fondo_alt"])
                self._texto(s, x + Inches(0.15), y, ancho, Inches(0.6), col["titulo"], size=22,
                            bold=True, color=self.tema["primario"], anchor=MSO_ANCHOR.MIDDLE)
                y += Inches(0.8)
            self._puntos(s, x, y, ancho, ALTO - y - Inches(0.7), col.get("puntos", []), size=18)
        self._pie(s, d.get("fuente"))
        self._notas(s, d)

    def tabla(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo"])
        self._titulo(s, d["titulo"])
        cab, filas = d["cabecera"], d["filas"]
        alto_fila = Inches(0.55)
        t = s.shapes.add_table(len(filas) + 1, len(cab), MARGEN, Inches(1.6),
                               ANCHO - 2 * MARGEN, alto_fila * (len(filas) + 1)).table
        size = 16 if len(filas) <= 6 else 13
        for r, fila in enumerate([cab] + filas):
            for c, valor in enumerate(fila):
                celda = t.cell(r, c)
                celda.text = str(valor)
                for p in celda.text_frame.paragraphs:
                    for run in p.runs:
                        run.font.size = Pt(size)
                        run.font.name = self.tema["fuente"]
                        run.font.bold = r == 0
                        run.font.color.rgb = rgb("FFFFFF" if r == 0 else self.tema["texto"])
                celda.fill.solid()
                celda.fill.fore_color.rgb = rgb(
                    self.tema["primario"] if r == 0 else
                    (self.tema["fondo_alt"] if r % 2 == 0 else self.tema["fondo"]))
        self._pie(s, d.get("fuente"))
        self._notas(s, d)

    def mensaje(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["primario"])
        self._texto(s, Inches(1.2), Inches(1.8), ANCHO - Inches(2.4), Inches(2.8), d["texto"],
                    size=36, bold=True, color="FFFFFF", align=PP_ALIGN.CENTER,
                    anchor=MSO_ANCHOR.MIDDLE)
        if d.get("subtexto"):
            self._texto(s, Inches(1.2), Inches(4.8), ANCHO - Inches(2.4), Inches(1.2),
                        d["subtexto"], size=20, color="E0F2F1", align=PP_ALIGN.CENTER)
        self._notas(s, d)
        self.numero += 1

    def referencias(self, d):
        s = self.prs.slides.add_slide(self.blank)
        self._fondo(s, self.tema["fondo"])
        self._titulo(s, d.get("titulo", "Bibliografía"))
        refs = d["referencias"]
        size = 14 if len(refs) <= 8 else 12 if len(refs) <= 12 else 10
        texto = "\n".join(f"{i}. {r}" for i, r in enumerate(refs, 1))
        self._texto(s, MARGEN, Inches(1.5), ANCHO - 2 * MARGEN, ALTO - Inches(2.2), texto,
                    size=size)
        self._pie(s)
        self._notas(s, d)

    def construir(self, salida):
        for i, d in enumerate(self.guion["diapositivas"], 1):
            tipo = d.get("tipo", "contenido")
            metodo = getattr(self, tipo, None)
            if metodo is None or tipo.startswith("_") or tipo == "construir":
                sys.exit(f"Diapositiva {i}: tipo desconocido '{tipo}'")
            metodo(d)
        salida.parent.mkdir(parents=True, exist_ok=True)
        self.prs.save(salida)
        print(f"Generada {salida} ({len(self.prs.slides)} diapositivas)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guion", type=Path)
    ap.add_argument("-o", "--salida", type=Path)
    args = ap.parse_args()
    guion = yaml.safe_load(args.guion.read_text(encoding="utf-8"))
    salida = (args.salida or RAIZ / "presentacion" / guion.get("archivo", "sesion-clinica.pptx")).resolve()
    Constructor(guion).construir(salida)


if __name__ == "__main__":
    main()
