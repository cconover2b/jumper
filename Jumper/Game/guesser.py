from Game import board

class Guesser:
    """The person looking for the word. 
    
    The responsibility of a Guesser is to solve a puzzle by guessing the letters of a secret word one at a time.
    
    Attributes:
        letter (str): The letter (a-z) that the Guesser inputs.
    """


    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._letters = []
        

    def add_letter(self, letter):
        self._letters.append(letter.lower())