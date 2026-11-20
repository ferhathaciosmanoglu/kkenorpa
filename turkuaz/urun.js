/* =====================================================================
   turkuaz/urun.js — TURKUAZ sayfasının BÜTÜN içeriği
   Kurallar: her metin { tr, en, ru } üçlüsüdür · eksik dil taslakta TR'ye düşer
   Tasarım Akuamarin ile birebir aynıdır (ENORPA turuncusu, bilet kart).
   {{...}} = doldurulacak · ⚠️ = doğrulanacak · ayrıntı: KILAVUZ_SABLONU.md §6
   Kaynak: "TURKUAZ SERİSİ" broşürü TR / EN / RU (2026-02) — s.3 tanıtım, s.4 Modül H teknik tablo
   ===================================================================== */
window.URUN = {
  sablonSurumu: "1.1",
  durum: "yayinda",                   // yayında — EN/RU çeviri onayı bekliyor
  kod: "turkuaz",
  belgeKodu: "TRK",
  ad: "Turkuaz",                      // çevrilmez (EN broşürde "Turquoise" yazıyor; 🟡 K-03 gereği sayfada "Turkuaz")
  rozet: null,
  tur: { tr: "Sıcak Su Kazanı", en: "Hot Water Boiler", ru: "Водогрейный котёл" },
  renk: { vurgu: "#D2541A", acik: "#FBEEE7", koyu: "#E2601F", doku: "#EE7A3D" }, // ENORPA turuncusu (Akuamarin ile aynı)

  meta: {
    baslik: {
      tr: "Turkuaz Kullanım Kılavuzu | ENORPA",
      en: "Turkuaz User Manual | ENORPA",
      ru: "Turkuaz — руководство по эксплуатации | ENORPA"
    },
    aciklama: {
      tr: "Turkuaz katı yakıtlı sıcak su kazanının kullanım kılavuzu, teknik bilgileri ve servis iletişimi.",
      en: "User manual, technical information and service contacts for the Turkuaz solid-fuel hot water boiler.",
      ru: "Руководство по эксплуатации, технические данные и сервисные контакты водогрейного котла Turkuaz на твёрдом топливе."
    }
  },

  hero: {
    // Broşür s.5: "Katı yakıtın (pellet, prina, kömür vb.) doldurulduğu hazne"
    altBaslik: {
      tr: "Pelet · Prina · Kömür",
      en: "Pellets · Olive pomace · Coal",
      ru: "Пеллеты · Оливковый жмых · Уголь"
    },
    slogan: null
  },

  ozet: [
    { etiket: { tr: "Kapasite", en: "Heat output", ru: "Мощность" },
      aralik: [200000, 1750000], birim: "kcalh",
      kaynak: "Broşür s.4 Modül H tablosu (TR2–TR17). ⚠️ Broşür s.3'te '100.000–1.750.000', EN broşürde '100.000–1.000.000' yazıyor" },
    { etiket: { tr: "Model", en: "Models", ru: "Модели" },
      deger: { tr: "9 model", en: "9 models", ru: "9 моделей" },
      kaynak: "Broşür s.4 tablo" },
    { etiket: { tr: "Yapı", en: "Design", ru: "Конструкция" },
      deger: { tr: "3 geçişli, tek külhanlı", en: "Three-pass, single furnace", ru: "Трёхходовой, с одной топкой" },
      kaynak: "Broşür s.3 'Katı Yakıtlı - 3 Geçişli', s.4 'Tek Külhanlı Sıcak Su Kazanı'" },
    { etiket: { tr: "Yakıt", en: "Fuel", ru: "Топливо" },
      deger: { tr: "Katı yakıt", en: "Solid fuel", ru: "Твёрдое топливо" },
      kaynak: "Broşür s.3" }
  ],

  // QR adresine ?model=TR10 eklenirse kartta o modelin değerleri gösterilir ("Turkuaz TR10").
  // [model no, kcal/h, kcal/h, su hacmi (kaynakta yok → null), en mm, boy mm, yükseklik mm, ağırlık kg, su gidiş–dönüş]
  // Kaynak: Broşür s.4 "Kazanların Modül H Kapsamına Göre Teknik Özellikleri"
  // Bütün modellerde: min. 55 °C · maks. 110 °C · işletme 3 bar · dizayn 3,45 bar · test 5,5 bar
  modelOnEki: "TR",
  modelEkCip: { etiket: { tr: "Su gidiş–dönüş", en: "Flow – return", ru: "Подача – обратка" }, sutun: 8 },
  modeller: [
    [2,   200000,  200000, null, 1750, 3450, 2040, 2800, "DN65"],
    [3,   300000,  300000, null, 1780, 3600, 2065, 3100, "DN80"],
    [4,   400000,  400000, null, 1840, 3690, 2125, 3455, "DN80"],
    [5,   500000,  500000, null, 1850, 4120, 2000, 3850, "DN80"],
    [7,   750000,  750000, null, 1880, 4600, 2000, 4650, "DN100"],
    [10, 1000000, 1000000, null, 1940, 5845, 2120, 5970, "DN125"],
    [12, 1250000, 1250000, null, 1975, 5900, 2170, 7200, "DN125"],
    [15, 1500000, 1500000, null, 2020, 6000, 2200, 7460, "DN125"],
    [17, 1750000, 1750000, null, 2150, 6300, 2350, 8150, "DN150"]
  ],
  // Genleşme / şönt hatları (tabloda var, kartta gösterilmiyor):
  // TR2 DN40/DN25 · TR3–TR5 DN50/DN25 · TR7 DN50/DN50 · TR10–12 DN65/DN50 · TR15 DN65/DN65 · TR17 DN80/DN65

  guvenlik: ["G2", "G3", "G4", "G6", "G5"],   // G1 gaz, G7 kılavuza atıf yaptığı için alınmadı

  // Render görselleri: gorsel/{ad}-{800|1600}.{webp|jpg}, 5:3, gri stüdyo zemini
  // Kaynak renderların kırmızı gövde rengi ENORPA turuncusuna çevrildi (Akuamarin tonu)
  gorselGenislikleri: [800, 1600],
  galeri: [
    { gorsel: "turkuaz-on",
      alt: { tr: "Önden üç çeyrek görünüm, kazan kapakları", en: "Front three-quarter view with boiler doors",
             ru: "Вид спереди в три четверти, дверцы котла" } },
    { gorsel: "turkuaz-sistem",
      alt: { tr: "Sistem: yakıt bunkeri, siklon ayırıcı, fanlar ve baca", en: "System: fuel bunker, cyclone separator, fans and chimney",
             ru: "Система: бункер топлива, циклон, вентиляторы и дымовая труба" } },
    { gorsel: "turkuaz-arka",
      alt: { tr: "Arkadan görünüm, yakıt bunkeri ve besleme helezonu", en: "Rear view with fuel bunker and feed screw",
             ru: "Вид сзади, бункер топлива и шнек подачи" } }
  ],
  galeriYedek: { gorsel: "turkuaz-yedek",
    alt: { tr: "Turkuaz sıcak su kazanı", en: "Turkuaz hot water boiler", ru: "Водогрейный котёл Turkuaz" } },

  dokumanlar: [
    {
      tur: "kullanim",
      ana: true,
      baslik: { tr: "Kullanım Kılavuzu", en: "User Manual", ru: "Руководство по эксплуатации" },
      belgeNo: "ENP-TRK",             // PDF kodları: ENP-TRK-TR / -EN / -RU · kaynak: araclar/kilavuz-pdf/uret_turkuaz.py
      diller: {
        tr: { dosya: "pdf/kilavuz-tr.pdf", indirmeAdi: "ENORPA_Turkuaz_Kullanim_Kilavuzu_TR_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 0.8, sayfa: 22, onbellek: "20261120" },
        en: { dosya: "pdf/kilavuz-en.pdf", indirmeAdi: "ENORPA_Turkuaz_User_Manual_EN_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 0.8, sayfa: 22, onbellek: "20261120" },
        ru: { dosya: "pdf/kilavuz-ru.pdf", indirmeAdi: "ENORPA_Turkuaz_Rukovodstvo_RU_Rev01.pdf",
              revizyon: "01", tarih: "2026-11", boyutMB: 0.9, sayfa: 22, onbellek: "20261120" }
      }
    },
    {
      // Ürün broşürü (2026-02) — sayfada şimdilik gösterilmiyor; doğrudan bağlantıyla açılabilir
      tur: "katalog",
      baslik: { tr: "Ürün Kataloğu", en: "Product Catalogue", ru: "Каталог продукции" },
      diller: {
        tr: { dosya: "pdf/katalog-tr.pdf", indirmeAdi: "ENORPA_Turkuaz_Urun_Katalogu_TR.pdf", revizyon: "2026-02", boyutMB: 1.0, sayfa: 7, onbellek: "20261120" },
        en: { dosya: "pdf/katalog-en.pdf", indirmeAdi: "ENORPA_Turkuaz_Product_Catalogue_EN.pdf", revizyon: "2026-02", boyutMB: 1.6, sayfa: 7, onbellek: "20261120" },
        ru: { dosya: "pdf/katalog-ru.pdf", indirmeAdi: "ENORPA_Turkuaz_Katalog_RU.pdf", revizyon: "2026-02", boyutMB: 1.4, sayfa: 7, onbellek: "20261120" }
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
