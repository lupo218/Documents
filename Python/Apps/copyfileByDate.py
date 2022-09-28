from pathlib import Path
import arrow,shutil
filepath = "\\\\xxx\\TRANS\\Services"
filedts = '\\\\192.168.42.10\\ftp\\PrimeLease'
daystocut = -2
filetime = arrow.now().shift(days= daystocut)


def filetocopy(filepath,filedts,daystocut):
    filetime = arrow.now().shift(days=daystocut)
    for _ in Path(filepath).glob('*'):
        if _.is_file():
            if arrow.get(_.stat().st_atime) > filetime:
                print(_.resolve())
                print(filedts)
                shutil.copy(_, filedts ,follow_symlinks=False)








filetocopy(filepath,filedts,daystocut)