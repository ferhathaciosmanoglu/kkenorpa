# -*- coding: utf-8 -*-
"""Kalsedon otomasyon panosu kullanım kılavuzu PDF üreticisi (TR, EN, RU).
Kullanım:  python3 araclar/kilavuz-pdf/uret_pano.py   → kalsedon/pdf/pano-{tr,en,ru}.pdf
Kılavuzlarla aynı sayfa düzenini (uret.py + stil.css) kullanır; içerik icerik_pano.py'den gelir."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import uret
import icerik_pano as K

for ad in ("BELGE", "KAPAK", "ICINDEKILER", "T", "SINIRLAR", "B", "GARANTI"):
    setattr(uret, ad, getattr(K, ad))
uret.TOPLAM = len(K.B) + 2
CIKTI = uret.KOK.parent.parent / "kalsedon" / "pdf"
BAS = [{"tr": "No", "en": "No.", "ru": "№"}, {"tr": "Öğe", "en": "Item", "ru": "Элемент"}, {"tr": "Açıklama", "en": "Description", "ru": "Описание"}]
CSS = """
.ekran figure{margin:0 0 3mm}.ekran figure img{display:block;width:100%;max-height:100mm;object-fit:contain;border-radius:1.6mm;background:#6f7d8c}
.ekran figure.dar img{width:62%;margin:0 auto;background:#fff}.ekran.cift figure img{max-height:66mm}
.ekran td.no{width:9mm;text-align:center}.ekran td.no span{display:inline-block;width:5.2mm;height:5.2mm;line-height:5.2mm;border-radius:50%;background:#E2601F;color:#fff;font-weight:700;font-size:7.5pt}
.ekran td.og{width:38%;font-weight:600}
"""


def isaret_tablo(liste, dil):
    sat = "".join(f'<tr><td class="no"><span>{i}</span></td><td class="og">{a[dil]}</td><td>{b[dil]}</td></tr>' for i, (a, b) in enumerate(liste, 1))
    return '<table class="t sik"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in BAS) + f"</tr></thead><tbody>{sat}</tbody></table>"


_ozel = uret.ozel_sayfa


def ozel_sayfa(b, dil):
    if b["ozel"] != "ekran":
        return _ozel(b, dil)
    h = f'<div class="ekran{" cift" if b.get("gorsel2") else ""}">' + uret.bloklar(b.get("once", []), dil)
    if b.get("gorsel"):
        alt = f'<figcaption>{b["gorsel_alt"][dil]}</figcaption>' if b.get("gorsel_alt") else ""
        h += f'<figure class="{"dar" if b.get("gorsel_dar") else ""}"><img src="gorsel/{b["gorsel"]}">{alt}</figure>'
    if b.get("isaretler"):
        h += isaret_tablo(b["isaretler"], dil)
    if b.get("gorsel2"):
        h += f'<figure style="margin-top:4mm"><img src="gorsel/{b["gorsel2"]}"></figure>' + isaret_tablo(b["isaretler2"], dil)
    return h + uret.bloklar(b.get("sonra", []), dil) + "</div>"


uret_kapak = uret.kapak
uret.ozel_sayfa = ozel_sayfa
uret.kapak = lambda dil: uret_kapak(dil).replace('src="gorsel/kapak.jpg"', 'src="gorsel/pano-ana.jpg" style="object-fit:contain"')


def main(diller=("tr", "en", "ru")):
    from playwright.sync_api import sync_playwright
    CIKTI.mkdir(parents=True, exist_ok=True)
    yol = os.environ.get("CHROME", "/usr/bin/google-chrome")
    with sync_playwright() as p:
        tarayici = p.chromium.launch(executable_path=yol) if os.path.exists(yol) else p.chromium.launch()
        for dil in diller:
            dosya = uret.KOK / f"_pano-{dil}.html"
            dosya.write_text(uret.html(dil).replace("</style>", CSS + "</style>", 1), encoding="utf-8")
            s = tarayici.new_page()
            s.goto(dosya.as_uri())
            s.wait_for_load_state("networkidle")
            n = s.evaluate("document.querySelectorAll('section.sayfa').length")
            tasan = s.evaluate("""[...document.querySelectorAll('section.sayfa')].map((e,i)=>{
                const f=e.querySelector('footer'); const g=e.querySelector('.govde'); if(!f||!g) return null;
                return g.getBoundingClientRect().bottom > f.getBoundingClientRect().top - 4 ? i+1 : null}).filter(Boolean)""")
            if tasan:
                print(f"UYARI {dil}: içerik altbilgiye taşıyor, sayfalar: {tasan}")
            s.pdf(path=str(CIKTI / f"pano-{dil}.pdf"), prefer_css_page_size=True, print_background=True, tagged=True)
            s.close()
            dosya.unlink()
            print(dil, "→", CIKTI / f"pano-{dil}.pdf", n, "sayfa")
        tarayici.close()


if __name__ == "__main__":
    main(tuple(sys.argv[1:]) or ("tr", "en", "ru"))
