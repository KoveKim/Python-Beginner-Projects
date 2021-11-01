# Translator program
# Replaces any vowels in the user's input with the letter G

def translate(phrase):
    translation = ""  # "phrase" is the input, "translation" is the output

    for letter in phrase:
        if letter.lower() in "aeiou":  # Checks to see if the letter is in this string
            if letter.isupper():  # Check to see if it's uppercase, replace accordingly
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation  # Output the translation


print(translate(input("Enter a word or phrase to translate: ")))
