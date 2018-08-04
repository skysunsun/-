from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_room():
    print("there is bear here.")
    print("the bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "take honey":
            dead("the bear kooks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("the bearhas moved from the door.")
            print("you can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("here you see the great evil cyhulhu.")
    print("He, it whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("you are in a dark room.")
    print("there is a door to your right and left.")
    print("which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("your stumble around the room until you starve.")


start()
