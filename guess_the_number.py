import random 
import time
count = 1
def start():
    n=["G","A","M","E"," ","S","T","A","R","T"]
    for i in range(len(n)):
        print(n[i],end="")
        time.sleep(0.1)
    time.sleep(0.1)
    print()
    print()
    print()
    l=["L","o","a","d","i","n","g"]
    for i in range(len(l)):
        print(l[i],end="")
        time.sleep(0.1)
    time.sleep(0.1)
    for i in range(25):
        time.sleep(0.1)
        print(".",end="")
    time.sleep(0.1)
    for i in range(10):
        print()
    time.sleep(0.1)
def game_crash():
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","z","x","y","z" ,
       "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
       "~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","|","\\","\'","\"",":",";",",","<",".",">","/","?",
       "1","2","3","4","5","6","7","8","9","0"]
    alen=len(a)
    for i in range(alen*2000):
        crash=random.randint(0,alen-1)
        if i%160 ==0:
              print()
        print(a[crash],end="")
    print()
    print()
    time.sleep(2)
    print("now you can play the game")
    time.sleep(2)
    global f
    f=1
    start()
def new_start():
    print()
    a=["O","N","E"," ","M","O","R","E"," ","G","A","M","E"]
    print("               ",end="")

    for i in range(len(a)):
        time.sleep(0.1)
        print(a[i],end="")
    print()
    print()
    print()
    time.sleep(0.1)
        
def user_input():
    ui=["E","n","t","e","r"," ","a","n","y"," ","n","u","m","b","e","r"," ","b","e","t","w","e","e","n"," ","(","1"," ","t","o"," ","1","0"," ",")",":"]
    for i in range(len(ui)):
        time.sleep(0.04)
        print(ui[i],end="")
    user_guess=int(input())
    print()
    time.sleep(0.1)
    if user_guess > 10 or user_guess < 0:
        f0=["S","o","r","r","y",","," ","t","h","e"," ","r","a","n","g","e"," ","i","s"," ","0"," ","t","o"," ","1","0"," ","o","n","l","y"," "," ",","," ","b","u","t"," ","y","o","u"," ","e","n","t","e","r"]
        for i in range(len(f0)):
            time.sleep(0.06)
            print(f0[i],end="")
        print(" ",user_guess)
        time.sleep(0.01)
        f01=["P","l","e","a","s","e"," ","c","o","r","r","e","c","t"," ","t","h","e"," ","m","i","s","t","a","k","e"]
        for i in range(len(f01)):
            time.sleep(0.06)
            print(f01[i],end="")
        print()
        time.sleep(0.1)
        test=True
        fun=1
        while test:
            for i in range(len(ui)):
                time.sleep(0.04)
                print(ui[i],end="")
            user_guess=int(input())
            print()
            time.sleep(0.1)
            
            if user_guess <= 10 and user_guess >= 0:
                test=False
                break
            else:   
                test=True 
                f1=["a","r","e"," ","y","o","u"," ","a"," ","h","u","m","a","n"," ","b","e","i","n","g"," ","?"
                    ," "," ","y","o","u"," ","d","o"," ","n","o","t"," ","k","n","o","w","n"," ","t","h","e"," ","s","i","m","p","l","e"
                    ," ","n","u","m","b","e","r"," ","b","e","t","w","e","e","n"," ","0"," ","t","o"," ","1","0"," "]
                #24
                f11=["o","k"," ",","," ","p","l","e","a","s","e"," ","e","n","t","e","r"," ","t","h","e"," ","n","u","m","b","e","r"]
                if fun == 1:
                    for i in range(len(f1)):
                        time.sleep(0.06)
                        print(f1[i],end="")
                        if i == 24:
                            print()         
                    fun+=1
                    time.sleep(0.4)
                    print()
                    for i in range(len(f11)):
                        print(f11[i],end="")
                        time.sleep(0.06)
                    print()
                    time.sleep(0.2)
                elif fun == 2 :
                    f2=["I"," ","t","h","i","n","k"," ","y","o","u"," ","l","o","s","t"," ","y","o","u","r"," ","m","i","n","d"]
                    f21=["T","a","k","e"," ","s","o","m","e"," ","t","i","m","e"," ","t","o"," ","e","n","t","e","r"," ","t","h","e"," ","n","u",
                         "m","b","e","r"]
                    fun+=1
                    for i in range(len(f2)):
                        time.sleep(0.06)
                        print(f2[i],end="")
                    print()
                    time.sleep(0.5)
                    for i in range(len(f21)):
                        time.sleep(0.06)
                        print(f21[i],end="")
                    print()
                    time.sleep(0.5)
                elif fun == 3:
                    f3=["y","o","u"," ","h","a","v","e"," ","t","h","e"," ","b","e","s","t"," ","b","r","a","i","n"]
                    f31=["o","k"," ",","," ","i"," ","t","e","l","l"," ","t","h","e"," ","n","u","m","b","e","r"," ","b","e","t","w","e","e"
                         ,"n"," "," ","0"," ","t","o"," ","1","0"," "]
                    f32=["(","0"," ","t","o"," ","1","0",")"," ","i","s"," 1"," ",","," ","2"," ",","," ","3"," ",","," ","4"," ",","," ","5"," ",","," ","6"," "
                         ,","," ","7"," ",","," ","8"," ",","," ","9"," ",","," ","1","0"," "]
                    fun+=1
                    for i in range(len(f3)):
                        time.sleep(0.06)
                        print(f3[i],end="")
                    print()
                    time.sleep(0.5)
                    for i in range(len(f31)):
                        time.sleep(0.06)
                        print(f31[i],end="")
                    print()
                    time.sleep(0.5)
                    
                    for i in range(len(f32)):
                        time.sleep(0.06)
                        print(f32[i],end="")
                    print()
                    time.sleep(0.5)
                else :
                    fun+=1
                    gacr=["G","A","M","E"," ","I","S"," ","C","R","A","S","H"]
                    for i in range(len(gacr)):
                        print(gacr[i],end="")
                        time.sleep(0.1)
                    print()
                    print()
                    time.sleep(2)
                    game_crash()
                
    return user_guess
def computer_input():
    computer_guess=random.randint(0,10)
    return computer_guess
def control(user_guess,computer_guess,count):
    game_over=False
    userst=["u","s","e","r","_","i","n","p","u","t",":"]
    compstr=["c","o","m","p","u","t","e","r","_","i","n","p","u","t",":"]
    if user_guess == computer_guess :
        overstr=["G","A","M","E"," ","O","V","E","R"]
        for i in range(len(overstr)):
            time.sleep(0.06)
            print(overstr[i],end="")
        time.sleep(0.1)
        print()
        print()
        for i in range(len(userst)):
                print(userst[i],end="")
                time.sleep(0.06)
        print(user_guess,end="")
        for  i in range(8):
            print(" ",end="")
            time.sleep(0.06)
        for i in range(len(compstr)):
                print(compstr[i],end="")
                time.sleep(0.06)
        print(computer_guess)
        time.sleep(0.1)
        print()
        print(f"round of win is {count}")
        game_over=True
    else:
        if abs(user_guess-computer_guess) <3:
            close=["I","t"," ","i","s"," ","c","l","o","s","e"," ","c","a","l","l"," ","b","r","o"]
            for i in range(len(close)):
                time.sleep(0.06)
                print(close[i],end="")
            time.sleep(0.3)
            print()
            print()
            time.sleep(0.1)
            for i in range(len(userst)):
                print(userst[i],end="")
                time.sleep(0.06)
            print(user_guess,end="")
            for  i in range(8):
                print(" ",end="")
                time.sleep(0.06)
            for i in range(len(compstr)):
                print(compstr[i],end="")
                time.sleep(0.06)
            print(computer_guess)
        else:
            not_close=["I","t"," ","i","s"," ","n","o","t"," ","a"," ","c","l","o","s","e"," ","c","a","l","l"," ","b","r","o"]
            for i in range(len(not_close)):
                time.sleep(0.06)
                print(not_close[i],end="")
            print()
            print()
            time.sleep(0.3)
            for i in range(len(userst)):
                print(userst[i],end="")
                time.sleep(0.06)
            print(user_guess,end="")
            for  i in range(8):
                print(" ",end="")
                time.sleep(0.06)
            for i in range(len(compstr)):
                print(compstr[i],end="")
                time.sleep(0.06)
            print(computer_guess)
        print()
        win=["N","U","M","B","E","R"," ","O","F"," ","W","I","N"," ",":"," "]
        for i in range(len(win)):
            time.sleep(0.06)
            print(win[i],end="")
        time.sleep(0.1)
        print(count)
        time.sleep(0.1)
        game_over=False
        
    if not game_over:
        return True
    else:
        return False






run=True
start() 
while run:
    
    user_guess=user_input()      
    computer_guess=computer_input()
    run=control(user_guess,computer_guess,count)
    if run:
        count = count + 1
        new_start()
        
    
        
    
