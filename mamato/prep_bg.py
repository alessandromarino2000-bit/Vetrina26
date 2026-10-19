"""Sfondi a foto singola per le locandine: un solo scatto per soggetto, viraggio caldo coerente."""
from PIL import Image, ImageEnhance
import numpy as np

WARM = [(0, (10, 3, 6)), (.25, (90, 14, 26)), (.5, (215, 70, 55)), (.75, (255, 178, 115)), (1, (255, 246, 228))]

def gmap(img, mix):
    a = np.asarray(img.convert('RGB')).astype(float) / 255
    L = .3 * a[..., 0] + .59 * a[..., 1] + .11 * a[..., 2]
    out = np.stack([np.interp(L, [s[0] for s in WARM], [s[1][c] / 255 for s in WARM]) for c in range(3)], -1)
    return Image.fromarray((np.clip(out * mix + a * (1 - mix), 0, 1) * 255).astype('uint8'))

def bg(src, box, name, mix, c=1.08, b=1.0):
    im = Image.open('reference/' + src).convert('RGB')
    if box: im = im.crop(box)
    im = ImageEnhance.Brightness(ImageEnhance.Contrast(im).enhance(c)).enhance(b)
    gmap(im, mix).save('assets/' + name, quality=93)

bg('mamato-facciata-2.jpg', None, 'bg-a-facciata.jpg', .35)
bg('mamato-dj-neon.jpg', None, 'bg-b-consolle.jpg', .25, 1.1, 1.12)
bg('mamato-facciata-pulita.jpg', (0, 0, 975, 1599), 'bg-c-folla.jpg', .3, 1.1, 1.08)   # a destra c'è l'albero: escluso
bg('mamato-karaoke-cantante.jpg', (0, 0, 1216, 1330), 'bg-d-cantante.jpg', .45)       # sotto c'è un'icona Instagram: esclusa
bg('mamato-cena-ragazze.jpg', None, 'bg-e-ragazze.jpg', .3)
bg('mamato-cena-tovaglioli.jpg', None, 'bg-f-tavolata.jpg', .3)
