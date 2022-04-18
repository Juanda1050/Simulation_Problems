import random
import sys
import os
from termcolor import colored


def main():
    # Print title
    title = colored('𝙶𝚎𝚗𝚎𝚛𝚊𝚍𝚘𝚛 𝙽𝚞𝚖𝚎𝚛𝚘𝚜 𝚁𝚎𝚌𝚝𝚊𝚗𝚐𝚞𝚕𝚊𝚛𝚎𝚜',
                    'green', attrs=['blink'])
    print(title, "\n")

    random_numbers = []
    n = getInput(prompt="Ingrese la cantidad de numeros aleatorios a generar: ", cast=int,
                 condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    for rnd in range(0, n):
        number = round(random.uniform(0, 1), 5)
        random_numbers.append(number)

    for i in range(len(random_numbers)):
        print(f'{random_numbers[i]}')

    restartProgram()


def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except IOError:
            print(errorMessage or "Invalid input. Try again.")


def restartProgram():
    while True:
        option = int(
            input("Ingrese (1) para reinicar el programa y (0) para salir: "))
        if option == 1:
            os.system("cls")
            main()
            break
        elif option == 0:
            sys.exit()
        else:
            print("Opcion invalida. Intente de nuevo.")
            continue


if __name__ == '__main__':
    main()
