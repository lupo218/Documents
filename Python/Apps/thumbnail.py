from PIL import Image , ImageFilter
from pathlib import Path
import sys , os

def convert(sdir ,dtsdir):
    if os.path.isdir(dtsdir):
        print(f"{dtsdir} is OK")
    else:
        os.mkdir(dtsdir)
        print(f" I heve create this DIR {dtsdir}")


    for _ in Path(sdir).glob('*'):
        if _.is_file():
            oldname = sdir + _.name
            print(_.absolute())
            f_img =Image.open(_)
            f_img.thumbnail((70, 70))
            fname = _.stem + ".png"
            newfullname  = dtsdir +"\\" + fname
            f_img.save(newfullname , "png")




sdir = sys.argv[1]
dstdir = sys.argv[2]
#convert("f:\\temp2\\" ,"f:\\temp2\\resize\\")
convert(sdir , dstdir)
#"f:\\temp2\\resize\\"
#f:\\temp2\\