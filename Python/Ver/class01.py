def swap(var1, var2):
    var3 = var1
    var1 = var2
    var2 = var3
    print(var1 ,var2)

def swap2(*args):
    if(len(args) == 2):
     print(args[::-1])


def cubes(*args):
    mylist = []
    print('Enter value:')
    mylist.append(int(input()))
    print("Eenter the second value")
    mylist.append(int(input()))
    print((sum(mylist))**3)


def equal():
    mylist = []
    print('Enter value:')
    mylist.append(int(input()))
    print("Enter the second value")
    mylist.append(int(input()))
    print("Enter the third value")
    mylist.append(int(input()))

    newlist = list(([x for x in mylist if mylist.count(x) > 1]))
    try:
        print(newlist[0])
    except:
        pass

def minf(*args):
    mylist = []
    print('Enter value:')
    mylist.append(int(input()))
    print("Enter the second value")
    mylist.append(int(input()))
    print("Enter the third value")
    mylist.append(int(input()))

    print(min(mylist))


#swap(44,77)
#swap2(44,77)
#cubes()
equal()
#minf()
