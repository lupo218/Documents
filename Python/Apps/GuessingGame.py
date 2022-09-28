import sys , random

#first = int(sys.argv[1]) #get parameter frome the cmd
first = 1
second = 5
#second = int(sys.argv[2])
numlist = list(range(first, second))
shufflelist = numlist.copy() #copy the list to new list in memory
#random.shuffle(shufflelist)

class nummem(): # kiping track of the list
    def __init__(self,numlist):
        self.numlist = numlist
    def keeplist(self,num):
        self.num = num
        self.numlist.remove(int(num))

a= nummem(shufflelist) #lode the c3lass
pinput = random.choice(a.numlist)
while True:
    while True: # check for valid input
        try:
            Uinput = int(input(f"Select a number from: {a.numlist}"))
            if Uinput in a.numlist:
                break
            else:
                print(f"you need to type a number from: {a.numlist}")
        except:
            print(f"you need to type a number from: {a.numlist}")
            continue

    if int(Uinput) == int(pinput):
        print("You succeeded")
        break
    else:
        print("Sorry not the correct number please try again" )
        a.keeplist(Uinput)




