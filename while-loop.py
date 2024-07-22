import random


print("Bienvenidxs al programa adivinador")
print("Las reglas son simples, pienso un número y tú adivinas")


number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input('Elije un número del 1 al 10: ')
    if int(guess) == number:
        print('Es correcto Haz ganado!!')
        isGuessRight = True
    else:
        print('Es incorrecto, intenta otra vez')