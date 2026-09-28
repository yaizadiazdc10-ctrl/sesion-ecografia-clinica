"""Convierte un tema de PowerPoint (.thmx) en una plantilla .pptx vacía que python-pptx puede abrir.

Uso:
    .venv/bin/python scripts/plantilla_desde_thmx.py "/Applications/Microsoft PowerPoint.app/Contents/Resources/Office Themes/Dividend.thmx" presentacion/plantilla-dividendo.pptx

El .thmx ya contiene presentation.xml, el patrón y los diseños; solo hay que hacer que la relación
principal del paquete apunte a la presentación (no al gestor de temas) y quitar las variantes.
"""
import re
import sys
import zipfile

origen, destino = sys.argv[1], sys.argv[2]
RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="theme/presentation.xml"/></Relationships>')

with zipfile.ZipFile(origen) as zin, zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        n = item.filename
        if n.startswith("themeVariants/") or n.startswith("docProps/"):
            continue
        datos = zin.read(n)
        if n == "_rels/.rels":
            datos = RELS.encode()
        elif n == "[Content_Types].xml":
            txt = datos.decode("utf-8-sig")
            txt = re.sub(r'<Override PartName="/themeVariants/[^>]*/>', "", txt)
            datos = txt.encode()
        zout.writestr(n, datos)
print(f"Plantilla creada: {destino}")
