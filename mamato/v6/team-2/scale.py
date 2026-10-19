# Pre-render each board's photo at its exact on-poster size with Lanczos + gentle unsharp mask,
# cropped to the board, so the browser does no resampling.
from PIL import Image, ImageFilter
B={'karaoke-feed':(1350,1476,-118,-10,1080,1350),'karaoke-story':(1970,2155,-389,-2,1080,1920),
   'latin-feed':(1200,1967,-60,-618,1080,1350),'latin-story':(1268,2079,-94,-473,1080,1920)}
SRC={'karaoke':('img/k-bg-d.jpg','img/k-fg-d.png'),'latin':('img/lc-bg-g2.jpg',None)}
for bid,(w,h,x,y,W,H) in B.items():
    bg,fg=SRC[bid.split('-')[0]]
    for f,suf in ((bg,'bg'),(fg,'fg')):
        if not f: continue
        im=Image.open(f); im=im.convert('RGBA' if suf=='fg' else 'RGB')
        im=im.resize((w,h),Image.LANCZOS)
        if suf=='bg': im=im.filter(ImageFilter.UnsharpMask(radius=1.6,percent=45,threshold=3))
        else:
            # take the colour from the already-scaled background so both layers are pixel-identical
            a=Image.new('L',(W,H),0); a.paste(im.getchannel('A'),(x,y))
            canvas=bgc.copy(); canvas.putalpha(a)
            out=f'img/{bid}-fg.png'; canvas.save(out); print(out); continue
        canvas=Image.new(im.mode,(W,H),(13,6,8))
        canvas.paste(im,(x,y)); bgc=canvas
        out=f'img/{bid}-{suf}.'+('png' if suf=='fg' else 'jpg')
        canvas.save(out,quality=95) if suf=='bg' else canvas.save(out)
        print(out)
