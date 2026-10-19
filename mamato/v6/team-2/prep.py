from PIL import Image, ImageFilter
import numpy as np
A='/home/user/Vetrina26/mamato/assets/'
bg=Image.open(A+'bg-d-cantante.jpg').convert('RGB')
cut=Image.open(A+'cut-cantante.png')
al=np.array(cut)[...,3].astype(float)/255
h,w=al.shape
yy,xx=np.mgrid[0:h,0:w]
# fade out below chest, remove crowd hand at lower-left
fade=np.clip((480-yy)/50,0,1)
hand=((xx<215)&(yy>350))
al=al*fade; al[hand]=0
# slight erosion+feather for clean edge
m=Image.fromarray((al*255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
full=Image.new('L',bg.size,0); full.paste(m,(230,260))
fg=bg.copy(); fg.putalpha(full)
fg.save('img/k-fg.png')
bg.save('img/k-bg.jpg',quality=95)
