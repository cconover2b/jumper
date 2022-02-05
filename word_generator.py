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
        self.word = 'None'
        self.word_len = 0
        self.option = random.randint(1, 9)
        self.word_list()

    def word_list(self):
        #dictionary holding possible word choices
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
        self.word = words[self.option]


    def word_count(self):
        '''
        Utility function: 
        Returns the length of self.word as an INT to the call point
        '''

        self.word_len = int(len(self.word))
        return self.word_len

    def return_word(self):
        #Returns self.word to the call point
        return self.word

