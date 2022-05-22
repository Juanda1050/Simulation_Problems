import os
import sys
import pandas as pd
import numpy as np
import math


def main():
    # Print title
    print('Prueba Estadística de Series', "\n")

    # Inputs
    num_rectangulares = []
    cant_num_rectangulares = getInput(prompt="Ingrese la cantidad de numeros rectangulares: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    alfa = getInput(prompt="Ingrese el porcentaje de alfa: ",
                    cast=float, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    subintervalo = getInput(prompt="Ingrese la cantidad de subinvertalos: ",
                            cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    for input_rectangulares in range(cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=str,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    sub_real = pow(subintervalo, 2)
    FEi = float(cant_num_rectangulares - 1) / sub_real
    listAlphabet = list(map(chr, range(65, 65 + subintervalo)))

    # Making pairs
    pairs_num = []
    for index, elem in enumerate(num_rectangulares):
        if index + 1 <= len(num_rectangulares) and index - 1 >= 0:
            prev_el = float(num_rectangulares[index - 1])
            curr_el = float(elem)
            pairs_num.append([prev_el, curr_el])


    # Locate pairs in the matrix
    print("\n")
    counters = []
    ranges_x = []
    ranges_y = []
    sumai = 0
    while sumai <= 1:
        ranges_x.append(sumai)
        ranges_y.append(sumai)
        sumai += 1 / subintervalo

    for i in range(len(ranges_x) - 1):
        x_counters = []
        for j in range(len(ranges_y) - 1):
            count = 0
            for pairs in pairs_num:
                if ranges_x[i] <= pairs[0] < ranges_x[i + 1] and ranges_y[j] <= pairs[1] < ranges_y[j + 1]:
                    print(f'({pairs[0]}, {pairs[1]}) {listAlphabet[i]}')
                    count += 1
            x_counters.append(count)
        counters.append(x_counters)

    df = pd.DataFrame(counters, columns=listAlphabet, index=listAlphabet)
    print("\n", df)

    # Table of calculations
    df1 = pd.read_csv("https://raw.githubusercontent.com/Juanda1050/Simulation_Problems/main/Frecuencias/Distribucion_chicuadrado.csv",
                      index_col=0, header=0)

    n_restada = pow((subintervalo), 2) - 1
    tdata = 0
    try:
        tdata = df1.loc[n_restada, str(alfa / 100)]
    except KeyError:
        print(f'\nNo existe dentro dentro la tabla de distribucion X², por ende es {tdata}')

    sumax = 0
    print("\n")
    print("FEi =", cant_num_rectangulares, "- 1 /(", subintervalo, ")² =", round(FEi, 2))
    print(f'Xo² = {pow((subintervalo), 2)} / {cant_num_rectangulares - 1}', end='[')

    for x in range(subintervalo):
        for y in range(subintervalo):
            sumax += math.pow(counters[x][y] - FEi, 2)
            print(f'({counters[x][y]} - {FEi :.2f})²', end='')
            if x + 1 <= subintervalo and y + 1 <= subintervalo:
                if y != subintervalo - 1:
                    print(" + ", end='')
        if x != subintervalo - 1:
            print(" + ", end='')

    print("]")
    x0t2 = (1 / FEi) * sumax

    print("Xo² =", round(x0t2, 2))
    print("X²", alfa / 100, ",", n_restada, "=", tdata)
    print(f'\nX²α, n - 1 > Xo²  \n{tdata} > {x0t2: .2f}')

    if x0t2 < tdata:
        print("Los numeros son aceptados")
    else:
        print("Los numeros no son aceptados")

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
