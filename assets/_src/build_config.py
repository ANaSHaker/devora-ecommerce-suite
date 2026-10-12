# Generates render.json (kept for documentation).
# Run: python build_config.py && node D:/shaker-github/_kit/render.mjs render.json
import json, os

S = 'D:/shaker-github/_store/'
HERE = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
U = lambda p: 'file:///' + p


def phone(kind, img, w=250):
    if kind == 'android':
        return f'<div class="android" style="--w:{w}px"><div class="scr"><div class="cam"></div><img src="{U(img)}"></div></div>'
    return f'<div class="iphone" style="--w:{w}px"><div class="scr"><div class="island"></div><img src="{U(img)}"></div></div>'


brands = [
    ('Aleefie · أليفي', 'Pet supplies', 'com.devora.alife', '#FD7E15', S + 'com.devora.alife/icon.png', 'iphone', S + 'ios_com.devora.alife/ios_shot_04.png', 'Play + App Store'),
    ('Deno Store · دينو ستور', 'Kids toys', 'com.devora.dinotoys', '#7CB342', S + 'com.devora.dinotoys/icon.png', 'android', S + 'com.devora.dinotoys/screen_02.png', 'Google Play'),
    ('StarMart · ستار مارت', 'Modest fashion', 'com.devora.starmart', '#C62828', S + 'com.devora.starmart/icon.png', 'android', S + 'com.devora.starmart/shot_02.png', 'Google Play'),
    ('Irtaah · ارتاح', 'Home services', 'com.irtaah.devora', '#2E7D32', S + 'com.irtaah.devora/icon.png', 'iphone', S + 'com.irtaah.devora/shot_01.png', 'Google Play'),
]

RP = "font-family:'Readex Pro',Inter"
cols = ''
for n, cat, pkg, col, ic, k, shot, store in brands:
    cols += f'''<div style="display:flex;flex-direction:column;align-items:center;gap:26px">
      <div style="filter:drop-shadow(0 0 40px {col}55)">{phone(k, shot)}</div>
      <div style="display:flex;align-items:center;gap:14px;width:330px;padding:14px 16px;border-radius:20px;background:#ffffff0d;border:1px solid #ffffff1f;border-top:4px solid {col}">
        <img src="{U(ic)}" style="width:58px;height:58px;border-radius:14px;background:#fff">
        <div style="display:flex;flex-direction:column;gap:3px;min-width:0">
          <div style="{RP};font-weight:700;font-size:20px;white-space:nowrap">{n}</div>
          <div style="font-size:15px;opacity:.75">{cat} · {store}</div>
          <div style="font-family:Consolas,monospace;font-size:13px;opacity:.6">{pkg}</div>
        </div></div></div>'''

more = ''.join(
    f'<img src="{U(HERE + "/" + p)}" style="height:52px;width:52px;object-fit:contain;border-radius:12px;background:#fff;padding:4px">'
    for p in ['logo_pets_with_admin.png', 'logo_gorcery_with_admin.png', 'logo_okaView.png', 'logo_ElWaseq.png'])

brands_body = f'''<div class="grid-bg"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;padding:54px 50px;gap:34px">
  <div style="display:flex;flex-direction:column;align-items:center;gap:12px">
    <div class="accent" style="font-size:22px;font-weight:700;letter-spacing:.18em">ONE CODEBASE → MANY BRANDS</div>
    <div class="title" style="font-size:52px">One Flutter engine, re-skinned per client</div>
  </div>
  <div style="display:flex;gap:30px;align-items:flex-start">{cols}</div>
  <div style="display:flex;align-items:center;gap:16px;font-size:19px;opacity:.9;padding:12px 22px;border-radius:99px;background:#ffffff0d;border:1px solid #ffffff1f">
    <span>Also white-labelled for</span>{more}<span>+ a shared store-owner admin app</span></div>
</div>'''

knobs = [('App name & copy', 'assets/languages/*.json'), ('Logo, icon & splash', 'flutter_launcher_icons'),
         ('Brand palette → theme', 'primary / accent colors'), ('Package / bundle id', 'change_app_package_name'),
         ('Firebase project', 'FCM · Crashlytics · Remote Config'), ('Content flags', 'AR / EN · inner categories'),
         ('Allowed countries', 'phone auth (e.g. IQ)')]
krows = ''.join(
    f'<div style="display:flex;justify-content:space-between;gap:20px;padding:13px 18px;border-radius:14px;background:#ffffff0a;border:1px solid #ffffff17"><b style="font-weight:600">{a}</b><span style="opacity:.6;font-family:Consolas,monospace;font-size:16px">{b}</span></div>'
    for a, b in knobs)
outs = ''.join(
    f'<div style="display:flex;align-items:center;gap:14px;padding:12px 16px;border-radius:16px;background:#ffffff0d;border:1px solid #ffffff1f;border-left:4px solid {col}"><img src="{U(ic)}" style="width:46px;height:46px;border-radius:12px;background:#fff"><div><div style="{RP};font-weight:700;font-size:18px">{n}</div><div style="font-size:14px;opacity:.65">{cat}</div></div></div>'
    for n, cat, pkg, col, ic, k, shot, store in brands)

wl_body = f'''<div class="grid-bg"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;padding:56px 70px;gap:36px">
 <div><div class="accent" style="font-size:22px;font-weight:700;letter-spacing:.14em">SIGNATURE · WHITE-LABEL PIPELINE</div>
 <div class="title" style="font-size:50px;margin-top:10px">A new brand is a config change, not a fork</div></div>
 <div style="display:flex;align-items:center;gap:36px;flex:1">
  <div style="width:560px;display:flex;flex-direction:column;gap:10px;font-size:19px">
    <div style="font-size:18px;opacity:.7;margin-bottom:4px">AppConstants + brand assets</div>{krows}</div>
  <div style="display:flex;align-items:center;gap:18px">
    <div style="font-size:56px" class="accent">→</div>
    <div style="padding:22px 26px;border-radius:22px;background:linear-gradient(135deg,#FD7E1533,#4F46E533);border:1px solid #ffffff2a;text-align:center;width:250px">
      <div style="font-weight:800;font-size:24px">Shared core</div>
      <div style="font-size:16px;opacity:.75;margin-top:8px;line-height:1.55">Catalog · Cart · Checkout<br>Orders · Coupons · Shipping<br>Auth · Notifications<br>Role-based admin</div></div>
    <div style="font-size:56px" class="accent">→</div></div>
  <div style="display:flex;flex-direction:column;gap:14px;width:330px">{outs}</div>
 </div></div>'''

cfg = {
    "outDir": "..",
    "brand": {"name": "DevOra E‑commerce Suite",
              "tagline": "One white-label Flutter codebase powering pet, toy, fashion and home-services brands — plus their admin app.",
              "accent": "#FD7E15", "accent2": "#4F46E5", "logo": "devora_logo.png"},
    "images": [
        {"type": "banner", "file": "banner.png", "kicker": "Case Study · White-label commerce",
         "screens": [S + 'ios_com.devora.alife/ios_shot_04.png', S + 'com.irtaah.devora/shot_01.png', S + 'com.devora.dinotoys/screen_02.png'],
         "devices": ["iphone", "iphone", "android"],
         "subtitle": "One Flutter codebase → many branded stores, plus a store-owner admin app.", "css": ".title{font-size:58px!important}",
         "chips": ["Flutter", "Bloc / Cubit", "White-label"]},
        {"type": "html", "file": "brands.png", "width": 1600, "height": 1080, "css": ".grain:after{opacity:.025}", "body": brands_body},
        {"type": "html", "file": "white-label.png", "width": 1600, "height": 780, "body": wl_body},
        {"type": "gallery", "file": "store-listings.png", "title": "Same engine, two storefronts — Aleefie & Deno Store",
         "device": "card", "cardRatio": 2.17, "cols": 6,
         "screens": [S + 'com.devora.alife/shot_03.png', S + 'com.devora.alife/shot_04.png', S + 'com.devora.alife/shot_01.png', S + 'com.devora.dinotoys/shot_02.png', S + 'com.devora.dinotoys/shot_01.png', S + 'com.devora.dinotoys/shot_05.png']},
        {"type": "gallery", "file": "irtaah-screens.png", "title": "Irtaah — the same core as a home-services marketplace",
         "device": "iphone", "cols": 5, "screens": [S + f'com.irtaah.devora/shot_0{i}.png' for i in range(1, 6)]},
        {"type": "gallery", "file": "customer-flows.png", "title": "Customer flows — welcome, sign-in, empty states, home",
         "device": "mixed", "devices": ["android", "android", "iphone", "iphone", "iphone"], "cols": 5,
         "screens": [S + 'com.devora.starmart/shot_02.png', S + 'com.devora.starmart/shot_03.png', S + 'ios_com.devora.alife/ios_shot_03.png',
                     S + 'ios_com.devora.alife/ios_shot_01.png', S + 'ios_com.devora.alife/ios_shot_04.png']},
    ]}
json.dump(cfg, open(os.path.join(HERE, 'render.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('render.json written')
