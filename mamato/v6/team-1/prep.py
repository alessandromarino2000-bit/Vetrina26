# Crops + shared "fashion" grade for both posters (derived files only, sources untouched)
import numpy as np
from PIL import Image, ImageFilter
R='/home/user/Vetrina26/mamato/reference/'
O='/home/user/Vetrina26/mamato/v6/team-1/img/'

def grade(im, cool2warm=0.0, expo=1.0, sat=0.85):
    a=np.asarray(im.convert('RGB')).astype(np.float32)/255.
    a=a*expo
    if cool2warm:  # rotate violet hues toward plum/magenta so both photos sit in one red family
        from PIL import Image as I
        hsv=np.asarray(I.fromarray((np.clip(a,0,1)*255).astype(np.uint8)).convert('HSV')).astype(np.float32)
        h=hsv[...,0]*360/255
        w=np.clip(1-np.abs(h-268)/45,0,1)          # only violets/blues
        h=h+w*cool2warm
        hsv[...,0]=(h%360)*255/360
        hsv[...,2]=hsv[...,2]*(1-w*0.10)
        a=np.asarray(I.fromarray(hsv.astype(np.uint8),'HSV').convert('RGB')).astype(np.float32)/255.
    lum=(a@np.array([.2126,.7152,.0722],np.float32))[...,None]
    a=lum+(a-lum)*sat
    # filmic contrast: S-curve, soft shoulder
    a=np.clip(a,0,1)
    a=a*a*(3-2*a)*0.55+a*0.45
    a=np.minimum(a,0.94)+np.maximum(a-0.94,0)*0.4
    # split tone: shadows -> wine/nero, highlights -> warm cream
    lum=(a@np.array([.2126,.7152,.0722],np.float32))[...,None]
    sh=np.array([0.07,0.02,0.035],np.float32); hi=np.array([1.0,0.94,0.86],np.float32)
    ws=np.clip(1-lum*2.2,0,1)**1.5; wh=np.clip((lum-0.55)/0.45,0,1)
    a=a*(1-ws*0.55)+sh*ws*0.55
    a=a*(1-wh*0.18)+hi*lum*wh*0.18
    return Image.fromarray((np.clip(a,0,1)*255+0.5).astype(np.uint8))

# LATIN: clean facade; cut the street sign (top) and the watermark (bottom)
f=Image.open(R+'mamato-facciata-pulita.jpg').crop((0,372,1206,1462))
grade(f,0.0,1.06,0.92).filter(ImageFilter.UnsharpMask(1.4,55,2)).save(O+'latin.jpg',quality=95)
# KARAOKE: singer between the tables; crop away the IG avatar bottom-left
k=Image.open(R+'mamato-karaoke-cantante.jpg').crop((0,0,1216,1330))
grade(k,38,0.93,0.8).filter(ImageFilter.UnsharpMask(1.6,70,2)).save(O+'karaoke.jpg',quality=95)
print('ok')
