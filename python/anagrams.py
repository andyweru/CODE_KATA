# returns words in list that are anagrams of word

def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]
