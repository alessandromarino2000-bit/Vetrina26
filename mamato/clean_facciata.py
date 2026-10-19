"""Ripulisce la foto di dicembre: via i neon EDONÈ/GINERDÌ e gli addobbi natalizi visibili."""
from PIL import Image, ImageFilter, ImageDraw

im = Image.open('reference/mamato-facciata.jpg').convert('RGB')

def patch(box, dx, dy, feather=8):
    x0, y0, x1, y1 = box
    src = im.crop((x0 + dx, y0 + dy, x1 + dx, y1 + dy))
    m = Image.new('L', (x1 - x0, y1 - y0), 0)
    ImageDraw.Draw(m).rectangle((feather, feather, x1 - x0 - feather, y1 - y0 - feather), fill=255)
    im.paste(src, (x0, y0), m.filter(ImageFilter.GaussianBlur(feather / 2)))

# neon: clonati dalla fascia di tende luminose subito sopra
for box in [(400, 696, 595, 776), (664, 702, 845, 771), (940, 682, 1160, 768)]:
    h = box[3] - box[1]
    patch(box, 0, -h + 6)
    patch(box, 0, -h + 6)   # secondo passaggio per il bagliore residuo
# caramelle giganti e stella sopra l'ingresso
patch((478, 498, 542, 582), -70, 0)
patch((1010, 585, 1080, 630), -80, 0)
patch((795, 905, 845, 990), -70, 0)
im.save('reference/mamato-facciata-pulita.jpg', quality=95)
im.crop((250, 450, 1206, 1000)).save('/tmp/claude-0/-home-user-Vetrina26/f751ba4b-4b75-5979-9df1-981bee0f3dc6/scratchpad/dec_clean.png')
