import os
import sys
import math  
from prettytable import PrettyTable

def main():
    media_estadistica = int(
        input("Ingrese la media estadistica variable: "))

    header_list = ["x", "Distribucion estadistica f(xi)", "Distribucion estadistica acumulada F(xi)"]
    table = PrettyTable(header_list)

    distribucion = []
    distribucion_acumulada = 0
    comprobar_rango = []
    i = 0
    print('\n')

    while True:
        distribucion.append((math.exp(-media_estadistica) * pow(media_estadistica, i)) / math.factorial(i))
        distribucion_acumulada += distribucion[i]
        comprobar_rango.append(distribucion_acumulada)
        table.add_row([str(i), f'{distribucion[i]: .5f}', str(round(distribucion_acumulada, 5))])
        print(f'Si R es > {distribucion[i]: .5f} y <= {round(distribucion_acumulada, 5)} entonces x = {i}')
        if distribucion_acumulada >= 0.99995:
            break
        else:
            i += 1
            continue

    print('\n', table)
    
    num_rectangulares = []
    cant_num_rectangulares = int(
        input("Ingrese la cantidad de numeros rectangulares: "))
    for input_rectangulares in range(0, cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=float,
                     condition=lambda x: x > 0,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    for i in range(cant_num_rectangulares):
        if(num_rectangulares[i] > distribucion[i] and num_rectangulares[i] <= comprobar_rango[i]):
            print(f'[{i}] = {num_rectangulares[i]} x = {i}')

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