/* =====================================================================
   ortak/js/uyarilar.js — standart güvenlik uyarıları G1–G7 (KILAVUZ_SABLONU.md §8.7)
   DURUM: TASLAK METİN. TR teknik onay + EN/RU çevirmen onayı sonrası "onayli: true" yapılır.
   ===================================================================== */
window.UYARILAR = {
  G1: { seviye: "tehlike", kosul: "kosul.gaz", onayli: false, metin: {
    tr: "Gaz kokusu alırsanız: elektrik anahtarlarına dokunmayın, kıvılcım çıkarmayın, gaz vanasını kapatın, ortamı havalandırın ve binayı terk edin. Dışarıdan doğal gaz acil hattını arayın (Türkiye: 187).",
    en: "If you smell gas: do not operate electrical switches or create sparks, close the gas valve, ventilate the room and leave the building. Call the gas emergency service from outside.",
    ru: "При запахе газа: не пользуйтесь электровыключателями и не допускайте искр, закройте газовый кран, проветрите помещение и покиньте здание. Из безопасного места позвоните в аварийную газовую службу." } },
  G2: { seviye: "uyari", onayli: false, metin: {
    tr: "Kazanın montajı, devreye alınması, bakımı ve onarımı yalnızca yetkili ve eğitimli personel tarafından yapılmalıdır.",
    en: "Installation, commissioning, maintenance and repair of the boiler must be carried out only by authorized, qualified personnel.",
    ru: "Монтаж, ввод в эксплуатацию, техническое обслуживание и ремонт котла должны выполнять только уполномоченные квалифицированные специалисты." } },
  G3: { seviye: "uyari", onayli: false, metin: {
    tr: "Emniyet ventilini ve diğer emniyet cihazlarını asla devre dışı bırakmayın, kapatmayın ve ayarlarını değiştirmeyin.",
    en: "Never disable or block the safety valve or other safety devices, and never change their settings.",
    ru: "Никогда не отключайте и не перекрывайте предохранительный клапан и другие устройства безопасности и не изменяйте их настройки." } },
  G4: { seviye: "uyari", onayli: false, metin: {
    tr: "Kontrol panosunu açmadan önce enerjiyi ana şalterden kesin ve tekrar açılmaya karşı emniyete alın.",
    en: "Before opening the control panel, switch off the power at the main switch and secure it against being switched back on.",
    ru: "Перед открытием щита управления отключите питание главным выключателем и заблокируйте его от повторного включения." } },
  G5: { seviye: "uyari", onayli: false, metin: {
    tr: "Kazan dairesinin havalandırma açıklıklarını kapatmayın ve kazan dairesinde yanıcı madde bulundurmayın.",
    en: "Do not block the boiler room ventilation openings, and do not store flammable materials in the boiler room.",
    ru: "Не закрывайте вентиляционные отверстия котельной и не храните в ней горючие материалы." } },
  G6: { seviye: "dikkat", onayli: false, metin: {
    tr: "Kazan yüzeyleri, baca bağlantısı ve borular çalışma sırasında çok ısınır; dokunmayın.",
    en: "Boiler surfaces, the flue connection and pipes become very hot during operation; do not touch them.",
    ru: "Поверхности котла, дымоход и трубопроводы во время работы сильно нагреваются — не прикасайтесь к ним." } },
  G7: { seviye: "not", onayli: false, metin: {
    tr: "Sistemi doldururken ve su takviyesi yaparken yalnızca kılavuzda belirtilen kalitede su kullanın; kireç ve korozyon garanti kapsamı dışında hasara yol açabilir.",
    en: "Use only water of the quality specified in this manual for filling and topping up; scale and corrosion can cause damage not covered by the warranty.",
    ru: "Для заполнения и подпитки используйте только воду, качество которой указано в руководстве: накипь и коррозия могут вызвать повреждения, на которые не распространяется гарантия." } }
};
