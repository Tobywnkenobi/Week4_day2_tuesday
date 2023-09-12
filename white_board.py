# 'stop gninnips my sdrow' challenge:

# Write a function that takes in a string of one or more words,
# and returns the same string,
# but with all five or more letter words reversed.
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# My solution:

def more_than_5(sent: str) -> str:
    words = sent.split(' ')
    for l, word in enumerate(words):
        if len(word) >= 5:
            words[l] = word[::-1]
    return " ".join(words)

test = "This is a pretty big whiteboard today, Heather is doing great"

more_than_5(test)

print(more_than_5(test))

#Heather's solution:

# def astring_edit(astring):
#     empty_string = []
#     for word in astring.split():
#         if len(word) >= 5:
#             empty_string.append(word[::-1])
#         else:
#             empty_string.append(word)
#     return ' ’.join(empty_string)