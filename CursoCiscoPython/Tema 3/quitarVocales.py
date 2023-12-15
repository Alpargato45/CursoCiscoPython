# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

print("Escribe tu palabra")
user_word = input()
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    print(letter)
    

