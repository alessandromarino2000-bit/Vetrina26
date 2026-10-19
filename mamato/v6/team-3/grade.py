# Filmic "warm night" grade shared by both posters (team-3 / Cinema).
import numpy as np
from PIL import Image, ImageFilter
import sys
SRC='/home/user/Vetrina26/mamato/reference/'
OUT='/home/user/Vetrina26/mamato/v6/team-3/img/'

def hexf(h): return np.array([int(h[i:i+2],16) for i in (1,3,5)],float)/255

def tritone(L, stops):
    # stops: list of (pos, rgb)
    out=np.zeros(L.shape+(3,))
    ps=[s[0] for s in stops]
    for c in range(3):
        out[...,c]=np.interp(L,ps,[s[1][c] for s in stops])
    return out

def smooth(x,a,b):
    t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)

def grade(img, k_tone, expo, spot=None, spot_r=0.6, spot_floor=0.35, sat=0.9, stops=None, lift=0.0, ax=1.0):
    a=np.asarray(img.convert('RGB'),float)/255
    a=a**(1/1.0)
    H,W,_=a.shape
    # exposure
    a=a*expo
    # spotlight relight: darken away from subject
    if spot is not None:
        yy,xx=np.mgrid[0:H,0:W]
        d=np.sqrt(((xx-spot[0]*W)/(W*ax))**2+((yy-spot[1]*H)/(H))**2)
        m=1-smooth(d,spot_r*0.25,spot_r)
        a=a*(spot_floor+(1-spot_floor)*m)[...,None]
    a=np.clip(a,0,1)
    L=0.2126*a[...,0]+0.7152*a[...,1]+0.0722*a[...,2]
    # saturation
    a=L[...,None]+(a-L[...,None])*sat
    tone=tritone(L,stops)
    a=a*(1-k_tone)+tone*k_tone
    # filmic s-curve
    a=np.clip(a,0,1)
    a=a+lift*(1-a)*0  # placeholder
    a=0.5+ (a-0.5)*1.0
    a=np.where(a<0.5, 2*a*a*0.5+a*0.5, a)  # deepen shadows a bit
    return Image.fromarray((np.clip(a,0,1)*255).astype('uint8'))

STOPS=[(0.0,hexf('#070304')),(0.12,hexf('#1c070b')),(0.35,hexf('#6b1420')),(0.62,hexf('#c4482f')),(0.85,hexf('#f2b36a')),(1.0,hexf('#fff1dc'))]

if __name__=='__main__':
    # LATIN: DJ booth / neon / crowd
    im=Image.open(SRC+'mamato-dj-neon.jpg')
    # burn the bright CDJ screen (bottom-right) so it does not compete with the neon
    a=np.asarray(im.convert('RGB'),float)
    yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]
    d=np.sqrt(((xx-890)/170.)**2+((yy-1460)/120.)**2)
    a=a*(0.25+0.75*smooth(d,0.6,1.4))[...,None]
    im=Image.fromarray(a.astype('uint8'))
    g=grade(im,k_tone=0.5,expo=1.0,sat=0.8,stops=STOPS)
    g.save(OUT+'latin.jpg',quality=93)
    # KARAOKE: singer (crop away IG avatar bottom-left)
    im=Image.open(SRC+'mamato-karaoke-cantante.jpg').crop((0,0,1216,1318))
    g=grade(im,k_tone=0.78,expo=0.80,spot=(0.42,0.42),spot_r=0.58,spot_floor=0.12,sat=0.8,stops=STOPS,ax=1.35)
    g.save(OUT+'karaoke.jpg',quality=93)
    print('ok')
