# -*- coding: utf-8 -*-
"""Turkuaz kullanım kılavuzu — içerik (TR ana kaynak; EN ve RU çeviri).
Sayısal değerler yalnızca "TURKUAZ SERİSİ" broşüründen (2026-02, s.3–7) alınmıştır:
model tablosu, bağlantı çapları, sıcaklık ve basınç değerleri, malzeme ve standartlar.
Su kalitesi bölümü Akuamarin kılavuzu (ENP-AKM R01) ile aynıdır (aynı üretici, aynı kazan sacı sınıfı).
Kaynakta olmayan değer yazılmamıştır; bunlar için "siparişe özel çizim / föy / etiket" esas alınır."""
import icerik as AKU

def L(tr, en, ru):
    return {"tr": tr, "en": en, "ru": ru}

BELGE = {
    "kod": L("ENP-TRK-TR", "ENP-TRK-EN", "ENP-TRK-RU"),
    "rev": "R01",
    "tarih": "20.11.2026",
    "dil": L("Türkçe", "English", "Русский"),
    "baslik": L("Turkuaz Serisi Katı Yakıtlı Sıcak Su Kazanları – Kullanım Kılavuzu",
                "Turkuaz Series Solid-Fuel Hot Water Boilers – User Manual",
                "Водогрейные котлы на твёрдом топливе серии Turkuaz – Руководство по эксплуатации"),
    "altbilgi": L("ENORPA · Turkuaz Serisi Sıcak Su Kazanları · Kullanım Kılavuzu",
                  "ENORPA · Turkuaz Series Hot Water Boilers · User Manual",
                  "ENORPA · Водогрейные котлы серии Turkuaz · Руководство по эксплуатации"),
}

KAPAK = {
    "ust": L("KULLANIM KILAVUZU", "USER MANUAL", "РУКОВОДСТВО ПО ЭКСПЛУАТАЦИИ"),
    "baslik": L("Turkuaz Serisi<br>Sıcak Su Kazanları", "Turkuaz Series<br>Hot Water Boilers",
                "Водогрейные котлы<br>серии Turkuaz"),
    "alt": L("Montaj · Devreye alma · İşletme · Bakım",
             "Installation · Commissioning · Operation · Maintenance",
             "Монтаж · Ввод в эксплуатацию · Эксплуатация · Обслуживание"),
    "hap": [L("200.000 – 1.750.000 kcal/h", "200,000 – 1,750,000 kcal/h", "200 000 – 1 750 000 ккал/ч"),
            L("katı yakıtlı", "solid fuel", "твёрдое топливо"),
            L("3 geçişli", "3-pass", "3-ходовой")],
    "not": L("Kılavuzu okuyun, devreye alma kaydını doldurun ve kazanın kullanım ömrü boyunca kazan dairesinde saklayın.",
             "Read this manual, complete the commissioning record and keep it in the boiler room for the entire service life of the boiler.",
             "Прочитайте руководство, заполните протокол ввода в эксплуатацию и храните его в котельной в течение всего срока службы котла."),
}

ICINDEKILER = {
    "ust": L("İÇİNDEKİLER", "CONTENTS", "СОДЕРЖАНИЕ"),
    "baslik": L("Bölümler", "Sections", "Разделы"),
    "hizli_b": L("HIZLI ERİŞİM", "QUICK ACCESS", "БЫСТРЫЙ ДОСТУП"),
    "hizli": L("Acil durum ve elektrik kesintisi adımları bölüm 02 ve 12'de, günlük kontroller bölüm 12'de, bakım aralıkları bölüm 13'te, teknik tablolar bölüm 16 ve 17'dedir.",
               "Emergency and power failure steps are in sections 02 and 12, daily checks in section 12, maintenance intervals in section 13 and technical tables in sections 16 and 17.",
               "Действия в аварийной ситуации и при отключении электроэнергии — в разделах 02 и 12, ежедневные проверки — в разделе 12, периодичность обслуживания — в разделе 13, технические таблицы — в разделах 16 и 17."),
}

T = dict(AKU.T)

# Broşür s.4 Modül H tablosu — bütün modellerde aynı
SINIRLAR = [
    (L("3 bar", "3 bar", "3 бар"), L("işletme basıncı", "operating pressure", "рабочее давление")),
    (L("3,45 bar", "3.45 bar", "3,45 бар"), L("dizayn basıncı", "design pressure", "расчётное давление")),
    (L("5,5 bar", "5.5 bar", "5,5 бар"), L("test basıncı", "test pressure", "испытательное давление")),
    (L("55 – 110 °C", "55 – 110 °C", "55 – 110 °C"), L("çalışma sıcaklığı", "operating temperature", "рабочая температура")),
    (L("Su", "Water", "Вода"), L("akışkan", "medium", "теплоноситель")),
]

# Model no, kcal/h, en, boy, yükseklik, ağırlık — broşür s.4
MODELLER = [
    (2, 200000, 1750, 3450, 2040, 2800), (3, 300000, 1780, 3600, 2065, 3100), (4, 400000, 1840, 3690, 2125, 3455),
    (5, 500000, 1850, 4120, 2000, 3850), (7, 750000, 1880, 4600, 2000, 4650), (10, 1000000, 1940, 5845, 2120, 5970),
    (12, 1250000, 1975, 5900, 2170, 7200), (15, 1500000, 2020, 6000, 2200, 7460), (17, 1750000, 2150, 6300, 2350, 8150)]
# Model no, su gidiş–dönüş, genleşme, şönt — broşür s.4
BAGLANTI = [
    (2, "DN65", "DN40", "DN25"), (3, "DN80", "DN50", "DN25"), (4, "DN80", "DN50", "DN25"), (5, "DN80", "DN50", "DN25"),
    (7, "DN100", "DN50", "DN50"), (10, "DN125", "DN65", "DN50"), (12, "DN125", "DN65", "DN50"),
    (15, "DN125", "DN65", "DN65"), (17, "DN150", "DN80", "DN65")]

B = []

# ---------------------------------------------------------------- 01
B.append(dict(no="01", ust=L("BAŞLAMADAN ÖNCE", "BEFORE YOU START", "ПЕРЕД НАЧАЛОМ РАБОТЫ"),
  baslik=L("Kapsam ve belge sırası", "Scope and order of documents", "Область применения и порядок документов"),
  bloklar=[
    ("p", L("Bu kılavuz, ENORPA Turkuaz serisi katı yakıtlı, üç geçişli, tek külhanlı sıcak su kazanlarının TR2 – TR17 modelleri (200.000 – 1.750.000 kcal/h) için hazırlanmıştır. Kazanın, yakıt besleme ünitesinin, fanların, siklonun ve bacanın montajını, devreye alınmasını, işletilmesini ve bakımını yapan personele yöneliktir.",
            "This manual covers the TR2 – TR17 models (200,000 – 1,750,000 kcal/h) of the ENORPA Turkuaz series of solid-fuel, three-pass, single-furnace hot water boilers. It is intended for the personnel who install, commission, operate and maintain the boiler, the fuel feed unit, the fans, the cyclone and the chimney.",
            "Настоящее руководство распространяется на модели TR2 – TR17 (200 000 – 1 750 000 ккал/ч) водогрейных котлов ENORPA серии Turkuaz: трёхходовых, с одной топкой, работающих на твёрдом топливе. Оно предназначено для персонала, выполняющего монтаж, ввод в эксплуатацию, эксплуатацию и обслуживание котла, узла подачи топлива, вентиляторов, циклона и дымовой трубы.")),
    ("h", L("Hangi belge esas alınır?", "Which document takes precedence?", "Какой документ имеет приоритет?")),
    ("tablo", [L("Belge", "Document", "Документ"), L("İçerik", "Content", "Содержание")], [
      [L("1. Ürün etiketi", "1. Product label", "1. Заводская табличка"), L("Kazanın üzerindeki etiket: seri numarası, ürün kodu, ısıl güç, işletme / dizayn / test basınçları.", "The label on the boiler: serial number, product code, heat output, operating / design / test pressures.", "Табличка на котле: серийный номер, код изделия, тепловая мощность, рабочее / расчётное / испытательное давление.")],
      [L("2. Siparişe özel belgeler", "2. Order-specific documents", "2. Документы по заказу"), L("Onaylı ölçü ve branşman çizimi, yerleşim ve beton planı, baca ve siklon çizimi, elektrik şeması ve otomasyon belgeleri.", "Approved dimension and connection drawing, layout and foundation plan, chimney and cyclone drawing, wiring diagram and automation documents.", "Утверждённый габаритный чертёж с патрубками, план размещения и фундамента, чертёж дымовой трубы и циклона, электрическая схема и документация на автоматику.")],
      [L("3. Bu kılavuz", "3. This manual", "3. Настоящее руководство"), L("Seri için geçerli genel montaj, işletme ve bakım kuralları.", "General installation, operation and maintenance rules applicable to the series.", "Общие правила монтажа, эксплуатации и обслуживания для всей серии.")],
      [L("4. Ekipman kılavuzları", "4. Equipment manuals", "4. Руководства на оборудование"), L("Fanlar, redüktörlü motorlar, invertör, pompalar, emniyet ventili, pano ve diğer ekipmanların kendi üretici talimatları.", "The manufacturers' own instructions for the fans, geared motors, inverter, pumps, safety valve, control panel and other equipment.", "Собственные инструкции изготовителей вентиляторов, мотор-редукторов, преобразователя частоты, насосов, предохранительного клапана, щита управления и другого оборудования.")],
    ], {"kalin1": True}),
    ("not", "dikkat", L("BELGELER BİRBİRİYLE ÇELİŞİYORSA", "IF THE DOCUMENTS CONTRADICT EACH OTHER", "ЕСЛИ ДОКУМЕНТЫ ПРОТИВОРЕЧАТ ДРУГ ДРУГУ"),
      L("Kazanı devreye almayın. Etiket ve siparişe özel çizim, bu kılavuzdaki genel tablolardan önce gelir; farkı ENORPA'ya bildirip yazılı açıklama isteyin.",
        "Do not commission the boiler. The label and the order-specific drawing take precedence over the general tables in this manual; report the discrepancy to ENORPA and request a written clarification.",
        "Не вводите котёл в эксплуатацию. Табличка и чертёж по заказу имеют приоритет над общими таблицами руководства; сообщите о расхождении в ENORPA и запросите письменное разъяснение.")),
    ("h", L("Kullanım amacı", "Intended use", "Назначение")),
    ("p", L("Kazan yalnızca katı yakıt (pelet, prina, kömür vb.) yakarak sıcak su üretmek için kullanılır. Seraların, binaların ve endüstriyel tesislerin ısıtma sistemlerinde çalışacak şekilde tasarlanmıştır. Etikette yazan basınç ve sıcaklık sınırlarının dışında ve siparişte belirtilmeyen bir yakıtla çalıştırılamaz.",
            "The boiler is used only for producing hot water by burning solid fuel (pellets, olive pomace, coal, etc.). It is designed for heating systems of greenhouses, buildings and industrial facilities. It must not be operated outside the pressure and temperature limits stated on the label or with a fuel not specified in the order.",
            "Котёл предназначен только для получения горячей воды при сжигании твёрдого топлива (пеллеты, оливковый жмых, уголь и т. п.). Он рассчитан на работу в системах отопления теплиц, зданий и промышленных объектов. Эксплуатация за пределами указанных на табличке давления и температуры, а также на топливе, не указанном в заказе, запрещена.")),
    ("h", L("Bu kılavuzdaki işaretler", "Symbols used in this manual", "Обозначения в руководстве")),
    ("isaretler", [
      ("tehlike", L("Cana gelebilecek zarar ve hayati tehlike.", "Risk of injury and danger to life.", "Опасность травмы и угроза жизни.")),
      ("dikkat", L("Maddi hasar, çevreye zarar veya garanti kaybı.", "Material damage, harm to the environment or loss of warranty.", "Материальный ущерб, вред окружающей среде или потеря гарантии.")),
      ("bilgi", L("İşi kolaylaştıran açıklama.", "An explanation that makes the work easier.", "Пояснение, облегчающее работу.")),
    ]),
    ("kucuk", L("Kılavuzu kazan dairesinde, operatörün ulaşabileceği bir yerde saklayın. Kazan başka bir işletmeye devredilirse kılavuzu ve doldurulmuş kayıt formlarını birlikte teslim edin.",
                "Keep the manual in the boiler room where the operator can reach it. If the boiler is transferred to another operator, hand over the manual together with the completed record forms.",
                "Храните руководство в котельной в месте, доступном оператору. При передаче котла другому владельцу передайте руководство вместе с заполненными формами записей.")),
  ]))

# ---------------------------------------------------------------- 02
B.append(dict(no="02", ust=L("PERSONEL VE ACİL DURUM", "PERSONNEL AND EMERGENCIES", "ПЕРСОНАЛ И АВАРИЙНЫЕ СИТУАЦИИ"),
  baslik=L("Güvenli çalışma", "Safe working", "Безопасная работа"),
  bloklar=[
    ("h", L("Kim, hangi işi yapar?", "Who does which work?", "Кто выполняет работы?")),
    ("tablo", [L("İş", "Work", "Работа"), L("Yetkili", "Authorised person", "Ответственный")], [
      [L("Kazan yakımı ve işletme", "Firing and operating the boiler", "Розжиг и эксплуатация котла"), L("6331 sayılı İş Sağlığı ve Güvenliği Kanunu kapsamında belgeli kazan operatörü.", "Boiler operator certified under Turkish Occupational Health and Safety Law No. 6331 (or the equivalent national regulations).", "Оператор котла, аттестованный согласно Закону Турции об охране труда № 6331 (или равноценным национальным нормам).")],
      [L("Elektrik ve pano", "Electrics and control panel", "Электрика и щит управления"), L("Uzman elektrikçi.", "Qualified electrician.", "Квалифицированный электрик.")],
      [L("İlk devreye alma", "First commissioning", "Первый ввод в эксплуатацию"), L("ENORPA veya ENORPA'nın yetkilendirdiği servis.", "ENORPA or a service partner authorised by ENORPA.", "ENORPA или сервис, уполномоченный ENORPA.")],
      [L("Fan, helezon ve redüktör bakımı", "Fan, screw and gear unit maintenance", "Обслуживание вентиляторов, шнека и редукторов"), L("Eğitimli bakım personeli; enerji kesilip kilitlendikten sonra.", "Trained maintenance staff, only after the power has been isolated and locked out.", "Обученный персонал — только после отключения и блокировки питания.")],
    ], {"kalin1": True}),
    ("not", "tehlike", L("ELEKTRİK KESİLDİĞİNDE", "IN THE EVENT OF A POWER FAILURE", "ПРИ ОТКЛЮЧЕНИИ ЭЛЕКТРОЭНЕРГИИ"), [
      L("Katı yakıt, elektrik kesilince de ocakta yanmaya devam eder; pompa durduğu için kazan suyu hızla ısınır.", "Solid fuel keeps burning in the furnace when the power fails; as the pump stops, the boiler water heats up quickly.", "Твёрдое топливо продолжает гореть в топке и после отключения электроэнергии; так как насос остановился, вода в котле быстро нагревается."),
      L("Kazan kapaklarını açmayın; ateşe hava vermeyin.", "Do not open the boiler doors; do not let air reach the fire.", "Не открывайте дверцы котла; не допускайте поступления воздуха к огню."),
      L("Termometre ve manometreyi izleyin; sıcaklık hızla yükseliyorsa kazanın yanından uzaklaşın ve servisi arayın.", "Watch the thermometer and pressure gauge; if the temperature rises rapidly, move away from the boiler and call service.", "Следите за термометром и манометром; при быстром росте температуры отойдите от котла и вызовите сервис."),
      L("Elektrik gelince önce sirkülasyon pompasının çalıştığını doğrulayın, sonra yakıt beslemeyi başlatın.", "When power returns, first check that the circulation pump is running, then restart the fuel feed.", "После восстановления питания сначала убедитесь, что циркуляционный насос работает, затем запускайте подачу топлива."),
    ]),
    ("not", "tehlike", L("BACA GAZI KOKUSU VEYA DUMAN", "FLUE GAS SMELL OR SMOKE", "ЗАПАХ ДЫМОВЫХ ГАЗОВ ИЛИ ДЫМ"),
      L("Baca gazı, karbonmonoksit nedeniyle zehirlenmeye yol açar. Yakıt beslemeyi durdurun, kazan dairesini havalandırın, kapıları açık tutun ve baca gazı fanının çalıştığını kontrol edin. Bunkerden veya besleme helezonundan duman geliyorsa geri yanma olabilir: beslemeyi durdurun, bunker kapağını açmayın ve servisi arayın.",
        "Flue gas causes poisoning because of carbon monoxide. Stop the fuel feed, ventilate the boiler room, keep the doors open and check that the flue gas fan is running. If smoke comes from the bunker or the feed screw, burn-back may be occurring: stop the feed, do not open the bunker lid and call service.",
        "Дымовые газы вызывают отравление угарным газом. Остановите подачу топлива, проветрите котельную, держите двери открытыми и проверьте работу дымососа. Если дым идёт из бункера или шнека подачи, возможен обратный прогар: остановите подачу, не открывайте крышку бункера и вызовите сервис.")),
    ("h", L("Kazana müdahaleden önce", "Before working on the boiler", "Перед работами на котле")),
    ("adim", [
      L("Yakıt beslemeyi durdurun ve ocaktaki yakıtın tamamen yanıp bitmesini bekleyin.", "Stop the fuel feed and wait until the fuel in the furnace has burnt out completely.", "Остановите подачу топлива и дождитесь полного выгорания топлива в топке."),
      L("Sistemin elektriğini ana panodan kesin ve yeniden açılmaması için kilitleyin.", "Isolate the system at the main panel and lock it against being switched back on.", "Обесточьте систему на главном щите и заблокируйте от повторного включения."),
      L("Kazanın soğumasını bekleyin. Basınç altındayken veya sıcakken hiçbir kapağı açmayın.", "Wait for the boiler to cool down. Do not open any door while it is under pressure or hot.", "Дождитесь остывания котла. Не открывайте никакие дверцы, пока котёл под давлением или горячий."),
      L("Su tarafında çalışılacaksa basıncın sıfıra indiğini göstergeden doğrulayın.", "If work is to be done on the water side, check on the gauge that the pressure has dropped to zero.", "При работах на водяной стороне убедитесь по манометру, что давление снизилось до нуля."),
    ]),
    ("not", "dikkat", L("SICAK YÜZEYLER, KÜL VE DÖNEN PARÇALAR", "HOT SURFACES, ASH AND ROTATING PARTS", "ГОРЯЧИЕ ПОВЕРХНОСТИ, ЗОЛА И ВРАЩАЮЩИЕСЯ ДЕТАЛИ"),
      L("Kapaklar, duman kanalları, siklon ve baca çok sıcaktır; koruyucu eldiven ve gözlük kullanın. Kül saatlerce kor halinde kalabilir; yalnızca metal ve kapaklı kaba alın. Helezon ve fanların koruyucularını çalışırken sökmeyin.",
        "The doors, flue ducts, cyclone and chimney are very hot; wear protective gloves and goggles. Ash can stay glowing for hours; collect it only in a metal container with a lid. Do not remove the guards of the screw and fans while they are running.",
        "Дверцы, газоходы, циклон и дымовая труба очень горячие; используйте защитные перчатки и очки. Зола может тлеть часами; собирайте её только в металлическую ёмкость с крышкой. Не снимайте ограждения шнека и вентиляторов во время работы.")),
    ("not", "tehlike", L("SUSUZ KAZAN", "BOILER WITHOUT WATER", "КОТЁЛ БЕЗ ВОДЫ"),
      L("Kazan ve tesisat tam dolu ve havası alınmış değilse kazanı yakmayın. Susuz kalmış sıcak kazana kesinlikle su eklemeyin.",
        "Do not fire the boiler unless the boiler and the system are completely filled and vented. Never add water to a hot boiler that has run dry.",
        "Не разжигайте котёл, если котёл и система не заполнены полностью и из них не удалён воздух. Ни в коем случае не добавляйте воду в горячий котёл, оставшийся без воды.")),
  ]))

# ---------------------------------------------------------------- 03
B.append(dict(no="03", ust=L("ÜRÜNÜ TANIYIN", "KNOW YOUR PRODUCT", "ЗНАКОМСТВО С ИЗДЕЛИЕМ"),
  baslik=L("Kazanın yapısı ve etiketi", "Boiler design and label", "Конструкция и табличка котла"),
  bloklar=[
    ("p", L("Turkuaz, katı yakıtlı, üç geçişli, tek külhanlı bir sıcak su kazanıdır. Yakıt, bunkerden redüktörlü helezonla yanma odasına beslenir; yanma havasını taze hava fanı verir. Duman gazları kazandaki geçişlerde ısısını suya bırakır, siklonda kaba külünden ayrılır ve baca gazı fanıyla bacaya basılır. Endüstriyel kullanım için enerji deposu görevi gören yüksek bir su hacmine sahiptir.",
            "Turkuaz is a solid-fuel, three-pass, single-furnace hot water boiler. The fuel is fed from the bunker into the combustion chamber by a screw driven by a geared motor; the combustion air is supplied by the fresh air fan. The flue gases give up their heat to the water in the boiler passes, are separated from coarse ash in the cyclone and are discharged into the chimney by the flue gas fan. A large water volume acts as an energy store for industrial use.",
            "Turkuaz — трёхходовой водогрейный котёл с одной топкой, работающий на твёрдом топливе. Топливо подаётся из бункера в топку шнеком с мотор-редуктором; воздух для горения подаёт дутьевой вентилятор. Дымовые газы отдают тепло воде в ходах котла, очищаются от крупной золы в циклоне и удаляются в дымовую трубу дымососом. Большой объём воды служит аккумулятором тепла при промышленном применении.")),
    ("tablo", [L("Özellik", "Feature", "Характеристика"), L("Turkuaz serisi", "Turkuaz series", "Серия Turkuaz")], [
      [L("Yakıt", "Fuel", "Топливо"), L("Katı yakıt: pelet, prina, kömür vb. (siparişte belirtilen yakıt)", "Solid fuel: pellets, olive pomace, coal, etc. (fuel specified in the order)", "Твёрдое топливо: пеллеты, оливковый жмых, уголь и т. п. (указанное в заказе)")],
      [L("Basınçlı kısım sacı", "Pressure part plates", "Листы деталей под давлением"), L("S235JR, EN 10028-2 sertifikalı", "S235JR, EN 10028-2 certified", "S235JR, сертификат EN 10028-2")],
      [L("Duman boruları", "Fire tubes", "Дымогарные трубы"), L("P235GH, TS 10217-2, PED sertifikalı", "P235GH, TS 10217-2, PED certified", "P235GH, TS 10217-2, сертификат PED")],
      [L("Tasarım standartları", "Design standards", "Стандарты проектирования"), L("TS 12953 · ASME BPVC · AD2000 · EN 12953 · GOST", "TS 12953 · ASME BPVC · AD2000 · EN 12953 · GOST", "TS 12953 · ASME BPVC · AD2000 · EN 12953 · GOST")],
      [L("Kaynak", "Welding", "Сварка"), L("EN ISO 15614-1 süreç; TS EN ISO 9606-1 belgeli kaynakçı", "EN ISO 15614-1 procedures; welders certified to TS EN ISO 9606-1", "Технология по EN ISO 15614-1; сварщики аттестованы по TS EN ISO 9606-1")],
      [L("Uygunluk", "Conformity", "Соответствие"), L("2014/68/EU Basınçlı Ekipmanlar Direktifi; B + F modülü CE", "Pressure Equipment Directive 2014/68/EU; CE module B + F", "Директива 2014/68/EU; CE по модулям B + F")],
      [L("Kontrol", "Control", "Управление"), L("Analog veya PLC kazan ve mahal kontrol panosu", "Analogue or PLC boiler and room control panel", "Аналоговый или ПЛК-щит управления котлом и помещением")],
    ], {"kalin1": True}),
    ("h", L("Etikette bulunan bilgiler", "Information on the label", "Данные на табличке")),
    ("tablo", [L("Alan", "Field", "Поле"), L("Ne için gerekli?", "What is it for?", "Для чего нужно?")], [
      [L("Seri no", "Serial no.", "Серийный №"), L("Servis ve yedek parça başvurularında istenir.", "Required for service and spare part requests.", "Требуется при обращении в сервис и заказе запчастей.")],
      [L("Ürün kodu", "Product code", "Код изделия"), L("Model (örnek: Turkuaz TR10).", "Model (example: Turkuaz TR10).", "Модель (пример: Turkuaz TR10).")],
      [L("Isıl güç", "Heat output", "Тепловая мощность"), L("kcal/h olarak anma kapasitesi.", "Rated output in kcal/h.", "Номинальная мощность в ккал/ч.")],
      [L("Basınçlar", "Pressures", "Давления"), L("İşletme, dizayn ve test basıncı; emniyet ventili ve genleşme sistemi bunlara göre seçilir.", "Operating, design and test pressure; the safety valve and expansion system are selected accordingly.", "Рабочее, расчётное и испытательное давление; по ним подбираются предохранительный клапан и расширительная система.")],
    ], {"kalin1": True}),
    ("h", L("Seri için ortak çalışma sınırları", "Common operating limits for the series", "Общие рабочие пределы для серии")),
    ("sinirlar",),
  ]))

# ---------------------------------------------------------------- 04
B.append(dict(no="04", ust=L("ÜRÜNÜ TANIYIN", "KNOW YOUR PRODUCT", "ЗНАКОМСТВО С ИЗДЕЛИЕМ"),
  baslik=L("Sistem bileşenleri", "System components", "Компоненты системы"),
  bloklar=[
    ("ikiresim", ("turkuaz-sistem.jpg", L("Sistem: yakıt bunkeri ve helezon, siklon, fanlar ve baca.", "System: fuel bunker and screw, cyclone, fans and chimney.", "Система: бункер и шнек, циклон, вентиляторы и дымовая труба.")),
                 ("turkuaz-arka.jpg", L("Bunker ve redüktörlü besleme helezonu; üstte baca gazı çıkışı.", "Bunker and geared feed screw; flue gas outlet at the top.", "Бункер и шнек подачи с мотор-редуктором; вверху выход дымовых газов."))),
    ("tablo", [L("Bileşen", "Component", "Компонент"), L("Görevi", "Function", "Назначение")], [
      [L("Yakıt bunkeri", "Fuel bunker", "Топливный бункер"), L("Katı yakıtın doldurulduğu haznedir. Altındaki redüktörlü motorlar yakıtı ihtiyaca göre otomatik olarak yanma odasına gönderir. Çift bunker yüksek kapasiteli modellerde kullanılır.", "The hopper filled with solid fuel. The geared motors underneath automatically feed the fuel into the combustion chamber as required. Double bunkers are used on high-capacity models.", "Ёмкость, в которую загружается твёрдое топливо. Мотор-редукторы под ним автоматически подают топливо в топку по потребности. Сдвоенный бункер применяется на моделях большой мощности.")],
      [L("Taze hava fanı", "Fresh air fan", "Дутьевой вентилятор"), L("Yakıtın tam yanması için gereken havayı yakıt yatağının altından yanma odasına üfler. Devri, ısı ihtiyacına ve besleme hızına göre genellikle invertörle ayarlanır.", "Blows the air needed for complete combustion into the combustion chamber from beneath the fuel bed. Its speed is usually adjusted by an inverter according to heat demand and feed rate.", "Подаёт под слой топлива воздух, необходимый для полного сгорания. Частота вращения обычно регулируется преобразователем частоты в зависимости от тепловой нагрузки и скорости подачи.")],
      [L("Baca gazı fanı", "Flue gas fan", "Дымосос"), L("Gazları siklondan çekip bacaya basar; yanma odasında hafif vakum (negatif basınç) oluşturarak dumanın kapak ve contalardan kazan dairesine sızmasını önler.", "Draws the gases from the cyclone and pushes them into the chimney; it keeps a slight vacuum (negative pressure) in the combustion chamber so that smoke cannot leak into the boiler room through doors and seals.", "Отсасывает газы из циклона и подаёт их в дымовую трубу; поддерживает в топке небольшое разрежение, чтобы дым не проникал в котельную через дверцы и уплотнения.")],
      [L("Siklon ayırıcı", "Cyclone separator", "Циклонный сепаратор"), L("Duman içindeki uçucu kül, kurum ve iri partikülleri merkezkaç kuvvetiyle ayırır; ayrılan kül konik alt kısımdan toplama haznesine düşer.", "Separates fly ash, soot and coarse particles from the flue gas by centrifugal force; the separated ash falls from the conical bottom into the collection hopper.", "Отделяет из дымовых газов летучую золу, сажу и крупные частицы центробежной силой; отделённая зола падает через коническое днище в сборник.")],
      [L("Baca", "Chimney", "Дымовая труба"), L("Filtrelenmiş gazları güvenli bir yükseklikte atmosfere verir; doğal çekiş de sağlar. Yoğuşma ve tıkanmayı önlemek için genellikle çift cidarlı ve yalıtımlıdır.", "Releases the filtered gases into the atmosphere at a safe height and also creates natural draught. It is usually double-walled and insulated to prevent condensation and blockage.", "Выводит очищенные газы в атмосферу на безопасной высоте и создаёт естественную тягу. Обычно выполняется двустенной и утеплённой для предотвращения конденсации и засорения.")],
      [L("Kapaklar", "Doors", "Дверцы"), L("Öndeki kapaklar ocağa, duman borularına ve kül alanına erişim sağlar.", "The front doors give access to the furnace, the fire tubes and the ash area.", "Передние дверцы обеспечивают доступ к топке, дымогарным трубам и зольной зоне.")],
    ], {"kalin1": True}),
    ("not", "dikkat", L("BİLEŞENLERİN YERİ SİPARİŞE GÖRE DEĞİŞİR", "COMPONENT POSITIONS VARY BY ORDER", "РАСПОЛОЖЕНИЕ КОМПОНЕНТОВ ЗАВИСИТ ОТ ЗАКАЗА"),
      L("Bunker sayısı, fanların, siklonun ve bacanın konumu kazan dairesine göre belirlenir. Ağızların ve bileşenlerin kesin yeri için onaylı yerleşim çizimini esas alın.",
        "The number of bunkers and the positions of the fans, cyclone and chimney are determined according to the boiler room. Use the approved layout drawing for the exact positions of nozzles and components.",
        "Количество бункеров и расположение вентиляторов, циклона и трубы определяются по котельной. Точное расположение патрубков и компонентов — по утверждённому чертежу размещения.")),
  ]))

# ---------------------------------------------------------------- 05
B.append(dict(no="05", ust=L("MEKANİK KURULUM", "MECHANICAL INSTALLATION", "МЕХАНИЧЕСКИЙ МОНТАЖ"),
  baslik=L("Teslim alma, taşıma ve depolama", "Receiving, transport and storage", "Приёмка, транспортировка и хранение"),
  bloklar=[
    ("h", L("Teslim alırken", "On receipt", "При приёмке")),
    ("adim", [
      L("Etiketteki ürün kodu ve seri numarasını sipariş belgeleriyle karşılaştırın.", "Compare the product code and serial number on the label with the order documents.", "Сверьте код изделия и серийный номер на табличке с документами заказа."),
      L("Kaporta saclarını, kapakları, flanş ağızlarını ve armatürleri darbe ve eksik açısından kontrol edin.", "Check the cladding sheets, doors, flanged nozzles and fittings for impact damage and missing items.", "Проверьте обшивку, дверцы, фланцевые патрубки и арматуру на повреждения и некомплектность."),
      L("Ayrı sevk edilen bunker, helezon, fanlar, siklon, baca parçaları ve pano adetlerini sevk listesiyle sayın.", "Count the separately shipped bunker, screw, fans, cyclone, chimney sections and panel against the packing list.", "Сверьте с упаковочным листом отдельно поставленные бункер, шнек, вентиляторы, циклон, секции трубы и щит."),
      L("Hasar veya eksik varsa fotoğraf ve seri numarasıyla kaydedip taşıyıcıya ve ENORPA'ya bildirin.", "If there is damage or anything missing, record it with photos and the serial number and report it to the carrier and to ENORPA.", "При повреждениях или некомплектности зафиксируйте их с фотографиями и серийным номером и сообщите перевозчику и в ENORPA."),
    ]),
    ("h", L("Kaldırma ve taşıma", "Lifting and transport", "Подъём и перемещение")),
    ("madde", [
      L("Kazanı yalnızca üzerindeki kaldırma mapalarından kaldırın. Flanş ağızlarından, kapaklardan, bunkerden veya kaporta saclarından kaldırmayın.", "Lift the boiler only by its lifting lugs. Do not lift it by the flanged nozzles, doors, bunker or cladding sheets.", "Поднимайте котёл только за подъёмные проушины. Не поднимайте за фланцевые патрубки, дверцы, бункер или обшивку."),
      L("Ağırlığı bölüm 16'daki tablodan ve etiketten doğrulayın (TR2: 2800 kg – TR17: 8150 kg); vinç ve sapan kapasitesini buna göre seçin.", "Confirm the weight from the table in section 16 and from the label (TR2: 2800 kg – TR17: 8150 kg); select the crane and sling capacity accordingly.", "Уточните массу по таблице раздела 16 и по табличке (TR2: 2800 кг – TR17: 8150 кг); выбирайте кран и стропы соответствующей грузоподъёмности."),
      L("Sapan boyunu çok kısa tutmayın; kısa sapan mapaları ve kaportayı yana doğru zorlar.", "Do not use slings that are too short; short slings pull the lugs and the cladding sideways.", "Не используйте слишком короткие стропы: они нагружают проушины и обшивку в боковом направлении."),
      L("İndirme ve kaldırma hareketlerini yavaş ve darbesiz yapın. Asılı yükün altında durmayın.", "Lower and lift slowly and without impact. Do not stand under a suspended load.", "Опускайте и поднимайте медленно, без ударов. Не стойте под подвешенным грузом."),
    ]),
    ("not", "dikkat", L("DARBE İÇ YALITIMA ZARAR VERİR", "IMPACT DAMAGES THE INTERNAL LINING", "УДАР ПОВРЕЖДАЕТ ВНУТРЕННЮЮ ФУТЕРОВКУ"),
      L("Kazanın sert düşmesi veya çarpması kapak ve ocak içindeki yalıtım ile refrakter malzemelere zarar verebilir. Taşıma sırasında darbe aldıysa devreye almadan önce ENORPA servisine haber verin.",
        "If the boiler is dropped hard or knocked, the insulation and refractory materials in the doors and furnace may be damaged. If it received an impact during transport, inform ENORPA service before commissioning.",
        "Сильное падение или удар котла может повредить изоляцию и огнеупорные материалы в дверцах и топке. Если при транспортировке был удар, сообщите в сервис ENORPA до ввода в эксплуатацию.")),
    ("h", L("Depolama", "Storage", "Хранение")),
    ("madde", [
      L("Kazanı ve elektrikli ekipmanları (motorlar, fanlar, pano) kuru ve kapalı bir alanda, düz zeminde bekletin.", "Keep the boiler and electrical equipment (motors, fans, panel) in a dry, enclosed area on level ground.", "Храните котёл и электрооборудование (двигатели, вентиляторы, щит) в сухом закрытом помещении на ровном основании."),
      L("Su ağızlarını, duman çıkışını ve bunker ağzını yabancı cisim ve su girişine karşı kapalı tutun.", "Keep the water nozzles, flue outlet and bunker opening covered against foreign objects and water ingress.", "Держите водяные патрубки, газовый выход и горловину бункера закрытыми от посторонних предметов и воды."),
      L("Uzun süre bekleyecekse donma riskine karşı içinde su bırakmayın.", "If it will stand for a long time, do not leave water inside because of the risk of freezing.", "При длительном хранении не оставляйте внутри воду из-за опасности замерзания."),
    ]),
  ]))

# ---------------------------------------------------------------- 06
B.append(dict(no="06", ust=L("MEKANİK KURULUM", "MECHANICAL INSTALLATION", "МЕХАНИЧЕСКИЙ МОНТАЖ"),
  baslik=L("Kazan dairesi ve yerleşim", "Boiler room and layout", "Котельная и размещение"),
  bloklar=[
    ("p", L("Kazan; bunker, fanlar, siklon ve baca ile birlikte bir sistem olarak yerleştirilir. Kesin ölçüler, servis boşlukları ve beton kaide ölçüsü siparişe özel yerleşim çiziminde verilir.",
            "The boiler is installed as a system together with the bunker, fans, cyclone and chimney. Exact dimensions, service clearances and the plinth size are given in the order-specific layout drawing.",
            "Котёл устанавливается как система вместе с бункером, вентиляторами, циклоном и дымовой трубой. Точные размеры, сервисные зазоры и размеры фундамента приведены в чертеже размещения по заказу.")),
    ("h", L("Zemin ve kaide", "Floor and plinth", "Пол и фундамент")),
    ("madde", [
      L("Kazanı, işletme ağırlığını (kazan ağırlığı + su) taşıyacak, düz ve terazide bir beton kaide üzerine oturtun.", "Place the boiler on a level concrete plinth able to carry the operating weight (boiler weight + water).", "Устанавливайте котёл на ровный горизонтальный бетонный фундамент, рассчитанный на рабочую массу (масса котла + вода)."),
      L("Siklon ayaklarını ve baca tabanını kendi kaidelerine sabitleyin; bacanın yükünü kazana ve siklona taşıtmayın.", "Fix the cyclone legs and the chimney base to their own foundations; do not let the chimney load rest on the boiler or cyclone.", "Закрепите опоры циклона и основание трубы на собственных фундаментах; не передавайте нагрузку трубы на котёл и циклон."),
    ]),
    ("h", L("Servis boşlukları", "Service clearances", "Сервисные зазоры")),
    ("madde", [
      L("Kazanın önünde, duman borularının temizlenebilmesi için en az boru boyu kadar boş alan bırakın.", "In front of the boiler, leave free space at least as long as the fire tubes so that they can be cleaned.", "Перед котлом оставьте свободное пространство не меньше длины дымогарных труб для их чистки."),
      L("Kapakların tam açılabileceği, kül alınabileceği ve kül arabasının dolaşabileceği alan bırakın.", "Leave room for the doors to open fully, for ash removal and for an ash cart to move around.", "Предусмотрите место для полного открытия дверец, удаления золы и проезда тележки для золы."),
      L("Bunker kapağına, helezon motoruna, fanlara ve siklonun kül haznesine rahat erişim olsun.", "Ensure easy access to the bunker lid, the screw motor, the fans and the cyclone ash hopper.", "Обеспечьте свободный доступ к крышке бункера, двигателю шнека, вентиляторам и золосборнику циклона."),
    ]),
    ("h", L("Havalandırma ve yakıt deposu", "Ventilation and fuel store", "Вентиляция и склад топлива")),
    ("madde", [
      L("Kazan dairesinde yanma havası için kapatılamayan alt menfez ve sıcak havanın çıkması için üst menfez bulunmalıdır.", "The boiler room must have a non-closable low-level vent for combustion air and a high-level vent for warm air to escape.", "В котельной должны быть незакрываемый нижний проём для воздуха горения и верхний проём для выхода тёплого воздуха."),
      L("Yakıtı kazan dairesinde yalnızca bunkerde bulundurun; yakıt deposunu kazandan ve sıcak yüzeylerden ayrı, kuru bir alanda tutun.", "Keep fuel in the boiler room only in the bunker; keep the fuel store in a dry area separate from the boiler and hot surfaces.", "В котельной храните топливо только в бункере; склад топлива держите в сухом месте отдельно от котла и горячих поверхностей."),
      L("Yangın söndürücü bulundurun ve kül için metal, kapaklı kap kullanın.", "Keep a fire extinguisher available and use a metal container with a lid for ash.", "Держите наготове огнетушитель и используйте для золы металлическую ёмкость с крышкой."),
    ]),
    ("not", "dikkat", L("ELEKTRİK BAĞLANTISI", "ELECTRICAL CONNECTION", "ЭЛЕКТРОПОДКЛЮЧЕНИЕ"),
      L("Pano, motorlar ve fanlar uzman elektrikçi tarafından elektrik şemasına göre bağlanır ve topraklanır. Pompanın ve fanların beslemesi, elektrik kesintisi senaryosu dikkate alınarak tasarlanmalıdır (bölüm 07).",
        "The panel, motors and fans must be connected and earthed by a qualified electrician according to the wiring diagram. The supply to the pump and fans must be designed with the power failure scenario in mind (section 07).",
        "Щит, двигатели и вентиляторы подключаются и заземляются квалифицированным электриком по электрической схеме. Питание насоса и вентиляторов проектируется с учётом сценария отключения электроэнергии (раздел 07).")),
  ]))

# ---------------------------------------------------------------- 07
B.append(dict(no="07", ust=L("TESİSAT BAĞLANTISI", "PIPEWORK", "ПОДКЛЮЧЕНИЕ К СИСТЕМЕ"),
  baslik=L("Su bağlantıları", "Water connections", "Водяные подключения"),
  bloklar=[
    ("h", L("Gidiş ve dönüş", "Flow and return", "Подача и обратка")),
    ("p", L("Sıcak su çıkışını gidiş ağzından, tesisat dönüşünü dönüş ağzından bağlayın; hatlar kesinlikle ters bağlanmaz. Boru ağırlığını kazan ağızlarına taşıtmayın, hatları bağımsız askıya alın. Ağız çapları bölüm 17'dedir.",
            "Connect the hot water outlet to the flow nozzle and the system return to the return nozzle; the lines must never be reversed. Do not let the pipe weight rest on the boiler nozzles; support the lines independently. Nozzle sizes are in section 17.",
            "Подключите выход горячей воды к патрубку подачи, а обратку системы — к обратному патрубку; линии ни в коем случае нельзя менять местами. Не передавайте массу труб на патрубки котла, подвешивайте трубопроводы отдельно. Размеры патрубков — в разделе 17.")),
    ("h", L("Dönüş suyu koruması (şönt hattı)", "Return temperature protection (shunt line)", "Защита обратки (линия шунта)")),
    ("p", L("Kazanın en düşük çalışma sıcaklığı 55 °C'dir. Soğuk dönüş suyu duman tarafında yoğuşma, katran ve korozyona yol açar. Şönt ağızları arasına bağlanan pompa, gidiş suyunun bir kısmını dönüşe karıştırarak dönüş sıcaklığını yükseltir. Şönt kullanılmayacaksa ağızları uygun kör flanşla kapatın.",
            "The minimum operating temperature of the boiler is 55 °C. Cold return water causes condensation, tar and corrosion on the flue gas side. A pump connected between the shunt nozzles mixes part of the flow water into the return and raises the return temperature. If the shunt is not used, close the nozzles with suitable blind flanges.",
            "Минимальная рабочая температура котла — 55 °C. Холодная обратная вода вызывает конденсацию, отложение смолы и коррозию со стороны газов. Насос между патрубками шунта подмешивает часть подающей воды в обратку и повышает её температуру. Если шунт не используется, закройте патрубки подходящими заглушками.")),
    ("h", L("Genleşme ve emniyet ventili", "Expansion and safety valve", "Расширение и предохранительный клапан")),
    ("madde", [
      L("Genleşme tankı, tüm tesisattaki su hacmine göre uzman kişi tarafından hesaplanır.", "The expansion tank is sized by a specialist according to the water volume of the whole system.", "Расширительный бак рассчитывается специалистом по объёму воды во всей системе."),
      L("Kazan ile genleşme tankı ve emniyet ventili arasına kapatılabilir vana koymayın.", "Do not install a shut-off valve between the boiler and the expansion tank or safety valve.", "Не устанавливайте запорную арматуру между котлом и расширительным баком или предохранительным клапаном."),
      L("Emniyet ventilinin tahliyesini insanlara zarar vermeyecek güvenli bir noktaya yönlendirin; ayarını değiştirmeyin.", "Route the safety valve discharge to a safe point where it cannot harm people; do not change its setting.", "Выведите сброс предохранительного клапана в безопасное место; не изменяйте его настройку."),
    ]),
    ("not", "tehlike", L("ELEKTRİK KESİNTİSİNE KARŞI ÖNLEM", "PROTECTION AGAINST POWER FAILURE", "ЗАЩИТА ПРИ ОТКЛЮЧЕНИИ ЭЛЕКТРОЭНЕРГИИ"),
      L("Katı yakıtlı kazanda elektrik kesilse de ocaktaki yakıt yanmaya devam eder. Tesisat projesinde, pompa durduğunda kazandaki ısının güvenle uzaklaştırılması öngörülmelidir: örneğin sirkülasyon pompası için kesintisiz güç kaynağı veya jeneratör, ya da açık genleşme / ısı tahliye düzeni. Uygun çözüm, tesisat projecisi ve ENORPA ile birlikte seçilir.",
        "In a solid-fuel boiler the fuel in the furnace keeps burning even if the power fails. The system design must provide for the safe removal of the boiler heat when the pump stops: for example an uninterruptible power supply or generator for the circulation pump, or an open expansion / heat dissipation arrangement. The suitable solution is chosen together with the system designer and ENORPA.",
        "В котле на твёрдом топливе топливо в топке продолжает гореть и при отключении электроэнергии. Проект системы должен предусматривать безопасный отвод тепла котла при остановке насоса: например, источник бесперебойного питания или генератор для циркуляционного насоса либо открытую расширительную систему / устройство сброса тепла. Решение выбирается совместно с проектировщиком системы и ENORPA.")),
    ("not", "dikkat", L("İLK DOLUMDAN ÖNCE", "BEFORE THE FIRST FILLING", "ПЕРЕД ПЕРВЫМ ЗАПОЛНЕНИЕМ"),
      L("Hatları kazana bağlamadan önce tesisatı yıkayarak kaynak cürufu ve pislikten arındırın. Dolum suyunun özellikleri için bölüm 10'a bakın.",
        "Before connecting the lines to the boiler, flush the system to remove welding slag and dirt. See section 10 for the fill water requirements.",
        "Перед подключением к котлу промойте систему от сварочного шлака и грязи. Требования к воде заполнения — в разделе 10.")),
  ]))

# ---------------------------------------------------------------- 08
B.append(dict(no="08", ust=L("TESİSAT BAĞLANTISI", "PIPEWORK", "ПОДКЛЮЧЕНИЕ К СИСТЕМЕ"),
  baslik=L("Baca, siklon ve fanlar", "Chimney, cyclone and fans", "Дымовая труба, циклон и вентиляторы"),
  bloklar=[
    ("h", L("Duman yolu", "Flue gas path", "Тракт дымовых газов")),
    ("p", L("Duman gazı sırasıyla kazan çıkışı → siklon → baca gazı fanı → baca yolunu izler. Bağlantı kanalları sızdırmaz olmalı, sökülebilir temizleme kapakları içermeli ve gereksiz dirsekten kaçınılmalıdır.",
            "The flue gas passes in this order: boiler outlet → cyclone → flue gas fan → chimney. The connecting ducts must be gas-tight, have removable cleaning covers and avoid unnecessary bends.",
            "Дымовые газы проходят в следующем порядке: выход котла → циклон → дымосос → дымовая труба. Соединительные газоходы должны быть герметичными, иметь съёмные лючки для чистки и не содержать лишних отводов.")),
    ("h", L("Baca", "Chimney", "Дымовая труба")),
    ("madde", [
      L("Baca kesiti ve yüksekliği siparişe özel çizime göre yapılır; kazan çıkış çapından küçük olamaz.", "The chimney cross-section and height follow the order-specific drawing; it must not be smaller than the boiler outlet.", "Сечение и высота трубы выполняются по чертежу заказа; сечение не может быть меньше выхода котла."),
      L("Yoğuşmayı önlemek için çift cidarlı ve yalıtımlı baca tercih edin; tabanda yoğuşma ve kurum tahliyesi bulunsun.", "Prefer a double-walled insulated chimney to prevent condensation; provide a condensate and soot drain at the base.", "Для предотвращения конденсации предпочтительна двустенная утеплённая труба; в основании предусмотрите отвод конденсата и сажи."),
      L("Bacayı yerel çevre ve imar mevzuatına uygun yükseklikte bitirin; şapka ile yağmur girişini önleyin.", "Terminate the chimney at a height complying with local environmental and building regulations; prevent rain ingress with a cap.", "Выводите трубу на высоту, соответствующую местным экологическим и строительным нормам; защитите от осадков колпаком."),
    ]),
    ("h", L("Siklon", "Cyclone", "Циклон")),
    ("madde", [
      L("Siklonu terazide ve sağlam bir zemine kurun; gaz girişini yön okuna göre bağlayın.", "Install the cyclone level on a firm base; connect the gas inlet according to the direction arrow.", "Устанавливайте циклон горизонтально на прочное основание; подключайте вход газа по стрелке направления."),
      L("Kül haznesi sızdırmaz kapanmalıdır; hava kaçağı siklonun ayırma verimini düşürür.", "The ash hopper must close tightly; air leakage reduces the separation efficiency of the cyclone.", "Золосборник должен плотно закрываться: подсос воздуха снижает эффективность циклона."),
    ]),
    ("h", L("Fanlar", "Fans", "Вентиляторы")),
    ("madde", [
      L("Fanları titreşim yalıtımlı ayaklara oturtun; dönüş yönünü gövdedeki oka göre kontrol edin.", "Mount the fans on vibration-isolated feet; check the direction of rotation against the arrow on the housing.", "Устанавливайте вентиляторы на виброопоры; проверьте направление вращения по стрелке на корпусе."),
      L("Taze hava fanının emişini temiz ve engelsiz tutun; baca gazı fanı ve kanalları sıcak gaza dayanıklı olmalıdır.", "Keep the fresh air fan intake clean and unobstructed; the flue gas fan and ducts must withstand hot gas.", "Держите всасывание дутьевого вентилятора чистым и свободным; дымосос и газоходы должны быть рассчитаны на горячие газы."),
    ]),
    ("not", "tehlike", L("BACA GAZI FANI ÇALIŞMADAN YAKMAYIN", "DO NOT FIRE WITHOUT THE FLUE GAS FAN", "НЕ РАЗЖИГАЙТЕ БЕЗ ДЫМОСОСА"),
      L("Baca gazı fanı durmuşken veya kanal tıkalıyken yanma odası basınç altına girer ve duman kazan dairesine yayılır. Pano, fan arızasında yakıt beslemeyi durduracak şekilde bağlanmalıdır.",
        "If the flue gas fan has stopped or the duct is blocked, the combustion chamber becomes pressurised and smoke spreads into the boiler room. The panel must be wired to stop the fuel feed if the fan fails.",
        "При остановленном дымососе или засорённом газоходе в топке возникает избыточное давление, и дым распространяется в котельную. Щит должен быть подключён так, чтобы при отказе дымососа подача топлива останавливалась.")),
  ]))

# ---------------------------------------------------------------- 09
B.append(dict(no="09", ust=L("YAKMA SİSTEMİ", "FIRING SYSTEM", "ТОПОЧНАЯ СИСТЕМА"),
  baslik=L("Yakıt ve yakıt besleme", "Fuel and fuel feed", "Топливо и подача топлива"),
  bloklar=[
    ("p", L("Kazanın yanma ayarları, siparişte bildirilen yakıta göre yapılır. Yakıt cinsi değişirse (örneğin peletten kömüre) besleme hızı ve hava ayarı yeniden yapılmalıdır.",
            "The combustion settings of the boiler are made for the fuel stated in the order. If the fuel type changes (for example from pellets to coal), the feed rate and air setting must be readjusted.",
            "Настройки горения выполняются под топливо, указанное в заказе. При смене вида топлива (например, с пеллет на уголь) скорость подачи и настройку воздуха нужно выполнить заново.")),
    ("h", L("Yakıtta aranacak özellikler", "Fuel requirements", "Требования к топливу")),
    ("tablo", [L("Özellik", "Property", "Свойство"), L("Kural", "Rule", "Правило")], [
      [L("Cins", "Type", "Вид"), L("Yalnızca siparişte belirtilen yakıt (pelet, prina, kömür vb.). Atık, plastik, boyalı veya emprenyeli ahşap yakılmaz.", "Only the fuel specified in the order (pellets, olive pomace, coal, etc.). Never burn waste, plastics, or painted or treated wood.", "Только топливо, указанное в заказе (пеллеты, оливковый жмых, уголь и т. п.). Запрещено сжигать отходы, пластик, окрашенную или пропитанную древесину.")],
      [L("Nem", "Moisture", "Влажность"), L("Kuru yakıt kullanın. Islak yakıt verimi düşürür, duman ve katran oluşturur, helezonda topaklanır.", "Use dry fuel. Wet fuel lowers efficiency, produces smoke and tar and forms lumps in the screw.", "Используйте сухое топливо. Влажное топливо снижает КПД, даёт дым и смолу и слёживается в шнеке.")],
      [L("Tane boyutu", "Particle size", "Размер частиц"), L("Helezonun taşıyabileceği boyutta ve düzgün dağılımlı olmalı; iri parça ve topak helezonu sıkıştırır.", "Must be of a size the screw can convey and evenly graded; large pieces and lumps jam the screw.", "Размер должен соответствовать шнеку, фракция — равномерной; крупные куски и комья заклинивают шнек.")],
      [L("Yabancı madde", "Foreign matter", "Посторонние примеси"), L("Taş, metal, tel, naylon olmamalı. Bunker ağzında ızgara varsa sökmeyin.", "No stones, metal, wire or plastic film. If there is a grid at the bunker opening, do not remove it.", "Без камней, металла, проволоки и плёнки. Если на горловине бункера есть решётка, не снимайте её.")],
    ], {"kalin1": True}),
    ("h", L("Bunker ve helezon", "Bunker and screw", "Бункер и шнек")),
    ("madde", [
      L("Bunkeri tamamen boşaltmayın; helezon boşa çalışırsa ateş besleme hattına doğru ilerleyebilir.", "Do not let the bunker run empty; if the screw runs empty the fire can move back towards the feed line.", "Не допускайте полного опорожнения бункера: при пустом шнеке огонь может распространиться к линии подачи."),
      L("Doldurma dışında bunker kapağını kapalı tutun; doldururken beslemeyi durdurmanız gerekmez, ancak ateşin yanına yakıt dökmeyin.", "Keep the bunker lid closed except when filling; the feed need not be stopped while filling, but never pour fuel near the fire.", "Держите крышку бункера закрытой, кроме времени загрузки; останавливать подачу при загрузке не нужно, но не сыпьте топливо рядом с огнём."),
      L("Helezon sıkışırsa enerjiyi kesip kilitleyin, ancak bundan sonra temizleyin. Elinizi asla çalışan helezona sokmayın.", "If the screw jams, isolate and lock out the power before clearing it. Never put your hand into a running screw.", "При заклинивании шнека отключите и заблокируйте питание и только затем очищайте. Никогда не засовывайте руку в работающий шнек."),
    ]),
    ("not", "tehlike", L("GERİ YANMA", "BURN-BACK", "ОБРАТНЫЙ ПРОГАР"),
      L("Helezonda veya bunkerde duman, koku ya da sıcaklık artışı geri yanma belirtisidir. Beslemeyi durdurun, bunker kapağını açmayın ve servisi arayın. Besleme hattında geri yanma emniyeti varsa (termostat, damper, sprinkler vb.) bunları devre dışı bırakmayın ve düzenli test edin.",
        "Smoke, smell or rising temperature at the screw or bunker are signs of burn-back. Stop the feed, do not open the bunker lid and call service. If the feed line has burn-back protection (thermostat, damper, sprinkler, etc.), never disable it and test it regularly.",
        "Дым, запах или рост температуры у шнека или бункера — признаки обратного прогара. Остановите подачу, не открывайте крышку бункера и вызовите сервис. Если на линии подачи есть защита от обратного прогара (термостат, заслонка, спринклер и т. п.), не отключайте её и регулярно проверяйте.")),
  ]))

# ---------------------------------------------------------------- 10 (Akuamarin ile aynı)
_su = [b for b in AKU.B if b["no"] == "10"][0]
B.append(dict(no="10", ust=_su["ust"], baslik=_su["baslik"], bloklar=_su["bloklar"]))

# ---------------------------------------------------------------- 11
B.append(dict(no="11", ust=L("KONTROLLÜ İLK ÇALIŞTIRMA", "CONTROLLED FIRST START-UP", "КОНТРОЛИРУЕМЫЙ ПЕРВЫЙ ПУСК"),
  baslik=L("Devreye alma", "Commissioning", "Ввод в эксплуатацию"),
  bloklar=[
    ("not", "dikkat", L("İLK DEVREYE ALMA", "FIRST COMMISSIONING", "ПЕРВЫЙ ВВОД В ЭКСПЛУАТАЦИЮ"),
      L("İlk işletmeye alma, ENORPA veya ENORPA'nın yetkilendirdiği teknik servis gözetiminde yapılır. Kazan susuz veya eksik suyla kesinlikle yakılmaz.",
        "The first start-up is carried out under the supervision of ENORPA or a service partner authorised by ENORPA. The boiler must never be fired without water or with insufficient water.",
        "Первый пуск выполняется под надзором ENORPA или уполномоченного ENORPA сервиса. Котёл ни в коем случае нельзя разжигать без воды или с недостаточным количеством воды.")),
    ("tablo", [L("Adım", "Step", "Шаг"), L("Kontrol edilecekler", "What to check", "Что проверить")], [
      [L("1. Genel montaj", "1. General installation", "1. Общий монтаж"), L("Kazan, bunker, helezon, fanlar, siklon ve baca montajı; cıvatalar ve kanal bağlantıları.", "Installation of boiler, bunker, screw, fans, cyclone and chimney; bolts and duct joints.", "Монтаж котла, бункера, шнека, вентиляторов, циклона и трубы; болты и соединения газоходов.")],
      [L("2. Su dolumu", "2. Water filling", "2. Заполнение водой"), L("Kazan ve tesisat suyla dolu; havası alınmış; basınç işletme değerine ayarlı.", "Boiler and system filled and vented; pressure set to the operating value.", "Котёл и система заполнены, воздух удалён; давление установлено на рабочее значение.")],
      [L("3. Genleşme ve emniyet", "3. Expansion and safety", "3. Расширение и защита"), L("Genleşme tankı, emniyet ventili, termostatlar, göstergeler; aralarında kapalı vana yok.", "Expansion tank, safety valve, thermostats, gauges; no closed valve in between.", "Расширительный бак, предохранительный клапан, термостаты, приборы; закрытой арматуры между ними нет.")],
      [L("4. Elektrik", "4. Electrics", "4. Электрика"), L("Ana besleme, pano bağlantıları, topraklama, invertör parametreleri.", "Main supply, panel connections, earthing, inverter parameters.", "Питание, подключение щита, заземление, параметры преобразователя частоты.")],
      [L("5. Dönüş yönleri", "5. Directions of rotation", "5. Направление вращения"), L("Pompalar, taze hava fanı, baca gazı fanı ve helezon motorları kısa süre çalıştırılarak kontrol edilir.", "Pumps, fresh air fan, flue gas fan and screw motors are checked by brief running.", "Насосы, дутьевой вентилятор, дымосос и двигатели шнеков проверяются кратковременным пуском.")],
      [L("6. Emniyet kilitlemeleri", "6. Safety interlocks", "6. Защитные блокировки"), L("Pompa, fan ve yüksek sıcaklık arızasında beslemenin durduğu denenir.", "It is tested that the feed stops on pump, fan and over-temperature faults.", "Проверяется остановка подачи при отказе насоса, вентилятора и перегреве.")],
      [L("7. Yakıt", "7. Fuel", "7. Топливо"), L("Siparişteki yakıt bunkere doldurulur; helezon boş olarak dolana kadar çalıştırılır.", "The fuel specified in the order is loaded into the bunker; the screw is run until it is filled.", "В бункер загружается указанное в заказе топливо; шнек запускается до заполнения.")],
      [L("8. İlk ateşleme", "8. First ignition", "8. Первый розжиг"), L("Baca gazı fanı çalışırken düşük beslemeyle ateş yakılır; yanma odası vakumu ve alev gözlenir.", "The fire is lit at low feed with the flue gas fan running; combustion chamber vacuum and flame are observed.", "Розжиг выполняется на малой подаче при работающем дымососе; контролируются разрежение в топке и пламя.")],
      [L("9. Kademeli ısıtma", "9. Gradual heating", "9. Постепенный прогрев"), L("Kazan yavaşça çalışma sıcaklığına çıkarılır; basınç, sıcaklık ve su dolaşımı izlenir.", "The boiler is brought slowly to operating temperature; pressure, temperature and water circulation are monitored.", "Котёл медленно выводится на рабочую температуру; контролируются давление, температура и циркуляция.")],
      [L("10. Yanma ayarı", "10. Combustion setting", "10. Наладка горения"), L("Besleme hızı ve hava oranı ayarlanır; O₂, CO ve baca gazı sıcaklığı ölçülür.", "Feed rate and air ratio are adjusted; O₂, CO and flue gas temperature are measured.", "Настраиваются скорость подачи и соотношение воздуха; измеряются O₂, CO и температура газов.")],
      [L("11. Teslim", "11. Handover", "11. Сдача"), L("Kaçak kontrolü, farklı yüklerde çalışma testi, operatör eğitimi ve kayıt formu.", "Leak check, test at different loads, operator training and record form.", "Проверка утечек, испытание на разных нагрузках, обучение оператора и протокол.")],
    ], {"kalin1": True, "sik": True}),
    ("kucuk", L("Her adımın sonucunu bölüm 18'deki “Devreye alma kayıt formu”na işleyin. Uygun olmayan bir adım varken sonraki adıma geçmeyin.",
                "Enter the result of each step in the “Commissioning record” in section 18. Do not move on to the next step while a step is not OK.",
                "Заносите результат каждого шага в «Протокол ввода в эксплуатацию» (раздел 18). Не переходите к следующему шагу, пока предыдущий не выполнен.")),
    ("not", "dikkat", L("İLK 50 ÇALIŞMA SAATİNDEN SONRA", "AFTER THE FIRST 50 OPERATING HOURS", "ПОСЛЕ ПЕРВЫХ 50 ЧАСОВ РАБОТЫ"),
      L("Kapak cıvatalarını, flanş ve kanal bağlantılarını, redüktör yağ seviyesini ve fan bağlantılarını kontrol edin; gerekiyorsa yeniden sıkın.",
        "Check the door bolts, flange and duct joints, gear unit oil level and fan mountings; retighten if necessary.",
        "Проверьте болты дверец, фланцевые соединения и газоходы, уровень масла в редукторах и крепление вентиляторов; при необходимости подтяните.")),
  ]))

# ---------------------------------------------------------------- 12
B.append(dict(no="12", ust=L("GÜNLÜK KULLANIM", "DAILY USE", "ЕЖЕДНЕВНАЯ ЭКСПЛУАТАЦИЯ"),
  baslik=L("İşletme ve durdurma", "Operation and shutdown", "Эксплуатация и останов"),
  bloklar=[
    ("h", L("Her gün", "Every day", "Ежедневно")),
    ("tablo", [L("Konu", "Item", "Пункт"), L("Yapılacak", "Action", "Действие")], [
      [L("Su basıncı ve sıcaklık", "Water pressure and temperature", "Давление и температура воды"), L("Göstergeleri kontrol edin. Dönüş suyu 55 °C'nin altına düşmemeli; basınç sürekli düşüyorsa kaçak arayın.", "Check the gauges. Return water must not fall below 55 °C; if the pressure keeps dropping, look for a leak.", "Проверьте приборы. Обратка не должна опускаться ниже 55 °C; при постоянном падении давления ищите утечку.")],
      [L("Bunker", "Bunker", "Бункер"), L("Yakıt seviyesini kontrol edin, boşalmadan doldurun; kapağı kapalı tutun.", "Check the fuel level and refill before it runs empty; keep the lid closed.", "Проверьте уровень топлива и досыпайте до опорожнения; держите крышку закрытой.")],
      [L("Kül", "Ash", "Зола"), L("Ocaktaki ve siklon haznesindeki külü, kazan tipine ve yakıta göre gereken sıklıkta alın.", "Remove the ash from the furnace and the cyclone hopper as often as required by the fuel and load.", "Удаляйте золу из топки и золосборника циклона с частотой, которую требуют топливо и нагрузка.")],
      [L("Yanma", "Combustion", "Горение"), L("Alev rengi, duman ve yanma odası vakumunu gözleyin; kapaklardan duman çıkmamalı.", "Watch the flame colour, smoke and combustion chamber vacuum; no smoke must escape from the doors.", "Следите за цветом пламени, дымом и разрежением в топке; из дверец не должен выходить дым.")],
      [L("Ses ve titreşim", "Noise and vibration", "Шум и вибрация"), L("Fan, helezon ve pompalarda olağandışı ses, ısınma veya titreşim olup olmadığını dinleyin.", "Listen for unusual noise, heating or vibration on fans, screws and pumps.", "Контролируйте отсутствие посторонних шумов, нагрева и вибрации вентиляторов, шнеков и насосов.")],
      [L("Kayıt", "Record", "Запись"), L("Basınç, sıcaklık ve eklenen suyu kazan işletme defterine yazın.", "Write pressure, temperature and water added in the boiler logbook.", "Записывайте давление, температуру и добавленную воду в журнал котла.")],
    ], {"kalin1": True}),
    ("h", L("Normal kapatma (bakım veya bekleme)", "Normal shutdown (maintenance or standby)", "Нормальный останов (обслуживание или резерв)")),
    ("adim", [
      L("Yakıt beslemeyi durdurun.", "Stop the fuel feed.", "Остановите подачу топлива."),
      L("Fanları ve sirkülasyon pompasını, ocaktaki yakıt tamamen yanıp bitene ve kazan suyu soğuyana kadar çalışır bırakın.", "Leave the fans and circulation pump running until the fuel in the furnace has burnt out and the boiler water has cooled.", "Оставьте вентиляторы и циркуляционный насос работать до полного выгорания топлива и остывания воды."),
      L("Ateş söndükten sonra sistemin elektriğini ana panodan kesin.", "After the fire is out, isolate the system at the main panel.", "После затухания огня обесточьте систему на главном щите."),
      L("Kazan sıcakken suyunu boşaltmayın; ısıl şok kazana zarar verir.", "Do not drain the boiler while it is hot; thermal shock damages the boiler.", "Не сливайте воду из горячего котла: тепловой удар повреждает котёл."),
    ]),
    ("not", "tehlike", L("POMPAYI ATEŞ VARKEN DURDURMAYIN", "DO NOT STOP THE PUMP WHILE THERE IS FIRE", "НЕ ОСТАНАВЛИВАЙТЕ НАСОС ПРИ ГОРЯЩЕМ ТОПЛИВЕ"),
      L("Ocakta yakıt varken sirkülasyon pompasını kapatmak, kazan suyunun aşırı ısınmasına ve emniyet ventilinin açmasına yol açar. Su kaçağı, olağandışı ses veya duman gördüğünüzde beslemeyi durdurun, kapakları açmayın ve servisi arayın.",
        "Switching off the circulation pump while there is fuel in the furnace overheats the boiler water and makes the safety valve open. If you see a water leak, unusual noise or smoke, stop the feed, do not open the doors and call service.",
        "Отключение циркуляционного насоса при наличии топлива в топке приводит к перегреву воды и срабатыванию предохранительного клапана. При утечке воды, посторонних шумах или дыме остановите подачу, не открывайте дверцы и вызовите сервис.")),
    ("h", L("Donma koruması ve sıcak su tahliyesi", "Frost protection and hot water draining", "Защита от замерзания и слив горячей воды")),
    ("p", L("Kazan kışın devre dışı kalacaksa su donmaya karşı korunmalıdır (antifriz veya kontrollü boşaltma). Kazandaki su 100 °C'yi geçebilir; kanalizasyona verilmeden önce 35 °C'nin altına soğutulmalıdır.",
            "If the boiler will be out of service in winter, the water must be protected against freezing (antifreeze or controlled draining). The boiler water can exceed 100 °C; it must be cooled below 35 °C before being discharged to the drain.",
            "Если котёл зимой выводится из работы, воду нужно защитить от замерзания (антифриз или контролируемый слив). Вода в котле может быть выше 100 °C; перед сбросом в канализацию её нужно охладить ниже 35 °C.")),
  ]))

# ---------------------------------------------------------------- 13
B.append(dict(no="13", ust=L("KAYITLI BAKIM PLANI", "RECORDED MAINTENANCE PLAN", "ПЛАН ОБСЛУЖИВАНИЯ С УЧЁТОМ"),
  baslik=L("Periyodik bakım", "Periodic maintenance", "Периодическое обслуживание"),
  bloklar=[
    ("p", L("Katı yakıtta kül ve kurum, ısıtma yüzeylerini sıvı / gaz yakıta göre çok daha hızlı kirletir. Kirli yüzey baca gazı sıcaklığını ve yakıt tüketimini artırır. Aşağıdaki aralıklar en az yapılması gerekenlerdir; yakıta ve yüke göre sıklaştırın.",
            "With solid fuel, ash and soot foul the heating surfaces much faster than with liquid / gas fuel. Fouled surfaces raise the flue gas temperature and fuel consumption. The intervals below are minimums; shorten them according to fuel and load.",
            "При твёрдом топливе зола и сажа загрязняют поверхности нагрева гораздо быстрее, чем при жидком / газовом. Загрязнение повышает температуру уходящих газов и расход топлива. Ниже приведены минимальные интервалы; сокращайте их в зависимости от топлива и нагрузки.")),
    ("tablo", [L("Ne zaman?", "When?", "Когда?"), L("Kontrol / işlem", "Check / action", "Проверка / действие")], [
      [L("Her gün", "Every day", "Ежедневно"), L("Bölüm 12'deki günlük kontroller; kül alma.", "Daily checks in section 12; ash removal.", "Ежедневные проверки раздела 12; удаление золы.")],
      [L("Haftada en az bir kez", "At least once a week", "Не реже раза в неделю"), L("Duman borularının kontrolü ve fırçayla temizliği; siklon kül haznesinin boşaltılması; kapak contalarının kontrolü.", "Inspection and brushing of the fire tubes; emptying the cyclone ash hopper; checking door seals.", "Осмотр и чистка дымогарных труб щёткой; опорожнение золосборника циклона; проверка уплотнений дверец.")],
      [L("Ayda en az bir kez", "At least once a month", "Не реже раза в месяц"), L("Duman kanalları ve baca gazı fanı çarkının temizliği; helezon ve bunkerin kontrolü; redüktör yağ seviyesi.", "Cleaning of flue ducts and flue gas fan impeller; inspection of screw and bunker; gear unit oil level.", "Чистка газоходов и рабочего колеса дымососа; осмотр шнека и бункера; уровень масла в редукторах.")],
      [L("Altı ayda en az bir kez", "At least every six months", "Не реже раза в полгода"), L("Su tarafının ve tesisatın bakımı; tortu ve çamur kontrolü; ocak içi ve yalıtımın kontrolü; baca tabanının temizliği.", "Maintenance of the water side and system; sludge check; inspection of the furnace interior and insulation; cleaning of the chimney base.", "Обслуживание водяной стороны и системы; проверка шлама; осмотр топки и изоляции; чистка основания трубы.")],
      [L("Yılda bir kez (sezon öncesi)", "Once a year (before the season)", "Раз в год (перед сезоном)"), L("ENORPA bakım ekibiyle genel kontrol; baca temizliği; emniyet kilitlemelerinin ve yanma ayarının kontrolü.", "General inspection with the ENORPA maintenance team; chimney sweeping; check of safety interlocks and combustion setting.", "Общая проверка с сервисом ENORPA; чистка трубы; проверка защитных блокировок и наладки горения.")],
      [L("Üreticisinin belirttiği aralıkta", "At the interval stated by its manufacturer", "С периодичностью по данным изготовителя"), L("Emniyet ventili, fanlar, motorlar, redüktörler, pompalar ve invertörün kendi bakımları.", "Own maintenance of the safety valve, fans, motors, gear units, pumps and inverter.", "Собственное обслуживание предохранительного клапана, вентиляторов, двигателей, редукторов, насосов и преобразователя.")],
    ], {"kalin1": True}),
    ("h", L("Bakıma başlamadan önce", "Before starting maintenance", "Перед началом обслуживания")),
    ("adim", [
      L("<b>Beslemeyi durdurun:</b> ocaktaki yakıtın tamamen yanıp bitmesini bekleyin.", "<b>Stop the feed:</b> wait until the fuel in the furnace has burnt out completely.", "<b>Остановите подачу:</b> дождитесь полного выгорания топлива в топке."),
      L("<b>Elektriği kesin:</b> ana şalteri kapatıp kilitleyin.", "<b>Isolate the power:</b> switch off and lock the main switch.", "<b>Отключите питание:</b> выключите и заблокируйте главный выключатель."),
      L("<b>Soğumasını bekleyin:</b> kazan basınç altındayken veya sıcakken kapakları açmayın.", "<b>Let it cool:</b> do not open the doors while the boiler is under pressure or hot.", "<b>Дайте остыть:</b> не открывайте дверцы, пока котёл под давлением или горячий."),
      L("<b>Suyu boşaltacaksanız:</b> basınç 0 bar ve su 70 °C'nin altındayken, havalık açık olarak boşaltın.", "<b>If draining:</b> drain only with the pressure at 0 bar, the water below 70 °C and a vent open.", "<b>При сливе:</b> сливайте только при давлении 0 бар, температуре воды ниже 70 °C и открытом воздушнике."),
    ]),
    ("not", "dikkat", L("OCAĞA VE DUMAN KANALINA GİRERKEN", "WHEN ENTERING THE FURNACE OR FLUE DUCT", "ПРИ ВХОДЕ В ТОПКУ ИЛИ ГАЗОХОД"),
      L("İçerideki zehirli gazların tahliye edildiğinden ve korun söndüğünden emin olun; toz maskesi ve gözlük kullanın, dışarıda bir gözcü bulundurun.",
        "Make sure toxic gases have been cleared and the embers are extinguished; wear a dust mask and goggles and keep an attendant outside.",
        "Убедитесь, что ядовитые газы удалены и угли потушены; используйте респиратор и очки, снаружи должен находиться наблюдающий.")),
  ]))

# ---------------------------------------------------------------- 14
B.append(dict(no="14", ust=L("KAYITLI BAKIM PLANI", "RECORDED MAINTENANCE PLAN", "ПЛАН ОБСЛУЖИВАНИЯ С УЧЁТОМ"),
  baslik=L("Temizlik ve kül", "Cleaning and ash", "Чистка и зола"),
  bloklar=[
    ("h", L("Duman borularının temizliği", "Cleaning the fire tubes", "Чистка дымогарных труб")),
    ("adim", [
      L("Bölüm 13'teki hazırlıkları yapın; ön kapakları açın.", "Carry out the preparations in section 13; open the front doors.", "Выполните подготовку по разделу 13; откройте передние дверцы."),
      L("Her boruyu kazanla verilen fırçayla boydan boya birkaç kez fırçalayın.", "Brush each tube several times along its full length with the brush supplied with the boiler.", "Прочистите каждую трубу по всей длине несколько раз щёткой из комплекта котла."),
      L("Dökülen kurum ve külü duman sandığından ve ocaktan alın.", "Remove the soot and ash that falls out from the smoke box and furnace.", "Удалите выпавшую сажу и золу из дымовой камеры и топки."),
      L("Contaları kontrol edin, kapakları cıvataları çapraz sırayla eşit sıkarak kapatın.", "Check the seals and close the doors, tightening the bolts evenly in a crosswise sequence.", "Проверьте уплотнения и закройте дверцы, равномерно затягивая болты крест-накрест."),
    ]),
    ("h", L("Ocak ve kül", "Furnace and ash", "Топка и зола")),
    ("madde", [
      L("Yanma bölgesindeki cüruf ve külü düzenli alın; hava deliklerinin tıkanmasına izin vermeyin.", "Remove slag and ash from the combustion zone regularly; do not let the air holes become blocked.", "Регулярно удаляйте шлак и золу из зоны горения; не допускайте засорения воздушных отверстий."),
      L("Külü yalnızca metal, kapaklı kaba alın ve yanıcı maddelerden uzakta en az 24 saat soğumaya bırakın.", "Put ash only in a metal container with a lid and leave it to cool for at least 24 hours away from combustible materials.", "Помещайте золу только в металлическую ёмкость с крышкой и оставляйте остывать не менее 24 часов вдали от горючих материалов."),
    ]),
    ("h", L("Siklon, fan ve baca", "Cyclone, fan and chimney", "Циклон, вентилятор и труба")),
    ("madde", [
      L("Siklon kül haznesini dolmadan boşaltın; dolu hazne külün yeniden gaz akışına karışmasına neden olur.", "Empty the cyclone ash hopper before it is full; a full hopper lets ash re-enter the gas flow.", "Опорожняйте золосборник циклона до заполнения: переполненный сборник возвращает золу в поток газов."),
      L("Baca gazı fanının çarkındaki birikinti dengesizlik ve titreşim yapar; temizleyip titreşimi kontrol edin.", "Deposits on the flue gas fan impeller cause imbalance and vibration; clean it and check the vibration.", "Отложения на колесе дымососа вызывают дисбаланс и вибрацию; очистите его и проверьте вибрацию."),
      L("Duman kanallarındaki temizleme kapaklarından kurumu alın; bacayı yılda en az bir kez temizletin.", "Remove soot through the cleaning covers in the flue ducts; have the chimney swept at least once a year.", "Удаляйте сажу через лючки газоходов; чистите трубу не реже раза в год."),
    ]),
    ("h", L("Helezon ve bunker", "Screw and bunker", "Шнек и бункер")),
    ("madde", [
      L("Bunker dibinde biriken toz ve ıslak yakıtı temizleyin; köprüleşme varsa giderin.", "Clean out dust and wet fuel collecting at the bottom of the bunker; clear any bridging.", "Удаляйте пыль и влажное топливо со дна бункера; устраняйте сводообразование."),
      L("Helezon yataklarını ve redüktörleri üretici talimatına göre yağlayın.", "Lubricate the screw bearings and gear units according to the manufacturer's instructions.", "Смазывайте подшипники шнека и редукторы по инструкции изготовителя."),
    ]),
    ("not", "dikkat", L("SU İLE TEMİZLEMEYİN", "DO NOT CLEAN WITH WATER", "НЕ ЧИСТИТЕ ВОДОЙ"),
      L("Duman tarafını, ocağı ve bunkeri su ile yıkamayın. Kül ve kurum suyla birleşince aşındırıcı bir çamur oluşturur ve korozyona yol açar.",
        "Do not wash the flue gas side, the furnace or the bunker with water. Ash and soot mixed with water form a corrosive sludge.",
        "Не промывайте водой газовую сторону, топку и бункер. Зола и сажа с водой образуют агрессивный шлам, вызывающий коррозию.")),
  ]))

# ---------------------------------------------------------------- 15
B.append(dict(no="15", ust=L("BELİRTİDEN KONTROLE", "FROM SYMPTOM TO CHECK", "ОТ ПРИЗНАКА К ПРОВЕРКЕ"),
  baslik=L("Arıza bulma", "Troubleshooting", "Поиск неисправностей"),
  bloklar=[
    ("kucuk", L("Aşağıdaki tablo ilk kontroller içindir. Emniyet donanımına müdahale gerektiren veya nedeni bulunamayan her durumda servisi arayın.",
                "The table below is for initial checks. Call service in every case that requires intervention on safety equipment or where the cause cannot be found.",
                "Таблица предназначена для первичных проверок. Вызывайте сервис во всех случаях, требующих вмешательства в защитные устройства или когда причину найти не удаётся.")),
    ("tablo", [L("Belirti", "Symptom", "Признак"), L("Olası neden", "Possible cause", "Возможная причина"), L("Yapılacak", "Action", "Действие")], [
      [L("Kazan istenen sıcaklığa çıkmıyor", "Boiler does not reach the set temperature", "Котёл не выходит на заданную температуру"), L("Kirli duman boruları, ıslak / uygunsuz yakıt, düşük besleme, hava eksikliği", "Fouled fire tubes, wet / unsuitable fuel, low feed, too little air", "Загрязнённые трубы, влажное / неподходящее топливо, малая подача, недостаток воздуха"), L("Boruları temizleyin, yakıtı kontrol edin, besleme ve hava ayarını servise yaptırın.", "Clean the tubes, check the fuel, have feed and air adjusted by service.", "Очистите трубы, проверьте топливо, поручите сервису настройку подачи и воздуха.")],
      [L("Kapaklardan duman çıkıyor", "Smoke escapes from the doors", "Из дверец выходит дым"), L("Baca gazı fanı durmuş / yavaş, kanal veya siklon tıkalı, conta hasarlı", "Flue gas fan stopped / slow, duct or cyclone blocked, damaged seal", "Дымосос остановлен / мало оборотов, засорён газоход или циклон, повреждено уплотнение"), L("Beslemeyi durdurun, havalandırın; fanı, kanalları ve contaları kontrol edin.", "Stop the feed, ventilate; check the fan, ducts and seals.", "Остановите подачу, проветрите; проверьте вентилятор, газоходы и уплотнения.")],
      [L("Bacadan yoğun siyah duman", "Dense black smoke from the chimney", "Густой чёрный дым из трубы"), L("Hava yetersiz, aşırı besleme, ıslak yakıt", "Insufficient air, excessive feed, wet fuel", "Недостаток воздуха, избыточная подача, влажное топливо"), L("Beslemeyi azaltın, taze hava fanını ve yakıtı kontrol edin.", "Reduce the feed, check the fresh air fan and the fuel.", "Уменьшите подачу, проверьте дутьевой вентилятор и топливо.")],
      [L("Helezon dönmüyor / motor termiği atıyor", "Screw does not turn / motor overload trips", "Шнек не вращается / срабатывает тепловое реле"), L("Yabancı cisim, topak, aşırı uzun parça", "Foreign object, lump, oversized pieces", "Посторонний предмет, комья, крупные куски"), L("Enerjiyi kesip kilitleyin, helezonu temizleyin; yakıtı eleyin.", "Isolate and lock out, clear the screw; screen the fuel.", "Отключите и заблокируйте питание, очистите шнек; просейте топливо.")],
      [L("Bunker veya helezonda duman / ısınma", "Smoke / heat at the bunker or screw", "Дым / нагрев у бункера или шнека"), L("Geri yanma, boş helezon", "Burn-back, empty screw", "Обратный прогар, пустой шнек"), L("Beslemeyi durdurun, bunker kapağını açmayın, servisi arayın.", "Stop the feed, do not open the bunker lid, call service.", "Остановите подачу, не открывайте крышку бункера, вызовите сервис.")],
      [L("Sıcaklık yükseliyor, emniyet ventili açıyor", "Temperature rising, safety valve opens", "Растёт температура, срабатывает предохранительный клапан"), L("Pompa durmuş, vana kapalı, tesisat ısı çekmiyor, elektrik kesintisi", "Pump stopped, valve closed, system not taking heat, power failure", "Насос остановлен, закрыта арматура, система не отбирает тепло, отключение питания"), L("Beslemeyi durdurun, kapakları açmayın; pompayı ve vanaları kontrol edin (bölüm 02).", "Stop the feed, do not open the doors; check the pump and valves (section 02).", "Остановите подачу, не открывайте дверцы; проверьте насос и арматуру (раздел 02).")],
      [L("Basınç sürekli düşüyor", "Pressure keeps dropping", "Давление постоянно падает"), L("Tesisatta veya kazanda su kaçağı, genleşme tankı arızası", "Water leak in the system or boiler, expansion tank fault", "Утечка в системе или котле, неисправность расширительного бака"), L("Kaçağı bulun; eklenen suyu kaydedin; tankın ön basıncını kontrol ettirin.", "Find the leak; record the water added; have the tank pre-pressure checked.", "Найдите утечку; записывайте добавленную воду; проверьте давление в баке.")],
      [L("Kazanda terleme, katran", "Condensation, tar in the boiler", "Конденсат, смола в котле"), L("Düşük dönüş sıcaklığı, şönt pompa çalışmıyor, ıslak yakıt", "Low return temperature, shunt pump not running, wet fuel", "Низкая температура обратки, не работает шунтирующий насос, влажное топливо"), L("Dönüşü 55 °C üzerinde tutun; şönt pompayı ve yakıtı kontrol edin.", "Keep the return above 55 °C; check the shunt pump and the fuel.", "Поддерживайте обратку выше 55 °C; проверьте шунтирующий насос и топливо.")],
      [L("Fanda titreşim / ses", "Fan vibration / noise", "Вибрация / шум вентилятора"), L("Çarkta birikinti, gevşek bağlantı, yatak arızası", "Deposits on the impeller, loose fixing, bearing fault", "Отложения на колесе, ослабление крепления, неисправность подшипника"), L("Durdurun; çarkı temizleyin, bağlantıları sıkın, gerekiyorsa servis çağırın.", "Stop it; clean the impeller, tighten the fixings, call service if necessary.", "Остановите; очистите колесо, подтяните крепления, при необходимости вызовите сервис.")],
    ], {"kalin1": True, "sik": True}),
    ("not", "bilgi", L("SERVİSE İLETİLECEK BİLGİLER", "INFORMATION TO GIVE THE SERVICE", "ИНФОРМАЦИЯ ДЛЯ СЕРВИСА"),
      L("Seri numarası ve ürün kodu, kullanılan yakıt, arızanın zamanı ve o andaki çalışma koşulu, su basıncı ve sıcaklık değerleri, varsa pano arıza kodu ve güvenli şekilde çekilmiş fotoğraf ya da video.",
        "Serial number and product code, fuel used, time of the fault and operating conditions at that moment, water pressure and temperature values, any panel fault code, and photos or video taken safely.",
        "Серийный номер и код изделия, используемое топливо, время неисправности и режим работы в этот момент, давление и температура воды, код ошибки щита (если есть), а также фото или видео, снятые безопасно.")),
  ]))

# ---------------------------------------------------------------- 16–17 teknik
TEKNIK_B = [L("Model", "Model", "Модель"), L("Isıl kapasite (kcal/h)", "Heat output (kcal/h)", "Тепловая мощность (ккал/ч)"),
            L("Genişlik (mm)", "Width (mm)", "Ширина (мм)"), L("Uzunluk (mm)", "Length (mm)", "Длина (мм)"),
            L("Yükseklik (mm)", "Height (mm)", "Высота (мм)"), L("Ağırlık (kg)", "Weight (kg)", "Масса (кг)")]
TEKNIK_NOT = L("Değerler “Kazanların Modül H kapsamına göre teknik özellikleri” tablosundan alınmıştır. Ölçüler kazan gövdesinin dış ölçüleridir; bunker, fanlar, siklon ve baca dahil değildir. Ağırlık susuz ağırlıktır. Tüm ölçüler bilgilendirme amaçlıdır; ENORPA tasarım ve ölçülerde değişiklik yapma hakkını saklı tutar. Yerleşim ve tesisat projesi için siparişe özel onaylı çizimi esas alın.",
               "Values are taken from the table “Technical specifications of boilers according to Module H”. Dimensions are the external dimensions of the boiler body; bunker, fans, cyclone and chimney are not included. Weight is the dry weight. All dimensions are for information only; ENORPA reserves the right to change designs and dimensions. Use the approved order-specific drawing for layout and system design.",
               "Значения взяты из таблицы «Технические характеристики котлов по модулю H». Указаны наружные размеры корпуса котла без бункера, вентиляторов, циклона и дымовой трубы. Масса указана без воды. Все размеры носят информационный характер; ENORPA оставляет за собой право изменять конструкцию и размеры. Для размещения и проектирования системы руководствуйтесь утверждённым чертежом по заказу.")
BAGLANTI_B = [L("Model", "Model", "Модель"), L("Su gidiş – dönüş", "Water flow – return", "Подача – обратка"),
              L("Genleşme hattı", "Expansion line", "Расширительная линия"), L("Şönt hattı", "Shunt line", "Линия шунта")]
BAGLANTI_NOT = L("Su ağızları flanşlıdır. Ağızların sırası ve yeri, baca gazı çıkış çapı, baca ve siklon ölçüleri siparişe özel çizimde verilir.",
                 "Water nozzles are flanged. The order and position of the nozzles, the flue gas outlet size and the chimney and cyclone dimensions are given in the order-specific drawing.",
                 "Водяные патрубки фланцевые. Порядок и расположение патрубков, диаметр газового выхода, размеры трубы и циклона приведены в чертеже по заказу.")
ISLETME_B = [L("Değer", "Value", "Параметр"), L("Tüm modeller", "All models", "Все модели")]
ISLETME = [
    (L("Min. çalışma sıcaklığı", "Min. operating temperature", "Мин. рабочая температура"), "55 °C"),
    (L("Maks. çalışma sıcaklığı", "Max. operating temperature", "Макс. рабочая температура"), "110 °C"),
    (L("İşletme basıncı", "Operating pressure", "Рабочее давление"), L("3 bar", "3 bar", "3 бар")),
    (L("Dizayn basıncı", "Design pressure", "Расчётное давление"), L("3,45 bar", "3.45 bar", "3,45 бар")),
    (L("Test basıncı", "Test pressure", "Испытательное давление"), L("5,5 bar", "5.5 bar", "5,5 бар")),
]
BAGLANTI_KUTU = (L("TABLODA OLMAYAN MODELLER VE KIZGIN SU", "MODELS NOT IN THE TABLE AND SUPERHEATED WATER", "МОДЕЛИ ВНЕ ТАБЛИЦЫ И ПЕРЕГРЕТАЯ ВОДА"),
                 L("TR17 üzerindeki kapasiteler, çift bunkerli veya farklı basınç sınıfındaki özel üretimler ve kızgın su (Turkuaz KS) kazanları için veriler siparişe özel teknik föyde verilir.",
                   "Data for capacities above TR17, special versions with twin bunkers or a different pressure class, and superheated water boilers (Turkuaz KS) are given in the order-specific technical data sheet.",
                   "Данные для мощностей выше TR17, специальных исполнений со сдвоенным бункером или другим классом давления, а также для котлов перегретой воды (Turkuaz KS) приведены в техническом листе по заказу."))

B.append(dict(no="16", ust=L("TEKNİK VERİLER", "TECHNICAL DATA", "ТЕХНИЧЕСКИЕ ДАННЫЕ"),
  baslik=L("Kapasite, ölçü ve ağırlık", "Capacity, dimensions and weight", "Мощность, размеры и масса"), ozel="teknik_trk"))
B.append(dict(no="17", ust=L("TEKNİK VERİLER", "TECHNICAL DATA", "ТЕХНИЧЕСКИЕ ДАННЫЕ"),
  baslik=L("Bağlantı çapları ve işletme değerleri", "Connection sizes and operating values", "Присоединительные размеры и рабочие параметры"), ozel="baglanti_trk"))

# ---------------------------------------------------------------- 18 form
FORM = dict(AKU.FORM)
FORM["ust_alanlar"] = [
    (L("Ürün kodu / seri no", "Product code / serial no.", "Код изделия / серийный №"), L("Kurulum yeri", "Installation site", "Место установки")),
    (L("Devreye alma tarihi", "Commissioning date", "Дата ввода в эксплуатацию"), L("Pano / invertör marka ve modeli", "Panel / inverter make and model", "Щит / преобразователь: марка и модель")),
    (L("Yakıt cinsi ve kaynağı", "Fuel type and source", "Вид и источник топлива"), L("Devreye alan firma / kişi", "Commissioning company / person", "Организация / лицо, выполнившее ввод"))]
FORM["kontroller"] = [
    (L("Kazan kaide üzerinde, terazide; servis boşlukları uygun", "Boiler on plinth, level; service clearances adequate", "Котёл на фундаменте, выровнен; сервисные зазоры достаточны"), "uygun"),
    (L("Gidiş – dönüş doğru ağızlara bağlı; şönt hattı bağlı veya körlenmiş", "Flow – return connected to the correct nozzles; shunt line connected or blanked", "Подача – обратка подключены к нужным патрубкам; шунт подключён или заглушен"), "uygun"),
    (L("Genleşme tankı ve emniyet ventili bağlı; aralarında kapalı vana yok", "Expansion tank and safety valve connected; no shut-off valve in between", "Расширительный бак и предохранительный клапан подключены; запорной арматуры между ними нет"), "uygun"),
    (L("Sistem suyla dolu, havası alınmış; su analizi uygun", "System filled with water and vented; water analysis OK", "Система заполнена водой, воздух удалён; анализ воды в норме"), "uygun"),
    (L("Elektrik kesintisine karşı önlem (UPS / jeneratör / ısı tahliyesi) mevcut", "Power failure protection (UPS / generator / heat dissipation) in place", "Защита при отключении питания (ИБП / генератор / сброс тепла) имеется"), "evet"),
    (L("Siklon, kanallar ve baca bağlı ve sızdırmaz; menfezler açık", "Cyclone, ducts and chimney connected and gas-tight; vents open", "Циклон, газоходы и труба подключены и герметичны; проёмы открыты"), "uygun"),
    (L("Pompa, fan ve helezon dönüş yönleri; topraklama", "Directions of rotation of pumps, fans and screws; earthing", "Направление вращения насосов, вентиляторов и шнеков; заземление"), "uygun"),
    (L("Fan, pompa ve aşırı sıcaklık arızasında besleme durdu", "Feed stopped on fan, pump and over-temperature faults", "Подача остановилась при отказе вентилятора, насоса и перегреве"), "evet"),
    (L("Kapak cıvataları, contalar ve flanşlar kontrol edildi", "Door bolts, seals and flanges checked", "Болты дверец, уплотнения и фланцы проверены"), "evet"),
]
FORM["olcum_b"] = (L("Ölçüm", "Measurement", "Измерение"), L("Düşük yük", "Low load", "Малая нагрузка"), L("Tam yük", "Full load", "Полная нагрузка"))
FORM["olcumler"] = [
    L("Helezon besleme ayarı / frekans", "Screw feed setting / frequency", "Настройка подачи шнека / частота"),
    L("Taze hava fanı ayarı / frekans", "Fresh air fan setting / frequency", "Дутьевой вентилятор: настройка / частота"),
    L("O₂ (%)", "O₂ (%)", "O₂ (%)"), L("CO (ppm)", "CO (ppm)", "CO (ppm)"),
    L("Baca gazı sıcaklığı (°C)", "Flue gas temperature (°C)", "Температура дымовых газов (°C)"),
    L("Yanma odası basıncı (Pa)", "Combustion chamber pressure (Pa)", "Давление в топке (Па)"),
    L("Gidiş / dönüş suyu sıcaklığı (°C)", "Flow / return water temperature (°C)", "Температура подачи / обратки (°C)"),
    L("Sistem basıncı (bar)", "System pressure (bar)", "Давление в системе (бар)")]
B.append(dict(no="18", ust=L("HER KAZAN İÇİN DOLDURUN", "COMPLETE FOR EACH BOILER", "ЗАПОЛНЯЕТСЯ ДЛЯ КАЖДОГО КОТЛА"),
  baslik=L("Devreye alma kayıt formu", "Commissioning record", "Протокол ввода в эксплуатацию"), ozel="form"))

KAYIT = AKU.KAYIT
B.append(dict(no="19", ust=L("SATIŞ SONRASI", "AFTER-SALES", "ПОСЛЕПРОДАЖНОЕ ОБСЛУЖИВАНИЕ"),
  baslik=L("Bakım ve servis kaydı", "Maintenance and service record", "Журнал обслуживания и сервиса"), ozel="kayit"))

GARANTI = AKU.GARANTI
B.append(dict(no="20", ust=L("SATIŞ SONRASI", "AFTER-SALES", "ПОСЛЕПРОДАЖНОЕ ОБСЛУЖИВАНИЕ"),
  baslik=L("Garanti ve iletişim", "Warranty and contact", "Гарантия и контакты"), ozel="garanti"))
