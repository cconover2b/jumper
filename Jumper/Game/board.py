class Board:

    def __init__(self):

        self._attempts = ""
        self._word = []
        self.board()
        self.attempt_1_board()
        self.attempt_2_board()
        self.attempt_3_board()
        self.attempt_4_board()

    def get_attempt(self):

        if self._attempts > 0:
            board = self.attempt_1_board(self._word)
        elif self._attempts > 1:
            board = self.attempt_2_board(self._word)
        elif self._attempts > 2:
            board = self.attempt_3_board(self._word)
        elif self._attempts > 3:
            board = self.attempt_4_board(self._word)

    def board():

        print()
        print("    - - - - -  ")
        print("      ___      ")
        print("     /___\     ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def attempt_1_board(word):

        print(f"{word}")
        print()
        print("    - - - - -  ")
        print("               ")
        print("     /___\     ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def attempt_2_board(word):

        print(f"{word}")
        print()
        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def attempt_3_board(word):

        print(f"{word}")
        print()
        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("               ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def attempt_4_board(word):

        print(f"{word}")
        print()
        print("    - - - - -  ")
        print("               ")
        print("               ")
        print("               ")
        print("               ")
        print("       X       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")
        print()
        print(f'Game Over (;.;)')
