#!/usr/bin/env python
# coding: utf-8

# In[129]:


def setd():
    mridd = {} # dictionary add valu
    for i in range(1,22):
        kub = 'k' + str(i)
        mridd.update({kub : " "})
    mridd.update({"k32" : "|"})
    mridd.update({"k33" : "|"})
    mridd.update({"k34" : "--"})
    mridd.update({"k35" : "--"})
    mridd.update({"k36" : "---"})
    mridd.update({"k10" : "|"})
    mridd.update({"k11" : "|"})
    mridd.update({"k14" : "--"})
    mridd.update({"k15" : "--"})
    mridd.update({"k16" : "---"})
    mridd.update({"k18" : "|"})
    mridd.update({"k20" : "|"})
    return mridd

def wbord(mridd):
    from IPython.display import clear_output
    print(mridd["k1"]  +" " + mridd["k32"] + mridd["k2"] + mridd["k33"] + mridd["k3"])
    print(mridd["k34"] + mridd["k35"] + mridd["k36"])
    print(mridd["k4"] + " " +mridd["k10"]  + mridd["k5"] +mridd["k11"] + mridd["k6"])
    print(mridd["k14"] + mridd["k15"] + mridd["k16"])
    print(mridd["k7"] + " " +mridd["k18"]  + mridd["k8"] + mridd["k18"] +mridd["k9"])
    
def chekwin2(up,mridd):
    win = "no"
    if mridd["k1"] == up and mridd["k2"] == up and  mridd["k3"] == up:
        win = "yes"
        return True
    if mridd["k4"] == up and mridd["k5"] == up and  mridd["k6"] == up:
        win = "yes"
        return True
    if mridd["k7"] == up and  mridd["k8"] == up and  mridd["k9"] == up:
        win = "yes"
        return True
    if mridd["k1"] == up and mridd["k4"] == up and  mridd["k7"] == up:
        win = "yes"
        return True
    if mridd["k2"] == up and mridd["k5"] == up and  mridd["k8"] == up:
        win = "yes"
        return True
    if mridd["k3"] == up and mridd["k6"] == up and  mridd["k9"] == up:
        win = "yes"
        return True
    if win == "no":
        return False
        
def chekwin(up,bord):
    win = "no"
    #print(sum([1 for i in list(bord)[0:3:] if  bord[i] == up]),"<<<<<<")
    if int(sum([1 for i in list(bord)[0:3:] if bord[i] == up])) == 3: #cell 1,2,3
        win = "yes"
    if int(sum([1 for i in list(bord)[3:6:] if bord[i] == up])) == 3:   #cell 4,5,6
        win = "yes"
    if int(sum([1 for i in list(bord)[6:9:] if bord[i] == up])) == 3:   #cell 7,8,9
        win = "yes"
    if int(sum([1 for i in list(bord)[0:10:3] if bord[i] == up])) == 3: #cell 1, 4, 7
        win = "yes"
    if int(sum([1 for i in list(bord)[1:10:3] if bord[i] == up])) == 3:   #cell 2, 5, 8
        win = "yes"
    if int(sum([1 for i in list(bord)[2:10:3] if bord[i] == up])) == 3:   #cell 3, 6, 9
        win = "yes"        
    if int(sum([1 for i in list(bord)[0:10:4] if bord[i] == up])) == 3:   #cell 1, 5, 9
        win = "yes"    
    if int(sum([1 for i in list(bord)[2:8:2] if bord[i] == up])) == 3:   #cell 3, 5, 7
        win = "yes"  
    if win == "yes":
        return True

def celectcell(up,bord,cellist):
    from random import randint
    import random
    pcnum = 0
    if pcnum == 0 or len(cellist) < 2:
        pcnum = int(random.choice(cellist))
        
    if int(sum([1 for i in list(bord)[0:3:] if bord[i] == up])) == 2: #cell 1,2,3
        print(cellist[0:3:],"<<<<<1")
        while not(pcnum > 0 and pcnum < 4):
            pcnum = int(random.choice(cellist[0:3:])) #find the emty cell in the line that as 2 other cell           
    if int(sum([1 for i in list(bord)[3:6] if bord[i] == up])) == 2: #cell 4,5,6
        print(cellist[3:6:],"<<<<2")
        while not(pcnum > 3 and pcnum < 7):
            pcnum = int(random.choice(cellist[3:6:]))
    if int(sum([1 for i in list(bord)[6:9:] if bord[i] == up])) == 2:   #cell 7,8,9
        print(cellist[6:9:],"<<<<3")
        while not(pcnum > 6 and pcnum < 10):
            pcnum = int(random.choice(cellist[6:9:]))
    return pcnum
        
    
    
    
def game():
    from IPython.display import clear_output
    from random import randint
    import random
    status = "start"
    cellist = list(range(1,10))
    check = lambda x : x in cellist #check if the number in the list
    bord = setd()
    choose = (input('Please select a X/O:')).upper()

    if choose == 'X':
        chooseu = 'X'
        choosepc = 'O'
    elif choose == 'O':
        chooseu ='O'
        choosepc = 'X'
    else:
        print('Error not select X/O')
        
    
    while(status == "start"):
        if chooseu:
            turn = "player"
            while(turn == "player" and len(cellist) >= 1):
                userselect = True
                while userselect:
                    wbord(bord)
                    cell = input('Please select a cell: ')
                    try:
                        if(int(cell)):
                            if check(int(cell)):
                                cellist.remove(int(cell))
                                userselect = False
                                print(f"OK you selet cell: {cell}")
                                bordcell = "k" + str(cell)
                                bord.update({bordcell : str(chooseu)})
                                #clear_output()
                                if chekwin(str(chooseu),bord):
                                    clear_output()
                                    wbord(bord)
                                    print("You Win !!")
                                    turn = "end"
                                    status = "end"
                                else:
                                    turn = "pc"
                                
                            else:

                                # ##### cellist

                                # In[90]:

                                if 2 in cellist:
                                    print("ok")

                                # In[4]:

                                check = lambda x: x in cellist

                                # In[14]:

                                print(check(2))

                                # In[2]:

                                list(range(1, 2))

                                # In[40]:

                                len(cellist)

                                # In[ ]:

                                mylist
                                print(f"Error the number {cell} that you selet is not available try again:")
                    except ValueError:
                        print("That's not an nomber! try again:")
                        
            while(turn == "pc" and len(cellist) >= 1):
                pcnum = str(celectcell(chooseu,bord,cellist))
                print(f"OK i will select: {pcnum}")
                bordcell = ("k" + pcnum)
                bord.update({bordcell : str(choosepc)})
                if chekwin(str(choosepc),bord):
                    print("I Win !!")
                    turn = "end"
                    status = "end"
                else:
                    turn = "player"
                
                
    
        if len(cellist) == 0:
            print("hhhh")
            break
game()

