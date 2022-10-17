import random
import string


print("H A N G M A N\n")

word_list = ["python", "github", "javascript", "java", "microsoft", "ineedjob", "please"]
games_win = 0
games_lost = 0

while True:
    what_to_do = (input("""Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:"""))
    guest_letters = set()
    chosen_word = random.choice(word_list)
    correct_letters = set(chosen_word)
    hidden = len(chosen_word) * "-"
    rounds = 8

    if what_to_do == "play":
        while hidden != chosen_word and rounds != 0:
            print(f"\n{hidden}")
            new_letter = input("Input a letter: ")

            if len(new_letter) != 1:
                print("Please, input a single letter.")
            elif new_letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            else:
                if new_letter in guest_letters:
                    print("You've already guessed this letter.")
                elif new_letter in correct_letters:
                    for x in range(len(chosen_word)):
                        if chosen_word[x] == new_letter:
                            hidden = hidden[:x] + new_letter + hidden[x+1:]
                else:
                    print("That letter doesn't appear in the word.")
                    rounds -= 1
                guest_letters.update(new_letter)

        if hidden == chosen_word:
            print(f"You guessed the word {chosen_word}!\n"
                  f"You survived!")
            games_win += 1
        else:
            print("You lost!")
            games_lost += 1

        print("")

    elif what_to_do == "results":
        print(f"You won: {games_win} times\n"
              f"You lost: {games_lost} times")

    elif what_to_do == "exit":
        break
