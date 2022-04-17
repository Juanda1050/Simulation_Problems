import os
import sys
import pandas as pd
import numpy as np
import math


def main():
    num_rectangulares = []
    cant_num_rectangulares = int(
        input("Ingrese la cantidad de numeros rectangulares: "))
    alfa = int(input("Ingrese el porcentaje de alfa: "))
    subintervalo = int(
        input("Ingrese la cantidad de subinvertalos: "))
    for input_rectangulares in range(cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=str,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    FEi = float(cant_num_rectangulares - 1) / (pow(subintervalo, 2))
    listAlphabet = list(map(chr, range(65, 65 + subintervalo)))

    pairs_num = []
    for index, elem in enumerate(num_rectangulares):
        if index + 1 <= len(num_rectangulares) and index - 1 >= 0:
            prev_el = float(num_rectangulares[index - 1])
            curr_el = float(elem)
            pairs_num.append([prev_el, curr_el])
            print(prev_el, curr_el)

    counters = []
    interval = 1 / subintervalo
    interval_x = 0
    interval_y = 0

    for _ in np.arange(interval_x, 1, (interval_x + interval)):
        x_values = []
        for _ in np.arange(interval_y, 1, (interval_y + interval)):
            count = 0
            for pairs in pairs_num:
                if interval_x <= pairs[0] < (interval_x + interval) and interval_y <= pairs[1] < (
                        interval_y + interval):
                    count += 1
            interval_y += interval
            x_values.append(count)
        interval_y = 0
        interval_x += interval
        counters.append(x_values)

    df = pd.DataFrame(counters, columns=listAlphabet, index=listAlphabet)
    print(df)

    df1 = pd.read_csv("https://raw.githubusercontent.com/Davvii1/X-2DistributionTableCSV/main/DistribucionX2.csv",
                      index_col=0, header=0)

    n_restada = pow((subintervalo), 2) - 1
    tdata = df1.loc[n_restada, str(alfa / 100)]

    sumax = 0
    print(
        f'Xo² = {pow((subintervalo), 2)} / {cant_num_rectangulares - 1}', end='[')
    for x in range(subintervalo):
        for y in range(subintervalo):
            sumax += math.pow(counters[x][y] - FEi, 2)
            print(f'({counters[x][y]} - {FEi})²', end='')
            if x + 1 <= subintervalo and y + 1 <= subintervalo:
                if y != subintervalo - 1:
                    print(" + ", end='')

    print("]")
    x0t2 = (1 / FEi) * sumax

    print("FEi =", cant_num_rectangulares, "- 1 /(", subintervalo, ")² =", FEi)
    print("Xo² =", round(x0t2, 2))
    print("X²", alfa / 100, ",", n_restada, "=", tdata)

    if x0t2 < tdata:
        print("Los numeros son aceptados")
    else:
        print("Los numeros no son aceptados")

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
