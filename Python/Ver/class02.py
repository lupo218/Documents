#A
def big(a,b):
    if int(a) > int(b):
       print('A is bigger')
    elif int(a) == int(b):
        print('They are equal')
    else:
        print('B is bigger')

#big(8,7)

#B
def loop(x):
 for x in range(x):
     print(x)

#loop(5)

#C
def seasons(x):
    if x == 1:
        print('summer')
    elif x == 2:
        print('winter')
    elif x == 3:
        print('fall')
    elif x == 4:
        print('spring')
    else:
        print(f'The number {x} does not match')
#seasons(4)


#D
#  1. 10
#  2. 10


#E
def fly():
    import requests , sys
    my_dict = {}
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()

    my_dict['currency'] = data["rates"]["ILS"]

    print('Enter your age:')
    my_dict['age'] = int(input())
    print('Enter your last name:')
    my_dict['lasname'] = input()[0]
    print('Did you flew abroad Yes/No')

    abroad = (input()).lower()

    if abroad == 'yes':
        abroad = True
    elif abroad == 'no':
        abroad = False
    else:
        print('I did not understand the answer GoodBy...')
        sys.exit()

    print('Enter apartment number:')
    my_dict['apartment'] = input()

    print(my_dict)
    print(f'Your age {my_dict["age"]} plus the currency {data["rates"]["ILS"] } is equal to: {(float(my_dict["age"]) + float(my_dict["currency"]))}')

#fly()

#F
def phone():
    print('Enter your phone number')
    print(f'Phone number:{input()}')
#phone()


#G
def printHello():
    print('hello')
#printHello()

def calculate():
    print(f'{float(5) + float(3.2)}')

#calculate()

#H

def name(n):
    print(n)

#name("guy")

def clac(x):
    print(f'{x/2}')
#clac(8)


#I

def calc3(n1,n2):
    print(f'{float(n1) + float(n2)}')

#calc3(5,10)


def Strings(s1,s2):
    print(f'{s1} {s2}')

Strings("Hi","Doron")





#K

def pyramid():
    for a in range(1,10,2):
        print("x" * a)
#pyramid()


#L
def drow(N):
    for i in range(N):
        for j in range(N):
            if (i == j) or ((N - j -1) == i):
                print('x', end = '')
            else:
                print(' ', end = '')
        print('')

#drow(5)

#M
def input1():
    def uinput():
        print('Enter number:')
        x = str(input())
        return x
    x = uinput()
    print(f'The sum of the digits is {int(x[0]) + int(x[1])} ')

#input1()


