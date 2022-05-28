# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from fileinput import filename

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        reader = f.read()
        print("\n {} \n" .format(reader))
    return reader


def count_words():
    text = read_file_content("./story.txt")
    d = dict()

    for line in text:
        line = line.strip()

        line = line.lower()

        words = line.split(" ")

        for word in words:

            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])

    # [assignment] Add your code here

    return {"as": 10, "would": 20}


read_file_content("./story.txt")

count_words()
