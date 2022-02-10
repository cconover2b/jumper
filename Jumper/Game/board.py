class Board:

    def __init__(self):
        """Constructs a new Board.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._attempt = 0

    def get_letter(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (Board): An instance of Board.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def display_letter(self, text):
        """Displays the given text on the terminal. 

        Args: 
        self (TerminalService): An instance of TerminalService.
        text (string): The text to display.
        """
        print(text)

    def get_attempt(self):

        if self._attempts > 0:
            board = self.attempt_1_board()
        elif self._attempts > 1:
            board = self.attempt_2_board()
        elif self._attempts > 2:
            board = self.attempt_3_board()
        elif self._attempts > 3:
            board = self.attempt_4_board()

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
