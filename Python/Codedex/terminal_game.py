#Proto-type of a terminal game.
#Player Start
player_name = "Peasant"
player_class = "None"
health = 100
mana = 50
endurance = 75
inventory = []
#introduction
print("Avalonion Guard: Welcome to Avalon. I need you to answer some questions before we can allow your passage into our land.\n")
#start game and update player name
while True:
    game_start = input(f"Avalonion Guard: To be clear, {player_name}, you are unwelcome here.\n Do you truly wish to venture into this realm?\n {player_name}: (Yes/No)")
    if game_start.lower() == "no":
        print("Avalonion Guard: HA! How pathetic you are, you are unwelcome here. I commend your ability to make a wise choice.")
        break
    elif game_start.lower() == "yes":
        print("Avalonion Guard: Is that so? How unfotunate for you, peace will not be found here for you. What is your name?")
        player_name = input(f"{player_name}: ")
        break
    else:
        print("Avalonion Guard: I didn't understand you, speak up you rat!")
        game_start = input(f"Avalonion Guard: Do you truly wish to venture into this realm?\n {player_name}: (Yes/No)")
#choosing a class
while True:
    print(f"Avalonion Guard: So your name is {player_name}, how original. What is your profession?\n (Warrior/Mage/Thief)")
    player_class = input(f"{player_name}: ")
    if player_class.lower() == "warrior":
        print(f"Avalonion Guard: A warrior? How cliche. You will be a burden to us, but I suppose we can use you for something.")
        break
    elif player_class.lower() == "mage":
        print(f"Avalonion Guard: A mage? How original. You will be a burden to us, but I suppose we can use you for something.")
        break
    elif player_class.lower() == "thief":
        print(f"Avalonion Guard: A thief? How clever. You will be a burden to us, but I suppose we can use you for something.")
        break
    else:
        print("Avalonion Guard: I didn't understand you, speak up fool!")
#command to check inventory and stats
while True:
    command = input(f"{player_name}: (Type 'stats' to check your stats, 'inventory' to check your inventory, or 'exit' to leave the game.)\n")
    if command.lower() == "stats":
        print(f"Name: {player_name}\nClass: {player_class}\nHealth: {health}\nMana: {mana}\nEndurance: {endurance}")
    elif command.lower() == "inventory":
        if inventory:
            print("Inventory:")
            for item in inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
    elif command.lower() == "exit":
        print("Closing the interface. Goodbye!")
        break
    else:
        print("I didn't understand that command. Please try again.")

#This is just a basic prototype of a terminal game. It can be expanded with more features such as quests, combat, and character progression. The player can interact with the game world and make choices that affect their journey in Avalon.