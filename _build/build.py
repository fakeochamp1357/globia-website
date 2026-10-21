# Builds index.html and the translated pages (en, fr, es, ur, hi).
# Run from the repo root:  python3 _build/build.py
# Edit texts in LANGS below, then re-run and commit the generated .html files.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I = json.load(open(os.path.join(ROOT, '_build', 'icons.json'), encoding='utf-8'))

PHONE = '+4915215994879'
PHONE_SHOWN = '+49 152 15994879'
EMAIL = 'pind-enterprise114@proton.me'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Hindenburgstra%C3%9Fe+220%2C+41061+M%C3%B6nchengladbach'
CAT_ICONS = [('grain', 'var(--gold)'), ('pepper', 'var(--red)'), ('leaf', 'var(--green)'),
             ('snow', 'var(--teal)'), ('cup', 'var(--orange)'), ('pot', '#8a5a2b')]

LANGS = [
 dict(code='de', file='index.html', name='Deutsch', dir='ltr',
      title='Globia – Supermarkt für Afrika &amp; Asien in Mönchengladbach',
      desc='Globia – Ihr Supermarkt für Lebensmittel aus Afrika und Asien in Mönchengladbach, Hindenburgstraße 220.',
      h1='Lebensmittel aus <em>Afrika &amp; Asien</em>', sub='Ihr Supermarkt in Mönchengladbach',
      call='Anrufen', route='Route', address='Adresse', hours_t='Öffnungszeiten',
      hours=['<strong>Montag – Samstag: 10:00 – 20:00 Uhr</strong>', 'Sonntag: geschlossen'],
      contact='Kontakt', products='Unser Sortiment',
      cats=['Reis &amp; Mehl', 'Gewürze &amp; Saucen', 'Obst &amp; Gemüse', 'Tiefkühlware', 'Getränke &amp; Snacks', 'Kochzutaten']),
 dict(code='en', file='en.html', name='English', dir='ltr',
      title='Globia – Supermarket for African &amp; Asian food in Mönchengladbach',
      desc='Globia – your supermarket for groceries from Africa and Asia in Mönchengladbach, Hindenburgstraße 220.',
      h1='Groceries from <em>Africa &amp; Asia</em>', sub='Your supermarket in Mönchengladbach',
      call='Call us', route='Directions', address='Address', hours_t='Opening hours',
      hours=['<strong>Monday – Saturday: 10 am – 8 pm</strong>', 'Sunday: closed'],
      contact='Contact', products='Our products',
      cats=['Rice &amp; flour', 'Spices &amp; sauces', 'Fruit &amp; vegetables', 'Frozen food', 'Drinks &amp; snacks', 'Cooking essentials']),
 dict(code='fr', file='fr.html', name='Français', dir='ltr',
      title='Globia – Supermarché africain et asiatique à Mönchengladbach',
      desc='Globia – votre supermarché de produits d’Afrique et d’Asie à Mönchengladbach, Hindenburgstraße 220.',
      h1='Produits d’<em>Afrique et d’Asie</em>', sub='Votre supermarché à Mönchengladbach',
      call='Appeler', route='Itinéraire', address='Adresse', hours_t='Horaires d’ouverture',
      hours=['<strong>Lundi – samedi : 10h – 20h</strong>', 'Dimanche : fermé'],
      contact='Contact', products='Nos produits',
      cats=['Riz &amp; farine', 'Épices &amp; sauces', 'Fruits &amp; légumes', 'Surgelés', 'Boissons &amp; snacks', 'Ingrédients de cuisine']),
 dict(code='es', file='es.html', name='Español', dir='ltr',
      title='Globia – Supermercado africano y asiático en Mönchengladbach',
      desc='Globia – tu supermercado de productos de África y Asia en Mönchengladbach, Hindenburgstraße 220.',
      h1='Alimentos de <em>África y Asia</em>', sub='Tu supermercado en Mönchengladbach',
      call='Llamar', route='Cómo llegar', address='Dirección', hours_t='Horario',
      hours=['<strong>Lunes – sábado: 10:00 – 20:00</strong>', 'Domingo: cerrado'],
      contact='Contacto', products='Nuestros productos',
      cats=['Arroz y harina', 'Especias y salsas', 'Frutas y verduras', 'Congelados', 'Bebidas y snacks', 'Ingredientes de cocina']),
 dict(code='ur', file='ur.html', name='اردو', dir='rtl',
      title='Globia – مونشن گلاڈباخ میں افریقی اور ایشیائی سپر مارکیٹ',
      desc='Globia – مونشن گلاڈباخ میں افریقہ اور ایشیا کی کھانے پینے کی اشیاء، Hindenburgstraße 220۔',
      h1='<em>افریقہ اور ایشیا</em> کی کھانے پینے کی اشیاء', sub='مونشن گلاڈباخ میں آپ کی سپر مارکیٹ',
      call='کال کریں', route='راستہ دیکھیں', address='پتہ', hours_t='اوقاتِ کار',
      hours=['<strong>پیر تا ہفتہ: صبح 10 بجے سے رات 8 بجے تک</strong>', 'اتوار: بند'],
      contact='رابطہ', products='ہماری مصنوعات',
      cats=['چاول اور آٹا', 'مصالحے اور ساس', 'پھل اور سبزیاں', 'فروزن اشیاء', 'مشروبات اور اسنیکس', 'کھانا پکانے کا سامان']),
 dict(code='hi', file='hi.html', name='हिन्दी', dir='ltr',
      title='Globia – Mönchengladbach में अफ्रीकी और एशियाई सुपरमार्केट',
      desc='Globia – Mönchengladbach में अफ्रीका और एशिया की खाने-पीने की चीज़ें, Hindenburgstraße 220.',
      h1='<em>अफ्रीका और एशिया</em> की खाने-पीने की चीज़ें', sub='Mönchengladbach में आपका सुपरमार्केट',
      call='कॉल करें', route='रास्ता देखें', address='पता', hours_t='खुलने का समय',
      hours=['<strong>सोमवार – शनिवार: सुबह 10 बजे से रात 8 बजे तक</strong>', 'रविवार: बंद'],
      contact='संपर्क', products='हमारे उत्पाद',
      cats=['चावल और आटा', 'मसाले और सॉस', 'फल और सब्ज़ियाँ', 'फ्रोज़न सामान', 'पेय और स्नैक्स', 'खाना पकाने का सामान']),
]


def page(L):
    alts = '\n'.join(f'<link rel="alternate" hreflang="{x["code"]}" href="https://globia.shop/{"" if x["file"] == "index.html" else x["file"]}">' for x in LANGS)
    switch = ''.join(
        f'<a href="{"/" if x["file"] == "index.html" else x["file"]}" lang="{x["code"]}"'
        + (' aria-current="page"' if x is L else '') + f'>{x["name"]}</a>' for x in LANGS)
    cats = '\n'.join(
        f'      <div class="cat"><div class="icon" style="background:{c}">{I[i]}</div><h3>{t}</h3></div>'
        for (i, c), t in zip(CAT_ICONS, L['cats']))
    hours = '<br>'.join(L['hours'])
    fav = f'<link rel="icon" href="{I["favicon"]}">\n' if I.get('favicon') else ''
    return f'''<!doctype html>
<html lang="{L["code"]}" dir="{L["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{L["title"]}</title>
<meta name="description" content="{L["desc"]}">
<meta name="theme-color" content="#1f7a4a">
{fav}{alts}
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><div class="wrap">
  <a class="logo" href="/" dir="ltr">{I["logo"]}Globia</a>
  <nav class="lang" aria-label="Sprache / Language">{switch}</nav>
</div></header>

<div class="hero"><div class="wrap">
  <h1>{L["h1"]}</h1>
  <p>{L["sub"]}</p>
  <div class="cta">
    <a class="btn btn-gold" href="tel:{PHONE}">{I["phone"]}{L["call"]}</a>
    <a class="btn btn-ghost" href="{MAPS}">{I["pin"]}{L["route"]}</a>
  </div>
</div></div>

<main class="wrap">
  <section id="besuch">
    <div class="visit">
      <div class="box"><div class="icon" style="background:var(--green)">{I["pin"]}</div>
        <h3>{L["address"]}</h3>
        <p dir="ltr">Globia<br>Hindenburgstraße 220<br>41061 Mönchengladbach</p>
      </div>
      <div class="box"><div class="icon" style="background:var(--orange)">{I["clock"]}</div>
        <h3>{L["hours_t"]}</h3>
        <p>{hours}</p>
      </div>
      <div class="box"><div class="icon" style="background:var(--teal)">{I["phone"]}</div>
        <h3>{L["contact"]}</h3>
        <p dir="ltr"><a href="tel:{PHONE}">{PHONE_SHOWN}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </section>

  <section id="sortiment">
    <div class="head"><h2>{L["products"]}</h2></div>
    <div class="grid">
{cats}
    </div>
  </section>
</main>

<footer><div class="wrap">
  <a class="logo" href="/" dir="ltr">{I["logo"]}Globia</a>
  <div lang="de" dir="ltr"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a><span>© 2026 Globia</span></div>
</div></footer>
</body>
</html>
'''


for L in LANGS:
    with open(os.path.join(ROOT, L['file']), 'w', encoding='utf-8') as f:
        f.write(page(L))
    print('wrote', L['file'])
