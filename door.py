from sys import exit
import time
import random

print("Welcome to door game!")
print("This game is only for people who have a brain and luck. Are you sure you want to put it to the test?")

def gold():
    print("Welcome to gold room.")
    time.sleep(0.3)
    print("There are three pedestals in front of you choose wisely.")
    time.sleep(0.5)
    print("\n1. The one who seeks without caution will fall into darkness. \n2. The one who values gold above all will meet their end. \n3. The one who chooses wisely shall be rewarded.")
    peds = int(input("Enter choice: "))
    
    if peds==1:
        print("The room starts to darken, and you’ll be trapped in a shifting labyrinth of gold coins that you can’t escape from.")
        time.sleep(0.5)
        fail()

    elif peds==2:
        print("The floor beneath you opens, and a trapdoor drops you into a pit of gold, where you’ll be buried under its weight.")
        time.sleep(0.5)
        fail()
    
    elif peds==3:
        print("You escape successfully and were rewarded with tons of gold for your wise choice.")
        time.sleep(0.5)
        win()

    else:
        print("You waited till thousands of gold block were dropped on you.")
        time.sleep(0.5)
        fail()

def fail():
    time.sleep(1)
    print("Game Over")
    time.sleep(0.4)
    print("You failed to survive...")
    time.sleep(0.2)
    cont()

def win():
    print("You win the game!")
    time.sleep(1)
    cont()

def bear():
    print("Welcome to Bear room.")
    time.sleep(0.3)
    print("There is a grizzly bear sitting in front of you, what will you do?")

    print("1. Shoot \n2. Offer Honey \n3. Run")
    b = int(input("Enter choice: "))

    if b==1:
        bl=random.randint(1,6)
        x=int(input("Select a number between 1 and 6: "))

        if bl==x:
            print("You have successfully hit the bear.")
            print("Moving to gold room...")
            time.sleep(1)
            gold()

        else:
            print("You missed the shot.")
            time.sleep(0.5)
            print("The bear slaps your face off")
            fail()

    elif b==2:
        print("The bear is more interested for blood than honey.")
        time.sleep(0.5)
        print("It devours you in a whole.")
        fail()

    elif b==3:
        print("the bear runs faster than you.")
        time.sleep(0.5)
        print("It chews your legs off.")
        fail()
    
    else:
        print("You waited till the bear stared to thrash you to death.")
        fail()

def snake():
    print("Welcome to Snake room")
    time.sleep(0.3)
    print("There are over hundreds of snakes surrounding this room, what will you do?")

    print("1. Play A Bean \n2. Try to kill them \n3. Walk over them")
    sn = int(input("Enter choice: "))

    if sn==1:
        s1 = random.randint(1,5)
        ch = int(input("Enter the correct tune number between 1 and 5: "))

        if ch==s1:
            print("You have played the right tune and managed to escape this room!")
            print("Moving to gold room...")
            time.sleep(1)
            gold()

        else:
            print("You played the wrong tune and angered the snakes.")
            time.sleep(0.5)
            print("The bite you till you blood stream is filled with venom.")
            fail()

    elif sn==2:
        print("There are over a hundred snakes in this room, what did you expect?")
        time.sleep(0.5)
        print("They feast on you.")
        fail()

    elif sn==3:
        print("The snakes didn't like you walking over them.")
        time.sleep(0.5)
        print("They attacked you till your body turned blue.")
        fail()
    
    else:
        print("You waited till they attached to you and bit you to death.")
        fail()

def tiger():
    print("Welcome to Tiger room")
    time.sleep(0.3)
    print("There is a tiger sleeping in front of you, what will you do?")

    print("1. Sneak \n2. Run. \n3. Punch the tiger")
    tg = int(input("Enter choice: "))

    if tg==1:
        tgp = int(input("Enter path number between 1 and 6: "))
        r = random.randint(1,6)

        if tgp==r:
            print("You chose the correct path and managed to escape this room!")
            print("Moving to gold room...")
            time.sleep(1)
            gold()

        else:
            print("You chose the wrong path and awakened the tiger.")
            time.sleep(0.5)
            print("It eats you for breakfast.")
            fail()
    
    elif tg==2:
        print("The noise you made awakned the tiger.")
        time.sleep(0.5)
        print("It chews your legs off.")
        fail()

    elif tg==3:
        print("You really thought you were Sher Shah Suri.")
        time.sleep(0.5)
        print("The tiger slaps your face off.")
        fail()

    else:
        print("You waited till the tiger woke up and it ate you alive.")
        fail()

def bees():
    print("Welcome to Bees room")
    time.sleep(0.3)
    print("There are a bunch of bees roaming in this room, what will you do?")

    print("1. Run \n2. Cover yourself and crawl \n3. Use smoke")
    bs = int(input("Enter choice: "))

    if bs==1:
        print("The bees became aware and swarmed you.")
        time.sleep(0.5)
        print("You felt nauseatic and faded, while the bees kept on biting you till you died.")
        fail()

    elif bs==2:
        pth = int(input("Enter path number between 1 and 3."))
        pb = random.randint(1,3)
        
        if pth==pb:
            print("You successful passed through the room!")
            print("Moving to gold room...")
            gold()
        
        else:
            print("You got stuck in a corner and the bees swarmed you.")
            time.sleep(0.5)
            print("They kept biting you to your death.")
            fail()
    
    elif bs==3:
        print("The bees started panicking.")
        time.sleep(0.5)
        print("They stung you in a panic and you feel unconscious.")
        fail()
    
    else:
        print("You waited till they stung you to death.")
        fail()

sc=0
def secret():
    global sc

    if sc==0:
        sc+=1
        print("You entered a secret room...")
        time.sleep(0.5)
        print("It turns out that there is Arthur Morgan in this room, speak with him to pass this level.")
        time.sleep(1)
        print("Try not to make him angry.")
        time.sleep(0.5)

        print("\tArthur: Well, ain't you a friendly face. What brings you 'round here?")
        print("\n1. I was lost \n2. A quiz brought me here")     
        rs1 = int(input("Enter response: "))

        if rs1 == 1:
            print("\tYou: I was lost.")
            print("\tArthur: You lost, or just takin' a break from all the madness out there?")
            time.sleep(0.5)
            print("\tArthur: Here’s somethin’ to chew on. I’m not sayin’ it’s easy, but you might just get it. What has keys but can't open locks")
            print("\n1. A map \n2. A piano \n. A chest")
            rdf = int(input("Enter response: "))

            if rdf==2:
                print("\tArthur: Huh, guess you ain’t as dumb as you look. Well done.")
                time.sleep(0.2)
                print("\tArthur: Alright, you’re free to go. Don’t make me come lookin’ for ya.")
                win()
            
            else:
                print("Arthur: Really? That’s the best you got? You’re gonna need more than that to make it outta here.")
                fail()

        elif rs1 == 2:
            print("\tYou: A quiz brought me here.")
            time.sleep(0.2)
            print("\tArthur: A quiz led you here? You expect me to believe that? Sounds like you’ve got worse luck than me.")
            time.sleep(0.5)
            print("\tArthur: Here's somethin' to chew on. I can be cracked, made, told, and played. What am I?")
            print("\n1. A secret \n2. A joke \n3. A promise")
            rdl = int(input("Enter response: "))

            if rdl==2:
                print("\tArthur: Huh, guess you ain’t as dumb as you look. Well done.")
                time.sleep(0.2)
                print("\tArthur: Alright, you’re free to go. Don’t make me come lookin’ for ya.")
                win()
            
            else:
                print("Arthur: Really? That’s the best you got? You’re gonna need more than that to make it outta here.")
                fail()

        else:
            print("\tArthur: You better start talkin’. What are you doin’ here?")
            ang1 = int(input("\n1. Just roaming around \n2. Mind your business"))

            if ang1==1:
                print("\tYou: I was just roaming around when I stumbled here.")
                print("\tArthur: Next time you feel like ‘roamin,’ try not roamin' into places that ain’t yours.")
                time.sleep(0.5)
                print("\tArthur: Here’s somethin’ to chew on. I’m not sayin’ it’s easy, but you might just get it. What runs but never walks, has a bed but never sleeps, and can have a mouth but never talk?")
                print("\n1. A River \n2. A Train \n3. A Storm")
                rd = int(input("Enter response: "))

                if rd==1:
                    print("\tArthur: Huh, guess you ain’t as dumb as you look. Well done.")
                    time.sleep(0.2)
                    print("\tArthur: Alright, you’re free to go. Don’t make me come lookin’ for ya.")
                    win()
                
                else:
                    print("Arthur: Really? That’s the best you got? You’re gonna need more than that to make it outta here.")
                    fail()
            
            elif ang1==2:
                print("\tYou: Just mind your own business man.")
                time.sleep(0.5)
                print("\tArthur: Mind my own business? Sure, just as soon as you find the door you came through.")
                time.sleep(0.5)
                print("What will you do?")
                print("\n1. Leave \n2. Stay")
                lv = int(input("Enter choice: "))

                if lv==1:
                    print("\tArthur: Good. Door’s that way. Don’t let it hit ya on the way out")
                    time.sleep(0.5)
                    print("You were sent back by Arthur")
                    
                    begin()
                
                elif lv==2:
                    print("\tArthur: Huh. So you got guts, I’ll give ya that. But guts don’t always mean you’re smart.")
                    time.sleep(0.5)

                    print("You get in a standoff with Arthur.")
                    guns=int(input("He gives you 3 guns to choose from, only one is loaded, choose the correct one:"))
                    gn = random.randint(1,3)

                    if guns==gn:
                        print("You chose the right gun and shot down Arthur.")
                        time.sleep(0.5)
                        print("\tArthur: Well, hell... didn’t see that comin’. Guess you’re tougher than you look.")
                        time.sleep(0.5)
                        win()
                    
                    else:
                        print("You chose the wrong gun and he shot you down.")
                        time.sleep(0.5)
                        print("\tArthur: I can’t take it back now... but you had it comin’.")
                        fail()

                else:
                    print("\tArthur: Hah, so that’s how it is, huh? Fine. Ignore me all you want, but don’t say I didn’t warn ya.")
                    time.sleep(0.2)
                    print("You were shot dead by Arthur.")
                    fail()

            else:
                print("\tArthur: You wanna play games? Fine, but don’t cry when it ends bad for you.")
                time.sleep(0.5)
                print("You get in a standoff with Arthur.")
                guns=int(input("He gives you 3 guns to choose from, only one is loaded, choose the correct one:"))
                gn = random.randint(1,3)

                if guns==gn:
                    print("You chose the right gun and shot down Arthur.")
                    time.sleep(0.5)
                    print("\tArthur: Well, hell... didn’t see that comin’. Guess you’re tougher than you look.")
                    time.sleep(0.5)
                    win()
                
                else:
                    print("You chose the wrong gun and he shot you down.")
                    print("\tArthurI can’t take it back now... but you had it comin’.")
                    fail()

    else:
        print("You entered Arthur's room again.")
        time.sleep(0.5)
        print("Arthur: You don’t listen too well, do ya? I ain’t got time for this nonsense. You’re pushin’ your luck")
        time.sleep(0.5)
        print("You get in a standoff with Arthur.")
        guns=int(input("He gives you 3 guns to choose from, only one is loaded, choose the correct one:"))
        gn = random.randint(1,3)

        if guns==gn:
            print("You chose the right gun and shot down Arthur.")
            time.sleep(0.5)
            print("\tArthur: Well, hell... didn’t see that comin’. Guess you’re tougher than you look.")
            time.sleep(0.5)
            win()
                
        else:
            print("You chose the wrong gun and he shot you down.")
            print("\tArthurI can’t take it back now... but you had it comin’.")
            fail()        

def begin():
    print("You are in an empty room, and there are 5 doors in front of you.")
    time.sleep(0.5)

    d = int(input("Enter door number: "))
    doors = ["bear", "snake", "tiger", "bees", "secret"]

    op1 = random.choice(doors)
    doors.remove(op1)
    op2 = random.choice(doors)
    doors.remove(op2)
    op3 = random.choice(doors)
    doors.remove(op3)
    op4 = random.choice(doors)
    doors.remove(op4)
    op5 = random.choice(doors)

    if d==1:
        if op1=="bear":
            bear()

        elif op1=="snake":
            snake()
        
        elif op1=="tiger":
            tiger()
        
        elif op1=="bees":
            bees()
        
        elif op1=="secret":
            secret()
    
    elif d==2:
        if op2=="bear":
            bear()

        elif op2=="snake":
            snake()
        
        elif op2=="tiger":
            tiger()
        
        elif op2=="bees":
            bees()
        
        elif op2=="secret":
            secret()
    
    elif d==3:
        if op3=="bear":
            bear()

        elif op3=="snake":
            snake()
        
        elif op3=="tiger":
            tiger()
        
        elif op3=="bees":
            bees()
        
        elif op3=="secret":
            secret()

    elif d==4:
        if op4=="bear":
            bear()

        elif op4=="snake":
            snake()
        
        elif op4=="tiger":
            tiger()
        
        elif op4=="bees":
            bees()
        
        elif op4=="secret":
            secret()

    elif d==5:
        if op5=="bear":
            bear()

        elif op5=="snake":
            snake()
        
        elif op5=="tiger":
            tiger()
        
        elif op5=="bees":
            bees()
        
        elif op5=="secret":
            secret()

    else:
        print("You waited till you starved to death.")
        time.sleep(0.5)
        fail()
            
def cont():
    c = int(input("Press 1 to countinue, press any other number to exit: "))

    if c==1:
        print("Looks like you are ready to put yourself to the test, lets go.")
        time.sleep(1)
        global sc
        sc=0
        begin()

    else:
        exit(0)

cont()