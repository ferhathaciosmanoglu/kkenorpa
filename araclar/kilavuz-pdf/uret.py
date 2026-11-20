# -*- coding: utf-8 -*-
"""Akuamarin kullanım kılavuzu PDF üreticisi (TR, EN, RU).
Kullanım:  python3 araclar/kilavuz-pdf/uret.py            → akuamarin/pdf/kilavuz-{tr,en,ru}.pdf
Gerekenler: Python 3, playwright (python) ve Chrome/Chromium; yazı tipi Inter (sistemde kurulu)."""
import os, sys, pathlib
sys.path.insert(0, os.path.dirname(__file__))
from icerik import *

KOK = pathlib.Path(__file__).resolve().parent
CIKTI = KOK.parent.parent / "akuamarin" / "pdf"
TOPLAM = 22

MODELLER = [  # kW, kcal min, kcal max, su m3, en, boy, yük, kg — KILAVUZ ENP-AKM-TR R01 §16
    (510, 309600, 438600, 1.715, 1580, 1965, 1745, 1820), (660, 438600, 567600, 2.047, 1625, 2230, 1790, 2040),
    (810, 567600, 696600, 2.366, 1675, 2450, 1840, 2325), (960, 696600, 825600, 2.787, 1730, 2660, 1895, 2570),
    (1200, 825600, 1032000, 3.228, 1775, 2930, 1940, 2920), (1500, 1032000, 1290000, 4.037, 1885, 3150, 2050, 3815),
    (1800, 1290000, 1548000, 4.772, 1955, 3425, 2120, 4280), (2400, 1548000, 2064000, 6.127, 2065, 3915, 2230, 5265),
    (3000, 2064000, 2580000, 7.035, 2120, 4335, 2285, 6045), (3600, 2580000, 3096000, 8.118, 2195, 4695, 2365, 6865),
    (4200, 3096000, 3612000, 9.129, 2255, 5025, 2420, 7670), (4800, 3612000, 4128000, 10.416, 2325, 5340, 2490, 8475),
    (5400, 4128000, 4644000, 11.671, 2395, 5590, 2560, 9830), (6000, 4644000, 5160000, 12.692, 2450, 5855, 2615, 10675),
    (6600, 5160000, 5676000, 13.835, 2505, 6100, 2670, 11470), (7200, 5676000, 6192000, 14.814, 2550, 6315, 2715, 12250),
    (8400, 6192000, 7224000, 16.871, 2645, 6715, 2810, 14470), (9600, 7224000, 8256000, 18.641, 2710, 7120, 2875, 15995)]


def sayi(n, dil, ondalik=0):
    s = f"{n:,.{ondalik}f}"  # 1,234.5
    if dil == "tr":
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    if dil == "ru":
        return s.replace(",", " ").replace(".", ",")
    return s


def kw(n, dil):
    return f"{n} {'кВт' if dil == 'ru' else 'kW'}"


def sayfa_bas(no, ust, baslik, dil):
    return (f'<header class="bb"><div class="no">{no}</div><div><div class="ust">{ust[dil]}</div>'
            f'<h1>{baslik[dil]}</h1></div></header>')


def altbilgi(sayfa, dil):
    return (f'<footer><span>{BELGE["altbilgi"][dil]}</span><span>{BELGE["kod"][dil]} · {BELGE["rev"]} · {BELGE["tarih"]}</span>'
            f'<b>{sayfa} / {TOPLAM}</b></footer>')


def tablo(bas, satirlar, dil, opt=None):
    opt = opt or {}
    cls = "t" + (" sik" if opt.get("sik") else "") + (" g1" if opt.get("genis1") else "") + (" bas-yok" if bas is None else "")
    h = f'<table class="{cls}">'
    if bas:
        h += "<thead><tr>" + "".join(f"<th>{c[dil]}</th>" for c in bas) + "</tr></thead>"
    h += "<tbody>"
    for r in satirlar:
        h += "<tr>" + "".join(
            f'<td class="{"k" if (i == 0 and opt.get("kalin1")) else ""}">{c[dil] if isinstance(c, dict) else c}</td>'
            for i, c in enumerate(r)) + "</tr>"
    return h + "</tbody></table>"


def notkutu(tur, baslik, icerik, dil):
    if isinstance(icerik, list):
        govde = "<ul>" + "".join(f"<li>{x[dil]}</li>" for x in icerik) + "</ul>"
    else:
        govde = f"<p>{icerik[dil]}</p>"
    return f'<div class="not {tur}"><b>{baslik[dil]}</b>{govde}</div>'


def sinirlar(dil):
    return '<div class="sinir">' + "".join(f"<div><b>{a[dil]}</b><span>{b[dil]}</span></div>" for a, b in SINIRLAR) + "</div>"


def bloklar(liste, dil):
    h = ""
    for b in liste:
        t = b[0]
        if t == "p": h += f"<p>{b[1][dil]}</p>"
        elif t == "h": h += f"<h2>{b[1][dil]}</h2>"
        elif t == "kucuk": h += f'<p class="kucuk">{b[1][dil]}</p>'
        elif t == "tablo": h += tablo(b[1], b[2], dil, b[3] if len(b) > 3 else None)
        elif t == "not": h += notkutu(b[1], b[2], b[3], dil)
        elif t == "adim": h += '<ol class="adim">' + "".join(f"<li>{x[dil]}</li>" for x in b[1]) + "</ol>"
        elif t == "madde": h += '<ul class="madde">' + "".join(f"<li>{x[dil]}</li>" for x in b[1]) + "</ul>"
        elif t == "sinirlar": h += sinirlar(dil)
        elif t == "isaretler":
            h += '<div class="isaret">' + "".join(f'<div class="not {k}"><b>{T[k][dil]}</b><p>{v[dil]}</p></div>' for k, v in b[1]) + "</div>"
        elif t == "yapi":
            _, metin, satirlar, alt = b
            h += ('<div class="yapi"><div><p>' + metin[dil] + "</p>" + tablo(None, satirlar, dil, {"kalin1": True}) + "</div>"
                  f'<figure><img src="gorsel/akuamarin-kesit.jpg"><figcaption>{alt[dil]}</figcaption></figure></div>')
        elif t == "ikiresim":
            h += '<div class="iki">' + "".join(
                f'<figure><img src="gorsel/{f}"><figcaption>{a[dil]}</figcaption></figure>' for f, a in b[1:]) + "</div>"
        elif t == "susema": h += su_semasi(b[1], dil)
    return h


def su_semasi(s, dil):
    g = lambda k: s[k][dil]
    return f'''<figure class="sema"><svg viewBox="0 0 600 205" font-family="Inter" font-size="9.5">
  <text x="138" y="12" text-anchor="middle" font-weight="700" fill="#1d5fb4">{g("donus")}</text>
  <text x="138" y="25" text-anchor="middle" fill="#333">{g("donus2")}</text>
  <path d="M138 31v17" stroke="#1d5fb4" stroke-width="2"/><path d="M133 43l5 7 5-7z" fill="#1d5fb4"/>
  <text x="430" y="12" text-anchor="middle" font-weight="700" fill="#c62828">{g("gidis")}</text>
  <text x="430" y="25" text-anchor="middle" fill="#333">{g("gidis2")}</text>
  <path d="M430 52V34" stroke="#c62828" stroke-width="2"/><path d="M425 37l5-7 5 7z" fill="#c62828"/>
  <text x="230" y="38" text-anchor="middle" fill="#333">{g("sont")}</text>
  <text x="300" y="38" text-anchor="middle" fill="#333">{g("genlesme")}</text>
  <rect x="129" y="55" width="18" height="15" fill="#2b2b2b"/><rect x="224" y="60" width="13" height="10" fill="#2b2b2b"/>
  <rect x="294" y="60" width="13" height="10" fill="#2b2b2b"/><rect x="421" y="55" width="18" height="15" fill="#2b2b2b"/>
  <rect x="88" y="70" width="388" height="102" fill="#f6e6dc" stroke="#e8650f" stroke-width="2"/>
  <rect x="88" y="172" width="388" height="9" fill="#2b2b2b"/>
  <rect x="38" y="112" width="50" height="36" fill="#2b2b2b"/>
  <text x="56" y="164" text-anchor="middle" fill="#333">{g("brulor")}</text>
  <circle cx="104" cy="139" r="6" fill="none" stroke="#2b2b2b" stroke-width="1.6"/>
  <text x="114" y="160" fill="#333">{g("onsont")}</text>
  <text x="282" y="118" text-anchor="middle" font-weight="700" font-size="11" fill="#222">{g("ad")}</text>
  <text x="282" y="133" text-anchor="middle" fill="#555">{g("yan")}</text>
  <rect x="478" y="80" width="26" height="26" fill="none" stroke="#2b2b2b" stroke-width="1.6"/>
  <text x="514" y="97" fill="#333">{g("baca")}</text>
  <circle cx="490" cy="148" r="9" fill="none" stroke="#2b2b2b" stroke-width="1.8"/>
  <text x="505" y="151" fill="#333">{g("patlama")}</text>
</svg><figcaption>{g("alt")}</figcaption></figure>'''


def yerlesim_semasi(s, dil):
    g = lambda k: s[k][dil]
    return f'''<figure class="sema2"><svg viewBox="0 0 300 140" font-family="Inter" font-size="5.6">
  <rect x="1" y="1" width="298" height="138" fill="#fff" stroke="#222" stroke-width="1.4"/>
  <rect x="6" y="34" width="62" height="64" fill="none" stroke="#999" stroke-dasharray="3 2"/>
  <text x="9" y="31" fill="#555">{g("bos")}</text>
  <rect x="72" y="58" width="16" height="20" fill="#2b2b2b"/><text x="74" y="87" fill="#333">{g("brulor")}</text>
  <rect x="90" y="45" width="140" height="46" fill="#f6e6dc" stroke="#e8650f" stroke-width="1.2"/>
  <text x="160" y="65" text-anchor="middle" font-weight="700" font-size="7" fill="#222">{g("kazan")}</text>
  <text x="160" y="74" text-anchor="middle" fill="#555">{g("ust")}</text>
  <circle cx="242" cy="68" r="7" fill="none" stroke="#222" stroke-width="1.1"/><text x="234" y="86" fill="#333">{g("baca")}</text>
  <g stroke="#e8650f" stroke-width=".9" fill="#e8650f">
    <path d="M160 3v40"/><path d="M157 7l3-5 3 5zM157 39l3 5 3-5z"/>
    <path d="M160 94v42"/><path d="M157 98l3-5 3 5zM157 132l3 5 3-5z"/>
    <path d="M3 122h84"/><path d="M7 119l-5 3 5 3zM83 119l5 3-5 3z"/>
    <path d="M233 122h64"/><path d="M237 119l-5 3 5 3zM293 119l5 3-5 3z"/>
  </g>
  <g fill="#c2410c" font-size="5.4"><text x="164" y="24">1500 mm</text><text x="164" y="117">1500 mm</text>
  <text x="10" y="130">{g("s")}</text><text x="250" y="130">1000 mm</text></g>
</svg><figcaption>{g("alt")}</figcaption></figure>'''


def ozel_sayfa(b, dil):
    o = b["ozel"]
    if o == "yerlesim":
        sol = '<ul class="madde">' + "".join(f"<li>{x[dil]}</li>" for x in b["maddeler"]) + "</ul>"
        satir = [[f'<span class="m">{kw(m, dil)}</span>', sayi(s, dil) if s else "–",
                  f"{e} × {bo}" if e else "–"] for m, s, e, bo in YERLESIM]
        sol += '<table class="t veri"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in b["tablo_b"]) + "</tr></thead><tbody>" + \
               "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in satir) + "</tbody></table>"
        sag = yerlesim_semasi(b["sema"], dil) + bloklar(b["sag"], dil)
        return f'<div class="ikisutun">' \
               f'<div>{sol}</div><div>{sag}</div></div>'
    if o == "teknik":
        rows = "".join(
            f'<tr><td><span class="m">{kw(m[0], dil)}</span></td><td>{sayi(m[1], dil)} – {sayi(m[2], dil)}</td><td>{sayi(m[3], dil, 3)}</td>'
            f'<td>{m[4]}</td><td>{m[5]}</td><td>{m[6]}</td><td>{sayi(m[7], dil)}</td></tr>' for m in MODELLER)
        return ('<table class="t veri buyuk"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in TEKNIK_B) + "</tr></thead><tbody>" + rows +
                "</tbody></table>" + sinirlar(dil) + f'<p class="kucuk">{TEKNIK_NOT[dil]}</p>')
    if o == "baglanti":
        rows = "".join("<tr>" + f'<td><span class="m">{kw(r[0], dil)}</span></td>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in BAGLANTI)
        return ('<table class="t veri buyuk"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in BAGLANTI_B) + "</tr></thead><tbody>" + rows +
                f'</tbody></table><p class="kucuk">{BAGLANTI_NOT[dil]}</p>' + notkutu("bilgi", BAGLANTI_KUTU[0], BAGLANTI_KUTU[1], dil))
    if o == "form":
        F = FORM
        alan = lambda a: f'<div class="alan"><span>{a[dil]}</span><i></i></div>'
        h = '<div class="alanlar">' + "".join(alan(a) + alan(c) for a, c in F["ust_alanlar"]) + "</div>"
        h += '<table class="t form"><thead><tr><th>' + F["kontrol_b"][0][dil] + '</th><th>' + F["kontrol_b"][1][dil] + "</th></tr></thead><tbody>"
        h += "".join(f'<tr><td>{k[dil]}</td><td class="sonuc">{T[s][dil]}</td></tr>' for k, s in F["kontroller"]) + "</tbody></table>"
        h += '<table class="t form olcum"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in F["olcum_b"]) + "</tr></thead><tbody>"
        h += "".join(f"<tr><td>{o_[dil]}</td><td></td><td></td></tr>" for o_ in F["olcumler"]) + "</tbody></table>"
        h += '<div class="alanlar">' + "".join(alan(a) + alan(c) for a, c in F["alt_alanlar"]) + "</div>"
        h += f'<div class="alanlar tek">{alan(F["uygunsuzluk"])}</div>'
        h += '<div class="imzalar">' + "".join(f'<div><i></i><b>{x[dil]}</b><span>{T["imza"][dil]}</span></div>' for x in F["imzalar"]) + "</div>"
        return h + f'<p class="kucuk">{F["not_"][dil]}</p>'
    if o == "kayit":
        K = KAYIT
        bos = lambda n, k: "".join("<tr>" + "<td></td>" * k + "</tr>" for _ in range(n))
        return (f'<p class="kucuk">{K["p"][dil]}</p><table class="t bos k1"><thead><tr>' + "".join(f"<th>{c[dil]}</th>" for c in K["b1"]) +
                "</tr></thead><tbody>" + bos(14, 4) + f'</tbody></table><h2>{K["h2"][dil]}</h2><table class="t bos k2"><thead><tr>' +
                "".join(f"<th>{c[dil]}</th>" for c in K["b2"]) + "</tr></thead><tbody>" + bos(7, 5) + "</tbody></table>")
    if o == "garanti":
        G = GARANTI
        alan = lambda a: f'<div class="alan"><span>{a[dil]}</span><i></i></div>'
        h = f'<h2>{G["h"][dil]}</h2><ul class="madde">' + "".join(f"<li>{x[dil]}</li>" for x in G["maddeler"]) + "</ul>"
        h += notkutu("dikkat", G["kutu"][0], G["kutu"][1], dil)
        h += f'<h2>{G["kayit_h"][dil]}</h2><div class="alanlar">' + "".join(alan(a) + alan(c) for a, c in G["kayit"]) + "</div>"
        h += f'<h2>{G["servis_h"][dil]}</h2><p>{G["servis_p"][dil]}</p>'
        h += (f'<div class="iletisim"><div><small>{G["uretici"][dil]}</small><b>Enorpa Enerji San. Tic. Ltd. Şti.</b><span>{G["adres"][dil]}</span></div>'
              f'<div><small>{G["telefon"][dil]}</small><b>+90 850 471 21 00</b><small style="margin-top:10px">{G["eposta"][dil]}</small><b>turuncu@enorpa.com</b></div>'
              f'<div><small>{G["web"][dil]}</small><b>www.enorpa.com</b></div></div>')
        h += f'<p class="kucuk">{G["surum"][dil].format(kod=BELGE["kod"][dil], rev=BELGE["rev"], tarih=BELGE["tarih"])}</p>'
        return h


def kapak(dil):
    K = KAPAK
    hap = '<span class="ayrac">|</span>'.join(f"<span>{x[dil]}</span>" for x in K["hap"])
    return f'''<section class="sayfa kapak">
  <img class="klogo" src="gorsel/logo-kapak.png" alt="ENORPA">
  <div class="kust">{K["ust"][dil]}</div>
  <h1>{K["baslik"][dil]}</h1>
  <div class="kalt">{K["alt"][dil]}</div>
  <div class="hap">{hap}</div>
  <div class="kresim"><img src="gorsel/kapak.jpg" alt=""></div>
  <div class="kbant"><div><b>{BELGE["kod"][dil]} · {BELGE["rev"]}</b><span>{BELGE["tarih"]} · {BELGE["dil"][dil]}</span></div><p>{K["not"][dil]}</p></div>
</section>'''


def icindekiler(dil):
    I = ICINDEKILER
    satir = "".join(f'<li><b>{b["no"]}</b><span>{b["baslik"][dil]}</span><i>{i + 3}</i></li>' for i, b in enumerate(B))
    return (f'<section class="sayfa"><header class="bb"><div class="no">–</div><div><div class="ust">{I["ust"][dil]}</div><h1>{I["baslik"][dil]}</h1></div></header>'
            f'<ol class="icind">{satir}</ol>' + notkutu("bilgi", I["hizli_b"], I["hizli"], dil) + altbilgi(2, dil) + "</section>")


def html(dil):
    sayfalar = kapak(dil) + icindekiler(dil)
    for i, b in enumerate(B):
        govde = ozel_sayfa(b, dil) if b.get("ozel") else bloklar(b["bloklar"], dil)
        sayfalar += f'<section class="sayfa s{b["no"]}">' + sayfa_bas(b["no"], b["ust"], b["baslik"], dil) + \
                    f'<div class="govde">{govde}</div>' + altbilgi(i + 3, dil) + "</section>"
    css = (KOK / "stil.css").read_text(encoding="utf-8")
    return f'''<!doctype html><html lang="{dil}"><head><meta charset="utf-8"><title>{BELGE["baslik"][dil]}</title>
<style>{css}</style></head><body class="dil-{dil}">{sayfalar}</body></html>'''


def main(diller=("tr", "en", "ru")):
    from playwright.sync_api import sync_playwright
    CIKTI.mkdir(parents=True, exist_ok=True)
    yol = os.environ.get("CHROME", "/usr/bin/google-chrome")
    with sync_playwright() as p:
        tarayici = p.chromium.launch(executable_path=yol) if os.path.exists(yol) else p.chromium.launch()
        for dil in diller:
            dosya = KOK / f"_kilavuz-{dil}.html"
            dosya.write_text(html(dil), encoding="utf-8")
            s = tarayici.new_page()
            s.goto(dosya.as_uri())
            s.wait_for_load_state("networkidle")
            sayfa_sayisi = s.evaluate("document.querySelectorAll('section.sayfa').length")
            tasan = s.evaluate("""[...document.querySelectorAll('section.sayfa')].map((e,i)=>{
                const f=e.querySelector('footer'); if(!f) return null;
                const g=e.querySelector('.govde'); if(!g) return null;
                return g.getBoundingClientRect().bottom > f.getBoundingClientRect().top - 4 ? i+1 : null}).filter(Boolean)""")
            if tasan:
                print(f"UYARI {dil}: içerik altbilgiye taşıyor, sayfalar: {tasan}")
            s.pdf(path=str(CIKTI / f"kilavuz-{dil}.pdf"), prefer_css_page_size=True, print_background=True, tagged=True)
            s.close()
            print(dil, "→", CIKTI / f"kilavuz-{dil}.pdf", sayfa_sayisi, "sayfa")
        tarayici.close()


if __name__ == "__main__":
    main(tuple(sys.argv[1:]) or ("tr", "en", "ru"))
