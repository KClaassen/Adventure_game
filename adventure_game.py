import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def cave(item, option):
    if "sword" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("You walk back to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.\n")
        item.append("sword")
    field(item, option)


def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        first_choice = input("What would you like to do?\n"
                             "(Please enter 1 or 2.)\n")
        if first_choice == "1":
            house(item, option)
            break
        elif first_choice == "2":
            cave(item, option)
            break


def house(item, option):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("The " + option + " attacks you!\n")
    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        second_choice = input("Would you like to (1) fight or (2) "
                              "run away?")
        if second_choice == "1":
            if "sword" in item:
                print_pause("As the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the " +
                            option + ".")
                print_pause("You have been defeated!\n")
            play_again()
            break
        if second_choice == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.\n")
            field(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\nGreat! Restarting the game ...\n")
        play_game()
    elif again == "n":
        print_pause("\nThanks for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["barhomet", "gorgon", "kraken", "troll",
                            "pirate", "dragon"])
    intro(item, option)
    field(item, option)


play_game()
