import random

def play(game_function):
    while True:
        input("Press Enter to spin the slot machine...")
        game_function()
        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break

def spin_slot_machine():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']
    results = random.choices(symbols, k=3)
    print(' | '.join(results))
    if results == [symbols[3]] * 3:
        print("Jackpot! 💰")


if __name__ == '__main__':
    play(spin_slot_machine)
