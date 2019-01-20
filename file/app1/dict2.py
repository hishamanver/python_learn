import json
from difflib import get_close_matches
from difflib import SequenceMatcher

with open("data.json") as knowledgeBank:
    data = json.load(knowledgeBank)
    print(type(data))
    
def array2text(array):
    text = "Definition(s): "
    for i in array:
        text = text + "\n" + i
    return text

# def checkcloseMatches() - use inheritance to functionise the get_close_matches

def getDefinition(key):
    if key.title() in data:
        definition = data[key.title()]
        return array2text(definition)
    elif key.lower() in data:
        definition = data[key.lower()]
        return array2text(definition)
    elif key.upper() in data:
        definition = data[key.upper()]
        return array2text(definition)
    elif get_close_matches(key.upper(), data.keys(), n=1, cutoff=0.8) != []:
        closeKey = get_close_matches(key.upper(), data.keys(), n=1, cutoff=0.8)[0]
        checkCloseKey = input("Cannot find the word \'%s\', did you mean \'%s\'? (Y = Yes, N = No): " % (key, closeKey)).lower()
        if checkCloseKey == "y":
            print("\nWord: %s" % closeKey)
            definition = data[closeKey]
            return array2text(definition)
        elif checkCloseKey =="n":
            return "Sorry about that! Exiting now..."
        else:
            return "Sorry did not get that! Exiting now..."
    elif get_close_matches(key.lower(), data.keys(), n=1, cutoff=0.8) != []:
        closeKey = get_close_matches(key.lower(), data.keys(), n=1, cutoff=0.8)[0]
        checkCloseKey = input("Cannot find the word \'%s\', did you mean \'%s\'? (Y = Yes, N = No): " % (key, closeKey)).lower()
        if checkCloseKey == "y":
            print("\nWord: %s" % closeKey)
            definition = data[closeKey]
            return array2text(definition)
        elif checkCloseKey =="n":
            return "Sorry about that! Exiting now..."
        else:
            return "Sorry did not get that! Exiting now..."
    elif get_close_matches(key.title(), data.keys(), n=1, cutoff=0.8) != []: #try 'delhj' for reason why required
        closeKey = get_close_matches(key.title(), data.keys(), n=1, cutoff=0.8)[0]
        checkCloseKey = input("Cannot find the word \'%s\', did you mean \'%s\'? (Y = Yes, N = No): " % (key, closeKey)).lower()
        if checkCloseKey == "y":
            print("\nWord: %s" % closeKey)
            definition = data[closeKey]
            return array2text(definition)
        elif checkCloseKey =="n":
            return "Sorry about that! Exiting now..."
        else:
            return "Sorry did not get that! Exiting now..."
    else:
        return "The word \'%s\' does not exist in this dictionary." % (key)

word = input("Word: ")

print(getDefinition(word))