import mysql.connector
import difflib
from difflib import SequenceMatcher #compares
from difflib import get_close_matches # gets close matches

#Storing the user information in the 'con' variable
con = mysql.connector.connect( #name of connection from database to computer
user = "ardit700_student", 
password = "ardit700_student",
host = "108.167.140.122", 
database = "ardit700_pm1database"
)

#Functions
def translate(w):
    w = w.lower()
    if w in results:
        return results.get(word)
    elif w.title() in results: #if user entered "texas" this will check for "Texas" as well.
        return results.get(word.title())
        #or could be return data[word]
    elif w.upper() in results: #in case user enters words like USA or NATO
        return results[w.upper()]
    elif len(get_close_matches(w, results.keys())) > 0: #compares it with close matches
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, results.keys())[0]).lower()
        if yn == "y":
            return results[get_close_matches(w, results.keys())[0]] #returns a list of close matches but only the first one because [0]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
cursor = con.cursor() #to navigate through table of database
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word) #accessing data from query
results = cursor.fetchall() #Gets all the information from selected expression

if results:
    for result in results:
        print(result[1])
else:
    print("no results found ")

    
#print("type of results table is: ", type(results))