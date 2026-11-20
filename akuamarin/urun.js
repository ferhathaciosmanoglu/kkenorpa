/* =====================================================================
   akuamarin/urun.js — AKUAMARİN sayfasının BÜTÜN içeriği
   Kurallar: her metin { tr, en, ru } üçlüsüdür · eksik dil taslakta TR'ye düşer
   Kullanım kılavuzu üç dilde (TR, EN, RU) zorunludur · Bölüm 8.11
   {{...}} = doldurulacak · ⚠️ = doğrulanacak · ayrıntı: KILAVUZ_SABLONU.md §6
   ===================================================================== */
window.URUN = {
  sablonSurumu: "1.1",
  durum: "taslak",                    // EN/RU PDF, çeviri onayı ve K-kararları gelince "yayinda"
  kod: "akuamarin",
  belgeKodu: "AKU",
  ad: "Akuamarin",                    // çevrilmez, CSS ile büyütülmez (🟡 K-03)
  rozet: null,
  tur: { tr: "Sıcak Su Kazanı", en: "Hot Water Boiler", ru: "Водогрейный котёл" },
  renk: { vurgu: "#D2541A", acik: "#FBEEE7", koyu: "#E2601F", doku: "#EE7A3D" }, // ENORPA turuncusu (logo #F26532)

  meta: {
    baslik: {
      tr: "Akuamarin Kullanım Kılavuzu | ENORPA",
      en: "Akuamarin User Manual | ENORPA",
      ru: "Akuamarin — руководство по эксплуатации | ENORPA"
    },
    aciklama: {
      tr: "Akuamarin sıcak su kazanının kullanım kılavuzu, teknik bilgileri ve servis iletişimi.",
      en: "User manual, technical information and service contacts for the Akuamarin hot water boiler.",
      ru: "Руководство по эксплуатации, технические данные и сервисные контакты водогрейного котла Akuamarin."
    }
  },

  hero: {
    // Kılavuz kapağındaki alt başlık (pazarlama sloganı değil; slogan 🟡 K-11 bekliyor)
    altBaslik: {
      tr: "Montaj · Devreye alma · İşletme · Bakım",
      en: "Installation · Commissioning · Operation · Maintenance",
      ru: "Монтаж · Ввод в эксплуатацию · Эксплуатация · Обслуживание"
    },
    slogan: null
  },

  // Kartın üst kısmında, ad altında
  ozet: [
    { etiket: { tr: "Kapasite", en: "Heat output", ru: "Мощность" },
      aralik: [510, 9600], birim: "kW",
      kaynak: "Kılavuz ENP-AKM-TR R01 — kapak ve §16" },
    { etiket: { tr: "Model", en: "Models", ru: "Модели" },
      deger: { tr: "18 model", en: "18 models", ru: "18 моделей" },
      kaynak: "Kılavuz ENP-AKM-TR R01 — §16 tablo" },
    { etiket: { tr: "Yapı", en: "Design", ru: "Конструкция" },
      deger: { tr: "3 geçişli, silindirik", en: "Three-pass, cylindrical", ru: "Трёхходовой, цилиндрический" },
      kaynak: "Kılavuz ENP-AKM-TR R01 — §01" },
    { etiket: { tr: "Yakıt", en: "Fuel", ru: "Топливо" },
      deger: { tr: "Sıvı / gaz", en: "Liquid / gas", ru: "Жидкое / газ" },
      kaynak: "Kılavuz ENP-AKM-TR R01 — kapak" }
  ],

  // QR adresine ?model=4800kW eklenirse kartta o modelin değerleri gösterilir.
  // [kW, kcal/h min, kcal/h max, su hacmi m³, en mm, boy mm, yükseklik mm, ağırlık kg]
  // Kaynak: Kılavuz ENP-AKM-TR R01 §16 "Kapasite, ölçü ve ağırlık"
  modeller: [
    [510,   309600,  438600,  1.715, 1580, 1965, 1745,  1820],
    [660,   438600,  567600,  2.047, 1625, 2230, 1790,  2040],
    [810,   567600,  696600,  2.366, 1675, 2450, 1840,  2325],
    [960,   696600,  825600,  2.787, 1730, 2660, 1895,  2570],
    [1200,  825600, 1032000,  3.228, 1775, 2930, 1940,  2920],
    [1500, 1032000, 1290000,  4.037, 1885, 3150, 2050,  3815],
    [1800, 1290000, 1548000,  4.772, 1955, 3425, 2120,  4280],
    [2400, 1548000, 2064000,  6.127, 2065, 3915, 2230,  5265],
    [3000, 2064000, 2580000,  7.035, 2120, 4335, 2285,  6045],
    [3600, 2580000, 3096000,  8.118, 2195, 4695, 2365,  6865],
    [4200, 3096000, 3612000,  9.129, 2255, 5025, 2420,  7670],
    [4800, 3612000, 4128000, 10.416, 2325, 5340, 2490,  8475],
    [5400, 4128000, 4644000, 11.671, 2395, 5590, 2560,  9830],
    [6000, 4644000, 5160000, 12.692, 2450, 5855, 2615, 10675],
    [6600, 5160000, 5676000, 13.835, 2505, 6100, 2670, 11470],
    [7200, 5676000, 6192000, 14.814, 2550, 6315, 2715, 12250],
    [8400, 6192000, 7224000, 16.871, 2645, 6715, 2810, 14470],
    [9600, 7224000, 8256000, 18.641, 2710, 7120, 2875, 15995]
  ],

  guvenlik: ["G1", "G2", "G3", "G6", "G7"],

  // Render görselleri: gorsel/{ad}-{800|1600}.{webp|jpg}, 5:3 (kaynak: gorsel/kaynak/, repoya girmez)
  // Kaynak eşleşmesi: F → onden · FRI → on · BLI → arka · L → yan (Enorpa A0600 renderları)
  // Bulunamayan görsel galeriden otomatik düşer; hiçbiri yoksa "yedek" görünür.
  gorselGenislikleri: [800, 1600],
  galeri: [
    { gorsel: "akuamarin-on",
      alt: { tr: "Önden üç çeyrek görünüm, brülörlü", en: "Front three-quarter view with burner",
             ru: "Вид спереди в три четверти, с горелкой" } },
    { gorsel: "akuamarin-yan",
      alt: { tr: "Yandan görünüm", en: "Side view", ru: "Вид сбоку" } },
    { gorsel: "akuamarin-onden",
      alt: { tr: "Ön kapak ve brülör", en: "Front door and burner", ru: "Передняя дверь и горелка" } },
    { gorsel: "akuamarin-arka",
      alt: { tr: "Arkadan üç çeyrek görünüm", en: "Rear three-quarter view", ru: "Вид сзади в три четверти" } }
  ],
  galeriYedek: { gorsel: "akuamarin-yedek",
    alt: { tr: "Akuamarin sıcak su kazanı", en: "Akuamarin hot water boiler", ru: "Водогрейный котёл Akuamarin" } },

  dokumanlar: [
    {
      tur: "kullanim",
      ana: true,
      baslik: { tr: "Kullanım Kılavuzu", en: "User Manual", ru: "Руководство по эксплуатации" },
      belgeNo: "ENP-AKM",             // ⚠️ PDF'te ENP-AKM-TR; şablon ENR-KLV-AKU öneriyor — birleştirilecek
      diller: {
        tr: {
          dosya: "pdf/kilavuz-tr.pdf",
          indirmeAdi: "ENORPA_Akuamarin_Kullanim_Kilavuzu_TR_Rev01.pdf",
          revizyon: "01", tarih: "2026-11", boyutMB: 1.0, sayfa: 22
        },
        en: null,                     // {{EN PDF}} — yayından önce zorunlu (Bölüm 8.11)
        ru: null                      // {{RU PDF}} — yayından önce zorunlu (Bölüm 8.11)
      }
    }
  ],

  iletisim: {                         // 🟡 K-06 — mevcut sayfadaki bilgiler
    unvan: "ENORPA ENERJİ SAN. TİC. LTD. ŞTİ.",
    telefon: "+90 850 471 21 00",
    whatsapp: null,                   // {{WHATSAPP_NUMARASI}} → yalnızca rakam: "90xxxxxxxxxx"
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
