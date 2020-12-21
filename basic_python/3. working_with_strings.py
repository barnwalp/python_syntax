#\n is used for creating a new line
print("Ant\nAcademy")
#\ is used for entering "
print("Ant\"Academy")

phrase = "Ant Academy"
print(phrase + " is cool")
#using lower function
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
#to get the length of the string
print(len(phrase))
#to get the few characters of the string
#in python, string start at 0th index
print(phrase[0])
#to get the index of the character or word
print(phrase.index("Acad"))
#it will result in the error if given
#character is not found
print(phrase.index("x"))

print(phrase.replace("Ant", "Panther"))

## you can get all function details by using
## dir(str) in the command line and then using
## help(str.function) for docs

