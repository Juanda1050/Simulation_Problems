import os
import sys
from prettytable import PrettyTable
from termcolor import colored


def main():
    # Print title
    title = colored('𝙶𝚎𝚗𝚎𝚛𝚊𝚍𝚘𝚛 𝙲𝚘𝚗𝚐𝚛𝚞𝚎𝚗𝚌𝚒𝚊𝚕 𝙼𝚒𝚡𝚝𝚘',
                    'green', attrs=['blink'])
    print(title, "\n")

    # Inputs
    multiplicativa = getInput(prompt="a = ",
                              cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    semilla = getInput(prompt="Xo = ",
                       cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    aditiva = getInput(prompt="c = ",
                       cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    modulo = getInput(prompt="m = ",
                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")

    header_list = ["n", "X₀", "((a * X₀) + c) mod m",
                   "Xn + 1", "Números Rectangulares"]
    table = PrettyTable(header_list)

    aux_semilla = semilla
    n = 1

    while True:
        solucion = ((multiplicativa * semilla) + aditiva) / modulo
        semilla_generada = ((multiplicativa * semilla) + aditiva) % modulo
        num_rectangulares = semilla_generada / modulo
        table.add_row([str(n), str(semilla), str(round(solucion, 5)) + " + " + str(semilla_generada) + " / " + str(modulo),
                      str(semilla_generada), str(semilla_generada) + " / " + str(modulo) + " = " + str(round(num_rectangulares, 5))])
        semilla = semilla_generada
        n += 1
        if(semilla_generada == aux_semilla):
            break
        elif (n > modulo):
            break
        else:
            continue

    print(table)

    if(aux_semilla == semilla_generada and n - 1 == modulo):
        print("Generador Congruencial Mixto Confiable")
    else:
        print("Generador Congruencial Mixto No Confiable")

    # Restart for .exe
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
