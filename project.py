# Creator: Oluyinka Ojolayo
# Creator's Email: yinkaojolayo@gmail.com
# Day of Creation: 7/12/22

# Story Ideas:
# You find yourself in a forest with no memory of who you are or what you're doing there. You see a small plume of smoke from afar. What do you do?
# you got a helpful fluffy friend and a mysterious cottage... which do you choose from?

import time

print("You wake up in a forest with no memory of who you are or how you got there.")
time.sleep(1.5)
print("You see a small plume of smoke from afar.")
time.sleep(1.5)
print("What do you do?")
time.sleep(0.5)
user_input = input("Would you like to 'look' or 'walk' to the smoke plume?: ")


def story(a):
    if (a.upper() == "LOOK"):
        print("You decide to look around a bit more to see if you missed anything.")
        time.sleep(2)
        print("After looking around, you spot a small fluffy thing a little far off from you")
        time.sleep(2)
        print("The fluffy thing wakes up and starts walking in a random direction")
        time.sleep(2)
        print("You follow the little thing for a while")
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("You end up at the edge of the forest. Turns out the forest was near your home town!")
        time.sleep(2)
        print("Ending 3: Well that was easy...")

    elif (a.upper() == "WALK"):
        print("You head over to the smoke plume and see a nice wooden cottage.")
        time.sleep(1.5)
        print(
            "As you approach the cottage, the door suddenly opens to a young lady. She welcomes you in rather quickly.")
        time.sleep(2.5)
        print("You tell her your situation and ask if she has any way to contact her family.")
        time.sleep(2.5)
        print("The lady stays quiet... You feel that there is something wrong here...")
        time.sleep(2)
        print(
            "A snake comes down from the ceiling suddenly. It wraps itself lazily around the lady's neck. The Lady then says that she is unable to contact anyone outside, but she'll make her home especially homey for you.")
        time.sleep(5)
        print("You're ushered into a room of your own. ")
        deci_1 = input("Should you 'sleep' for the night or find a way to 'escape'?: ")
        deci_1_count = 0

        while (deci_1_count != 1):
            if (deci_1.upper() == "SLEEP"):
                print("The snake sneaks in while you're sleeping an eats you alive :( ")
                time.sleep(2)
                print("Ending 1: Snake Supper")
                deci_1_count = 1

            elif (deci_1.upper() == "ESCAPE"):
                print(
                    "You have a very bad feeling about this lady. You jump through the nearest window and make your escape.")
                time.sleep(2)
                print("While you have no idea where you're going, you decide that it's better than staying with them.")
                time.sleep(2.5)
                print("After you walk a bit, you see the end of the forest. Horray!")
                print("Ending 2: The Escape")
                deci_1_count = 1

            else:
                print("You can't do that, Try again.")
                deci_1 = input("Should you 'sleep' for the night or find a way to 'escape'?: ")


    else:
        print("You can't do that, Try again.")
        b = input("Enter your response again... ")
        story(b)


story(user_input)
