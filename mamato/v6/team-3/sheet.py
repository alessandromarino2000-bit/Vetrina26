from PIL import Image
import sys
E='/home/user/Vetrina26/mamato/v6/team-3/export/'
names=['latin-feed','karaoke-feed','latin-story','karaoke-story']
ims=[Image.open(E+n+'.png').convert('RGB') for n in names]
h=900
row=[im.resize((int(im.width*h/im.height),h)) for im in ims]
W=sum(r.width for r in row)+30*5
s=Image.new('RGB',(W,h+60),(40,40,40));x=30
for r in row: s.paste(r,(x,30)); x+=r.width+30
s.save('/home/user/Vetrina26/mamato/v6/team-3/work/sheet.jpg',quality=88)
# thumbnails (instagram grid size ~ 180px)
t=Image.new('RGB',(2*200+30,260),(255,255,255))
for i,n in enumerate(['latin-feed','karaoke-feed']):
    im=Image.open(E+n+'.png').convert('RGB').resize((180,225),Image.LANCZOS); t.paste(im,(10+i*210,15))
t.save('/home/user/Vetrina26/mamato/v6/team-3/work/thumbs.png')
