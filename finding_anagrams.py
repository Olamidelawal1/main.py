# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

from gettext import find


def find_anagram(word, anagram):
    word = str(input("desired word: "))
    anagram = str(input ("desired anagram: "))

#convert both strings into lowercase
    word = word.lower()
    anagram = anagram.lower()

#check word length
    if (len(word) == len(anagram)):
    
#sort strings
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

#if words are anagram
    if (sorted_word == sorted_anagram):
        return True

    else:
        return False

check =find_anagram('word' ,'anagram')
print(check)
     
    