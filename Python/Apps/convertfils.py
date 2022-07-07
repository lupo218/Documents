import os.path
import pandas as pd
from os import walk
import os
import glob
import pathlib

mypath = '\\\xxx\\x\\'
dst = '\\\xxx\\x\\'
def convert(file,dst):
    try:
        csvfile = file.name.replace(str(file).split('.')[-1], "csv") # rename file type to csv
        read_file = pd.read_excel(str(file))
        newdts = os.path.join(dst,csvfile)
        read_file.to_csv (newdts, index = None, header=True ,encoding = "ISO-8859-8")
    except:
        pass
    # os.remove(sys.argv[1])


for file in list(pathlib.Path(mypath).glob('*.xlsx')):
    convert(file,dst)
