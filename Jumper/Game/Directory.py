from game.terminal_service import TerminalService
from game.word import Word
from game.guesser import Guesser


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
        self._word = Word()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the word guessed.

        Args:
            self (Director): An instance of Director.
        """
        new_guess = self._terminal_service.read_word("\nEnter a word: ")
        self._guesser.add_guess(new_guess)
        
    def _do_updates(self):
        """Keeps watch on where the guesses given to the guesser.

        Args:
            self (Director): An instance of Director.
        """
        self._word.watch_guesser(self._guesser)
        
    def _do_outputs(self):
        """Provides hints for the guesser to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._word.get_hint()
        self._terminal_service.write_text(hint)
        if self._word.is_found():
            self._is_playing = False