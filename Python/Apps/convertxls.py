import pandas as pd
import sys , os

csvfile = sys.argv[1].replace("xls", "csv")

read_file = pd.read_excel(sys.argv[1])
read_file.to_csv (csvfile, index = None, header=True ,encoding = "ISO-8859-8")
os.remove(sys.argv[1])
