# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for possible_anagram in word_list:
            sorted_possible_anagram = sorted(possible_anagram)
            
            if sorted_word == sorted_possible_anagram:
                matches.append(possible_anagram)
        return matches
