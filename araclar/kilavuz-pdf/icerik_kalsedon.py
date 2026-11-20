# -*- coding: utf-8 -*-
"""Kalsedon kullanım kılavuzu — içerik (TR ana kaynak; EN ve RU çeviri).
Kaynaklar:
  - Kalsedon Serisi Kazan Kullanım & Bakım Kılavuzu 2018-R.2 (işletme, bakım, arıza, pano cihazları, çalıştırma senaryosu)
  - Kalsedon Otomasyon Panosu Kullanım Kılavuzu (PLC, opsiyonel)
  - "KALSEDON SERİSİ" broşürü 2026, s.4 Modül H tablosu (modeller, ölçü, ağırlık, çaplar, basınç, sıcaklık)
  - KALS 1500–3500 model föyleri (2023): yakıt tüketimi
Su kalitesi bölümü Akuamarin kılavuzu ile, güvenli çalışma bölümü Turkuaz kılavuzu ile aynıdır."""
import icerik as AKU
import icerik_turkuaz as TRK

def L(tr, en, ru):
    return {"tr": tr, "en": en, "ru": ru}

def bolum(kaynak, no):
    return [b for b in kaynak.B if b["no"] == no][0]

BELGE = {
    "kod": L("ENP-KLS-TR", "ENP-KLS-EN", "ENP-KLS-RU"),
    "rev": "R01",
    "tarih": "20.11.2026",
    "dil": L("Türkçe", "English", "Русский"),
    "baslik": L("Kalsedon Serisi Kömür Yakıtlı Sıcak Su Kazanları – Kullanım Kılavuzu",
                "Kalsedon Series Coal-Fired Hot Water Boilers – User Manual",
                "Водогрейные угольные котлы серии Kalsedon – Руководство по эксплуатации"),
    "altbilgi": L("ENORPA · Kalsedon Serisi Sıcak Su Kazanları · Kullanım Kılavuzu",
                  "ENORPA · Kalsedon Series Hot Water Boilers · User Manual",
                  "ENORPA · Водогрейные котлы серии Kalsedon · Руководство по эксплуатации"),
}

KAPAK = {
    "ust": L("KULLANIM KILAVUZU", "USER MANUAL", "РУКОВОДСТВО ПО ЭКСПЛУАТАЦИИ"),
    "baslik": L("Kalsedon Serisi<br>Sıcak Su Kazanları", "Kalsedon Series<br>Hot Water Boilers",
                "Водогрейные котлы<br>серии Kalsedon"),
    "alt": L("Montaj · Devreye alma · İşletme · Bakım",
             "Installation · Commissioning · Operation · Maintenance",
             "Монтаж · Ввод в эксплуатацию · Эксплуатация · Обслуживание"),
    "hap": [L("1.500.000 – 3.500.000 kcal/h", "1,500,000 – 3,500,000 kcal/h", "1 500 000 – 3 500 000 ккал/ч"),
            L("kömür · çift ocak", "coal · twin furnace", "уголь · две топки"),
            L("3 geçişli", "3-pass", "3-ходовой")],
    "not": TRK.KAPAK["not"],
}

ICINDEKILER = {
    "ust": L("İÇİNDEKİLER", "CONTENTS", "СОДЕРЖАНИЕ"),
    "baslik": L("Bölümler", "Sections", "Разделы"),
    "hizli_b": L("HIZLI ERİŞİM", "QUICK ACCESS", "БЫСТРЫЙ ДОСТУП"),
    "hizli": L("Acil durum adımları bölüm 02'de, pano ve emniyet cihazları bölüm 11'de, ilk yakma bölüm 12'de, bakım aralıkları bölüm 14'te, teknik tablolar bölüm 17 ve 18'dedir.",
               "Emergency steps are in section 02, the control panel and safety devices in section 11, first firing in section 12, maintenance intervals in section 14 and technical tables in sections 17 and 18.",
               "Действия в аварийной ситуации — в разделе 02, щит управления и защитные устройства — в разделе 11, первый розжиг — в разделе 12, периодичность обслуживания — в разделе 14, технические таблицы — в разделах 17 и 18."),
}

T = dict(AKU.T)
SINIRLAR = TRK.SINIRLAR   # broşür s.4: 3 / 3,45 / 5,5 bar, 55–110 °C — Kalsedon ile aynı

# Model no, kcal/h, genişlik, uzunluk, yükseklik, ağırlık — broşür s.4
MODELLER = [(15, 1500000, 2400, 6720, 2600, 9570), (17, 1750000, 2400, 6950, 2600, 10265),
            (20, 2000000, 2400, 7100, 2550, 10725), (25, 2500000, 2400, 7350, 2600, 12985),
            (30, 3000000, 2400, 8350, 2600, 15800), (35, 3500000, 2400, 8890, 2600, 16280)]
# Model no, su gidiş–dönüş, genleşme, şönt — broşür s.4
BAGLANTI = [(15, "DN150", "DN65", "DN50"), (17, "DN150", "DN65", "DN65"), (20, "DN150", "DN80", "DN65"),
            (25, "DN150", "DN80", "DN65"), (30, "DN150", "DN100", "DN65"), (35, "DN200", "DN125", "DN80")]
# Model (kcal/h), maks. ve ortalama yakıt tüketimi kg/h — KALS föyleri 2023 (KL17 için föy yok)
TUKETIM = [(15, "400", "208"), (20, "535", "278,2"), (25, "670", "348,4"), (30, "800", "416"), (35, "935", "486,2")]

B = []

# ---------------------------------------------------------------- 01
B.append(dict(no="01", ust=L("BAŞLAMADAN ÖNCE", "BEFORE YOU START", "ПЕРЕД НАЧАЛОМ РАБОТЫ"),
  baslik=L("Kapsam ve belge sırası", "Scope and order of documents", "Область применения и порядок документов"),
  bloklar=[
    ("p", L("Bu kılavuz, ENORPA Kalsedon serisi kömür yakıtlı, üç geçişli, çift ocaklı (çift külhanlı), stokerli sıcak su kazanlarının KL15 – KL35 modelleri (1.500.000 – 3.500.000 kcal/h) için hazırlanmıştır. Kazanın, kamyon ve kazan bunkerlerinin, helezonların, fanların, multisiklonun ve bacanın montajını, devreye alınmasını, işletilmesini ve bakımını yapan personele yöneliktir. Kalsedon, özellikle sıcak su ile ısıtılan seralar için tasarlanmıştır.",
            "This manual covers the KL15 – KL35 models (1,500,000 – 3,500,000 kcal/h) of the ENORPA Kalsedon series of coal-fired, three-pass, twin-furnace, stoker-fired hot water boilers. It is intended for the personnel who install, commission, operate and maintain the boiler, the truck and boiler bunkers, the screws, the fans, the multicyclone and the chimney. Kalsedon is designed especially for greenhouses heated with hot water.",
            "Настоящее руководство распространяется на модели KL15 – KL35 (1 500 000 – 3 500 000 ккал/ч) водогрейных котлов ENORPA серии Kalsedon: угольных, трёхходовых, с двумя топками и стокерной подачей. Оно предназначено для персонала, выполняющего монтаж, ввод в эксплуатацию, эксплуатацию и обслуживание котла, приёмного и котлового бункеров, шнеков, вентиляторов, мультициклона и дымовой трубы. Kalsedon разработан прежде всего для теплиц с водяным отоплением.")),
    ("h", L("Hangi belge esas alınır?", "Which document takes precedence?", "Какой документ имеет приоритет?")),
    bolum(TRK, "01")["bloklar"][2],
    bolum(TRK, "01")["bloklar"][3],
    ("h", L("Kullanım amacı", "Intended use", "Назначение")),
    ("p", L("Kazan yalnızca kömür yakarak sıcak su üretmek için kullanılır. Etikette yazan basınç ve sıcaklık sınırlarının dışında ve bölüm 09'daki şartları sağlamayan bir yakıtla çalıştırılamaz.",
            "The boiler is used only for producing hot water by burning coal. It must not be operated outside the pressure and temperature limits stated on the label or with a fuel that does not meet the requirements in section 09.",
            "Котёл предназначен только для получения горячей воды при сжигании угля. Эксплуатация за пределами указанных на табличке давления и температуры, а также на топливе, не отвечающем требованиям раздела 09, запрещена.")),
    ("h", L("Bu kılavuzdaki işaretler", "Symbols used in this manual", "Обозначения в руководстве")),
    bolum(TRK, "01")["bloklar"][7],
    bolum(TRK, "01")["bloklar"][8],
  ]))

# ---------------------------------------------------------------- 02 (Turkuaz ile aynı)
_g = bolum(TRK, "02")
B.append(dict(no="02", ust=_g["ust"], baslik=_g["baslik"], bloklar=_g["bloklar"]))

# ---------------------------------------------------------------- 03
B.append(dict(no="03", ust=L("ÜRÜNÜ TANIYIN", "KNOW YOUR PRODUCT", "ЗНАКОМСТВО С ИЗДЕЛИЕМ"),
  baslik=L("Kazanın yapısı ve etiketi", "Boiler design and label", "Конструкция и табличка котла"),
  bloklar=[
    ("yapi",
      L("Kalsedon, iki ayrı yanma odası (ocak) bulunan, üç geçişli bir sıcak su kazanıdır. Kömür bunkerden (1) her ocağa ayrı stoker helezonuyla (2) beslenir ve potada (3) yanar; yanma havasını her ocağın kendi temiz hava fanı verir. Duman gazları duman borularından geçerek ısısını suya bırakır, multisiklonda kurumundan ayrılır ve baca gazı fanıyla bacaya basılır. İki ocak birlikte veya tek ocakla çalıştırılabilir.",
        "Kalsedon is a three-pass hot water boiler with two separate combustion chambers (furnaces). Coal is fed from the bunker (1) to each furnace by its own stoker screw (2) and burns in the retort (3); each furnace has its own fresh air fan for combustion air. The flue gases give up their heat to the water in the fire tubes, are cleaned of soot in the multicyclone and are discharged into the chimney by the flue gas fan. The boiler can run on both furnaces or on one furnace only.",
        "Kalsedon — трёхходовой водогрейный котёл с двумя отдельными топками. Уголь из бункера (1) подаётся в каждую топку собственным шнеком стокера (2) и сгорает в реторте (3); воздух для горения каждой топке подаёт свой дутьевой вентилятор. Дымовые газы отдают тепло воде в дымогарных трубах, очищаются от сажи в мультициклоне и удаляются в трубу дымососом. Котёл может работать на двух топках или на одной."),
      [
        [L("Yakıt", "Fuel", "Топливо"), L("Kömür (bölüm 09)", "Coal (section 09)", "Уголь (раздел 09)")],
        [L("Ocak", "Furnace", "Топка"), L("2 adet; her biri ayrı stoker, redüktör ve fan", "2; each with its own stoker, gear motor and fan", "2; у каждой свой стокер, мотор-редуктор и вентилятор")],
        [L("Gövde sacı", "Shell plates", "Листы корпуса"), L("S235JR, EN 10028-2", "S235JR, EN 10028-2", "S235JR, EN 10028-2")],
        [L("Duman boruları", "Fire tubes", "Дымогарные трубы"), L("P235GH, TS 10217-2, PED", "P235GH, TS 10217-2, PED", "P235GH, TS 10217-2, PED")],
        [L("Uygunluk", "Conformity", "Соответствие"), L("2014/68/EU; TS 12953 · ASME · AD2000 · EN 12953 · GOST", "2014/68/EU; TS 12953 · ASME · AD2000 · EN 12953 · GOST", "2014/68/EU; TS 12953 · ASME · AD2000 · EN 12953 · GOST")],
      ],
      L("Kesit: (1) kazan bunkeri, (2) stoker besleme helezonları, (3) potalar.", "Section: (1) boiler bunker, (2) stoker feed screws, (3) retorts.", "Разрез: (1) бункер котла, (2) шнеки подачи стокеров, (3) реторты.")),
    ("h", L("Etikette bulunan bilgiler", "Information on the label", "Данные на табличке")),
    ("tablo", [L("Alan", "Field", "Поле"), L("Ne için gerekli?", "What is it for?", "Для чего нужно?")], [
      [L("Seri no", "Serial no.", "Серийный №"), L("Servis ve yedek parça başvurularında istenir.", "Required for service and spare part requests.", "Требуется при обращении в сервис и заказе запчастей.")],
      [L("Ürün kodu", "Product code", "Код изделия"), L("Model (örnek: Kalsedon KL30 / Kalsedon 3000).", "Model (example: Kalsedon KL30 / Kalsedon 3000).", "Модель (пример: Kalsedon KL30 / Kalsedon 3000).")],
      [L("Isıl güç", "Heat output", "Тепловая мощность"), L("kcal/h olarak anma kapasitesi.", "Rated output in kcal/h.", "Номинальная мощность в ккал/ч.")],
      [L("Basınçlar", "Pressures", "Давления"), L("İşletme, dizayn ve test basıncı; emniyet ventili ve genleşme sistemi bunlara göre seçilir.", "Operating, design and test pressure; the safety valve and expansion system are selected accordingly.", "Рабочее, расчётное и испытательное давление; по ним подбираются предохранительный клапан и расширительная система.")],
    ], {"kalin1": True}),
    ("h", L("Seri için ortak tasarım sınırları", "Common design limits for the series", "Общие расчётные пределы для серии")),
    ("sinirlar",),
  ]))

# ---------------------------------------------------------------- 04
B.append(dict(no="04", ust=L("ÜRÜNÜ TANIYIN", "KNOW YOUR PRODUCT", "ЗНАКОМСТВО С ИЗДЕЛИЕМ"),
  baslik=L("Sistem bileşenleri", "System components", "Компоненты системы"),
  bloklar=[
    ("ikiresim", ("kalsedon-arka.jpg", L("Kazan bunkeri, iki stoker redüktörü ve temiz hava fanı.", "Boiler bunker, two stoker gear motors and fresh air fan.", "Бункер котла, два мотор-редуктора стокеров и дутьевой вентилятор.")),
                 ("kalsedon-sistem.jpg", L("Sistem: kazan, multisiklon, baca gazı fanı ve baca.", "System: boiler, multicyclone, flue gas fan and chimney.", "Система: котёл, мультициклон, дымосос и дымовая труба."))),
    ("tablo", [L("Bileşen", "Component", "Компонент"), L("Görevi", "Function", "Назначение")], [
      [L("Kamyon bunkeri", "Truck bunker", "Приёмный бункер"), L("Kamyonla gelen kömürün ana stok alanı; kömür buradan yükleme helezonuyla kazan bunkerine taşınır.", "Main store for coal delivered by truck; from here the loading screw carries coal to the boiler bunker.", "Основной склад угля, привозимого самосвалом; отсюда загрузочный шнек подаёт уголь в бункер котла.")],
      [L("Kömür yükleme helezonu", "Coal loading screw", "Загрузочный шнек угля"), L("Kamyon bunkerinden kazan bunkerine kömür taşır (elektrik motoru, redüktör, kaplin, bakım kapakları).", "Carries coal from the truck bunker to the boiler bunker (electric motor, gear unit, coupling, inspection covers).", "Подаёт уголь из приёмного бункера в бункер котла (электродвигатель, редуктор, муфта, лючки).")],
      [L("Kazan bunkeri", "Boiler bunker", "Бункер котла"), L("Kömürü yakılmadan önce stoklar. Üstündeki ızgaralı tel iri parçaların geçmesini önler; yanlarında temizleme kapakları vardır.", "Stores coal before firing. The grid on top stops oversized pieces; there are cleaning covers on the sides.", "Хранит уголь перед сжиганием. Решётка сверху задерживает крупные куски; по бокам — чистящие лючки.")],
      [L("Stoker besleme helezonları", "Stoker feed screws", "Шнеки подачи стокеров"), L("Her ocağa, MCB-9 zaman rölesinde ayarlı besleme / bekleme sürelerine göre kömür besler.", "Feed coal to each furnace according to the feed / pause times set on the MCB-9 timer relay.", "Подают уголь в каждую топку по временам подачи / паузы, установленным на реле времени MCB-9.")],
      [L("Temiz hava fanları", "Fresh air fans", "Дутьевые вентиляторы"), L("Stokere yanma havası verir; debi fan üzerindeki klapeyle ayarlanır.", "Supply combustion air to the stoker; flow is set with the damper on the fan.", "Подают воздух горения на стокер; расход регулируется заслонкой на вентиляторе.")],
      [L("Baca gazı fanı", "Flue gas fan", "Дымосос"), L("Duman gazlarını multisiklon üzerinden emip bacaya basar; debisi bağlantı kanalındaki klapeyle ayarlanır.", "Draws the flue gases through the multicyclone and pushes them into the chimney; flow is set with the damper in the connecting duct.", "Отсасывает дымовые газы через мультициклон и подаёт в трубу; расход регулируется заслонкой в газоходе.")],
      [L("Multisiklon kurum tutucu", "Multicyclone soot separator", "Мультициклон-сажеуловитель"), L("Kurumu baca gazından ayırıp kül haznesinde toplar; kurumun bacadan atılmasını önler.", "Separates soot from the flue gas and collects it in the ash hopper so that it is not discharged from the chimney.", "Отделяет сажу от дымовых газов и собирает её в золосборнике, не допуская выброса через трубу.")],
      [L("Kül boşaltma helezonu", "Ash discharge screw", "Шнек золоудаления"), L("Kazan önündeki kül toplama haznesindeki külü dışarı taşır (pano anahtarı B8).", "Carries ash out of the ash collection hopper in front of the boiler (panel switch B8).", "Выводит золу из золосборника перед котлом (переключатель B8 на щите).")],
    ], {"kalin1": True, "sik": True}),
    ("not", "dikkat", bolum(TRK, "04")["bloklar"][2][2], bolum(TRK, "04")["bloklar"][2][3]),
  ]))

# ---------------------------------------------------------------- 05
_t05 = bolum(TRK, "05")["bloklar"]
B.append(dict(no="05", ust=L("MEKANİK KURULUM", "MECHANICAL INSTALLATION", "МЕХАНИЧЕСКИЙ МОНТАЖ"),
  baslik=L("Teslim alma, taşıma ve depolama", "Receiving, transport and storage", "Приёмка, транспортировка и хранение"),
  bloklar=[
    _t05[0], _t05[1], _t05[2],
    ("madde", [
      L("Kazanı yalnızca üzerindeki kaldırma mapalarından kaldırın. Flanş ağızlarından, kapaklardan, bunkerden veya kaporta saclarından kaldırmayın.", "Lift the boiler only by its lifting lugs. Do not lift it by the flanged nozzles, doors, bunker or cladding sheets.", "Поднимайте котёл только за подъёмные проушины. Не поднимайте за фланцевые патрубки, дверцы, бункер или обшивку."),
      L("Ağırlığı bölüm 17'deki tablodan ve etiketten doğrulayın (KL15: 9570 kg – KL35: 16280 kg); vinç ve sapan kapasitesini buna göre seçin.", "Confirm the weight from the table in section 17 and from the label (KL15: 9570 kg – KL35: 16280 kg); select the crane and sling capacity accordingly.", "Уточните массу по таблице раздела 17 и по табличке (KL15: 9570 кг – KL35: 16280 кг); выбирайте кран и стропы соответствующей грузоподъёмности."),
    ] + _t05[3][1][2:]),
    _t05[4], _t05[5], _t05[6],
  ]))

# ---------------------------------------------------------------- 06
_t06 = bolum(TRK, "06")["bloklar"]
B.append(dict(no="06", ust=L("MEKANİK KURULUM", "MECHANICAL INSTALLATION", "МЕХАНИЧЕСКИЙ МОНТАЖ"),
  baslik=L("Kazan dairesi ve yerleşim", "Boiler room and layout", "Котельная и размещение"),
  bloklar=_t06[:5] + [
    ("h", L("Kamyon bunkeri ve yakıt", "Truck bunker and fuel", "Приёмный бункер и топливо")),
    ("madde", [
      L("Kamyon bunkerine yağmur ve yüzey suyu girmemeli, içinde su birikmemelidir; ıslak kömür tozu çamurlaşıp helezonu kilitler.", "Rain and surface water must not enter the truck bunker and no water may collect in it; wet coal dust turns to sludge and locks the screw.", "В приёмный бункер не должны попадать дождевые и поверхностные воды, вода не должна в нём скапливаться: влажная угольная пыль превращается в шлам и блокирует шнек."),
      L("Kamyon bunkerinin kenar betonlarını kırık ve dökülmeye karşı düzenli kontrol edin.", "Regularly check the concrete edges of the truck bunker for cracks and spalling.", "Регулярно проверяйте бетонные кромки приёмного бункера на трещины и выкрашивание."),
      L("Kazan dairesinde kömürü yalnızca kazan bunkerinde bulundurun; yangın söndürücü ve kül için metal kap hazır tutun.", "In the boiler room keep coal only in the boiler bunker; keep a fire extinguisher and a metal ash container ready.", "В котельной храните уголь только в бункере котла; держите наготове огнетушитель и металлическую ёмкость для золы."),
    ]),
    ("not", "dikkat", L("ELEKTRİK BAĞLANTISI", "ELECTRICAL CONNECTION", "ЭЛЕКТРОПОДКЛЮЧЕНИЕ"),
      L("Pano, motorlar ve fanlar uzman elektrikçi tarafından elektrik projesine göre bağlanır ve topraklanır. Besleme kablosu kesiti modele uygun olmalıdır (Kalsedon 3500 için en az 4×10 mm²). Kazan dairesi ana hat ve güç kabloları müşteriye aittir.",
        "The panel, motors and fans must be connected and earthed by a qualified electrician according to the electrical design. The supply cable cross-section must suit the model (at least 4×10 mm² for Kalsedon 3500). The boiler room main line and power cables are the customer's responsibility.",
        "Щит, двигатели и вентиляторы подключаются и заземляются квалифицированным электриком по электрическому проекту. Сечение питающего кабеля должно соответствовать модели (для Kalsedon 3500 — не менее 4×10 мм²). Главная линия и силовые кабели котельной — за счёт заказчика.")),
  ]))

# ---------------------------------------------------------------- 07
_t07 = bolum(TRK, "07")["bloklar"]
def _yer(d, a, b):
    return {k: v.replace(a[k], b[k]) for k, v in d.items()}
_p07 = _yer(_t07[1][1], {"tr": "bölüm 17", "en": "section 17", "ru": "разделе 17"}, {"tr": "bölüm 18", "en": "section 18", "ru": "разделе 18"})
B.append(dict(no="07", ust=L("TESİSAT BAĞLANTISI", "PIPEWORK", "ПОДКЛЮЧЕНИЕ К СИСТЕМЕ"),
  baslik=L("Su bağlantıları", "Water connections", "Водяные подключения"),
  bloklar=[
    _t07[0], ("p", _p07), _t07[2], _t07[3],
    ("kucuk", L("PLC otomasyonlu sistemlerde dönüş suyu sıcaklığına göre kelebek vana kademeli açılarak kazanın terlemesi önlenir (pano kılavuzunda “terleme sistemi”).",
                "In systems with PLC automation, a butterfly valve opens step by step according to the return water temperature to prevent condensation in the boiler (the “condensation protection” in the panel manual).",
                "В системах с ПЛК дисковый затвор открывается ступенчато в зависимости от температуры обратки, предотвращая конденсацию в котле («система защиты от конденсации» в руководстве щита).")),
    _t07[4], _t07[5], _t07[6], _t07[7],
  ]))

# ---------------------------------------------------------------- 08
B.append(dict(no="08", ust=L("TESİSAT BAĞLANTISI", "PIPEWORK", "ПОДКЛЮЧЕНИЕ К СИСТЕМЕ"),
  baslik=L("Baca, multisiklon ve fanlar", "Chimney, multicyclone and fans", "Дымовая труба, мультициклон и вентиляторы"),
  bloklar=[
    ("h", L("Duman yolu", "Flue gas path", "Тракт дымовых газов")),
    ("p", L("Duman gazı sırasıyla kazan çıkışı → multisiklon → baca gazı fanı → baca yolunu izler. Kanallar, kapaklar ve flanşlar sızdırmaz olmalıdır; hava emişi multisiklonun verimini ve çekişi düşürür. Kapak fitillerini ve flanş altı silikonlarını kontrol edip gerektiğinde yenileyin.",
            "The flue gas passes in this order: boiler outlet → multicyclone → flue gas fan → chimney. Ducts, covers and flanges must be gas-tight; air ingress reduces the multicyclone efficiency and the draught. Check the cover seals and the silicone under the flanges and renew them when necessary.",
            "Дымовые газы проходят в порядке: выход котла → мультициклон → дымосос → дымовая труба. Газоходы, лючки и фланцы должны быть герметичными: подсос воздуха снижает эффективность мультициклона и тягу. Проверяйте уплотнения лючков и силикон под фланцами и при необходимости заменяйте.")),
    ("h", L("Baca", "Chimney", "Дымовая труба")),
    bolum(TRK, "08")["bloklar"][3],
    ("h", L("Multisiklon", "Multicyclone", "Мультициклон")),
    ("madde", [
      L("Kül alma kapağı, kül alındıktan sonra kapatılır ve kazan çalışırken kesinlikle kapalı tutulur.", "The ash removal cover is closed after the ash has been removed and must be kept closed while the boiler is running.", "Лючок золоудаления закрывается после удаления золы и во время работы котла должен быть закрыт."),
      L("Multisiklonu terazide ve sağlam zemine kurun; kül haznesine ve üst hazne temizleme kapağına erişim bırakın.", "Install the multicyclone level on a firm base; leave access to the ash hopper and the upper chamber cleaning cover.", "Устанавливайте мультициклон горизонтально на прочное основание; оставьте доступ к золосборнику и лючку верхней камеры."),
    ]),
    ("h", L("Fanlar ve klapeler", "Fans and dampers", "Вентиляторы и заслонки")),
    ("madde", [
      L("Fan dönüş yönü gövdedeki oka uygun olmalıdır; ilk çalıştırmada her fanın yönünü kontrol edin.", "The fan direction of rotation must match the arrow on the housing; check each fan at the first start.", "Направление вращения вентиляторов должно соответствовать стрелке на корпусе; проверьте каждый вентилятор при первом пуске."),
      L("Temiz hava fanlarının klapesi gerekli yanma havasını, baca gazı kanalındaki klape uygun emiş debisini sağlayacak konumda ayarlanır. Ocak üzerindeki deliklerden hava geldiğinden emin olun.", "The fresh air fan dampers are set to give the required combustion air, and the damper in the flue gas duct to give the correct extraction flow. Make sure air comes out of the holes in the furnace.", "Заслонки дутьевых вентиляторов устанавливаются на необходимый расход воздуха горения, заслонка в газоходе — на нужный расход отсоса. Убедитесь, что воздух выходит из отверстий в топке."),
    ]),
    ("not", "tehlike", bolum(TRK, "08")["bloklar"][-1][2],
      L("Baca gazı fanı durmuşken ocak basınç altına girer ve duman kazan dairesine yayılır. Pano, baca gazı fanı çalışmadan temiz hava fanlarının çalışmasına izin vermez ve baca gazı fanı devre dışı bırakılamaz; bu kilitlemeleri iptal etmeyin.",
        "If the flue gas fan stops, the furnace becomes pressurised and smoke spreads into the boiler room. The panel does not allow the fresh air fans to run without the flue gas fan, and the flue gas fan cannot be disabled; never bypass these interlocks.",
        "При остановленном дымососе в топке возникает избыточное давление, и дым распространяется в котельную. Щит не допускает работы дутьевых вентиляторов без дымососа, а дымосос нельзя вывести из работы; не обходите эти блокировки.")),
  ]))

# ---------------------------------------------------------------- 09
B.append(dict(no="09", ust=L("YAKMA SİSTEMİ", "FIRING SYSTEM", "ТОПОЧНАЯ СИСТЕМА"),
  baslik=L("Kömür ve kömür besleme", "Coal and coal feed", "Уголь и подача угля"),
  bloklar=[
    ("p", L("Kalsedon kazanları kömürle çalışacak şekilde tasarlanmıştır. Besleme ve hava ayarları kullanılan kömüre göre yapılır; kömür cinsi değişirse ayarlar yeniden yapılmalıdır.",
            "Kalsedon boilers are designed to run on coal. Feed and air settings are made for the coal used; if the coal type changes, the settings must be made again.",
            "Котлы Kalsedon рассчитаны на работу на угле. Настройки подачи и воздуха выполняются под используемый уголь; при смене угля их нужно выполнить заново.")),
    ("tablo", [L("Özellik", "Property", "Свойство"), L("Şart", "Requirement", "Требование")], [
      [L("Tane boyutu", "Particle size", "Размер кусков"), L("Kazanda 10 – 50 mm. Kamyon bunkerine dökülen kömür en az 10 mm, en fazla 55 mm olmalı; iri kömür redüktör ve kaplinleri zorlar, kırar.", "10 – 50 mm in the boiler. Coal tipped into the truck bunker must be at least 10 mm and at most 55 mm; oversized coal overloads and breaks gear units and couplings.", "В котле 10 – 50 мм. Уголь, засыпаемый в приёмный бункер, — не менее 10 и не более 55 мм; крупный уголь перегружает и ломает редукторы и муфты.")],
      [L("Isıl değer", "Calorific value", "Теплота сгорания"), L("6.000 – 7.000 kcal/kg", "6,000 – 7,000 kcal/kg", "6 000 – 7 000 ккал/кг")],
      [L("Nem", "Moisture", "Влажность"), L("Nemli ve ıslak kömür kesinlikle kullanılmaz. Kömür tozu nemle birleşip çamur tabakası oluşturur ve helezonları durdurur.", "Damp or wet coal must never be used. Coal dust mixes with moisture into a sludge layer that stops the screws.", "Влажный и мокрый уголь использовать запрещено. Угольная пыль с влагой образует шлам, который останавливает шнеки.")],
      [L("Yabancı madde", "Foreign matter", "Посторонние примеси"), L("Odun, taş, demir parçası vb. olmamalı.", "No wood, stones, pieces of iron, etc.", "Без дерева, камней, кусков железа и т. п.")],
    ], {"kalin1": True}),
    ("h", L("Kazan bunkeri", "Boiler bunker", "Бункер котла")),
    ("madde", [
      L("Kazan çalışırken bunker kesinlikle kömürsüz kalmamalıdır; seviyeyi sık kontrol edin. PLC'li sistemde bunker belirlenen sürede dolmazsa alarm verir.", "While the boiler is running, the bunker must never run out of coal; check the level often. With PLC, an alarm sounds if the bunker does not fill within the set time.", "Во время работы котла бункер ни в коем случае не должен оставаться без угля; часто проверяйте уровень. В системе с ПЛК подаётся сигнал, если бункер не заполнился за заданное время."),
      L("Izgaralı tel üzerinde çok kömür birikiyorsa yüklenen kömür uygun boyutta değildir. Izgara deforme olursa onarın veya yenileyin; sökmeyin.", "If a lot of coal collects on the grid, the coal loaded is not the right size. Repair or replace a deformed grid; never remove it.", "Если на решётке скапливается много угля, его размер не подходит. Деформированную решётку отремонтируйте или замените; не снимайте её."),
    ]),
    ("not", "dikkat", L("STOKER KÖMÜRSÜZ KALMAMALI", "THE STOKER MUST NOT RUN OUT OF COAL", "СТОКЕР НЕ ДОЛЖЕН ОСТАВАТЬСЯ БЕЗ УГЛЯ"),
      L("Kömür yüklemesi düzgün yapılmazsa stoker haznesi kömürsüz kalır; bu, stokerin ve stoker helezonunun yanmasına ve eğilmesine, yüksek onarım masraflarına yol açar. Yakım sırasında stoker üzerindeki kömür yüksekliğini ve pota üzerindeki dağılımı sürekli izleyin.",
        "If coal loading is not done properly, the stoker chamber runs empty; this burns and bends the stoker and its screw and causes high repair costs. During firing, keep watching the coal height on the stoker and its distribution on the retort.",
        "При неправильной загрузке угля камера стокера опустеет; это приводит к прогоранию и изгибу стокера и его шнека и к дорогому ремонту. Во время работы постоянно следите за высотой угля на стокере и его распределением на реторте.")),
    ("h", L("Besleme süreleri", "Feed times", "Время подачи")),
    ("p", L("Stoker redüktörlerinin besleme ve bekleme süreleri MCB-9 zaman rölesinde (PLC'li sistemde ayarlar sayfasında) ayarlanır. Bu değerlerin oynanması az veya fazla beslemeye, kazanın sönmesine ve aşırı duman çıkışına yol açar; kazanınıza uygun süreler için ENORPA ile görüşün.",
            "The feed and pause times of the stoker gear motors are set on the MCB-9 timer relay (on the settings page with PLC). Changing these values leads to under- or over-feeding, the fire going out and heavy smoke; contact ENORPA for the times suitable for your boiler.",
            "Время подачи и паузы мотор-редукторов стокеров задаётся на реле времени MCB-9 (в системе с ПЛК — на странице настроек). Изменение этих значений приводит к недостаточной или избыточной подаче, затуханию котла и сильному дымлению; для подходящих значений обратитесь в ENORPA.")),
    ("not", "tehlike", bolum(TRK, "09")["bloklar"][-1][2], bolum(TRK, "09")["bloklar"][-1][3]),
  ]))

# ---------------------------------------------------------------- 10 (Akuamarin ile aynı)
_su = bolum(AKU, "10")
B.append(dict(no="10", ust=_su["ust"], baslik=_su["baslik"], bloklar=_su["bloklar"]))

# ---------------------------------------------------------------- 11
B.append(dict(no="11", ust=L("KONTROL PANOSU", "CONTROL PANEL", "ЩИТ УПРАВЛЕНИЯ"),
  baslik=L("Pano ve emniyet cihazları", "Panel and safety devices", "Щит и защитные устройства"),
  bloklar=[
    ("tablo", [L("Cihaz", "Device", "Устройство"), L("Görevi ve kontrolü", "Function and check", "Назначение и проверка")], [
      [L("T1 sıcaklık kontrol cihazı", "T1 temperature controller", "Регулятор температуры T1"), L("İstenen kazan suyu sıcaklığı buradan set edilir (50 – 85 °C); kazan bu değere göre otomatik çalışır.", "The required boiler water temperature is set here (50 – 85 °C); the boiler runs automatically to this value.", "Здесь задаётся требуемая температура воды котла (50 – 85 °C); котёл работает автоматически по этому значению.")],
      [L("Limit (emniyet) termostatı", "Limit (safety) thermostat", "Предохранительный термостат"), L("Kazan suyu sıcaklığını mekanik olarak denetler; aşıldığında kazanı elektriksel olarak devre dışı bırakır. En fazla 90 °C'ye ayarlanır ve T1 set değerinin üzerinde olmalıdır.", "Monitors the boiler water temperature mechanically and switches the boiler off electrically if it is exceeded. Set to at most 90 °C and above the T1 set point.", "Механически контролирует температуру воды и при превышении электрически отключает котёл. Настраивается не выше 90 °C и выше уставки T1.")],
      [L("MKC-06 faz koruma rölesi", "MKC-06 phase protection relay", "Реле контроля фаз MKC-06"), L("“ON” ve “OUT” ledleri yanıyorsa fazlar normaldir. Yanmıyorsa şebeke voltajını ve faz sırasını kontrol edin. Ayarları yalnızca teknik servis değiştirir.", "If the “ON” and “OUT” LEDs are lit, the phases are normal. If not, check the mains voltage and phase sequence. Only service may change its settings.", "Если светятся светодиоды «ON» и «OUT», фазы в норме. Если нет — проверьте напряжение сети и порядок фаз. Настройки меняет только сервис.")],
      [L("SSRC04 sıvı seviye rölesi", "SSRC04 liquid level relay", "Реле уровня SSRC04"), L("Su kritik seviyeye inerse kazanı durdurur ve çalışmasına izin vermez. “OUT” ledi yanmıyorsa su seviyesini ve tesisatı kaçağa karşı kontrol edip su besleyin.", "Stops the boiler and prevents it from running if the water falls to a critical level. If the “OUT” LED is off, check the water level and the system for leaks and top up.", "Останавливает котёл и блокирует его работу при критическом снижении уровня воды. Если светодиод «OUT» не горит, проверьте уровень воды и систему на утечки и подпитайте.")],
      [L("MCB-9 zaman rölesi", "MCB-9 timer relay", "Реле времени MCB-9"), L("Stokerlerin besleme ve bekleme sürelerini belirler (bölüm 09).", "Sets the stoker feed and pause times (section 09).", "Задаёт время подачи и паузы стокеров (раздел 09).")],
      [L("220 V priz", "220 V socket", "Розетка 220 В"), L("Yalnızca bakım amaçlıdır; başka amaçla kullanılmaz.", "For maintenance only; not to be used for other purposes.", "Только для обслуживания; для других целей не использовать.")],
    ], {"kalin1": True}),
    ("not", "tehlike", L("EMNİYET CİHAZLARINI DEVRE DIŞI BIRAKMAYIN", "NEVER DISABLE THE SAFETY DEVICES", "НЕ ОТКЛЮЧАЙТЕ ЗАЩИТНЫЕ УСТРОЙСТВА"),
      L("Emniyet termostatı veya sıvı seviye elektrodu hata verirken sistem başlatılamaz; motorların manuel çalışması da engellenir. Bu cihazları köprülemeyin, ayarlarını yükseltmeyin.",
        "While the safety thermostat or the liquid level electrode reports a fault, the system cannot be started and even manual motor operation is blocked. Never bridge these devices or raise their settings.",
        "Пока предохранительный термостат или электрод уровня сигнализируют ошибку, систему нельзя запустить, ручной пуск двигателей также заблокирован. Не шунтируйте эти устройства и не повышайте их уставки.")),
    ("h", L("PLC otomasyon (opsiyonel)", "PLC automation (optional)", "Автоматика на ПЛК (опция)")),
    ("madde", [
      L("Kazan set sıcaklığına ulaşınca uykuya geçer; sıcaklık ayarlanan değer kadar düşünce yeniden yanar.", "The boiler goes to sleep when it reaches the set temperature and fires again when the temperature has dropped by the set amount.", "По достижении заданной температуры котёл переходит в режим ожидания и снова включается после снижения температуры на заданную величину."),
      L("Arızalanan motor otomatik olarak pasife alınır; baca gazı fanı dışındaki bir arızada kazan diğer ocakla çalışmaya devam eder.", "A failed motor is automatically taken out of service; for any fault other than the flue gas fan, the boiler continues on the other furnace.", "Неисправный двигатель автоматически выводится из работы; при любой неисправности, кроме дымососа, котёл продолжает работу на другой топке."),
      L("Çalışma süreleri, arıza geçmişi, sıcaklık kayıtları ve yaklaşık kömür tüketimi raporlanır; elektrik kesintisinde alarm verilir. Alarm “arıza resetle” ile susturulur, ancak arıza giderilmeden kaybolmaz.", "Operating times, fault history, temperature records and approximate coal consumption are reported; an alarm is given on power failure. The alarm is silenced with “reset fault”, but the fault itself remains until it is cleared.", "Регистрируются время работы, история неисправностей, температуры и примерный расход угля; при отключении питания подаётся сигнал. Сигнал заглушается кнопкой сброса, но неисправность сохраняется до устранения."),
    ]),
  ]))

# ---------------------------------------------------------------- 12
B.append(dict(no="12", ust=L("KONTROLLÜ İLK ÇALIŞTIRMA", "CONTROLLED FIRST START-UP", "КОНТРОЛИРУЕМЫЙ ПЕРВЫЙ ПУСК"),
  baslik=L("Devreye alma ve kazanın yakılması", "Commissioning and firing the boiler", "Ввод в эксплуатацию и розжиг котла"),
  bloklar=[
    ("not", "dikkat", bolum(TRK, "11")["bloklar"][0][2], bolum(TRK, "11")["bloklar"][0][3]),
    ("p", L("İlk devreye almadan önce bölüm 19'daki formun kontrol satırlarını tamamlayın. Bütün helezon ve fanların dönüş yönlerinin doğru olduğundan emin olun. Standart panoda kazan şu sırayla yakılır:",
            "Before the first commissioning, complete the check rows of the form in section 19. Make sure all screws and fans turn in the right direction. On the standard panel the boiler is fired in this order:",
            "Перед первым вводом заполните контрольные строки протокола в разделе 19. Убедитесь, что все шнеки и вентиляторы вращаются в правильном направлении. На стандартном щите розжиг выполняется в следующем порядке:")),
    ("adim", [
      L("B1 acil stop basılı olmamalı; H1-H2-H3 faz ışıkları ve MKC-06 “ON / OUT” ledleri yanmalıdır.", "B1 emergency stop must not be pressed; the H1-H2-H3 phase lamps and the MKC-06 “ON / OUT” LEDs must be lit.", "Аварийная кнопка B1 не нажата; горят фазные лампы H1-H2-H3 и светодиоды «ON / OUT» реле MKC-06."),
      L("Kazan suyu tam olmalı (SSRC04 “OUT” ledi yanar).", "The boiler must be full of water (SSRC04 “OUT” LED lit).", "Котёл полностью заполнен водой (горит «OUT» реле SSRC04)."),
      L("T1 cihazından su sıcaklığını 50 – 85 °C arasında istenen değere ayarlayın; limit termostatının bunun üzerinde olduğunu kontrol edin.", "Set the water temperature on T1 to the required value between 50 and 85 °C; check that the limit thermostat is set above it.", "Установите на T1 требуемую температуру воды в пределах 50 – 85 °C; убедитесь, что предохранительный термостат настроен выше."),
      L("Kamyon bunkeri doluysa B7 ile kazan bunkerini doldurun; yeterli seviyede B7'yi kapatın.", "If the truck bunker is full, fill the boiler bunker with B7; switch B7 off at a sufficient level.", "Если приёмный бункер заполнен, заполните бункер котла переключателем B7; при достаточном уровне выключите B7."),
      L("B4 ve B6 manuel besleme butonlarıyla Ocak-1 ve Ocak-2'yi uygun seviyeye kadar kömürle doldurun. İlk yakmada pota üzerine 10 – 15 cm kömür yığın.", "Fill Furnace 1 and Furnace 2 with coal to a suitable level with the B4 and B6 manual feed buttons. For the first firing, heap 10 – 15 cm of coal on the retort.", "Кнопками ручной подачи B4 и B6 заполните углём Топку 1 и Топку 2 до нужного уровня. При первом розжиге насыпьте на реторту слой угля 10 – 15 см."),
      L("Uygun bir tutuşturucu ile kömürü tutuşturun ve B2 ile baca gazı fanını çalıştırın.", "Light the coal with a suitable fire starter and start the flue gas fan with B2.", "Разожгите уголь подходящим растопочным средством и включите дымосос кнопкой B2."),
      L("Ocak-1 için B3, Ocak-2 için B5 anahtarını açın (tek ocak isteniyorsa yalnız onunkini). Sistem ayarlı besleme / bekleme sürelerine göre otomatik çalışır ve set sıcaklıkta beklemeye geçer.", "Switch on B3 for Furnace 1 and B5 for Furnace 2 (only the one required if a single furnace is used). The system runs automatically with the set feed / pause times and goes to standby at the set temperature.", "Включите B3 для Топки 1 и B5 для Топки 2 (при работе на одной топке — только её). Система работает автоматически по заданным временам подачи / паузы и переходит в ожидание при заданной температуре."),
    ]),
    ("not", "bilgi", L("PLC'Lİ SİSTEMDE", "WITH PLC AUTOMATION", "В СИСТЕМЕ С ПЛК"),
      L("Stokerler kazan kontrol sayfasındaki manuel butonlarla beslenir; temiz hava fanı butonları, baca gazı fanı manuel çalıştırılmadan görünmez. Yanma yeni kömür besleyebilecek seviyeye gelince start butonuna basılır; sistem bunkeri de otomatik doldurur.",
        "The stokers are fed with the manual buttons on the boiler control page; the fresh air fan buttons only appear after the flue gas fan has been started manually. When the fire is able to take new coal, press start; the system also fills the bunker automatically.",
        "Стокеры подают уголь ручными кнопками на странице управления котлом; кнопки дутьевых вентиляторов появляются только после ручного пуска дымососа. Когда горение способно принять новый уголь, нажмите «Пуск»; система также автоматически заполняет бункер.")),
    ("kucuk", L("Yanma ayarını (besleme süreleri, klapeler; O₂, CO ve baca gazı sıcaklığı ölçümü) yetkili servis yapar ve sonuçları bölüm 19'daki forma işler. İlk 50 çalışma saatinden sonra kapak cıvatalarını, flanş ve kanal bağlantılarını ve redüktör yağlarını kontrol edin.",
                "The combustion setting (feed times, dampers; measurement of O₂, CO and flue gas temperature) is made by authorised service and recorded in the form in section 19. After the first 50 operating hours, check the door bolts, flange and duct joints and gear unit oil.",
                "Наладку горения (время подачи, заслонки; измерение O₂, CO и температуры газов) выполняет уполномоченный сервис с записью в протокол раздела 19. После первых 50 часов работы проверьте болты дверец, фланцевые соединения, газоходы и масло редукторов.")),
  ]))

# ---------------------------------------------------------------- 13
_t12 = bolum(TRK, "12")["bloklar"]
B.append(dict(no="13", ust=L("GÜNLÜK KULLANIM", "DAILY USE", "ЕЖЕДНЕВНАЯ ЭКСПЛУАТАЦИЯ"),
  baslik=L("İşletme ve durdurma", "Operation and shutdown", "Эксплуатация и останов"),
  bloklar=[
    _t12[0], _t12[1],
    ("h", L("Durdurma ve kül alma", "Shutdown and ash removal", "Останов и удаление золы")),
    ("adim", [
      L("Kazanı durdurmak için B2'yi kapatın (PLC'de stop). Sirkülasyon pompası, ocaktaki kömür bitip kazan suyu soğuyana kadar çalışmaya devam etmelidir.", "To stop the boiler, switch off B2 (stop on the PLC). The circulation pump must keep running until the coal in the furnace has burnt out and the boiler water has cooled.", "Для останова выключите B2 (на ПЛК — «Стоп»). Циркуляционный насос должен работать до выгорания угля в топке и остывания воды."),
      L("Ateş söndükten sonra kazan kapağından gelberiyle çekilen külü kül toplama haznesine alın.", "After the fire is out, rake the ash out through the boiler door with the ash rake into the ash collection hopper.", "После затухания огня выгребите золу кочергой через дверцу котла в золосборник."),
      L("B8 ile kül boşaltma helezonunu çalıştırın; boşaltma bitince B8'i kapatın.", "Run the ash discharge screw with B8; switch B8 off when discharge is complete.", "Включите шнек золоудаления переключателем B8; по окончании выключите B8."),
      L("Kazan sıcakken suyunu boşaltmayın; ısıl şok kazana zarar verir.", "Do not drain the boiler while it is hot; thermal shock damages the boiler.", "Не сливайте воду из горячего котла: тепловой удар повреждает котёл."),
    ]),
    _t12[4], _t12[5], _t12[6],
  ]))

# ---------------------------------------------------------------- 14
B.append(dict(no="14", ust=L("KAYITLI BAKIM PLANI", "RECORDED MAINTENANCE PLAN", "ПЛАН ОБСЛУЖИВАНИЯ С УЧЁТОМ"),
  baslik=L("Periyodik bakım", "Periodic maintenance", "Периодическое обслуживание"),
  bloklar=[
    bolum(TRK, "13")["bloklar"][0],
    ("tablo", [L("Ne zaman?", "When?", "Когда?"), L("Kontrol / işlem", "Check / action", "Проверка / действие")], [
      [L("Her gün", "Every day", "Ежедневно"), L("Bölüm 13'teki günlük kontroller; bunker seviyesi; pota üzerindeki kömür dağılımı; kül alma; multisiklon kül haznesi.", "Daily checks in section 13; bunker level; coal distribution on the retort; ash removal; multicyclone ash hopper.", "Ежедневные проверки раздела 13; уровень бункера; распределение угля на реторте; удаление золы; золосборник мультициклона.")],
      [L("Haftada en az bir kez", "At least once a week", "Не реже раза в неделю"), L("Duman borularının harbiyle temizliği; arka duman sandığı yan kapaklarından kurum alma; pota hava deliklerinin açılması; pota temizleme kapağından toz ve kül alma.", "Cleaning the fire tubes with the tube brush; removing soot through the rear smoke box side covers; clearing the retort air holes; removing dust and ash through the retort cleaning cover.", "Чистка дымогарных труб ёршиком; удаление сажи через боковые лючки задней дымовой камеры; прочистка воздушных отверстий реторты; удаление пыли и золы через лючок реторты.")],
      [L("Ayda en az bir kez", "At least once a month", "Не реже раза в месяц"), L("Cehennemlik temizliği; multisiklon üst hazne ve hücre temizliği; baca gazı fanı kanatlarının kontrol ve temizliği; kamyon bunkeri tabanı ve helezon ağızlarının temizliği; kapak fitilleri.", "Cleaning the rear combustion pass (“hell box”); cleaning the multicyclone upper chamber and cells; checking and cleaning the flue gas fan blades; cleaning the truck bunker floor and screw inlets; door seals.", "Чистка задней поворотной камеры; чистка верхней камеры и ячеек мультициклона; проверка и чистка лопаток дымососа; чистка дна приёмного бункера и входов шнеков; уплотнения дверец.")],
      [L("Altı ayda en az bir kez", "At least every six months", "Не реже раза в полгода"), L("Su tarafının ve tesisatın bakımı; helezonlar, kaplinler ve redüktörlerin aşınma kontrolü; kamyon bunkeri betonları.", "Maintenance of the water side and system; wear check of screws, couplings and gear units; truck bunker concrete.", "Обслуживание водяной стороны и системы; проверка износа шнеков, муфт и редукторов; бетон приёмного бункера.")],
      [L("Yılda bir kez (sezon öncesi)", "Once a year (before the season)", "Раз в год (перед сезоном)"), L("ENORPA bakım ekibiyle genel kontrol; baca temizliği; emniyet termostatı ve seviye rölesinin denenmesi.", "General inspection with the ENORPA maintenance team; chimney sweeping; testing of the safety thermostat and level relay.", "Общая проверка с сервисом ENORPA; чистка трубы; проверка предохранительного термостата и реле уровня.")],
      [L("Üreticisinin belirttiği aralıkta", "At the interval stated by its manufacturer", "С периодичностью по данным изготовителя"), L("Emniyet ventili, fanlar, motorlar, redüktörler ve pompaların kendi bakımları.", "Own maintenance of the safety valve, fans, motors, gear units and pumps.", "Собственное обслуживание предохранительного клапана, вентиляторов, двигателей, редукторов и насосов.")],
    ], {"kalin1": True, "sik": True}),
    bolum(TRK, "13")["bloklar"][2], bolum(TRK, "13")["bloklar"][3], bolum(TRK, "13")["bloklar"][4],
  ]))

# ---------------------------------------------------------------- 15
B.append(dict(no="15", ust=L("KAYITLI BAKIM PLANI", "RECORDED MAINTENANCE PLAN", "ПЛАН ОБСЛУЖИВАНИЯ С УЧЁТОМ"),
  baslik=L("Temizlik", "Cleaning", "Чистка"),
  bloklar=[
    ("not", "dikkat", L("TEMİZLİKTEN ÖNCE", "BEFORE CLEANING", "ПЕРЕД ЧИСТКОЙ"),
      L("Kazanın enerjisini kesin, alevin kendiliğinden sönmesini bekleyin ve kazanın zarar vermeyecek şekilde soğuduğundan emin olun.",
        "Isolate the power, wait for the flame to go out by itself and make sure the boiler has cooled down enough to be safe.",
        "Отключите питание, дождитесь самостоятельного затухания пламени и убедитесь, что котёл остыл до безопасной температуры.")),
    ("h", L("Yanma odası ve pota", "Combustion chamber and retort", "Топка и реторта")),
    ("madde", [
      L("Yanma odası kapağını açın, birikmiş külü gelberiyle kül haznesine çekin; büyük kesekleri çekiçle kül helezonunun taşıyabileceği boyuta kırın.", "Open the combustion chamber door and rake the ash into the ash hopper; break large clinker with a hammer to a size the ash screw can carry.", "Откройте дверцу топки и сгребите золу кочергой в золосборник; крупный шлак разбейте молотком до размера, который возьмёт шнек золоудаления."),
      L("Pota hava deliklerini sık kontrol edin; kömür tozuyla kapanan delikleri şişle açın, aksi halde düzgün yanma olmaz.", "Check the retort air holes often; open holes blocked by coal dust with a poker, otherwise combustion will be poor.", "Часто проверяйте воздушные отверстия реторты; забитые угольной пылью отверстия прочищайте пикой, иначе горение будет плохим."),
      L("Döküm ızgaraların altındaki pota temizleme kapağından potaya dolan toz ve külü sık aralıkla alın.", "Regularly remove the dust and ash that collect in the retort through the retort cleaning cover under the cast grates.", "Регулярно удаляйте пыль и золу из реторты через лючок под чугунными колосниками."),
    ]),
    ("h", L("Duman boruları, duman sandığı ve cehennemlik", "Fire tubes, smoke box and rear pass", "Дымогарные трубы, дымовая камера и задняя камера")),
    ("madde", [
      L("Ön duman sandığı kapaklarını açın, duman borularını uygun tel fırçayla (harbi) temizleyin. Başta sık kontrol edin; sonra kömüre göre, en geç haftada bir tekrarlayın.", "Open the front smoke box doors and clean the fire tubes with a suitable wire tube brush. Check often at first; then repeat according to the coal, at least once a week.", "Откройте дверцы передней дымовой камеры и прочистите дымогарные трубы подходящим ёршиком. Сначала проверяйте часто, затем повторяйте в зависимости от угля, не реже раза в неделю."),
      L("Ardından arka duman sandığının iki yanındaki temizleme kapaklarından dökülen kurumu gelberiyle alın.", "Then remove the soot that has fallen out through the cleaning covers on both sides of the rear smoke box.", "Затем удалите выпавшую сажу через чистящие лючки с обеих сторон задней дымовой камеры."),
      L("Kazanın arkasındaki cehennemlik temizleme kapağından kül ve kurumu temizleyin.", "Clean ash and soot through the rear pass (“hell box”) cleaning cover at the back of the boiler.", "Очистите золу и сажу через лючок задней поворотной камеры на задней стороне котла."),
    ]),
    ("h", L("Multisiklon, fan ve bunkerler", "Multicyclone, fan and bunkers", "Мультициклон, вентилятор и бункеры")),
    ("madde", [
      L("Kül haznesini kül alma kapağından boşaltın; üst hazne temizleme kapağını açıp siklon hücreleri üstündeki tozu temizleyin.", "Empty the ash hopper through the ash removal cover; open the upper chamber cleaning cover and clean the dust above the cyclone cells.", "Опорожните золосборник через лючок; откройте лючок верхней камеры и очистите пыль над ячейками циклона."),
      L("Fan bakım kapağından baca gazı fanı kanatlarını kontrol edin; kirli kanat balansı bozar ve titreşim yapar.", "Check the flue gas fan blades through the fan inspection cover; dirty blades upset the balance and cause vibration.", "Проверьте лопатки дымососа через лючок; загрязнение нарушает балансировку и вызывает вибрацию."),
      L("Kamyon bunkeri tabanındaki kömür tozunu ve helezon giriş ağızlarına sıvanmış tozu temizleyin.", "Clean coal dust from the truck bunker floor and caked dust from the screw inlets.", "Удаляйте угольную пыль со дна приёмного бункера и налипшую пыль на входах шнеков."),
    ]),
    ("kucuk", L("Temizlikten sonra bütün kapakları sızdırmaz şekilde kapatın; fitilleri kontrol edip gerekiyorsa yenileyin. Duman tarafını ve bunkerleri su ile yıkamayın.",
                "After cleaning, close all covers gas-tight; check the seals and renew them if necessary. Do not wash the flue gas side or the bunkers with water.",
                "После чистки плотно закройте все лючки; проверьте уплотнения и при необходимости замените. Не промывайте газовую сторону и бункеры водой.")),
  ]))

# ---------------------------------------------------------------- 16
B.append(dict(no="16", ust=L("BELİRTİDEN KONTROLE", "FROM SYMPTOM TO CHECK", "ОТ ПРИЗНАКА К ПРОВЕРКЕ"),
  baslik=L("Arıza bulma", "Troubleshooting", "Поиск неисправностей"),
  bloklar=[
    bolum(TRK, "15")["bloklar"][0],
    ("tablo", [L("Belirti", "Symptom", "Признак"), L("Kontrol", "Check", "Проверка"), L("Çözüm", "Remedy", "Устранение")], [
      [L("Helezon dönmüyor (yükleme, stoker veya kül)", "Screw does not turn (loading, stoker or ash)", "Шнек не вращается (загрузочный, стокера или золы)"), L("Pano bağlantıları ve manuel çalışma; redüktörde zorlanma, inleme; kaplin; helezonda kırılma veya yabancı cisim.", "Panel connections and manual run; gear unit straining or whining; coupling; broken screw or foreign object.", "Подключение и ручной пуск со щита; перегрузка или вой редуктора; муфта; поломка шнека или посторонний предмет."), L("Sinyal yoksa arızalı devre elemanını değiştirin. Redüktör inleyip dönmüyorsa hemen durdurun, enerjiyi kilitleyip bakım kapaklarından yabancı cismi çıkarın. Kırık kaplin veya helezonu aynısıyla değiştirin.", "If there is no signal, replace the faulty circuit component. If the gear unit whines but does not turn, stop at once, lock out and remove the foreign object through the inspection covers. Replace a broken coupling or screw with an identical one.", "Нет сигнала — замените неисправный элемент схемы. Редуктор воет, но не вращается — немедленно остановите, заблокируйте питание и удалите предмет через лючки. Сломанную муфту или шнек замените аналогичными.")],
      [L("Bunkerde kömür var, stokere gitmiyor", "Coal in bunker but not reaching the stoker", "Уголь в бункере есть, но не идёт к стокеру"), L("Döküş şutunda iri parça veya çamurlaşmış toz; bunker ızgarası.", "Oversized piece or caked dust on the feed chute; bunker grid.", "Крупный кусок или слипшаяся пыль на течке; решётка бункера."), L("Bunker yan temizleme kapaklarından tıkanmayı alın; ızgarayı onarın; ıslak kömür yüklemeyi kesin.", "Clear the blockage through the bunker side cleaning covers; repair the grid; stop loading wet coal.", "Устраните затор через боковые лючки бункера; отремонтируйте решётку; прекратите загрузку мокрого угля.")],
      [L("Stoker helezonu zorlanıyor, kaplin kırık", "Stoker screw strained, coupling broken", "Шнек стокера перегружен, муфта сломана"), L("Bunker tarafında sıkışma; yoksa ön kapaktan stoker deliğinden helezon ucunda deformasyon.", "Jam on the bunker side; if not, deformation at the screw tip seen through the stoker opening from the front door.", "Затор со стороны бункера; если нет — деформация конца шнека, видимая через отверстие стокера из передней дверцы."), L("Sıkışmayı giderin. Uç deforme ise arka redüktörü söküp helezonu çıkarın, onarın veya yenileyin.", "Clear the jam. If the tip is deformed, remove the rear gear unit, pull out the screw and repair or replace it.", "Устраните затор. При деформации конца снимите задний редуктор, извлеките шнек, отремонтируйте или замените.")],
      [L("Kötü yanma, sönme, aşırı duman", "Poor combustion, fire goes out, heavy smoke", "Плохое горение, затухание, сильный дым"), L("Pota hava delikleri; temiz hava fanı yönü ve klapesi; kömür boyutu ve nemi; MCB-9 süreleri.", "Retort air holes; fresh air fan direction and damper; coal size and moisture; MCB-9 times.", "Воздушные отверстия реторты; направление и заслонка дутьевого вентилятора; размер и влажность угля; времена MCB-9."), L("Delikleri açın, fanı ve klapeyi ayarlayın, uygun kömür kullanın; süreler için ENORPA'ya danışın.", "Open the holes, adjust fan and damper, use suitable coal; consult ENORPA about the times.", "Прочистите отверстия, отрегулируйте вентилятор и заслонку, используйте подходящий уголь; по временам — консультация ENORPA.")],
      [L("Fan gürültülü, titreşimli veya dönmüyor", "Fan noisy, vibrating or not turning", "Вентилятор шумит, вибрирует или не вращается"), L("Kanatlarda kurum; yataklar; elektrik bağlantısı.", "Soot on the blades; bearings; electrical connection.", "Сажа на лопатках; подшипники; электроподключение."), L("Kanatları temizleyin; yatak ve bağlantıları servise kontrol ettirin.", "Clean the blades; have bearings and connections checked by service.", "Очистите лопатки; поручите сервису проверку подшипников и подключения.")],
      [L("Kazan çalışmıyor, faz ışıkları / MKC-06 ledleri sönük", "Boiler not running, phase lamps / MKC-06 LEDs off", "Котёл не работает, фазные лампы / светодиоды MKC-06 не горят"), L("Şebeke voltajı, faz sırası, B1 acil stop.", "Mains voltage, phase sequence, B1 emergency stop.", "Напряжение сети, порядок фаз, аварийная кнопка B1."), L("Voltajı ve faz sırasını düzeltin; röle ayarına dokunmayın.", "Correct voltage and phase sequence; do not touch the relay settings.", "Восстановите напряжение и порядок фаз; не трогайте настройки реле.")],
      [L("Kazan durdu, SSRC04 “OUT” sönük", "Boiler stopped, SSRC04 “OUT” off", "Котёл остановлен, «OUT» SSRC04 не горит"), L("Düşük su seviyesi; tesisatta kaçak.", "Low water level; leak in the system.", "Низкий уровень воды; утечка в системе."), L("Kaçağı giderin, soğuk kazana su besleyin.", "Fix the leak and top up the cooled boiler.", "Устраните утечку, подпитайте остывший котёл.")],
      [L("Sıcaklık yükseliyor, emniyet termostatı attı", "Temperature rising, safety thermostat tripped", "Растёт температура, сработал предохранительный термостат"), L("Pompa, vanalar, ısı çekişi, elektrik kesintisi.", "Pump, valves, heat demand, power failure.", "Насос, арматура, теплоотбор, отключение питания."), L("Beslemeyi durdurun, kapakları açmayın; nedeni giderip termostatı soğuyunca resetleyin (bölüm 02).", "Stop the feed, do not open the doors; remove the cause and reset the thermostat once cool (section 02).", "Остановите подачу, не открывайте дверцы; устраните причину и сбросьте термостат после остывания (раздел 02).")],
    ], {"kalin1": True, "sik": True}),
    ("not", "bilgi", bolum(TRK, "15")["bloklar"][-1][2], bolum(TRK, "15")["bloklar"][-1][3]),
  ]))

# ---------------------------------------------------------------- 17–18 teknik
TEKNIK_B = TRK.TEKNIK_B
TEKNIK_NOT = L("Değerler “Kazanların Modül H kapsamına göre teknik özellikleri” tablosundan alınmıştır. Ölçüler kazan gövdesinin dış ölçüleridir; bunkerler, fanlar, multisiklon ve baca dahil değildir. Ağırlık susuz ağırlıktır. Tüm ölçüler bilgilendirme amaçlıdır; siparişe özel onaylı çizimi esas alın.",
               "Values are taken from the table “Technical specifications of boilers according to Module H”. Dimensions are the external dimensions of the boiler body; bunkers, fans, multicyclone and chimney are not included. Weight is the dry weight. All dimensions are for information only; use the approved order-specific drawing.",
               "Значения взяты из таблицы «Технические характеристики котлов по модулю H». Указаны наружные размеры корпуса котла без бункеров, вентиляторов, мультициклона и трубы. Масса указана без воды. Все размеры носят информационный характер; руководствуйтесь утверждённым чертежом по заказу.")
TUKETIM_B = [L("Model", "Model", "Модель"), L("Maks. yakıt tüketimi (kg/h)", "Max. fuel consumption (kg/h)", "Макс. расход топлива (кг/ч)"),
             L("Ortalama yakıt tüketimi (kg/h)", "Average fuel consumption (kg/h)", "Средний расход топлива (кг/ч)")]
TUKETIM_NOT = L("Tüketim değerleri 2023 tarihli model föylerinden alınmıştır (KL17 için föy yoktur). Gerçek tüketim kömürün ısıl değerine, nemine ve ısı ihtiyacına göre değişir.",
                "Consumption values are taken from the 2023 model data sheets (there is no data sheet for KL17). Actual consumption depends on the calorific value and moisture of the coal and on the heat demand.",
                "Значения расхода взяты из листов моделей 2023 г. (для KL17 лист отсутствует). Фактический расход зависит от теплоты сгорания и влажности угля и от тепловой нагрузки.")
BAGLANTI_B = TRK.BAGLANTI_B
BAGLANTI_NOT = L("Su ağızları flanşlıdır. Ağızların sırası ve yeri, baca gazı çıkış ölçüsü, baca ve multisiklon ölçüleri siparişe özel çizimde verilir.",
                 "Water nozzles are flanged. The order and position of the nozzles, the flue gas outlet size and the chimney and multicyclone dimensions are given in the order-specific drawing.",
                 "Водяные патрубки фланцевые. Порядок и расположение патрубков, размер газового выхода, размеры трубы и мультициклона приведены в чертеже по заказу.")
ISLETME_B = TRK.ISLETME_B
ISLETME = TRK.ISLETME + [
    (L("T1 kazan suyu set aralığı", "T1 boiler water set range", "Диапазон уставки T1"), "50 – 85 °C"),
    (L("Emniyet termostatı (en fazla)", "Safety thermostat (maximum)", "Предохранительный термостат (не выше)"), "90 °C"),
]
BAGLANTI_KUTU = (L("TASARIM VE İŞLETME SICAKLIĞI", "DESIGN AND OPERATING TEMPERATURE", "РАСЧЁТНАЯ И РАБОЧАЯ ТЕМПЕРАТУРА"),
                 L("Tablodaki 110 °C kazanın tasarım sınırıdır. Standart panoda emniyet termostatı en fazla 90 °C'ye, kazan suyu 50 – 85 °C arasına ayarlanır. Daha yüksek sıcaklık veya kızgın su istenirse siparişe özel teknik föy esastır.",
                   "The 110 °C in the table is the design limit of the boiler. On the standard panel the safety thermostat is set to at most 90 °C and the boiler water to 50 – 85 °C. If a higher temperature or superheated water is required, the order-specific data sheet applies.",
                   "Значение 110 °C в таблице — расчётный предел котла. На стандартном щите предохранительный термостат настраивается не выше 90 °C, вода котла — на 50 – 85 °C. При необходимости более высокой температуры или перегретой воды действует технический лист по заказу."))

B.append(dict(no="17", ust=L("TEKNİK VERİLER", "TECHNICAL DATA", "ТЕХНИЧЕСКИЕ ДАННЫЕ"),
  baslik=L("Kapasite, ölçü, ağırlık ve tüketim", "Capacity, dimensions, weight and consumption", "Мощность, размеры, масса и расход"), ozel="teknik_kls"))
B.append(dict(no="18", ust=L("TEKNİK VERİLER", "TECHNICAL DATA", "ТЕХНИЧЕСКИЕ ДАННЫЕ"),
  baslik=L("Bağlantı çapları ve işletme değerleri", "Connection sizes and operating values", "Присоединительные размеры и рабочие параметры"), ozel="baglanti_kls"))

# ---------------------------------------------------------------- 19 form
FORM = dict(TRK.FORM)
FORM["kontroller"] = [k for k in TRK.FORM["kontroller"]][:6] + [
    (L("Pompa, fan ve tüm helezon dönüş yönleri; topraklama; faz sırası", "Directions of rotation of pumps, fans and all screws; earthing; phase sequence", "Направление вращения насосов, вентиляторов и всех шнеков; заземление; порядок фаз"), "uygun"),
    (L("Emniyet termostatı (≤ 90 °C) ve SSRC04 seviye rölesi denendi", "Safety thermostat (≤ 90 °C) and SSRC04 level relay tested", "Предохранительный термостат (≤ 90 °C) и реле уровня SSRC04 проверены"), "evet"),
    (L("Kapak cıvataları, fitiller, multisiklon kapakları kontrol edildi", "Door bolts, seals and multicyclone covers checked", "Болты дверец, уплотнения и лючки мультициклона проверены"), "evet"),
]
FORM["olcum_b"] = (L("Ölçüm", "Measurement", "Измерение"), L("Ocak 1", "Furnace 1", "Топка 1"), L("Ocak 2", "Furnace 2", "Топка 2"))
FORM["olcumler"] = [
    L("MCB-9 besleme / bekleme süresi (s)", "MCB-9 feed / pause time (s)", "MCB-9 время подачи / паузы (с)"),
    L("Temiz hava fanı klape konumu", "Fresh air fan damper position", "Положение заслонки дутьевого вентилятора"),
    L("O₂ (%)", "O₂ (%)", "O₂ (%)"), L("CO (ppm)", "CO (ppm)", "CO (ppm)"),
    L("Baca gazı sıcaklığı (°C)", "Flue gas temperature (°C)", "Температура дымовых газов (°C)"),
    L("Yanma odası basıncı (Pa)", "Combustion chamber pressure (Pa)", "Давление в топке (Па)"),
    L("Gidiş / dönüş suyu sıcaklığı (°C)", "Flow / return water temperature (°C)", "Температура подачи / обратки (°C)"),
    L("Sistem basıncı (bar)", "System pressure (bar)", "Давление в системе (бар)")]
B.append(dict(no="19", ust=L("HER KAZAN İÇİN DOLDURUN", "COMPLETE FOR EACH BOILER", "ЗАПОЛНЯЕТСЯ ДЛЯ КАЖДОГО КОТЛА"),
  baslik=L("Devreye alma kayıt formu", "Commissioning record", "Протокол ввода в эксплуатацию"), ozel="form"))

KAYIT = AKU.KAYIT
B.append(dict(no="20", ust=L("SATIŞ SONRASI", "AFTER-SALES", "ПОСЛЕПРОДАЖНОЕ ОБСЛУЖИВАНИЕ"),
  baslik=L("Bakım ve servis kaydı", "Maintenance and service record", "Журнал обслуживания и сервиса"), ozel="kayit"))

GARANTI = AKU.GARANTI
B.append(dict(no="21", ust=L("SATIŞ SONRASI", "AFTER-SALES", "ПОСЛЕПРОДАЖНОЕ ОБСЛУЖИВАНИЕ"),
  baslik=L("Garanti ve iletişim", "Warranty and contact", "Гарантия и контакты"), ozel="garanti"))
