
# Read text from a file, and count the occurence of words in that 
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
  
    with open(filename,'r') as file:
        file = open(filename, "r").read()
    return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts



print('This is the story and number of time each word appears')
print(count_words())
