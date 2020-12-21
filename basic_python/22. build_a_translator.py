# Ant Language
# vowels -> g
# ------------

def translate(phrase):
    translation = ""
    for index in range(len(phrase)):
        if phrase[index] == 'a' or phrase[index] == 'e' or phrase[index] == 'i' or phrase[index] == 'o' or phrase[index] == 'u':
            translation += 'g'
        else:
            translation += phrase[index]

    # or
    # for letter in phrase:
    #     you can also use letter.lower in "aeiou"
    #     if letter in "AEIOUaeiou":
    #           if letter.isupper():
    #               translation += 'G'
    #           else:
    #               translation += 'g'
    #     else:
    #         translation += letter
    return translation


phrase = input("Enter a phrase: ")
print(translate(phrase))
