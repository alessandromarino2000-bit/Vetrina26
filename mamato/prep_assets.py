"""Prepara le foto del locale per le locandine: viraggi colore, duotoni, ritagli e scontorni."""
import sys
from PIL import Image, ImageEnhance
import numpy as np

REF, OUT, CUT = 'reference/', 'assets/', sys.argv[1]
RED = [(0, (10, 2, 8)), (.2, (80, 6, 30)), (.45, (220, 30, 60)), (.7, (255, 110, 120)), (1, (255, 232, 210))]
WARM = [(0, (12, 4, 6)), (.25, (100, 15, 25)), (.5, (225, 70, 50)), (.75, (255, 175, 110)), (1, (255, 245, 225))]
DUO = [(0, (8, 3, 5)), (.35, (60, 8, 18)), (.65, (200, 40, 60)), (1, (255, 238, 215))]   # nero-rosso-crema
BW = [(0, (10, 8, 8)), (1, (250, 240, 228))]

def gmap(img, stops, mix):
    rgba = img.convert('RGBA'); a = np.asarray(rgba).astype(float) / 255
    L = .3 * a[..., 0] + .59 * a[..., 1] + .11 * a[..., 2]
    out = np.stack([np.interp(L, [s[0] for s in stops], [s[1][c] / 255 for s in stops]) for c in range(3)], -1)
    rgb = out * mix + a[..., :3] * (1 - mix)
    return Image.fromarray((np.clip(np.dstack([rgb, a[..., 3]]), 0, 1) * 255).astype('uint8'))

def load(f, c=1.1, b=1.05):
    return ImageEnhance.Brightness(ImageEnhance.Contrast(Image.open(REF + f).convert('RGB')).enhance(c)).enhance(b)

def jpg(im, name, q=90): im.convert('RGB').save(OUT + name, quality=q)

def clean_cut(path, stops, mix):
    im = Image.open(path).convert('RGBA'); a = np.asarray(im).astype(float)
    a[..., 3] = np.clip((a[..., 3] - 90) / 110, 0, 1) * 255      # via le zone semitrasparenti
    return gmap(Image.fromarray(a.astype('uint8')), stops, mix)

# Latin night
jpg(gmap(load('mamato-facciata-2.jpg', 1.12, 1.0), RED, .45), 'facciata-fuego.jpg', 92)
jpg(gmap(load('mamato-facciata-2.jpg', 1.15, 1.05).crop((40, 230, 1130, 1440)), DUO, .85), 'facciata-duo.jpg')
jpg(gmap(load('mamato-dj-neon.jpg', 1.1, 1.15).crop((80, 420, 1200, 1540)), RED, .3), 'pista-dj.jpg')
jpg(gmap(load('mamato-dj-neon.jpg', 1.15, 1.1).crop((0, 150, 1200, 1600)), RED, .35), 'pista-dj-full.jpg', 92)
# folla davanti al locale (foto di dicembre: solo la parte bassa, senza neon né albero)
crowd = load('mamato-facciata.jpg', 1.25, 1.45).crop((0, 1040, 930, 1455))
jpg(gmap(crowd, DUO, .9), 'folla-duo.jpg'); jpg(gmap(crowd, BW, 1), 'folla-bw.jpg')
# cena e karaoke
k = load('mamato-karaoke-cantante.jpg')
jpg(gmap(k.crop((0, 270, 1216, 1190)), WARM, .55), 'karaoke-cantante.jpg', 92)
jpg(gmap(k.crop((0, 600, 1216, 1250)), WARM, .55), 'karaoke-basso.jpg', 92)          # cornice per il pop-out
clean_cut(CUT + '/singer_isnet-general-use.png', WARM, .55).save(OUT + 'cut-cantante.png')  # crop (230,260)-(900,960)
jpg(gmap(load('mamato-cena-tovaglioli.jpg'), WARM, .3), 'cena-tovaglioli.jpg', 92)
jpg(gmap(load('mamato-cena-tovaglioli.jpg'), DUO, .85), 'cena-tovaglioli-duo.jpg')
jpg(gmap(load('mamato-cena-ragazze.jpg'), WARM, .3), 'cena-ragazze.jpg')
clean_cut(CUT + '/ragazze.png', WARM, .3).save(OUT + 'cut-ragazze.png')                  # crop (0,60)-(1250,988)
print('ok')
