# -*- coding: utf-8 -*-
"""Kalsedon otomasyon panosu kullanım kılavuzu — içerik (TR ana kaynak; EN ve RU çeviri).
Kaynak: "KALSEDON OTOMASYON PANOSU KULLANIM KLAVUZU" (Word, 13 sayfa). İçerik birebir aktarılmış,
ekran görüntülerindeki açıklama kutuları numaralı işaretlere dönüştürülmüştür. Ekran üzerindeki
yazılar (HMI) Türkçedir; EN/RU metinlerde Türkçe buton adı tırnak içinde verilir."""
import icerik as AKU
import icerik_kalsedon as KLS

def L(tr, en, ru):
    return {"tr": tr, "en": en, "ru": ru}

BELGE = {
    "kod": L("ENP-KLS-PANO-TR", "ENP-KLS-PANO-EN", "ENP-KLS-PANO-RU"),
    "rev": "R01",
    "tarih": "24.11.2026",
    "dil": L("Türkçe", "English", "Русский"),
    "baslik": L("Kalsedon Otomasyon Panosu – Kullanım Kılavuzu", "Kalsedon Automation Panel – User Manual",
                "Щит автоматики Kalsedon – Руководство по эксплуатации"),
    "altbilgi": L("ENORPA · Kalsedon Otomasyon Panosu · Kullanım Kılavuzu", "ENORPA · Kalsedon Automation Panel · User Manual",
                  "ENORPA · Щит автоматики Kalsedon · Руководство"),
}
KAPAK = {
    "ust": L("PANO KULLANIM KILAVUZU", "PANEL USER MANUAL", "РУКОВОДСТВО ПО ЩИТУ"),
    "baslik": L("Kalsedon<br>Otomasyon Panosu", "Kalsedon<br>Automation Panel", "Щит автоматики<br>Kalsedon"),
    "alt": L("PLC · Dokunmatik operatör paneli · Kazanın yakılması", "PLC · Touch operator panel · Firing the boiler",
             "ПЛК · Сенсорная панель оператора · Розжиг котла"),
    "hap": [L("Siemens SIMATIC HMI", "Siemens SIMATIC HMI", "Siemens SIMATIC HMI"),
            L("PLC otomasyon", "PLC automation", "автоматика на ПЛК"), L("Kalsedon serisi", "Kalsedon series", "серия Kalsedon")],
    "not": L("Bu kılavuz, Kalsedon kazanı kullanım kılavuzunun (ENP-KLS) ekidir; ikisini birlikte kazan dairesinde saklayın.",
             "This manual is a supplement to the Kalsedon boiler user manual (ENP-KLS); keep both together in the boiler room.",
             "Настоящее руководство является приложением к руководству по эксплуатации котла Kalsedon (ENP-KLS); храните оба документа вместе в котельной."),
}
ICINDEKILER = {
    "ust": L("İÇİNDEKİLER", "CONTENTS", "СОДЕРЖАНИЕ"),
    "baslik": L("Bölümler", "Sections", "Разделы"),
    "hizli_b": L("EKRAN YAZILARI", "SCREEN LABELS", "НАДПИСИ НА ЭКРАНЕ"),
    "hizli": L("Operatör panelindeki yazılar Türkçedir. Ekranlarda numaralı işaretler, her ekranın altındaki tabloda açıklanır. Ekranda F8 fonksiyon tuşu her zaman ana ekrana döndürür.",
               "The labels on the operator panel are in Turkish; in this manual the Turkish label is given in quotes with its meaning. The numbered markers on each screen are explained in the table below it. The F8 function key always returns to the main screen.",
               "Надписи на панели оператора выполнены на турецком языке; в руководстве турецкая надпись приводится в кавычках с переводом. Номера на снимках экранов поясняются в таблице под каждым снимком. Функциональная клавиша F8 всегда возвращает на главный экран."),
}
T = dict(AKU.T)
SINIRLAR = []

def _ek(baslik, aciklama):
    return (baslik, aciklama)

B = []

B.append(dict(no="01", ust=L("EMNİYET", "SAFETY", "БЕЗОПАСНОСТЬ"), baslik=L("Uyarı ve pano", "Warning and panel", "Предупреждение и щит"), ozel="ekran",
  once=[
    ("not", "tehlike", L("UYARI", "WARNING", "ПРЕДУПРЕЖДЕНИЕ"),
      L("Kazanda emniyet ekipmanları olarak emniyet termostatı ve sıvı seviye elektrodu bulunur. Emniyet termostatı maksimum 90 °C'ye ayarlanmış durumdadır. Emniyet termostatı veya sıvı seviye elektrodu PLC'ye hata uyarısı verirken sistem start durumuna geçirilemez. Motorların manuel olarak çalışması bile sistem tarafından engellenir.",
        "The boiler is equipped with a safety thermostat and a liquid level electrode as safety devices. The safety thermostat is set to a maximum of 90 °C. While the safety thermostat or the liquid level electrode is reporting a fault to the PLC, the system cannot be switched to start. Even manual operation of the motors is blocked by the system.",
        "В качестве защитных устройств котёл оснащён предохранительным термостатом и электродом уровня воды. Предохранительный термостат настроен не выше 90 °C. Пока предохранительный термостат или электрод уровня передают в ПЛК сигнал ошибки, систему нельзя перевести в режим «Пуск». Система блокирует даже ручной пуск двигателей.")),
    ("h", L("Otomasyon panosu", "Automation panel", "Щит автоматики")),
    ("p", L("Otomasyon panosu içerisindeki ana sigorta, panoyu ve birinci kazanın ekipmanlarını enerjilendirir. Panoda ayrıca PLC ve modülleri ile start ve çalıştı bilgilerinin alındığı röleler bulunur. Kazan çalıştırılacağında önce ana sigorta kaldırılır. Otomasyon panosu üzerindeki tüm otomatlar kaldırıldığında PLC çalışmaya başlar.",
            "The main fuse in the automation panel energises the panel and the equipment of the first boiler. The panel also contains the PLC and its modules and the relays that provide the start and running signals. To operate the boiler, first switch on the main fuse. When all circuit breakers on the automation panel are switched on, the PLC starts.",
            "Главный автомат в щите автоматики подаёт питание на щит и оборудование первого котла. В щите также находятся ПЛК с модулями и реле, от которых поступают сигналы пуска и работы. Для пуска котла сначала включите главный автомат. После включения всех автоматов на щите ПЛК начинает работу.")),
  ],
  gorsel="pano-foto.jpg", gorsel_dar=True,
  gorsel_alt=L("Kalsedon otomasyon panosu.", "Kalsedon automation panel.", "Щит автоматики Kalsedon.")))

B.append(dict(no="02", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Ana kontrol sayfası", "Main control page", "Главная страница управления"), ozel="ekran",
  gorsel="pano-ana.jpg",
  isaretler=[
    (L("“KAZAN 1” butonu", "“KAZAN 1” (Boiler 1) button", "Кнопка «KAZAN 1» (Котёл 1)"), L("Kazan izleme butonudur; kazan kontrol sayfasına gider.", "Boiler monitoring button; opens the boiler control page.", "Кнопка контроля котла; открывает страницу управления котлом.")),
    (L("“RAPORLAR” butonu", "“RAPORLAR” (Reports) button", "Кнопка «RAPORLAR» (Отчёты)"), L("Arıza ve sıcaklık kayıtlarının tutulduğu sayfaya yönlendirir.", "Opens the page where fault and temperature records are kept.", "Открывает страницу с журналом неисправностей и температур.")),
    (L("“AYARLAR” butonu", "“AYARLAR” (Settings) button", "Кнопка «AYARLAR» (Настройки)"), L("Bekleme ve besleme süreleri gibi tüm ayarların yapıldığı sayfaya yönlendirir.", "Opens the page where all settings such as pause and feed times are made.", "Открывает страницу всех настроек, например времени паузы и подачи.")),
    (L("Kazan start / stop butonu", "Boiler start / stop button", "Кнопка пуска / останова котла"), L("Kazan otomatik durumda start veya stop ettirilir.", "Starts or stops the boiler in automatic mode.", "Запуск или останов котла в автоматическом режиме.")),
    (L("“DÖNÜŞ SUYU”", "“DÖNÜŞ SUYU” (Return water)", "«DÖNÜŞ SUYU» (Обратная вода)"), L("Dönüş suyu sıcaklığı.", "Return water temperature.", "Температура обратной воды.")),
    (L("“ARIZA RESETLE” butonu", "“ARIZA RESETLE” (Reset fault) button", "Кнопка «ARIZA RESETLE» (Сброс ошибки)"), L("Alarm çaldığında alarmı susturur. Arıza devam etse de alarm susar.", "Silences the alarm when it sounds. The alarm is silenced even if the fault persists.", "Отключает звуковой сигнал. Сигнал отключается, даже если неисправность сохраняется.")),
  ],
  sonra=[("kucuk", L("Ana kontrol sayfasında kazan durumunu gösteren simgeler yer alır (bölüm 03). Kazan stop durumundaysa simgeler gri, start durumundaysa turuncu tonda görünür. Ekrandaki F8 fonksiyon tuşu ana ekrana döndürür.",
                     "The main control page shows the symbols for boiler status (section 03). When the boiler is stopped the symbols are grey; when it is started they are orange. The F8 function key returns to the main screen.",
                     "На главной странице отображаются символы состояния котла (раздел 03). При остановленном котле символы серые, при запущенном — оранжевые. Функциональная клавиша F8 возвращает на главный экран."))]))

B.append(dict(no="03", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Kazan durum simgeleri", "Boiler status symbols", "Символы состояния котла"), ozel="ekran",
  gorsel="pano-simge.jpg",
  isaretler=[
    (L("Alev simgesi", "Flame symbol", "Символ пламени"), L("Kazan otomatik start durumundaysa renkli görünür.", "Shown in colour when the boiler is in automatic start.", "Цветной, когда котёл в режиме автоматического пуска.")),
    (L("Arıza simgesi", "Fault symbol", "Символ неисправности"), L("Kazanda herhangi bir arıza varsa görünür.", "Appears if there is any fault on the boiler.", "Появляется при любой неисправности котла.")),
    (L("Elektrik simgesi", "Power symbol", "Символ электропитания"), L("Elektrik kesintisi meydana geldiyse görünür.", "Appears if there has been a power failure.", "Появляется, если было отключение электроэнергии.")),
    (L("Su seviyesi simgesi", "Water level symbol", "Символ уровня воды"), L("Kazan su seviyesi düşükse görünür.", "Appears if the boiler water level is low.", "Появляется при низком уровне воды в котле.")),
    (L("Sıcaklık simgesi", "Temperature symbol", "Символ температуры"), L("Kazan aşırı ısınmışsa görünür.", "Appears if the boiler has overheated.", "Появляется при перегреве котла.")),
    (L("Kazan suyu sıcaklığı", "Boiler water temperature", "Температура воды котла"), L("Kazanın güncel su sıcaklığını gösterir.", "Shows the current boiler water temperature.", "Показывает текущую температуру воды в котле.")),
    (L("“KAZAN UYKUDA”", "“KAZAN UYKUDA” (Boiler asleep)", "«KAZAN UYKUDA» (Котёл в ожидании)"), L("Kazan set edilen sıcaklığa ulaştığında uykuya geçer ve bu simge görünür.", "When the boiler reaches the set temperature it goes to sleep and this symbol appears.", "При достижении заданной температуры котёл переходит в режим ожидания, и появляется этот символ.")),
    (L("Duman görseli", "Smoke image", "Изображение дыма"), L("Kazanın start durumunda olduğunu gösterir.", "Shows that the boiler is in start mode.", "Показывает, что котёл в режиме «Пуск».")),
    (L("Alarm simgesi", "Alarm symbol", "Символ тревоги"), L("Alarm çalıyorsa görünür.", "Appears if the alarm is sounding.", "Появляется при звуковом сигнале тревоги.")),
  ],
  sonra=[("kucuk", L("Kelebek vana, ana sayfada okunan dönüş suyu sıcaklığına göre kontrol edilir (bölüm 06).", "The butterfly valve is controlled according to the return water temperature read on the main page (section 06).", "Дисковый затвор управляется по температуре обратной воды, отображаемой на главной странице (раздел 06)."))]))

B.append(dict(no="04", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Kazan 1 kontrol sayfası", "Boiler 1 control page", "Страница управления котлом 1"), ozel="ekran",
  gorsel="pano-kazan.jpg",
  isaretler=[
    (L("“SET” sıcaklığı", "“SET” temperature", "Уставка «SET»"), L("Kazanın set sıcaklığını görüp değiştirebileceğiniz kısımdır.", "Where you can view and change the boiler set temperature.", "Здесь можно посмотреть и изменить заданную температуру котла.")),
    (L("Bunker doldurma motoru", "Bunker filling motor", "Двигатель загрузки бункера"), L("Bunker doldurma motorunun çalıştığını gösterir. Bunker doluysa “BUNKER DOLU” simgesi görünür.", "Shows that the bunker filling motor is running. When the bunker is full, the “BUNKER DOLU” (bunker full) symbol appears.", "Показывает работу двигателя загрузки бункера. Когда бункер полон, появляется символ «BUNKER DOLU» (бункер полон).")),
    (L("Kelebek vana açılımı (%)", "Butterfly valve opening (%)", "Открытие затвора (%)"), L("Kelebek vana açılım oranını gösterir; dönüş suyu sıcaklığı arttıkça oran artar.", "Shows the butterfly valve opening; it increases as the return water temperature rises.", "Показывает степень открытия затвора; растёт с ростом температуры обратной воды.")),
    (L("Manuel besleme süresi (sn)", "Manual feed time (s)", "Время ручной подачи (с)"), L("Manuel kömür besleme süresidir. Süre dolduğunda besleme otomatik olarak durur.", "Manual coal feed time. When it runs out, feeding stops automatically.", "Время ручной подачи угля. По его истечении подача останавливается автоматически.")),
    (L("Çarpı işaretleri", "Cross marks", "Значки «крест»"), L("İlgili motorun pasif durumda olduğunu gösterir.", "Show that the related motor is disabled.", "Показывают, что соответствующий двигатель отключён.")),
    (L("Baca gazı fanı", "Flue gas fan", "Дымосос"), L("Baca gazı fanı çalışıyorsa pervane simgesi görünür.", "The impeller symbol appears when the flue gas fan is running.", "При работе дымососа отображается символ крыльчатки.")),
    (L("Manuel kontrol butonları", "Manual control buttons", "Кнопки ручного управления"), L("Kazandaki tüm motorlar buradan manuel çalıştırılır: “BUNKER DOLDUR” (bunker doldur), “KÖRÜK FANI” (temiz hava fanı), “KÖMÜR BESLEME” (kömür besleme), “BACA GAZI FANI”.", "All boiler motors can be run manually here: “BUNKER DOLDUR” (fill bunker), “KÖRÜK FANI” (fresh air fan), “KÖMÜR BESLEME” (coal feed), “BACA GAZI FANI” (flue gas fan).", "Здесь вручную запускаются все двигатели котла: «BUNKER DOLDUR» (загрузка бункера), «KÖRÜK FANI» (дутьевой вентилятор), «KÖMÜR BESLEME» (подача угля), «BACA GAZI FANI» (дымосос).")),
  ],
  sonra=[("p", L("Baca gazı fanı çalışmıyorken temiz hava fanlarının butonları görünmez; manuel çalıştırmak için önce baca gazı fanına manuel start verilmelidir. Bu kısım kazan ilk yakılırken gerekir. Kömür besleme butonunun kapatılması unutulabileceği için motorlar belli bir süre sonra otomatik durur; kalan süre stokerlerin üzerindeki zaman sayaçlarında görünür. Bunker doldurma başlatılırsa motor, bunker dolana veya operatör işlemi iptal edene kadar çalışır.",
                  "While the flue gas fan is not running, the fresh air fan buttons are hidden; to run them manually, first give the flue gas fan a manual start. This is needed when the boiler is first fired. Because the coal feed button might be left on, the motors stop automatically after a set time; the remaining time is shown on the timers above the stokers. When bunker filling is started, the motor runs until the bunker is full or the operator cancels it.",
                  "Пока дымосос не работает, кнопки дутьевых вентиляторов скрыты; для их ручного пуска сначала вручную запустите дымосос. Это необходимо при первом розжиге котла. Поскольку кнопку подачи угля могут забыть выключить, двигатели автоматически останавливаются через заданное время; оставшееся время видно на таймерах над стокерами. После запуска загрузки бункера двигатель работает, пока бункер не заполнится или оператор не отменит загрузку."))]))

B.append(dict(no="05", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Kazan 1 ayarlar sayfası", "Boiler 1 settings page", "Страница настроек котла 1"), ozel="ekran",
  gorsel="pano-ayar.jpg",
  isaretler=[
    (L("Motor devre dışı anahtarları", "Motor disable switches", "Переключатели отключения двигателей"), L("Kazanda çalışması istenmeyen motorlar burada devre dışı bırakılır (“DEVRE DIŞI”).", "Motors that should not run are disabled here (“DEVRE DIŞI” = disabled).", "Здесь отключаются двигатели, которые не должны работать («DEVRE DIŞI» — отключён).")),
    (L("“UYKUDAN UYANMA REFERANS DEĞERİ”", "“UYKUDAN UYANMA REFERANS DEĞERİ” (wake-up reference)", "«UYKUDAN UYANMA REFERANS DEĞERİ» (порог выхода из ожидания)"), L("Kazan set sıcaklığa ulaşınca uykuya geçer. Yeniden uyanması için sıcaklığın kaç derece düşmesi gerektiği burada ayarlanır.", "The boiler sleeps once it reaches the set temperature. Here you set by how many degrees the temperature must fall for it to wake up again.", "По достижении уставки котёл переходит в ожидание. Здесь задаётся, на сколько градусов должна снизиться температура для повторного пуска.")),
    (L("Bunker tekrar doldurma aralığı", "Bunker refill interval", "Интервал повторной загрузки бункера"), L("Kömür besleme helezonları kazana kömür besledikçe bunkerdeki kömür azalır. Stokerler kaç saniye besleme yaptıktan sonra bunkerin tekrar doldurulacağı saniye cinsinden yazılır.", "As the feed screws feed coal into the boiler, the coal in the bunker decreases. Enter, in seconds, after how many seconds of stoker feeding the bunker is refilled.", "По мере подачи угля в котёл шнеками количество угля в бункере уменьшается. Укажите в секундах, после скольких секунд подачи стокеров бункер загружается повторно.")),
    (L("Bunker maks. doldurma süresi", "Bunker max. filling time", "Макс. время загрузки бункера"), L("Kuyuda kömür bitmesi veya yakıt gelmemesine karşı bunker doldurma süresinin üst sınırı girilir. Bu sürede bunker dolmazsa alarm çalar.", "Upper limit for the bunker filling time, in case the pit runs out of coal or fuel stops coming. If the bunker is not full within this time, the alarm sounds.", "Верхний предел времени загрузки бункера на случай, если в приёмной яме закончится уголь или топливо перестанет поступать. Если бункер не заполнится за это время, срабатывает сигнал.")),
    (L("Stoker bekleme / besleme süreleri", "Stoker pause / feed times", "Время паузы / подачи стокеров"), L("Her stoker için bekleme süresi (ekranda min. 60 – maks. 360 sn) ve besleme süresi (min. 15 – maks. 120 sn).", "For each stoker: pause time (on screen min. 60 – max. 360 s) and feed time (min. 15 – max. 120 s).", "Для каждого стокера: время паузы (на экране мин. 60 – макс. 360 с) и время подачи (мин. 15 – макс. 120 с).")),
  ],
  sonra=[("p", L("Temiz hava fanı 1 devre dışı bırakılırsa kömür besleme 1 de otomatik olarak devre dışı kalır; aynısı temiz hava fanı 2 ve kömür besleme 2 için geçerlidir. Baca gazı fanı devre dışı bırakılamaz. Bunker yükleme devre dışı bırakılırsa bunker otomatik doldurulmaz. Sistem otomatik çalışırken bir motor arızaya geçerse otomatik olarak pasife alınır; arızalı motor baca gazı fanı değilse kazan çalışmaya devam eder. Örneğin temiz hava fanı 2 arızalanırsa temiz hava fanı 2 ve kömür besleme 2 pasife geçer, temiz hava fanı 1 ve kömür besleme 1 çalışmaya devam eder.",
                  "If fresh air fan 1 is disabled, coal feed 1 is disabled automatically as well; the same applies to fresh air fan 2 and coal feed 2. The flue gas fan cannot be disabled. If bunker loading is disabled, the bunker is not filled automatically. If a motor fails while the system runs in automatic mode, it is disabled automatically; unless the failed motor is the flue gas fan, the boiler keeps running. For example, if fresh air fan 2 fails, fresh air fan 2 and coal feed 2 are disabled while fresh air fan 1 and coal feed 1 keep running.",
                  "При отключении дутьевого вентилятора 1 автоматически отключается и подача угля 1; то же относится к вентилятору 2 и подаче 2. Дымосос отключить нельзя. При отключении загрузки бункер не заполняется автоматически. Если при автоматической работе какой-либо двигатель неисправен, он автоматически отключается; если это не дымосос, котёл продолжает работу. Например, при отказе дутьевого вентилятора 2 отключаются вентилятор 2 и подача угля 2, а вентилятор 1 и подача 1 продолжают работать."))]))

B.append(dict(no="06", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Genel ayarlar sayfası", "General settings page", "Страница общих настроек"), ozel="ekran",
  gorsel="pano-genel.jpg",
  isaretler=[
    (L("“KELEBEK VANA OTOMATİK KONTROL”", "“KELEBEK VANA OTOMATİK KONTROL” (butterfly valve auto control)", "«KELEBEK VANA OTOMATİK KONTROL» (автоуправление затвором)"), L("Kelebek vana devre dışı bırakılırsa kazanın terleme sistemi de devre dışı kalır.", "If the butterfly valve is disabled, the boiler's condensation protection is disabled as well.", "При отключении затвора отключается и система защиты котла от конденсации.")),
    (L("“KELEBEK VANA AÇILIM ORANLARI”", "“KELEBEK VANA AÇILIM ORANLARI” (valve opening rates)", "«KELEBEK VANA AÇILIM ORANLARI» (степени открытия)"), L("Kelebek vananın sıcaklık kademelerinde (minimum, orta, maksimum) yüzde kaç açılacağı ayarlanır.", "Sets the valve opening percentage at each temperature step (minimum, medium, maximum).", "Задаётся процент открытия затвора на каждой температурной ступени (минимум, средняя, максимум).")),
    (L("“KELEBEK VANA SICAKLIK REFERANSLARI”", "“KELEBEK VANA SICAKLIK REFERANSLARI” (temperature references)", "«KELEBEK VANA SICAKLIK REFERANSLARI» (температурные пороги)"), L("Kelebek vananın minimum ve maksimum sıcaklık kademeleri; vana burada set edilen değerlere göre pozisyon alır.", "The minimum and maximum temperature steps of the valve; the valve positions itself according to the values set here.", "Минимальная и максимальная температурные ступени; затвор занимает положение по заданным здесь значениям.")),
    (L("“KAZAN ÇALIŞMA SAATLERİ”", "“KAZAN ÇALIŞMA SAATLERİ” (boiler operating hours)", "«KAZAN ÇALIŞMA SAATLERİ» (наработка котла)"), L("Saat cinsinden hafızada tutulur. “AKTİF”: kazanın start durumunda kaldığı süre; “YANMA”: start durumunda uykuya geçmeden çalıştığı süre; “UYKU”: start durumunda uykuda geçirdiği süre.", "Stored in hours. “AKTİF” (active): time in start mode; “YANMA” (firing): time running in start mode without sleeping; “UYKU” (sleep): time asleep while in start mode.", "Хранится в часах. «AKTİF» (активно): время в режиме «Пуск»; «YANMA» (горение): время работы в режиме «Пуск» без ожидания; «UYKU» (ожидание): время в ожидании в режиме «Пуск».")),
  ]))

B.append(dict(no="07", ust=L("OPERATÖR PANELİ", "OPERATOR PANEL", "ПАНЕЛЬ ОПЕРАТОРА"), baslik=L("Raporlar ve kömür tüketimi", "Reports and coal consumption", "Отчёты и расход угля"), ozel="ekran",
  gorsel="pano-rapor.jpg", gorsel2="pano-komur.jpg",
  isaretler=[
    (L("“KAZANLAR İZLEME”", "“KAZANLAR İZLEME” (boiler monitoring)", "«KAZANLAR İZLEME» (контроль котлов)"), L("Kazan çalışma bilgileri bu kısımda görünür.", "Boiler operating information is shown here.", "Здесь отображается информация о работе котла.")),
    (L("“ARIZA KAYITLARI”", "“ARIZA KAYITLARI” (fault records)", "«ARIZA KAYITLARI» (журнал неисправностей)"), L("Arıza geçmişi sayfasına yönlendirir.", "Opens the fault history page.", "Открывает страницу истории неисправностей.")),
    (L("“SICAKLIK RAPORU”", "“SICAKLIK RAPORU” (temperature report)", "«SICAKLIK RAPORU» (отчёт по температуре)"), L("Geçmiş sıcaklık kayıtlarını gösterir.", "Shows past temperature records.", "Показывает архив температур.")),
    (L("“KÖMÜR TÜKETİM RAPORU”", "“KÖMÜR TÜKETİM RAPORU” (coal consumption report)", "«KÖMÜR TÜKETİM RAPORU» (отчёт о расходе угля)"), L("Kömür tüketim bilgilerinin tutulduğu sayfadır (alttaki ekran).", "The page where coal consumption is kept (screen below).", "Страница учёта расхода угля (нижний снимок).")),
  ],
  isaretler2=[
    (L("“KAZAN 1 TOPLAM KÖMÜR TÜKETİMİ”", "“KAZAN 1 TOPLAM KÖMÜR TÜKETİMİ” (total coal used)", "«KAZAN 1 TOPLAM KÖMÜR TÜKETİMİ» (общий расход)"), L("Şimdiye kadar tüketilen kömür miktarını gösterir.", "Shows the amount of coal consumed so far.", "Показывает количество угля, израсходованного на данный момент.")),
    (L("“STOKERİN 60 SN'DE BESLEDİĞİ KÖMÜR MİKTARI”", "“STOKERİN 60 SN'DE BESLEDİĞİ KÖMÜR MİKTARI” (coal fed per 60 s)", "«STOKERİN 60 SN'DE BESLEDİĞİ KÖMÜR MİKTARI» (подача за 60 с)"), L("Sistemin hesaplama yapması için stokerin dakikada beslediği ortalama kömür miktarı buraya girilir; böylece kömür tüketimi yaklaşık olarak öğrenilir.", "Enter the average amount of coal the stoker feeds per minute so that the system can calculate; consumption is then known approximately.", "Для расчёта введите средний объём угля, подаваемый стокером за минуту; так расход определяется приблизительно.")),
  ]))

B.append(dict(no="08", ust=L("İLK ÇALIŞTIRMA", "FIRST START-UP", "ПЕРВЫЙ ПУСК"), baslik=L("Kazanın yakılması", "Firing the boiler", "Розжиг котла"), ozel="ekran",
  once=[
    ("adim", [
      L("Operatör bunkerde yakıt olup olmadığını kontrol eder. Kazanı yakmak için yeterli yakıt varsa bunkeri tamamen doldurmadan devam edebilir; kazan otomatik starta alındığında sistem bunkeri dolduracaktır.", "The operator checks whether there is fuel in the bunker. If there is enough fuel to fire the boiler, he can continue without filling the bunker completely; once the boiler is put into automatic start, the system will fill the bunker.", "Оператор проверяет наличие топлива в бункере. Если топлива достаточно для розжига, можно продолжать, не заполняя бункер полностью: после перевода котла в автоматический пуск система заполнит бункер."),
      L("Bunkerde yeterli yakıt varsa stokerleri manuel çalıştırarak kazan içine gerekli miktarda yakıt besler.", "If there is enough fuel in the bunker, he runs the stokers manually to feed the required amount of fuel into the boiler.", "При достаточном количестве топлива оператор вручную запускает стокеры и подаёт в котёл нужное количество топлива."),
      L("Tutuşturmayı gerçekleştirir ve baca gazı fanını çalıştırır.", "He lights the fuel and starts the flue gas fan.", "Выполняет розжиг и включает дымосос."),
      L("Yanma gerekli seviyeye geldiğinde temiz hava fanlarını çalıştırır.", "When combustion reaches the required level, he starts the fresh air fans.", "Когда горение достигает нужного уровня, включает дутьевые вентиляторы."),
      L("Kazan içindeki kömür yeterli değilse manuel takviye yapılabilir: pano üzerindeki butonlar veya “KAZAN 1” sayfasındaki kömür besleme butonları kullanılır.", "If there is not enough coal in the boiler, it can be topped up manually using the buttons on the panel or the coal feed buttons on the “KAZAN 1” page.", "Если угля в котле недостаточно, его можно добавить вручную кнопками на щите или кнопками подачи угля на странице «KAZAN 1»."),
      L("Tutuşma kazanın yeni kömür besleyebileceği seviyeye gelince kazan kontrol sayfasındaki start butonuna basılır ve kazan otomatik start durumuna alınır.", "When ignition has reached the point where the boiler can take new coal, press the start button on the boiler control page to put the boiler into automatic start.", "Когда горение достигло уровня, при котором котёл может принимать новый уголь, нажмите кнопку пуска на странице управления котлом и переведите котёл в автоматический пуск."),
    ]),
    ("not", "dikkat", L("KAZAN KULLANIM KILAVUZU", "BOILER USER MANUAL", "РУКОВОДСТВО ПО КОТЛУ"),
      L("İlk yakma öncesi kontroller, kömür şartları, bakım ve arıza bulma için Kalsedon kazanı kullanım kılavuzuna (ENP-KLS) bakın.", "For pre-firing checks, coal requirements, maintenance and troubleshooting, refer to the Kalsedon boiler user manual (ENP-KLS).", "Проверки перед розжигом, требования к углю, обслуживание и поиск неисправностей — см. руководство по эксплуатации котла Kalsedon (ENP-KLS).")),
  ]))

GARANTI = AKU.GARANTI
