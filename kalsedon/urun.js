/* =====================================================================
   kalsedon/urun.js — KALSEDON sayfasının BÜTÜN içeriği
   Kurallar: her metin { tr, en, ru } üçlüsüdür · eksik dil taslakta TR'ye düşer
   Tasarım Akuamarin / Turkuaz ile birebir aynıdır (ENORPA turuncusu, bilet kart).
   Kaynaklar: "KALSEDON SERİSİ" broşürü TR/EN/RU (2026, s.4 Modül H tablosu),
   Kalsedon Kullanım & Bakım Kılavuzu 2018-R.2, KALS 1500–3500 föyleri (2023)
   ===================================================================== */
window.URUN = {
  sablonSurumu: "1.1",
  durum: "yayinda",                   // yayında — EN/RU çeviri onayı bekliyor
  kod: "kalsedon",
  belgeKodu: "KLS",
  ad: "Kalsedon",                     // çevrilmez (🟡 K-03)
  rozet: null,
  tur: { tr: "Sıcak Su Kazanı", en: "Hot Water Boiler", ru: "Водогрейный котёл" },
  renk: { vurgu: "#D2541A", acik: "#FBEEE7", koyu: "#E2601F", doku: "#EE7A3D" }, // ENORPA turuncusu (Akuamarin ile aynı)

  meta: {
    baslik: {
      tr: "Kalsedon Kullanım Kılavuzu | ENORPA",
      en: "Kalsedon User Manual | ENORPA",
      ru: "Kalsedon — руководство по эксплуатации | ENORPA"
    },
    aciklama: {
      tr: "Kalsedon kömür yakıtlı, çift ocaklı sıcak su kazanının kullanım kılavuzu, teknik bilgileri ve servis iletişimi.",
      en: "User manual, technical information and service contacts for the Kalsedon coal-fired twin-furnace hot water boiler.",
      ru: "Руководство по эксплуатации, технические данные и сервисные контакты водогрейного котла Kalsedon на угле с двумя топками."
    }
  },

  hero: {
    altBaslik: {
      tr: "Çift ocak · Stokerli · Sera ısıtma",
      en: "Twin furnace · Stoker-fired · Greenhouse heating",
      ru: "Две топки · Стокерная подача · Обогрев теплиц"
    },
    slogan: null
  },

  ozet: [
    { etiket: { tr: "Kapasite", en: "Heat output", ru: "Мощность" },
      aralik: [1500000, 3500000], birim: "kcalh",
      kaynak: "Broşür s.4 Modül H tablosu (KL15–KL35)" },
    { etiket: { tr: "Model", en: "Models", ru: "Модели" },
      deger: { tr: "6 model", en: "6 models", ru: "6 моделей" },
      kaynak: "Broşür s.4 tablo" },
    { etiket: { tr: "Yapı", en: "Design", ru: "Конструкция" },
      deger: { tr: "3 geçişli, çift ocaklı", en: "Three-pass, twin furnace", ru: "Трёхходовой, с двумя топками" },
      kaynak: "Broşür s.3 '3 Geçişli'; Kılavuz 2018 'çift yanma odalı'" },
    { etiket: { tr: "Yakıt", en: "Fuel", ru: "Топливо" },
      deger: { tr: "Kömür (katı yakıt)", en: "Coal (solid fuel)", ru: "Уголь (твёрдое топливо)" },
      kaynak: "Kılavuz 2018 'kömürle çalışabilecek şekilde dizayn edilmiştir'" }
  ],

  // QR adresine ?model=KL30 (veya sahadaki adıyla ?model=3000) eklenirse kartta o modelin değerleri gösterilir.
  // [model no, kcal/h, kcal/h, su hacmi (kaynakta yok → null), en mm, boy mm, yükseklik mm, ağırlık kg, su gidiş–dönüş]
  // Kaynak: Broşür s.4 "Kazanların Modül H Kapsamına Göre Teknik Özellikleri"
  // Bütün modellerde: min. 55 °C · maks. 110 °C · işletme 3 bar · dizayn 3,45 bar · test 5,5 bar
  modelOnEki: "KL",
  modelCarpan: 100,                   // "Kalsedon 3000" = KL30
  modelEkCip: { etiket: { tr: "Su gidiş–dönüş", en: "Flow – return", ru: "Подача – обратка" }, sutun: 8 },
  modeller: [
    [15, 1500000, 1500000, null, 2400, 6720, 2600,  9570, "DN150"],
    [17, 1750000, 1750000, null, 2400, 6950, 2600, 10265, "DN150"],
    [20, 2000000, 2000000, null, 2400, 7100, 2550, 10725, "DN150"],
    [25, 2500000, 2500000, null, 2400, 7350, 2600, 12985, "DN150"],
    [30, 3000000, 3000000, null, 2400, 8350, 2600, 15800, "DN150"],
    [35, 3500000, 3500000, null, 2400, 8890, 2600, 16280, "DN200"]
  ],
  // Genleşme / şönt: KL15 DN65/DN50 · KL17 DN65/DN65 · KL20–25 DN80/DN65 · KL30 DN100/DN65 · KL35 DN125/DN80

  guvenlik: ["G2", "G3", "G4", "G6", "G5"],

  gorselGenislikleri: [800, 1600],
  galeri: [
    { gorsel: "kalsedon-on",
      alt: { tr: "Önden üç çeyrek görünüm, iki ocak kapağı", en: "Front three-quarter view with the two furnace doors",
             ru: "Вид спереди в три четверти, дверцы двух топок" } },
    { gorsel: "kalsedon-arka",
      alt: { tr: "Arkadan görünüm: kazan bunkeri, stoker redüktörleri ve temiz hava fanı", en: "Rear view: boiler bunker, stoker gear motors and fresh air fan",
             ru: "Вид сзади: бункер котла, мотор-редукторы стокеров и дутьевой вентилятор" } },
    { gorsel: "kalsedon-sistem",
      alt: { tr: "Sistem: kazan, multisiklon, baca gazı fanı ve baca", en: "System: boiler, multicyclone, flue gas fan and chimney",
             ru: "Система: котёл, мультициклон, дымосос и дымовая труба" } }
  ],
  galeriYedek: { gorsel: "kalsedon-yedek",
    alt: { tr: "Kalsedon sıcak su kazanı", en: "Kalsedon hot water boiler", ru: "Водогрейный котёл Kalsedon" } },

  dokumanlar: [
    {
      tur: "kullanim",
      ana: true,
      baslik: { tr: "Kullanım Kılavuzu", en: "User Manual", ru: "Руководство по эксплуатации" },
      belgeNo: "ENP-KLS",             // PDF kodları: ENP-KLS-TR / -EN / -RU · kaynak: araclar/kilavuz-pdf/uret_kalsedon.py
      diller: {
        tr: { dosya: "pdf/kilavuz-tr.pdf", indirmeAdi: "ENORPA_Kalsedon_Kullanim_Kilavuzu_TR_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 1.0, sayfa: 23, onbellek: "20261120" },
        en: { dosya: "pdf/kilavuz-en.pdf", indirmeAdi: "ENORPA_Kalsedon_User_Manual_EN_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 1.0, sayfa: 23, onbellek: "20261120" },
        ru: { dosya: "pdf/kilavuz-ru.pdf", indirmeAdi: "ENORPA_Kalsedon_Rukovodstvo_RU_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 1.1, sayfa: 23, onbellek: "20261120" }
      }
    },
    {
      // Otomasyon panosu kullanım kılavuzu — TR/EN/RU · ENP-KLS-PANO · kaynak: araclar/kilavuz-pdf/uret_pano.py (Word kılavuzundan)
      tur: "pano",
      goster: true,
      belgeNo: "ENP-KLS-PANO",
      baslik: { tr: "Otomasyon Panosu Kullanım Kılavuzu", en: "Automation Panel User Manual", ru: "Руководство по щиту автоматики" },
      diller: {
        tr: { dosya: "pdf/pano-tr.pdf", indirmeAdi: "ENORPA_Kalsedon_Pano_Kullanim_Kilavuzu_TR_Rev01.pdf", revizyon: "01", tarih: "2026-11", boyutMB: 2.0, sayfa: 10, onbellek: "20261124" },
        en: { dosya: "pdf/pano-en.pdf", indirmeAdi: "ENORPA_Kalsedon_Panel_Manual_EN_Rev01.pdf", revizyon: "01", tarih: "2026-11", boyutMB: 2.0, sayfa: 10, onbellek: "20261124" },
        ru: { dosya: "pdf/pano-ru.pdf", indirmeAdi: "ENORPA_Kalsedon_Rukovodstvo_Shchit_RU_Rev01.pdf", revizyon: "01", tarih: "2026-11", boyutMB: 2.0, sayfa: 10, onbellek: "20261124" }
      }
    },
    {
      // Ürün broşürü (2026) — sayfada şimdilik gösterilmiyor; doğrudan bağlantıyla açılabilir
      tur: "katalog",
      baslik: { tr: "Ürün Kataloğu", en: "Product Catalogue", ru: "Каталог продукции" },
      diller: {
        tr: { dosya: "pdf/katalog-tr.pdf", indirmeAdi: "ENORPA_Kalsedon_Urun_Katalogu_TR.pdf", revizyon: "2026", boyutMB: 1.1, sayfa: 7, onbellek: "20261120" },
        en: { dosya: "pdf/katalog-en.pdf", indirmeAdi: "ENORPA_Kalsedon_Product_Catalogue_EN.pdf", revizyon: "2026", boyutMB: 1.5, sayfa: 7, onbellek: "20261120" },
        ru: { dosya: "pdf/katalog-ru.pdf", indirmeAdi: "ENORPA_Kalsedon_Katalog_RU.pdf", revizyon: "2026", boyutMB: 2.3, sayfa: 7, onbellek: "20261120" }
      }
    }
  ],

  iletisim: {                         // Akuamarin ile aynı (🟡 K-06)
    unvan: "ENORPA ENERJİ SAN. TİC. LTD. ŞTİ.",
    telefon: "+90 850 471 21 00",
    whatsapp: null,
    eposta: "turuncu@enorpa.com",
    web: "https://enorpa.com/",
    adres: {
      tr: "Sanayi Mahallesi 3231 Sokak No:12, 32200 Isparta, Türkiye",
      en: "Sanayi Mahallesi 3231 Sokak No:12, 32200 Isparta, Türkiye",
      ru: "Sanayi Mahallesi 3231 Sokak No:12, 32200 Ыспарта, Турция"
    },
    harita: "https://www.google.com/maps/search/?api=1&query=Sanayi+Mahallesi+3231+Sokak+No%3A12+32200+Isparta",
    calismaSaatleri: null
  },

  ceviriOnay: { en: null, ru: null }
};
