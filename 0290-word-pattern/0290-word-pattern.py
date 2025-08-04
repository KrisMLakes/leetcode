class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_to_char = {}
        char_to_word = {}
        words = s.split()
        #print (words, pattern)
        if len(pattern) != len(words):
            return False
        for word, char in zip(words, pattern):
            if word in word_to_char:
                if word_to_char[word] != char:
                    #print (word_to_char, char, word, word_to_char[word])
                    return False
            else:
                word_to_char[word] = char

            if char in char_to_word:
                if char_to_word[char] != word:
                    #print (char_to_word, char, word)
                    return False
            else:
                char_to_word[char] = word
        return True
