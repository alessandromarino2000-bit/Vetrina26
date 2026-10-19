import sys
from PIL import Image
d='/home/user/Vetrina26/mamato/v6/final/export/'
ims=[Image.open(d+n+'.png') for n in ['latin-feed','karaoke-feed','latin-story','karaoke-story']]
# thumbs at ~ Instagram grid size
t=Image.new('RGB',(4*300+50,560),(30,30,30));x=10
for im in ims:
    w=300 if im.height==1350 else 300; h=int(im.height*w/1080)
    t.paste(im.convert('RGB').resize((w,h),Image.LANCZOS),(x,10)); x+=w+10
t.save('/home/user/Vetrina26/mamato/v6/final/work/thumbs.png')
