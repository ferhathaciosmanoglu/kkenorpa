// araclar/qr-uret.mjs — KILAVUZ_SABLONU.md §9.5
// Kullanım:
//   node araclar/qr-uret.mjs akuamarin https://kilavuz.enorpa.com/akuamarin/            → dilsiz QR
//   node araclar/qr-uret.mjs akuamarin https://kilavuz.enorpa.com/akuamarin/ tr en ru   → dile sabit QR'lar (?lang=xx)
// Ayar §9.2: hata düzeltme Q, 4 modül sessiz alan, siyah modül / beyaz zemin.
import QRCode from "qrcode";
import { mkdirSync } from "node:fs";

const [seri, adres, ...diller] = process.argv.slice(2);
if (!seri || !adres?.endsWith("/")) throw new Error("Seri ve sonu / ile biten adres verin");
const ayar = { errorCorrectionLevel: "Q", margin: 4, color: { dark: "#000000", light: "#FFFFFF" } };
mkdirSync(`${seri}/qr`, { recursive: true });

const isler = diller.length ? diller.map((d) => [`-${d}`, `${adres}?lang=${d}`]) : [["", adres]];
for (const [ek, hedef] of isler) {
  await QRCode.toFile(`${seri}/qr/${seri}-qr${ek}.svg`, hedef, { ...ayar, type: "svg" });
  await QRCode.toFile(`${seri}/qr/${seri}-qr${ek}.png`, hedef, { ...ayar, width: 1200 });
  const q = QRCode.create(hedef, ayar);
  console.log(`QR hazır: ${seri}-qr${ek}  ${hedef}  (sürüm ${q.version}, ${q.modules.size}×${q.modules.size} modül)`);
}
