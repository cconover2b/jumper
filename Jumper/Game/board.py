class Board:

    def __init__(self):
        """Constructs a new Board.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._attempt = 0
        self._hint = ""

    def get_letter(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (Board): An instance of Board.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def display_letter(self):
        """Displays the given text on the terminal. 

        Args: 
        self (TerminalService): An instance of TerminalService.
        text (string): The text to display.
        """
        print(self._hint)

    def get_attempt(self):

        if self._attempt == 0:
            self.board()

        elif self._attempt == 1:
            self.attempt_1_board()

        elif self._attempt == 2:
            self.attempt_2_board()

        elif self._attempt == 3:
            self.attempt_3_board()

        elif self._attempt == 4:
            self.attempt_4_board()

    def board(self):

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

    def attempt_1_board(self):

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

    def attempt_2_board(self):

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

    def attempt_3_board(self):

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

    def attempt_4_board(self):

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
        print('Game Over (;.;)')
