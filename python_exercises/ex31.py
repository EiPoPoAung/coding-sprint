print("""You  enter a dark room with two doors.
        Do you go though door #1 or door #2?""")
door=input(">")
if door=="!":
    print("There's a gaint bear here eating a Cheese cake.")
    print("What do you do?")
    print("1.Take the cake.")
    print("2.scream at the bear.")
    bear=input(">")
    if bear=="1":
        print("The bear eats your face off.Good job!")
    elif bear=="2":
        print("The bear eats your legs off.Good job!")
    else:
        print(f"Well,doing {bear}is probably better.")
        print("Bear runs away.")
    elif door=="2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1,Blueberries.")
        print("2,Yellow jacket clothespins.")
        print("3,Understanding revolvers yelling melodies.")
        insanity=input(">")
        if insanity=="1" or insanity=="2":
            print("Your body survives powered by a mind of jello.")
            print("Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck.")
            print("Good job!")
    else:
        print("youu stumble around and fall on aknife and die. Good job!")
