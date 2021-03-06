from sys import exit


def check_user_input(inp):
    try:
        val = int(inp)
        if(isinstance(val, int)):
            return val
    except ValueError:
        print("Enter a number:")
        inp = input("> ")
        return (check_user_input(inp))


def gold_room():
    print("This room is full of gold. How much do you take? ")

    choice = input("> ")
    how_much = check_user_input(choice)
    if how_much < 50:
        print("Nice, you won")
        exit()
    else:
        print("Greedy bastard")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear")
    bearMoved = False

    while True:
        choice = input("> ")

        if choice == 'take honey':
            dead("The bear looks at you and slaps your face off")
        elif choice == 'taunt bear':
            if not bearMoved:
                print("The bear has moved from the door.")
                print("You can go through it now")
                bearMoved = True
            else:
                dead("The bear gets pissed off and eats your legs off")
        elif choice == 'open door' and bearMoved:
            gold_room()
        else:
            print("I got no idea what that means")


def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat you head?")

    choice = input("> ")

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()


def start():
    print("you are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take")

    choice = input("> ")

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead("You stumble around until you starve")


def dead(why):
    print(why, "Good job!")
    exit(0)


start()
