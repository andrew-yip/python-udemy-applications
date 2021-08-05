import json
data = json.load(open("/Users/andrewyip/Desktop/data.json")) #LOADING THE JSON file from our desktop (creating a data object)

import difflib
from difflib import SequenceMatcher #compares
from difflib import get_close_matches # gets close matches

#Functions
def translate(w):
    w = w.lower()
    if w in data:
        return data.get(word)
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data.get(word.title())
        #or could be return data[word]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: #compares it with close matches
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]] #returns a list of close matches but only the first one because [0]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
 
#Main 
word = input("Enter word: ")
output = translate(word)
if isinstance(output, list): #because the output returns a list
    for item in output: 
        print(item) #prints each item out in that list if output is a list
else: #if it is a string then it just prints out the output
    print(output)