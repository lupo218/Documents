import requests
from datetime import datetime

def checkurl(url):
    rec = requests.get(url)
    print(rec)

#checkurl("http://127.0.0.1:5000/content/F:/temp/words.txt")


# with open("f:\\temp\\1.txt", 'w') as newfile:
#      newfile.write("guy")
#
# with open("f:\\temp\\1.txt", 'r') as newfile:
#     contetnd = newfile.read()
#     print(contetnd)
# now = datetime.now()
# with open("f:\\temp\\1.txt", 'w') as newfile:
#     newfile.write(F' Hello my name is guy and tha date is {now.strftime("%Y%D")}')

def wname(x):
    with open("f:\\temp\\1.txt", 'w') as newfile:
      newfile.write(x)

def rname():
    with open("f:\\temp\\1.txt", 'r') as newfile:
        con = newfile.read()
        print(con)

# wname("guy")
# rname()


def chek_empty(file):
    with open(file, 'r') as newfile:
        con = newfile.read()
        if len(con) > 0:
            print("file is not empty ")
        else:
            print("file is empty ")
#chek_empty("f:\\temp\\1.txt")

def readline(file,line):
    with open(file, 'r') as newfile:
        con = newfile.read()
    print(con.split("\n")[line])

#readline("f:\\temp\\1.txt",3)


# file = "f:\\temp\\1.txt"
def maxword(file):
    with open(file, 'r') as newfile:
        con = newfile.read()
        mylist = list(con.split(" "))
    tnum = 0
    for i in mylist:
        if len(i) > tnum:
            tnum = len(i)
            word  = i
    print(word)
#maxword("f:\\temp\\1.txt")



def countword(file,word):
    with open(file, 'r') as newfile:
        con = newfile.read().lower()
        mylist = list(con.split(" "))
        print(mylist.count(word.lower()))
#countword("f:\\temp\\1.txt","The")




# mylist = con.split(" ")
# print(mylist)
# print((len(mylist[0])))