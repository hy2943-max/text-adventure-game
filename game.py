# Write you adventure here!
def game_over():
    print("GAME OVER")

def location_1():
    print("You're in a forest and you got a tent.")
    print("ACTION MENU:")
    print("- burn the tent")
    print("- sleep in it at night")
    action = input("INPUT ACTION: ")
    if action == "sleep in it at night":
        print("You wake up fresh and continue to explore.")
        location_2()
    elif action == "burn the tent":
        print("You died at night.")
        game_over()
    else:
        print(f"Invalid action: {action}")
        location_1()

def location_2():
    print("A leprechaun is attrated by your tent, and he said he can lead you to your friend.")
    print("ACTION MENU:")
    print("- follow him")
    print("- reject him")
    action = input("INPUT ACTION: ")
    if action == "follow him":
        location_3()
    elif action == "reject him" :
        print("He is mad and turns you into a frog")
        game_over()
    else:
        print(f"Invalid action: {action}")
        location_2()

def location_3():
    print("The leprechaun helped you to find your friend. You won!")

location_1()

