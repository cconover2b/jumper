import random
#Todo: test stuff, add more words
class word_generator:
    '''
    word_generator randomly chooses a word.

    Usage:
    Call return_word() to send the current selection to the call point.
    word_count() will return the legnth of the string (how many letters) as an intager
    to the call point.
    '''

    def __init__(self):
        #Initilize and set up default values
        # self.word_len = 0
        words = {
            1: 'Handbook',
            2: 'Dictionary',
            3: 'Empire',
            4: 'Valuable',
            5: 'Organization',
            6: 'Audience',
            7: 'Modifying',
            8: 'Drawing',
            9: 'Development'
        }
        option = random.randint(1, 9)
        self._word = words[option].lower()

    def compare_letters(self, _guesser):

        hint = ""

        for letter in self._word:
            if letter in _guesser._letters:
                hint += letter
            else:
                hint += "_"

        return hint

    def is_found(self, guessed_letters):

        for letter in self._word:
            if letter in guessed_letters:
                pass
            else:
                return True

        return False

    def count_attempts(self, _guesser):

        attempt = 0

        for guessed_letter in _guesser._letters:
            if guessed_letter in self._word:
                pass
            else:
                attempt += 1

        return attempt


    # def word_count(self):
    #     '''
    #     Utility function: 
    #     Returns the length of self.word as an INT to the call point
    #     '''

    #     self.word_len = int(len(self.word))
    #     return self.word_len

    # def return_word(self):
    #     #Returns self.word to the call point
    #     return self.word

