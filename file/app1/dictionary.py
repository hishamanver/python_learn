import json
from difflib import get_close_matches

with open("data.json") as knowledgeBank:
    data = json.load(knowledgeBank)
    
def array2text(array):
    text = "Definition(s): "
    for i in array:
        text = text + "\n" + i
    return text

def getDefinition(key):
    try:
        definition = data[key.lower()]
        return array2text(definition)
    except KeyError:
        closeKeyArray = get_close_matches(key, data.keys(), n=1, cutoff=0.8)
        if closeKeyArray != []:
            closeKey = closeKeyArray[0]
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