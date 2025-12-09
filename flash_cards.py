import json
import os

flash_cards = {}

if os.path.exists("flashcards.json"):
    with open ("flashcards.json", "r") as file:
        try:
            flash_cards = json.load(file)
        except json.JSONDecodeError:
            flash_cards = {}
else:
    with open("flashcards.json", "w") as file:
        json.dump({}, file)


while True:
    menu_input = str(input("What do you want to do?\nq : quit \nn : new flash card\nl : list all flash cards\nr : review flash cards (quiz)\n>"))
    if menu_input == "q":
        
        print("bye!")
        break
    elif menu_input == "l":
        print(flash_cards)

    elif menu_input == "n":
        newflashcard = str(input("what's your new flashcard?\n"))
        newflashcard_deifnintion = str(input("what's the flashcard's definition\n"))
        flash_cards[newflashcard] = newflashcard_deifnintion
        with open ("flashcards.json", "w") as file:
            json.dump(flash_cards, file, indent=4)
        print("saving done!\n")
    elif menu_input == "r":
        for q, a in flash_cards.items():
            guess = input(f"{q} ? ")
            if guess.lower() == a.lower():
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is: {a}\n")

    else:
        print("Invalid option!\n")