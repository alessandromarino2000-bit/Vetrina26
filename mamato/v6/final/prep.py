# Final photo prep: one shared wine/rosso/amber grade for both posters, local light control,
# and per-board pre-scaling (Lanczos + mild unsharp) so the browser never resamples.
# Sources in reference/ are read-only; everything is written to final/img/.
import numpy as np
from PIL import Image, ImageFilter
R = '/home/user/Vetrina26/mamato/reference/'
O = '/home/user/Vetrina26/mamato/v6/final/img/'

def hexf(h): return np.array([int(h[i:i+2], 16) for i in (1, 3, 5)], np.float32) / 255
def smooth(x, a, b):
    t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

# palette ramp nero -> wine -> rosso -> amber -> crema
STOPS = [(0.00, '#070304'), (0.13, '#1e070c'), (0.36, '#6e1522'), (0.62, '#c64a33'), (0.85, '#f0b56e'), (1.00, '#fff1dc')]
def ramp(L):
    out = np.zeros(L.shape + (3,), np.float32)
    ps = [s[0] for s in STOPS]; cs = [hexf(s[1]) for s in STOPS]
    for c in range(3): out[..., c] = np.interp(L, ps, [x[c] for x in cs])
    return out

def ellipse(H, W, cx, cy, rx, ry):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    return np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)

def hue_shift(a, centre, width, amount, sat_mul=1.0):
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).convert('HSV')
    hsv = np.asarray(im).astype(np.float32)
    h = hsv[..., 0] * 360 / 255
    d = np.abs(((h - centre) + 180) % 360 - 180)
    w = np.clip(1 - d / width, 0, 1)
    # pull toward the target hue (centre + amount) instead of a flat rotation
    tgt = (centre + amount) % 360
    delta = ((tgt - h) + 180) % 360 - 180
    hsv[..., 0] = ((h + w * delta) % 360) * 255 / 360
    hsv[..., 1] = hsv[..., 1] * (1 - w * (1 - sat_mul))
    return np.asarray(Image.fromarray(hsv.astype(np.uint8), 'HSV').convert('RGB')).astype(np.float32) / 255

def finish(a, k_tone, sat):
    a = np.clip(a, 0, 1)
    L = a @ np.array([.2126, .7152, .0722], np.float32)
    a = L[..., None] + (a - L[..., None]) * sat
    a = a * (1 - k_tone) + ramp(L) * k_tone
    a = np.clip(a, 0, 1)
    a = a * a * (3 - 2 * a) * 0.45 + a * 0.55          # gentle filmic S
    a = np.minimum(a, 0.95) + np.maximum(a - 0.95, 0) * 0.35
    return a

# ---------------- LATIN: the DJ booth + crowd inside Mamatò (no Christmas decor) -------------
def latin():
    a = np.asarray(Image.open(R + 'mamato-dj-neon.jpg').convert('RGB')).astype(np.float32) / 255
    H, W, _ = a.shape                                    # 1200 x 1600
    # blue/violet ceiling + side wall -> plum/wine, so the frame lives in the brand family
    a = hue_shift(a, 260, 90, 85, 0.7)
    # neon sign + CDJ screens sit under the info block: pull them down to an ember glow
    neon = 1 - smooth(ellipse(H, W, 760, 1290, 520, 150), 0.55, 1.25)
    a = a * (1 - 0.8 * neon)[..., None]
    cdj = 1 - smooth(ellipse(H, W, 890, 1460, 190, 130), 0.5, 1.3)
    a = a * (1 - 0.8 * cdj)[..., None]
    # bright edge of the booth's glass top runs right under the title baseline: knock it back
    glass = 1 - smooth(ellipse(H, W, 900, 1022, 380, 45), 0.4, 1.2)
    a = a * (1 - 0.55 * glass)[..., None]
    # wall lettering (partial logo) at the far left: knock it back
    lg = 1 - smooth(ellipse(H, W, 40, 815, 130, 60), 0.5, 1.3)
    a = a * (1 - 0.7 * lg)[..., None]
    # the bar's pink backlight is the brightest thing up top: keep it, but not hotter than the title
    bar = 1 - smooth(ellipse(H, W, 900, 560, 260, 120), 0.4, 1.2)
    a = a * (1 - 0.18 * bar)[..., None]
    # faces in the crowd: tiny lift so people read as people
    crowd = 1 - smooth(ellipse(H, W, 640, 860, 560, 260), 0.3, 1.2)
    a = a * (1 + 0.35 * crowd)[..., None]
    # the room is very dark: open the shadows (soft lift + exposure) before toning
    a = np.clip(a * LEXP, 0, 1)
    a = 1 - (1 - a) ** 1.25
    return Image.fromarray((finish(a, 0.34, 0.88) * 255 + .5).astype(np.uint8))

# ---------------- KARAOKE: singer between the tables, relit and pulled into wine/amber ---------
def karaoke():
    src = Image.open(R + 'mamato-karaoke-cantante.jpg').convert('RGB').crop((0, 0, 1216, 1318))  # IG avatar cropped away
    a = np.asarray(src).astype(np.float32) / 255
    H, W, _ = a.shape
    # violet/lavender -> rose/wine
    a = hue_shift(a, 300, 85, 52, 0.8)
    a = a * 0.9
    # spotlight relight: the singer is the brightest point, the wall falls off
    d = ellipse(H, W, 0.42 * W, 0.40 * H, 0.42 * W, 0.40 * H)
    a = a * (0.50 + 0.50 * (1 - smooth(d, 0.4, 1.15)))[..., None]
    # bright pale wall right of the singer (between head and pillar): extra burn
    wall = 1 - smooth(ellipse(H, W, 0.70 * W, 0.30 * H, 0.18 * W, 0.26 * H), 0.2, 1.1)
    a = a * (1 - 0.35 * wall)[..., None]
    # raised hands / light wall at title height (lower-left quadrant): darken so the kicker reads
    hands = 1 - smooth(ellipse(H, W, 0.18 * W, 0.66 * H, 0.34 * W, 0.16 * H), 0.2, 1.2)
    a = a * (1 - 0.3 * hands)[..., None]
    # phone torch at the left edge
    torch = 1 - smooth(ellipse(H, W, 0.035 * W, 0.40 * H, 0.06 * W, 0.06 * H), 0.3, 1.3)
    a = a * (1 - 0.55 * torch)[..., None]
    a = np.clip(a, 0, 1) ** 1.06                       # deepen the haze over the tables
    return Image.fromarray((finish(a, KT, 0.8) * 255 + .5).astype(np.uint8))

KT = 0.7
LEXP = 1.25
# per board: (scale, left, top) -> exact-size image, nero fill outside the photo
BOARDS = {
    'latin-feed':    ('latin',   1.10, -120, -330),
    'latin-story':   ('latin',   1.20, -150,    0),
    'karaoke-feed':  ('karaoke', 1.06,  -90, -130),
    'karaoke-story': ('karaoke', 1.36, -300,    0),
}
SIZES = {'feed': (1080, 1350), 'story': (1080, 1920)}

if __name__ == '__main__':
    import sys
    srcs = {'latin': latin(), 'karaoke': karaoke()}
    for k, im in srcs.items(): im.save(O + f'{k}-graded.jpg', quality=94)
    for bid, (k, s, x, y) in BOARDS.items():
        im = srcs[k]
        w, h = round(im.width * s), round(im.height * s)
        if k == 'karaoke':   # the source is noisy: gentle median denoise before enlarging so faces stay clean
            im = Image.blend(im, im.filter(ImageFilter.MedianFilter(3)), 0.65)
        if s != 1: im = im.resize((w, h), Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=30, threshold=6))
        W, H = SIZES[bid.split('-')[1]]
        if y + h < H:   # photo ends above the board bottom: feather its last 180px into nero (no hard edge)
            arr = np.asarray(im).astype(np.float32)
            f = np.clip(np.arange(h)[::-1] / 180.0, 0, 1)[:, None, None]
            arr = arr * f + np.array([13, 6, 8], np.float32) * (1 - f)
            im = Image.fromarray(arr.astype(np.uint8))
        c = Image.new('RGB', (W, H), (13, 6, 8)); c.paste(im, (x, y))
        c.save(O + f'{bid}.jpg', quality=95)
        print(bid, w, h)
