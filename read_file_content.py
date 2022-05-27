# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
import string
from tabnanny import check


def read_file_content(filename):
    with open('story.txt', 'r') as file:
        read_file = file.read()
    return read_file

def count_words():
    text =read_file_content("./story.txt")
    words =text.split()
    counter ={}
    for i in words:
        import string
        i = i.translate(i.maketrans('', '', string.punctuation))
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter
print(count_words())

    