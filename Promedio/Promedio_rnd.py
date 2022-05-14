from cmath import sqrt
import random
import os
import sys
import pandas as pd


def main():
    # Print title
    print('Prueba Estadística de Promedio', "\n")

    # Inputs
    num_rectangulares = []
    sumatoria = 0
    cant_num_rectangulares = getInput(prompt="Ingrese la cantidad de numeros rectangulares: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    alfa = getInput(prompt="Ingrese el porcentaje de alfa: ",
                    cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    for rnd in range(0, cant_num_rectangulares):
        number = round(random.uniform(0, 1), 5)
        num_rectangulares.append(number)
        sumatoria += num_rectangulares[rnd]

    # Total of inputs and average
    promedio = sumatoria / cant_num_rectangulares
    print("\nΣ =", round(sumatoria, 5))
    print("x̄ =", round(promedio, 5))

    # Statistical
    Zo = abs(((promedio - 0.5) * sqrt(cant_num_rectangulares)) / sqrt((1 / 12)))
    print(
        f'Zo = |(({promedio: .5f} - ¹⁄₂ ) √{cant_num_rectangulares}) / √(¹⁄₁₂)| = {Zo: .5f}')

    # Table statistic
    alfa_real = (100 - alfa) / 100
    estadistico_Z = alfa_real / 2
    print(f'\nαreal = 100 - {alfa} = {int(alfa_real * 100)}%')
    print(f'Zα⁄₂ = {alfa_real} / 2 = {estadistico_Z}')

    # Get index and header of the table statistics
    df1 = pd.read_csv(
        "https://raw.githubusercontent.com/Juanda1050/Simulation_Problems/main/Promedio/Distribucion_normal.csv", header=0)
    df1 = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]
    df2 = df1[df1.eq(estadistico_Z).any(1)]
    lista = list([[df2.columns.values][0], [df2.values][0][0]])
    for x in range(len(lista[0])):
        if lista[1][x] == estadistico_Z:
            col = lista[0][x]
    index = list(df2.index.where(df2[str(col)] == estadistico_Z))[0]

    estadistico_tablas = float(col) + (float(index) / 10)
    print(f'Zα⁄₂ = {estadistico_tablas}')

    # Compare statistics
    print("\nZo < Zα⁄₂")
    print(f'{Zo: .5f} < {estadistico_tablas}')

    # Print analysis
    if (Zo < estadistico_tablas):
        print("Los numeros son aceptados")
    else:
        print("Los numeros no son aceptados")

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
