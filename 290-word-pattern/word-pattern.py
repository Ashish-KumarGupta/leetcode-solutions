class Solution(object):
    def wordPattern(self, pattern, s):
        word = s.split()

        if len(pattern) != len(word):
            return False
        
        letter_to_word = {}
        word_to_letter = {}
        

        for letter, word in zip(pattern, word):
            if letter in letter_to_word:
                if letter_to_word[letter] != word:
                    return False
            if word in word_to_letter:
                if word_to_letter[word] != letter:
                    return False

            letter_to_word[letter] = word
            word_to_letter[word] = letter
        return True