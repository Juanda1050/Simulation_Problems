import os
import sys
import math
from prettytable import PrettyTable


def main():
    # Print title
    print('Distribución Poisson', "\n")

    # Inputs
    media_estadistica = getInput(prompt="Ingrese la media estadistica variable: ",
                                 cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    header_list = [
        "x", "Distribucion estadistica f(xi)", "Distribucion estadistica acumulada F(xi)"]
    table = PrettyTable(header_list)

    distribucion = []
    distribucion_acumulada = 0
    comprobar_rango = []
    i = 0
    comprobar_rango.append(0)

    # Get values
    while True:
        distribucion.append((math.exp(-media_estadistica)
                            * pow(media_estadistica, i)) / math.factorial(i))
        distribucion_acumulada += distribucion[i]
        comprobar_rango.append(distribucion_acumulada)
        table.add_row([str(i), f'{distribucion[i]: .5f}', str(
            round(distribucion_acumulada, 5))])
        if distribucion_acumulada >= 0.99995:
            break
        else:
            i += 1
            continue
    print('\n', table)

    # Print ranges
    print("\n")
    for j in range(len(comprobar_rango) - 1):
        print(f'Si R es > {comprobar_rango[j]: .5f} y <= {round(comprobar_rango[j + 1], 5)} entonces x = {j}')

    # Input numbers
    print("\n")
    num_rectangulares = []
    cant_num_rectangulares = getInput(prompt="Ingrese la cantidad de numeros rectangulares: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    for input_rectangulares in range(0, cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=float,
                     condition=lambda x: x > 0,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    #Locate the numbers into the ranges
    print("\n")
    demanda_total = 0
    for x in range(len(comprobar_rango)):
        for y in range(cant_num_rectangulares):
            if(num_rectangulares[y] > comprobar_rango[x] and num_rectangulares[y] <= comprobar_rango[x + 1]):
                print(f'[{y + 1}] = {num_rectangulares[y]} x = {x}')
                demanda_total += x
    print("Demanda total = ", demanda_total)

 # Restart for .exe
    restartProgram()


# Condition for inputs
def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except IOError:
            print(errorMessage or "Invalido. Intenta de nuevo.")


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
