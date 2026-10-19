# Bake the series grade: deep warm blacks, controlled highlights, violet nudged to plum.
from PIL import Image
import numpy as np, sys
def grade(arr, gamma=2.2, blue=0.9, red=1.04, lift=(13,6,8), sat=1.0):
    a = arr.astype(float)/255
    a = a**gamma
    a[...,0]*=red; a[...,2]*=blue
    l = a.mean(2,keepdims=True)
    a = l + (a-l)*sat
    a = np.clip(a,0,1)
    lift=np.array(lift)/255
    a = lift + a*(1-lift)
    return (np.clip(a,0,1)*255+.5).astype(np.uint8)
if __name__=='__main__':
    src,dst,g,b,r,s=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:7])
    im=Image.open(src); mode=im.mode
    arr=np.array(im.convert('RGBA'))
    arr[...,:3]=grade(arr[...,:3],g,b,r,sat=s)
    out=Image.fromarray(arr,'RGBA')
    (out if dst.endswith('.png') else out.convert('RGB')).save(dst,quality=95)
