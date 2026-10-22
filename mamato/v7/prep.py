"""Sfondi v7: facciata rosso/magenta per la Latin night, tavolata calda per la cena."""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import numpy as np

def grade(im, lift_red=1.0, warm=False):
    a = np.asarray(im.convert('RGB')).astype(float) / 255
    L = .3 * a[..., 0] + .59 * a[..., 1] + .11 * a[..., 2]
    # neri profondi: curva a S che schiaccia le ombre
    k = np.clip((L - .06) / .94, 0, 1) ** 1.35 / np.maximum(L, 1e-3)
    a = np.clip(a * k[..., None], 0, 1)
    if warm:   # ambra: alza rosso/verde, abbassa blu
        a[..., 0] *= 1.08; a[..., 1] *= .97; a[..., 2] *= .78
    else:      # rosso fuoco/magenta: verde giù, rosso su
        a[..., 0] *= 1.12 * lift_red; a[..., 1] *= .78; a[..., 2] *= .92
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype('uint8'))

# 1 · facciata: sotto l'insegna, sopra il logo stampato in basso
f = Image.open('reference/mamato-facciata-pulita.jpg').convert('RGB').crop((15, 330, 1191, 1470))
f = ImageEnhance.Contrast(f).enhance(1.12)
f = grade(f)
# spegne l'albero di Natale a destra dell'ingresso
m = Image.new('L', f.size, 0)
ImageDraw.Draw(m).ellipse((880, 560, 1300, 1060), fill=255)
dark = ImageEnhance.Brightness(ImageEnhance.Color(f).enhance(.15)).enhance(.08)
f.paste(dark, (0, 0), m.filter(ImageFilter.GaussianBlur(45)))
f = f.resize((1080, round(f.height * 1080 / f.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 40, 2))
f.save('v7/assets/bg-facciata.jpg', quality=93)

# 2 · amici che cantano e agitano i tovaglioli
t = Image.open('reference/mamato-cena-tovaglioli.jpg').convert('RGB').crop((150, 0, 1440, 994))
t = grade(ImageEnhance.Contrast(t).enhance(1.06), warm=True)
t = t.resize((1080, round(t.height * 1080 / t.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 40, 2))
t.save('v7/assets/bg-tavolata.jpg', quality=93)
print(f.size, t.size)
