import sys; sys.path.insert(0,'/home/user/Vetrina26/mamato/v6/final')
import prep
from PIL import Image
out=Image.new('RGB',(1500,550))
for i,k in enumerate([0.62,0.7,0.78]):
    prep.KT=k; im=prep.karaoke(); out.paste(im.resize((500,542)),(i*500,0))
out.save('/home/user/Vetrina26/mamato/v6/final/work/ktest.jpg',quality=88)
