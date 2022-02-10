from Game.board import Board
from Game.word_generator import word_generator
from Game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): The game's hidden word.
        is_playing (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's guesser.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_generator = word_generator()
        self._is_playing = True
        self._guesser = Guesser()
        self._board = Board()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            _status = self._do_updates()
            self._do_outputs()
            if _status == 4:
                #Will stop program if out of guesses
                self._is_playing = False
                return
        print("GG")

    def _get_inputs(self):
        """Gets the word guessed.

        Args:
            self (Director): An instance of Director.
        """
        new_guess = self._board.get_letter("\nEnter a letter: ")
        self._guesser.add_letter(new_guess)
        
    def _do_updates(self):
        """Keeps watch on where the guesses given to the guesser.

        Args:
            self (Director): An instance of Director.
        """
        self._board._hint = self._word_generator.compare_letters(self._guesser)
        self._board._attempt = self._word_generator.count_attempts(self._guesser)

        status = self._board._attempt
        return status

        
    def _do_outputs(self):
        """Provides hints for the guesser to use.

        Args:
            self (Director): An instance of Director.
        """
        
        self._board.display_letter()
        self._board.get_attempt()

        self._is_playing = self._word_generator.is_found(self._guesser._letters)
