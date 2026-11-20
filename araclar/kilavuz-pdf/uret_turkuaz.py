# -*- coding: utf-8 -*-
"""Turkuaz kullanım kılavuzu PDF üreticisi (TR, EN, RU).
Kullanım:  python3 araclar/kilavuz-pdf/uret_turkuaz.py      → turkuaz/pdf/kilavuz-{tr,en,ru}.pdf
Akuamarin üreticisinin (uret.py) sayfa düzenini ve stil.css'i aynen kullanır; yalnızca içerik
icerik_turkuaz.py'den gelir ve Turkuaz'a özel teknik sayfalar burada çizilir."""
import os, sys, pathlib
sys.path.insert(0, os.path.dirname(__file__))
import uret
import icerik_turkuaz as K

for ad in ("BELGE", "KAPAK", "ICINDEKILER", "T", "SINIRLAR", "B", "FORM", "KAYIT", "GARANTI"):
    setattr(uret, ad, getattr(K, ad))
uret.TOPLAM = len(K.B) + 2
CIKTI = uret.KOK.parent.parent / "turkuaz" / "pdf"

_ozel = uret.ozel_sayfa
m_ad = lambda n: f'<span class="m">TR{n}</span>'
deger = lambda v, dil: v[dil] if isinstance(v, dict) else v


def ozel_sayfa(b, dil):
    o = b["ozel"]
    if o == "teknik_trk":
        rows = "".join(f"<tr><td>{m_ad(m[0])}</td><td>{uret.sayi(m[1], dil)}</td><td>{m[2]}</td><td>{m[3]}</td>"
                       f"<td>{m[4]}</td><td>{uret.sayi(m[5], dil)}</td></tr>" for m in K.MODELLER)
        return ('<table class="t veri buyuk"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in K.TEKNIK_B) +
                "</tr></thead><tbody>" + rows + "</tbody></table>" + uret.sinirlar(dil) + f'<p class="kucuk">{K.TEKNIK_NOT[dil]}</p>')
    if o == "baglanti_trk":
        rows = "".join("<tr>" + f"<td>{m_ad(r[0])}</td>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in K.BAGLANTI)
        isl = "".join(f'<tr><td class="k">{a[dil]}</td><td>{deger(v, dil)}</td></tr>' for a, v in K.ISLETME)
        return ('<table class="t veri buyuk"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in K.BAGLANTI_B) +
                "</tr></thead><tbody>" + rows + f'</tbody></table><p class="kucuk">{K.BAGLANTI_NOT[dil]}</p>' +
                '<table class="t"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in K.ISLETME_B) + "</tr></thead><tbody>" + isl +
                "</tbody></table>" + uret.notkutu("bilgi", K.BAGLANTI_KUTU[0], K.BAGLANTI_KUTU[1], dil))
    return _ozel(b, dil)


def kapak(dil):
    return uret_kapak(dil).replace('src="gorsel/kapak.jpg"', 'src="gorsel/turkuaz-kapak.jpg"')


uret_kapak = uret.kapak
uret.ozel_sayfa = ozel_sayfa
uret.kapak = kapak


def main(diller=("tr", "en", "ru")):
    from playwright.sync_api import sync_playwright
    CIKTI.mkdir(parents=True, exist_ok=True)
    yol = os.environ.get("CHROME", "/usr/bin/google-chrome")
    with sync_playwright() as p:
        tarayici = p.chromium.launch(executable_path=yol) if os.path.exists(yol) else p.chromium.launch()
        for dil in diller:
            dosya = uret.KOK / f"_turkuaz-{dil}.html"
            dosya.write_text(uret.html(dil), encoding="utf-8")
            s = tarayici.new_page()
            s.goto(dosya.as_uri())
            s.wait_for_load_state("networkidle")
            n = s.evaluate("document.querySelectorAll('section.sayfa').length")
            tasan = s.evaluate("""[...document.querySelectorAll('section.sayfa')].map((e,i)=>{
                const f=e.querySelector('footer'); const g=e.querySelector('.govde'); if(!f||!g) return null;
                return g.getBoundingClientRect().bottom > f.getBoundingClientRect().top - 4 ? i+1 : null}).filter(Boolean)""")
            if tasan:
                print(f"UYARI {dil}: içerik altbilgiye taşıyor, sayfalar: {tasan}")
            s.pdf(path=str(CIKTI / f"kilavuz-{dil}.pdf"), prefer_css_page_size=True, print_background=True, tagged=True)
            s.close()
            dosya.unlink()
            print(dil, "→", CIKTI / f"kilavuz-{dil}.pdf", n, "sayfa")
        tarayici.close()


if __name__ == "__main__":
    main(tuple(sys.argv[1:]) or ("tr", "en", "ru"))
