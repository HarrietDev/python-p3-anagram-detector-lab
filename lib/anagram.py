anagram_words = [
    "silent",
    "dust",
    "heart",
    "listen",
    "night",
    "earth",
    "thing",
    "stud",
    "evil",
    "live"
]

class Anagram:
    def __init__(self,word):
        self.word = word

    def match (self, words_list):
        sorted_word = sorted(self.word.lower())
        return [word for word in words_list if sorted(word.lower())== sorted_word and word.lower() != self.word.lower()]

find_words = Anagram("Listen")
print(find_words.match(anagram_words))
