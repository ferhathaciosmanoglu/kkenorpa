/* =====================================================================
   ortak/js/kilavuz.js — sayfa çizimi, dil sistemi, bilet kart, galeri
   Bütün seriler bu dosyayı kullanır; seriye özel metin burada yer almaz.
   Ayrıntı: KILAVUZ_SABLONU.md §4, §5
   ===================================================================== */
(function () {
  "use strict";

  /* ---------- Dil sistemi (§5.2) ---------- */
  const DILLER = ["tr", "en", "ru"];
  const DIL_ADI = { tr: "Türkçe", en: "English", ru: "Русский" };
  const VARSAYILAN_DIL = "en";                     // 🟡 K-09
  const DEPO_ANAHTARI = "enorpa-kilavuz-dil";
  const TARAYICI_ESLEME = {
    tr: "tr", az: "tr",
    en: "en",
    ru: "ru", be: "ru", kk: "ru", ky: "ru", uz: "ru", tg: "ru"
  };
  const YEREL = { tr: "tr-TR", en: "en-GB", ru: "ru-RU" };
  const YEDEK_SIRASI = { tr: ["tr", "en"], en: ["en", "tr"], ru: ["ru", "en", "tr"] };
  const HAREKET_AZ = matchMedia("(prefers-reduced-motion: reduce)");
  const DEBUG = new URLSearchParams(location.search).has("debug");

  let aktifDil;
  let seciciyiGuncelle = () => {};

  function ilkDiliBul() {
    const p = new URLSearchParams(location.search).get("lang");
    if (DILLER.includes(p)) return p;
    try {
      const k = localStorage.getItem(DEPO_ANAHTARI);
      if (DILLER.includes(k)) return k;
    } catch (_) { /* gizli sekme */ }
    const liste = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""];
    for (const etiket of liste) {
      const kok = String(etiket).toLowerCase().split("-")[0];
      if (TARAYICI_ESLEME[kok]) return TARAYICI_ESLEME[kok];
    }
    return VARSAYILAN_DIL;
  }

  function metin(alan, dil) {
    if (alan == null) return "";
    if (typeof alan === "string") return alan;
    if (!alan[dil] && DEBUG) console.warn("Eksik çeviri (" + dil + "):", alan.tr);
    return alan[dil] || alan.tr || "";
  }
  function arayuz(anahtar, dil, degisken) {
    let s = metin(window.METIN[anahtar], dil) || anahtar;
    if (degisken) for (const k in degisken) s = s.replace("{" + k + "}", degisken[k]);
    return s;
  }
  const birim = (b, dil) => metin(window.BIRIM[b], dil) || b;

  /* ---------- Biçimler (§5.7) ---------- */
  const sayi = (n, dil, ondalik = 0) =>
    new Intl.NumberFormat(YEREL[dil], { minimumFractionDigits: ondalik, maximumFractionDigits: ondalik }).format(n);
  const aralik = ([a, b], dil, ondalik = 0) => sayi(a, dil, ondalik) + "–" + sayi(b, dil, ondalik);

  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  /* ---------- İkonlar (Lucide, ISC lisansı — satır içi, CDN yok) ---------- */
  const IKON = {
    indir: '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    goz: '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    paylas: '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/>',
    telefon: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    whatsapp: '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M9 10a.5.5 0 0 0 1 0V9a.5.5 0 0 0-1 0v1a5 5 0 0 0 5 5h1a.5.5 0 0 0 0-1h-1a.5.5 0 0 0 0 1"/>',
    zarf: '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    harita: '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    dunya: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    ucgen: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    bilgi: '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    dosya: '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    sol: '<path d="m15 18-6-6 6-6"/>',
    sag: '<path d="m9 18 6-6-6-6"/>',
    kapat: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    raptiye: '<path d="M12 17v5"/><path d="M9 10.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24V16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V7a1 1 0 0 1 1-1 2 2 0 0 0 0-4H8a2 2 0 0 0 0 4 1 1 0 0 1 1 1z"/>'
  };
  const ikon = (ad, sinif = "ikon") =>
    '<svg class="' + sinif + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + IKON[ad] + "</svg>";

  // Gerçek ENORPA logosu (ortak/img/enorpa-logo.png'den türetilmiş beyaz sürüm)
  const kartLogo = '<img class="bilet-logo" src="../ortak/img/enorpa-logo-beyaz.png" width="480" height="117" alt="ENORPA">';

  /* ---------- Yardımcılar ---------- */
  const URUN = () => window.URUN;
  const anaDokuman = () => URUN().dokumanlar.find((d) => d.ana) || URUN().dokumanlar[0];

  function pdfBaglantisi(dok, dil) {
    const kullanilan = YEDEK_SIRASI[dil].find((x) => dok.diller[x]);
    if (!kullanilan) return null;
    const d = dok.diller[kullanilan];
    return {
      dil: kullanilan,
      href: d.dosya + "?v=" + encodeURIComponent(d.onbellek || d.revizyon),
      indirmeAdi: d.indirmeAdi,
      boyutMB: d.boyutMB,
      revizyon: d.revizyon,
      farkliDil: kullanilan !== dil
    };
  }
  const mbYaz = (mb, dil) => (mb == null ? "" : sayi(mb, dil, 1) + " " + birim("MB", dil));

  // QR parametreleri: ?model=4800kW&seri=2345-0683-AKT1-I112 (eski sayfayla uyumlu)
  function qrBilgisi() {
    const q = new URLSearchParams(location.search);
    const temiz = (v) => (v || "").replace(/[^0-9A-Za-zÇĞİÖŞÜçğıöşü .\-\/]/g, "").slice(0, 40).trim();
    const modelHam = temiz(q.get("model"));
    const seri = temiz(q.get("seri") || q.get("sn"));
    const kw = parseInt(modelHam.replace(/\D/g, ""), 10);
    const c = URUN().modelCarpan;       // ör. Kalsedon: "3000" → KL30
    const satir = (URUN().modeller || []).find((m) => m[0] === kw || (c && m[0] * c === kw)) || null;
    return { modelHam, seri, satir };
  }

  /* ---------- Bilet dokusu: akuamarin dithering (Bayer 4×4, "warp" deseni) ----------
     React/WebGL bileşenindeki Dithering shader'ının saf Canvas 2D karşılığı.
     Düşük çözünürlükte çizilip CSS ile pikselli büyütülür; ekran dışındayken durur. */
  const BAYER4 = [0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5].map((v) => v / 16);
  function hexRgb(h) {
    h = h.replace("#", "");
    return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
  }
  const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

  function dokuyuBaslat(canvas) {
    const ctx = canvas.getContext && canvas.getContext("2d");
    if (!ctx) return;
    const PX = 3;                                  // bir doku pikseli = 3 CSS pikseli
    const arka = hexRgb(URUN().renk.koyu || "#0A5670");
    const on = hexRgb(URUN().renk.doku || "#117A99");
    let w = 0, h = 0, img = null, raf = 0, gorunur = true, son = 0, t0 = performance.now();

    function boyutla() {
      const r = canvas.getBoundingClientRect();
      w = Math.max(1, Math.round(r.width / PX));
      h = Math.max(1, Math.round(r.height / PX));
      canvas.width = w; canvas.height = h;
      img = ctx.createImageData(w, h);
      ciz(performance.now());
    }
    function ciz(simdi) {
      if (!img) return;
      const t = ((simdi - t0) / 1000) * 0.4 * 0.5;
      const d = img.data;
      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          let u = (x - w / 2) * 0.03, v = (y - h / 2) * 0.03;
          for (let i = 1; i < 6; i++) {
            u += (0.6 / i) * Math.cos(i * 2.5 * v + t);
            v += (0.6 / i) * Math.cos(i * 1.5 * u + t);
          }
          let s = 0.15 / Math.max(0.001, Math.abs(Math.sin(t - v - u)));
          s = smooth(0.02, 1, s);
          const esik = BAYER4[(y & 3) * 4 + (x & 3)] - 0.5;
          const c = s + esik >= 0.5 ? on : arka;
          const k = (y * w + x) * 4;
          d[k] = c[0]; d[k + 1] = c[1]; d[k + 2] = c[2]; d[k + 3] = 255;
        }
      }
      ctx.putImageData(img, 0, 0);
    }
    function dongu(simdi) {
      raf = 0;
      if (!gorunur || document.hidden || HAREKET_AZ.matches) return;
      if (simdi - son > 33) { ciz(simdi); son = simdi; }   // ~30 fps yeter
      raf = requestAnimationFrame(dongu);
    }
    const baslat = () => { if (!raf) raf = requestAnimationFrame(dongu); };

    new ResizeObserver(boyutla).observe(canvas);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(([e]) => { gorunur = e.isIntersecting; if (gorunur) baslat(); }).observe(canvas);
    }
    document.addEventListener("visibilitychange", baslat);
    HAREKET_AZ.addEventListener && HAREKET_AZ.addEventListener("change", baslat);
    boyutla();
    baslat();
  }

  /* ---------- Eğim: farede imleçle, telefonda cihazı sağa sola yatırınca ---------- */
  const MAX_EGIM = 6;
  let egimKart = null;               // dil değişiminde kart yeniden çizilir; jiroskop dinleyicisi tek kalır
  let jiroKuruldu = false;
  const SABIT_ANAHTARI = "enorpa-kilavuz-sabit";
  let sabit = false;
  try { sabit = localStorage.getItem(SABIT_ANAHTARI) === "1"; } catch (_) {}

  function duzle(kart) {
    kart.style.transition = "";
    kart.style.transform = "";
    kart.querySelector(".bilet-parlama").style.background = "transparent";
  }

  function egimUygula(kart, dx, dy, max = MAX_EGIM, maxDikey = max) {  // dx, dy: -0.5 … 0.5
    if (sabit) return;
    const parlama = kart.querySelector(".bilet-parlama");
    kart.style.transform = "rotateX(" + (-dy * 2 * maxDikey) + "deg) rotateY(" + (dx * 2 * max) + "deg)";
    parlama.style.background = "radial-gradient(45% 35% at " + (dx + 0.5) * 100 + "% " + (dy + 0.5) * 100 + "%, rgb(255 255 255 / .16), transparent 70%)";
  }

  function jiroskopKur() {
    if (jiroKuruldu || !("DeviceOrientationEvent" in window)) return;
    jiroKuruldu = true;
    let taban = null, hedef = [0, 0], simdi = [0, 0], raf = 0;
    const sinirla = (v) => Math.max(-0.5, Math.min(0.5, v));
    function ciz() {
      raf = 0;
      if (!egimKart || HAREKET_AZ.matches || sabit) return;
      simdi[0] += (hedef[0] - simdi[0]) * 0.15;
      simdi[1] += (hedef[1] - simdi[1]) * 0.15;
      egimKart.style.transition = "none";
      egimUygula(egimKart, simdi[0], simdi[1], 14, 4);   // telefonda: sağa-sola belirgin, öne-arkaya hafif (kart yukarı taşmasın)
      if (Math.abs(hedef[0] - simdi[0]) + Math.abs(hedef[1] - simdi[1]) > 0.002) raf = requestAnimationFrame(ciz);
    }
    function yonelim(e) {
      if (e.gamma == null || e.beta == null) return;
      const yatay = Math.abs(screen.orientation ? screen.orientation.angle : window.orientation || 0) === 90;
      const x = yatay ? e.beta : e.gamma, y = yatay ? -e.gamma : e.beta;
      if (!taban) taban = [x, y];
      taban[0] += (x - taban[0]) * 0.03;      // eğik tutulunca kart birkaç saniyede düz konuma döner
      taban[1] += (y - taban[1]) * 0.05;
      hedef = [sinirla((x - taban[0]) / 30), sinirla((y - taban[1]) / 30)];
      if (!raf) raf = requestAnimationFrame(ciz);
    }
    addEventListener("deviceorientation", yonelim, { passive: true });   // Android: hemen çalışır
    const D = window.DeviceOrientationEvent;
    if (typeof D.requestPermission === "function") {
      // iOS: izin yalnızca bir dokunuşla istenebilir — veri gelmiyorsa ilk dokunuşta bir kez sorulur
      const iste = () => {
        removeEventListener("touchend", iste);
        if (!taban) D.requestPermission().catch(() => {});
      };
      addEventListener("touchend", iste, { passive: true });
    }
  }

  // Raptiye üst barın solunda durur; kart her çizimde yenilense de düğme tektir
  let raptiyeDil = "tr";
  function raptiyeGuncelle() {
    const d = document.querySelector(".raptiye");
    if (!d) return;
    d.setAttribute("aria-pressed", String(sabit));
    d.setAttribute("aria-label", arayuz(sabit ? "kart.serbest" : "kart.sabitle", raptiyeDil));
    d.title = d.getAttribute("aria-label");
  }
  function raptiyeKur(kart, dil) {
    raptiyeDil = dil;
    const d = document.querySelector(".raptiye");
    if (!d) return;
    raptiyeGuncelle();
    if (d.dataset.kurulu) return;
    d.dataset.kurulu = "1";
    d.addEventListener("click", () => {
      sabit = !sabit;
      try { localStorage.setItem(SABIT_ANAHTARI, sabit ? "1" : "0"); } catch (_) {}
      if (sabit && egimKart) duzle(egimKart);
      raptiyeGuncelle();
      bildir(arayuz(sabit ? "kart.sabitlendi" : "kart.serbestBirakildi", raptiyeDil));
    });
  }

  function egimKur(kart) {
    egimKart = kart;
    if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
      kart.addEventListener("pointermove", (e) => {
        if (HAREKET_AZ.matches) return;
        const r = kart.getBoundingClientRect();
        kart.style.transition = "none";
        egimUygula(kart, (e.clientX - r.left) / r.width - 0.5, (e.clientY - r.top) / r.height - 0.5);
      });
      kart.addEventListener("pointerleave", () => duzle(kart));
    } else {
      jiroskopKur();
    }
  }

  /* ---------- Bölümler ---------- */
  function biletHTML(dil) {
    const u = URUN();
    const dok = anaDokuman();
    const pdf = pdfBaglantisi(dok, dil);
    const dokTr = dok.diller[pdf ? pdf.dil : "tr"] || {};
    const qr = qrBilgisi();

    const ozetSatiri = u.ozet
      .filter((o) => o.aralik && o.birim)
      .map((o) => aralik(o.aralik, dil) + " " + birim(o.birim, dil))
      .concat(u.ozet.filter((o) => o.etiket.tr === "Yakıt").map((o) => metin(o.deger, dil)))
      .join(" · ");

    let modelKutu = "";
    if (qr.modelHam || qr.seri) {
      const parca = [];
      if (qr.satir) parca.push(esc(u.ad) + " " + (u.modelOnEki ? esc(u.modelOnEki) + qr.satir[0] : sayi(qr.satir[0], dil) + " " + birim("kW", dil)));
      else if (qr.modelHam) parca.push(esc(u.ad) + " " + esc(qr.modelHam));
      modelKutu =
        '<div class="bilet-model"><span>' + arayuz("kart.buKazan", dil) + "</span>" +
        (parca.length ? "<b>" + parca.join("") + "</b>" : "") +
        (qr.seri ? "<div>" + arayuz("kart.seriNo", dil) + ": " + esc(qr.seri) + "</div>" : "") +
        "</div>";
    }

    // Özet çipler: model biliniyorsa o modelin değerleri, değilse seri özeti
    let cipler;
    if (qr.satir) {
      const m = qr.satir;
      cipler = [
        [arayuz("model.kapasite", dil), (m[1] === m[2] ? sayi(m[1], dil) : aralik([m[1], m[2]], dil)) + " " + birim("kcalh", dil)],
        // su hacmi kaynakta yoksa (null) yerine urun.js'deki modelEkCip sütunu gösterilir
        m[3] != null || !u.modelEkCip
          ? [arayuz("model.suHacmi", dil), sayi(m[3], dil, 3) + " " + birim("m3", dil)]
          : [metin(u.modelEkCip.etiket, dil), String(m[u.modelEkCip.sutun])],
        [arayuz("model.olcu", dil), sayi(m[4], dil) + " × " + sayi(m[5], dil) + " × " + sayi(m[6], dil) + " " + birim("mm", dil)],
        [arayuz("model.agirlik", dil), sayi(m[7], dil) + " " + birim("kg", dil)]
      ];
    } else {
      cipler = u.ozet.map((o) => [
        metin(o.etiket, dil),
        o.aralik ? aralik(o.aralik, dil) + " " + birim(o.birim, dil) : metin(o.deger, dil)
      ]);
    }

    // gorsel/{ad}-{800|1600}.{webp|jpg} (§3.4 adlandırma); büyük görünüm 1600 px'i açar
    const G = u.gorselGenislikleri || [800, 1600];
    const set = (ad, uz) => G.map((w) => "gorsel/" + esc(ad) + "-" + w + "." + uz + " " + w + "w").join(", ");
    const galeri = u.galeri.length ? u.galeri : [u.galeriYedek];
    const slaytlar = galeri.map((g, i) =>
      '<figure data-i="' + i + '"><button type="button" data-buyut="' + i + '" data-buyuk="gorsel/' + esc(g.gorsel) + "-" + G[G.length - 1] + '.jpg" aria-label="' + esc(arayuz("galeri.buyut", dil) + ": " + metin(g.alt, dil)) + '">' +
      '<picture><source type="image/webp" srcset="' + set(g.gorsel, "webp") + '" sizes="(min-width: 480px) 448px, calc(100vw - 32px)">' +
      '<img src="gorsel/' + esc(g.gorsel) + "-" + G[0] + '.jpg" srcset="' + set(g.gorsel, "jpg") + '" sizes="(min-width: 480px) 448px, calc(100vw - 32px)" alt="' + esc(metin(g.alt, dil)) + '" ' +
      (i === 0 ? 'fetchpriority="high"' : 'loading="lazy"') + ' decoding="async" width="1760" height="1056"></picture></button></figure>'
    ).join("");

    let indir = "";
    if (pdf) {
      const meta = pdf.boyutMB != null ? arayuz("goruntule.meta", dil, { boyut: mbYaz(pdf.boyutMB, dil) }) : "PDF";
      indir =
        '<a class="btn-ana" href="' + esc(pdf.href) + '" target="_blank" rel="noopener" hreflang="' + pdf.dil + '">' +
        ikon("goz") + "<span><b>" + (dok.butonEtiketi ? esc(metin(dok.butonEtiketi, dil)) : arayuz("goruntule", dil)) + "</b><small>" + meta + "</small></span></a>" +
        (pdf.farkliDil ? '<p class="belge-dili">' + arayuz("belgeDili", dil, { dil: arayuz("dilAdi." + pdf.dil, dil) }) + "</p>" : "") +
        '<div class="ikincil-satir">' +
        '<a class="btn-ikincil" href="' + esc(pdf.href) + '" download="' + esc(pdf.indirmeAdi) + '" hreflang="' + pdf.dil + '">' + ikon("indir") + arayuz("indir", dil) + "</a>" +
        '<button class="btn-ikincil" type="button" data-paylas>' + ikon("paylas") + arayuz("paylas", dil) + "</button>" +
        "</div>";
    }

    return (
      '<div class="bilet-sahne"><article class="bilet" aria-labelledby="seri-adi">' +
        '<div class="bilet-ust">' +
          '<canvas class="bilet-doku" aria-hidden="true"></canvas>' +
          '<span class="bilet-filigran" aria-hidden="true">' + esc(u.belgeKodu) + "</span>" +
          '<div class="bilet-satir">' + kartLogo +
            '<span class="bilet-rev">' + (dok.kartEtiketi ? esc(metin(dok.kartEtiketi, dil)) : arayuz("kart.etiket", dil)) + "</span>" +
          "</div>" +
          '<div class="bilet-tur">' + esc(metin(u.tur, dil)) + "</div>" +
          '<h1 id="seri-adi">' + esc(u.ad) + (u.rozet ? '<span class="bilet-rozet">' + esc(u.rozet) + "</span>" : "") + "</h1>" +
          '<p class="bilet-alt-baslik">' + esc(ozetSatiri) + "</p>" +
          (u.hero.altBaslik ? '<p class="bilet-alt-baslik" style="font-size:13px;opacity:.8">' + esc(metin(u.hero.altBaslik, dil)) + "</p>" : "") +
          modelKutu +
        "</div>" +
        '<div class="bilet-delik" aria-hidden="true"><i></i></div>' +
        '<div class="bilet-alt">' +
          '<div class="galeri" role="region" aria-roledescription="carousel" aria-label="' + arayuz("bolum.galeri", dil) + '">' +
            '<div class="galeri-serit" tabindex="0">' + slaytlar + "</div>" +
            '<button class="galeri-ok" type="button" data-yon="-1" aria-label="' + arayuz("galeri.onceki", dil) + '">' + ikon("sol") + "</button>" +
            '<button class="galeri-ok" type="button" data-yon="1" aria-label="' + arayuz("galeri.sonraki", dil) + '">' + ikon("sag") + "</button>" +
            '<div class="galeri-noktalar" aria-hidden="true"></div>' +
          "</div>" +
          '<h2 class="gizli">' + arayuz("bolum.ozet", dil) + "</h2>" +
          '<div class="ozet">' + cipler.map((c) => '<div class="cip"><span>' + esc(c[0]) + "</span><b>" + esc(c[1]) + "</b></div>").join("") + "</div>" +
          '<div class="eylemler">' + indir + "</div>" +
        "</div>" +
        '<div class="bilet-parlama" aria-hidden="true"></div>' +
      "</article></div>"
    );
  }

  function guvenlikHTML(dil) {
    const liste = URUN().guvenlik.slice(0, 5).map((g) => (typeof g === "string" ? window.UYARILAR[g] : g)).filter(Boolean);
    if (!liste.length) return "";
    const satir = (u) =>
      '<li class="uyari" data-seviye="' + u.seviye + '">' +
        '<span class="uyari-seviye">' + arayuz("seviye." + u.seviye, dil) +
          (u.kosul ? "<small>" + arayuz(u.kosul, dil) + "</small>" : "") + "</span>" +
        "<p>" + esc(metin(u.metin, dil)) + "</p></li>";
    const ilk = liste.slice(0, 1), kalan = liste.slice(1);
    return (
      '<section class="bolum" aria-labelledby="b-guvenlik"><h2 id="b-guvenlik">' + arayuz("bolum.guvenlik", dil) + "</h2>" +
      '<div class="panel">' +
        '<ul class="uyarilar">' + ilk.map(satir).join("") + "</ul>" +
        (kalan.length
          ? '<details class="uyari-diger"><summary><span class="ac">' + arayuz("guvenlik.tumu", dil, { n: kalan.length }) + "</span>" +
            '<span class="kapa">' + arayuz("guvenlik.gizle", dil) + "</span>" + ikon("sag", "ikon ok") + "</summary>" +
            '<ul class="uyarilar">' + kalan.map(satir).join("") + "</ul></details>"
          : "") +
      "</div></section>"
    );
  }

  // Ek dokümanlar: urun.js'de "goster: true" olan, ana olmayan belgeler (ör. pano kılavuzu)
  function dokumanlarHTML(dil) {
    const liste = (URUN().dokumanlar || []).filter((d) => !d.ana && d.goster);
    if (!liste.length) return "";
    const satirlar = liste.map((d) => {
      const pdf = pdfBaglantisi(d, dil);
      if (!pdf) return "";
      const meta = [d.diller[pdf.dil].sayfa ? d.diller[pdf.dil].sayfa + " " + ({ tr: "sayfa", en: "pages", ru: "стр." })[dil] : "", mbYaz(pdf.boyutMB, dil),
        pdf.farkliDil ? arayuz("dilAdi." + pdf.dil, dil) : ""].filter(Boolean).join(" · ");
      return '<a class="ilt-satir" href="' + esc(pdf.href) + '" target="_blank" rel="noopener" hreflang="' + pdf.dil + '">' +
        '<span class="ilt-ikon">' + ikon("dosya") + "</span>" +
        '<span class="ilt-metin"><small>PDF' + (meta ? " · " + esc(meta) : "") + "</small><b>" + esc(metin(d.baslik, dil)) + "</b></span>" +
        ikon("indir", "ikon ok") + "</a>";
    }).join("");
    return '<section class="bolum" aria-labelledby="b-dokumanlar"><h2 id="b-dokumanlar">' + arayuz("bolum.dokumanlar", dil) + "</h2>" +
      '<div class="panel iletisim">' + satirlar + "</div></section>";
  }

  function iletisimHTML(dil) {
    const i = URUN().iletisim;
    if (!i) return "";
    const bos = (v) => !v || /\{\{/.test(v);
    const qr = qrBilgisi();
    const konu = ["Servis talebi", URUN().ad, qr.modelHam, qr.seri ? "SN " + qr.seri : ""].filter(Boolean).join(" – ");
    const s = [];
    const satir = (href, ik, etiket, deger, yeni) =>
      '<a class="ilt-satir" href="' + esc(href) + '"' + (yeni ? ' target="_blank" rel="noopener"' : "") + ">" +
        '<span class="ilt-ikon">' + ikon(ik) + "</span>" +
        '<span class="ilt-metin"><small>' + etiket + "</small><b>" + esc(deger) + "</b></span>" +
        ikon("sag", "ikon ok") + "</a>";
    if (!bos(i.telefon)) s.push(satir("tel:" + i.telefon.replace(/[^\d+]/g, ""), "telefon", arayuz("iletisim.telefon", dil), i.telefon));
    if (!bos(i.whatsapp)) s.push(satir("https://wa.me/" + i.whatsapp, "whatsapp", arayuz("iletisim.whatsapp", dil), "+" + i.whatsapp, true));
    if (!bos(i.eposta)) s.push(satir("mailto:" + i.eposta + "?subject=" + encodeURIComponent(konu), "zarf", arayuz("iletisim.eposta", dil), i.eposta));
    if (!bos(i.harita)) s.push(satir(i.harita, "harita", arayuz("iletisim.adres", dil), metin(i.adres, dil), true));
    if (!bos(i.web)) s.push(satir(i.web, "dunya", arayuz("iletisim.web", dil), i.web.replace(/^https?:\/\/|\/$/g, ""), true));
    return (
      '<section class="bolum" aria-labelledby="b-iletisim"><h2 id="b-iletisim">' + arayuz("bolum.iletisim", dil) + "</h2>" +
      '<div class="panel iletisim">' + s.join("") + "</div>" +
      '<p class="iletisim-not">' + ikon("bilgi") + "<span>" + arayuz("iletisim.seriNo", dil) + "</span></p>" +
      "</section>"
    );
  }

  function altBilgiHTML(dil) {
    const i = URUN().iletisim || {};
    return "<b>" + esc(i.unvan || "ENORPA") + "</b>" +
      esc(metin(i.adres, dil)) + "<br>© " + new Date().getFullYear() + " ENORPA · " + arayuz("altbilgi.haklar", dil) + " · v" + esc(URUN().sablonSurumu);
  }

  /* ---------- Etkileşimler ---------- */
  function galeriKur(kok, dil) {
    const serit = kok.querySelector(".galeri-serit");
    if (!serit) return;
    const noktalar = kok.querySelector(".galeri-noktalar");
    const oklar = kok.querySelectorAll(".galeri-ok");
    const slaytlar = () => [...serit.querySelectorAll("figure")];

    // Bulunamayan görseli düşür; hiçbiri kalmazsa yedeği göster
    serit.querySelectorAll("img").forEach((img) => {
      const dus = () => {
        img.closest("figure").remove();
        if (!slaytlar().length) {
          const y = URUN().galeriYedek;
          serit.innerHTML = '<figure><img src="gorsel/' + esc(y.gorsel) + '.jpg" alt="' + esc(metin(y.alt, dil)) + '"></figure>';
        }
        guncelle();
      };
      if (img.complete && img.naturalWidth === 0) dus();
      else img.addEventListener("error", dus, { once: true });
    });

    function sira() { return Math.round(serit.scrollLeft / Math.max(1, serit.clientWidth)); }
    function guncelle() {
      const n = slaytlar().length, i = sira();
      noktalar.innerHTML = n > 1 ? Array.from({ length: n }, (_, k) => '<span class="' + (k === i ? "aktif" : "") + '"></span>').join("") : "";
      oklar[0].disabled = i <= 0;
      oklar[1].disabled = i >= n - 1;
    }
    let bekle;
    serit.addEventListener("scroll", () => { cancelAnimationFrame(bekle); bekle = requestAnimationFrame(guncelle); }, { passive: true });
    oklar.forEach((o) => o.addEventListener("click", () => {
      serit.scrollTo({ left: (sira() + Number(o.dataset.yon)) * serit.clientWidth, behavior: HAREKET_AZ.matches ? "auto" : "smooth" });
    }));
    serit.addEventListener("keydown", (e) => {
      const yon = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (!yon) return;
      e.preventDefault();
      serit.scrollTo({ left: (sira() + yon) * serit.clientWidth, behavior: "smooth" });
    });

    // Büyütme
    serit.addEventListener("click", (e) => {
      const b = e.target.closest("[data-buyut]");
      if (!b) return;
      const img = b.querySelector("img");
      let d = document.getElementById("buyuk");
      if (!d || !d.showModal) { window.open(img.src, "_blank", "noopener"); return; }
      d.querySelector("img").src = b.dataset.buyuk || img.currentSrc || img.src;
      d.querySelector("img").alt = img.alt;
      d.querySelector("button").setAttribute("aria-label", arayuz("galeri.kapat", dil));
      d.showModal();
    });
    guncelle();
  }

  function bildir(s) {
    let b = document.querySelector(".bildirim");
    if (!b) { b = document.createElement("div"); b.className = "bildirim"; b.setAttribute("role", "status"); document.body.append(b); }
    b.textContent = s;
    b.classList.add("goster");
    clearTimeout(bildir.z);
    bildir.z = setTimeout(() => b.classList.remove("goster"), 2200);
  }

  async function paylas(dil) {
    const url = location.href;
    const veri = { title: document.title, text: metin(URUN().meta.aciklama, dil), url };
    try {
      if (navigator.share) { await navigator.share(veri); return; }
    } catch (e) { if (e && e.name === "AbortError") return; }
    try { await navigator.clipboard.writeText(url); bildir(arayuz("baglantiKopyalandi", dil)); }
    catch (_) { prompt("", url); }
  }

  /* ---------- Çizim ---------- */
  function sayfayiCiz(dil) {
    const icerik = document.getElementById("icerik");
    const kaydirma = window.scrollY;
    const galeriKonum = icerik.querySelector(".galeri-serit");
    const galeriSol = galeriKonum ? galeriKonum.scrollLeft : 0;

    icerik.innerHTML = biletHTML(dil) + guvenlikHTML(dil) + dokumanlarHTML(dil) + iletisimHTML(dil);
    document.querySelector(".alt-bilgi").innerHTML = altBilgiHTML(dil);

    const serit = icerik.querySelector(".galeri-serit");
    if (serit && galeriSol) serit.scrollLeft = galeriSol;
    galeriKur(icerik, dil);
    const kart = icerik.querySelector(".bilet");
    if (galeriKonum) kart.style.animation = "none";   // dil değişiminde giriş animasyonu tekrarlanmaz
    dokuyuBaslat(icerik.querySelector(".bilet-doku"));
    egimKur(kart);
    raptiyeKur(kart, dil);
    icerik.querySelector("[data-paylas]")?.addEventListener("click", () => paylas(dil));
    window.scrollTo(0, kaydirma);
  }

  /* ---------- Dil seçici (§5.4) ---------- */
  function ustBarCiz() {
    const bar = document.querySelector(".ust-bar");
    bar.innerHTML =
      '<button class="raptiye" type="button" aria-pressed="false">' + ikon("raptiye") + "</button>" +
      '<div class="dil-alani">' + ikon("dunya", "dil-ikon") +
      '<div class="dil-secici" role="radiogroup" aria-label="Dil · Language · Язык" data-aktif="tr">' +
      DILLER.map((d, i) =>
        '<button type="button" role="radio" aria-checked="' + (i === 0) + '" tabindex="' + (i === 0 ? 0 : -1) + '" data-dil="' + d + '" lang="' + d + '" title="' + DIL_ADI[d] + '" aria-label="' + DIL_ADI[d] + '">' + d.toUpperCase() + "</button>"
      ).join("") +
      '<span class="dil-gosterge" aria-hidden="true"></span></div></div>';
    addEventListener("scroll", () => bar.classList.toggle("golgeli", scrollY > 4), { passive: true });
  }

  function seciciyiKur() {
    const secici = document.querySelector(".dil-secici");
    const dugmeler = [...secici.querySelectorAll("[data-dil]")];
    secici.addEventListener("click", (e) => {
      const d = e.target.closest("[data-dil]");
      if (d) dilDegistir(d.dataset.dil);
    });
    secici.addEventListener("keydown", (e) => {
      const yon = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
      if (!yon) return;
      e.preventDefault();
      const i = DILLER.indexOf(aktifDil);
      const yeni = DILLER[(i + yon + DILLER.length) % DILLER.length];
      dilDegistir(yeni);
      secici.querySelector('[data-dil="' + yeni + '"]').focus();
    });
    return (dil) => {
      secici.dataset.aktif = dil;
      for (const d of dugmeler) {
        const secili = d.dataset.dil === dil;
        d.setAttribute("aria-checked", String(secili));
        d.tabIndex = secili ? 0 : -1;
      }
    };
  }

  function dilDegistir(dil) {
    if (dil === aktifDil || !DILLER.includes(dil)) return;
    const bekle = HAREKET_AZ.matches ? 0 : 150;
    const icerik = document.getElementById("icerik");
    seciciyiGuncelle(dil);
    icerik.classList.add("dil-gecisi");
    setTimeout(() => { diliUygula(dil); icerik.classList.remove("dil-gecisi"); }, bekle);
    try { localStorage.setItem(DEPO_ANAHTARI, dil); } catch (_) {}
    const url = new URL(location.href);
    url.searchParams.set("lang", dil);
    history.replaceState(null, "", url);
  }

  function diliUygula(dil) {
    aktifDil = dil;
    document.documentElement.lang = dil;
    document.title = metin(URUN().meta.baslik, dil);
    document.querySelector('meta[name="description"]')?.setAttribute("content", metin(URUN().meta.aciklama, dil));
    seciciyiGuncelle(dil);
    const serit = document.querySelector(".taslak-seridi");
    if (serit) serit.textContent = arayuz("taslak", dil);
    sayfayiCiz(dil);
  }

  document.addEventListener("DOMContentLoaded", () => {
    const u = URUN();
    const kok = document.documentElement.style;
    kok.setProperty("--vurgu", u.renk.vurgu);
    kok.setProperty("--vurgu-acik", u.renk.acik);
    if (u.renk.koyu) kok.setProperty("--vurgu-koyu", u.renk.koyu);
    if (u.durum === "taslak") {
      const s = document.createElement("div");
      s.className = "taslak-seridi";
      s.setAttribute("role", "note");
      document.body.prepend(s);
    }
    ustBarCiz();
    seciciyiGuncelle = seciciyiKur();
    diliUygula(ilkDiliBul());
  });
})();
