"""Télécharge les portraits de l'annuaire public, les recadre en 128 px
et les injecte dans campus/index.html (à partir de index.template.html).
Usage : python tools/photos/build_photos.py
"""
import base64, io, json, os, pathlib, urllib.request
from PIL import Image  # pip install pillow (>= 11.2 pour l'AVIF)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CDN = "https://cdn.prod.website-files.com/673f1ce410f6be12bd830bb2/"
out = {}
for line in (ROOT / "tools/photos/annuaire.txt").read_text(encoding="utf-8").splitlines():
    name, path = line.split("|", 1)
    raw = urllib.request.urlopen(CDN + path, timeout=30).read()
    im = Image.open(io.BytesIO(raw)).convert("RGBA")
    bg = Image.new("RGBA", im.size, (236, 238, 236, 255)); bg.alpha_composite(im); im = bg.convert("RGB")
    w, h = im.size; s = int(w * .78); x = (w - s) // 2; y = int(h * .05)
    im = im.crop((x, y, x + s, y + s)).resize((128, 128), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=76, optimize=True, progressive=True)
    out[name] = "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
tpl = (ROOT / "campus/index.template.html").read_text(encoding="utf-8")
html = tpl.replace("/*PHOTOS*/", "const PHOTOS=" + json.dumps(out, ensure_ascii=False) + ";")
(ROOT / "campus/index.html").write_text(html, encoding="utf-8")
print(f"{len(out)} photos injectées")
