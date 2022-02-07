word = list("apple")
hidden = []
for letter in word:
    hidden.append("_")

attempts = 3
max_attempt = 5

isgameover = False
while not isgameover:

    hiddenstring = " ".join(hidden)

    if attempts > 0:

        print(f"The current word is{hiddenstring}")

        print("    - - - - -  ")
        print("               ")
        print("     /___\     ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")

        print("    ^^^^^^^^^  ")

        print(f"you have {attempts} attemps")
        hiddenstring = " ".join(hidden)

    elif attempts > 1:

        print(f"The current word is{hiddenstring}")

        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")

        print("    ^^^^^^^^^  ")

        print(f"you have {attempts} attemps")
        hiddenstring = " ".join(hidden)

    elif attempts > 2:

        print(f"The current word is{hiddenstring}")

        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("               ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")

        print("    ^^^^^^^^^  ")

        print(f"you have {attempts} attemps")
        hiddenstring = " ".join(hidden)

    elif attempts > 2:

        print(f"The current word is{hiddenstring}")

        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("               ")
        print("               ")
        print("       X       ")
        print("      /|\      ")
        print("      / \      ")

        print("    ^^^^^^^^^  ")

        print(f"you have {attempts} attemps")
        hiddenstring = " ".join(hidden)

    else:
        ""

    break
