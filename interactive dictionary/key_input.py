import json
from difflib import get_close_matches as getm

dictionary = json.load(open("data.json"))

def sense(w):
    w = w.lower()
    if w in dictionary.keys():
        return dictionary[w]
    elif w.title() in dictionary.keys():
        return dictionary[w.title()]
    elif w.upper() in dictionary.keys():
        return dictionary[w.upper()]
    elif len(getm(w, dictionary.keys(), cutoff = 0.8)) > 0:
        word_to_compare = getm(w, dictionary.keys())[0]
        ask_user = input("Did you mean %s instead? Enter Y if yes, or N if no:  " %word_to_compare)
        if ask_user.lower() == "y":
            return dictionary[word_to_compare]
        elif ask_user.lower() == "n":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist."

while True:
    word = input("Enter word: ")
    if word == "!":
        print("exit")
        break
    else:
        output = sense(word)
        if type(output) == str:
            print(output)
        elif type(output) == list:
            for item in output:
                print(item)
