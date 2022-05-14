import random
import sys
from prettytable import PrettyTable
import os
import pandas as pd


def main():
    # Print title
    print('Prueba Estadística de Kolmogorov - Smirnov', "\n")

    # Inputs
    num_rectangulares = []
    cant_num_rectangulares = getInput(prompt="Ingrese la cantidad de numeros aleatorios a generar: ", cast=int,
                                      condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    alfa = getInput(prompt="Ingrese el valor porcentual de alfa (en entero): ", cast=int,
                    condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    for rnd in range(0, cant_num_rectangulares):
        number = round(random.uniform(0, 1), 5)
        num_rectangulares.append(number)

    # Sort array of numbers
    num_rectangulares.sort(key=float)

    Fx = [None] * len(num_rectangulares)
    Dn = [None] * len(num_rectangulares)
    header_list = ["i", "Xi", "F(Xi)", "Dn = max|Fx(i) - Xi|"]
    table = PrettyTable(header_list)

    for i in range(len(num_rectangulares)):
        Fx[i] = float(i + 1) / cant_num_rectangulares
        Dn[i] = abs(Fx[i] - num_rectangulares[i])
        table.add_row([str(i + 1), str(num_rectangulares[i]),
                      str(round(Fx[i], 2)), str(round(Dn[i], 5))])

    max_Dn = round(max(Dn), 5)
    print(table)

    # Table calculations
    df1 = pd.read_csv(
        "https://raw.githubusercontent.com/Juanda1050/Simulation_Problems/main/Kolmogorov/Estadistico_tablas.csv", index_col=0, header=0)
    table_value = 0
    try:
        table_value = df1.loc[cant_num_rectangulares, str(alfa)]
        print(table_value)
    except KeyError:
        print(
            f'\nNo existe dentro dentro la tabla de distribucion X², por ende es {table_value}')
        sys.exit()

    print("Valor mayor de estadisticos calculados:", max_Dn)
    print("Estadistico de tablas:", table_value)
    print("" + str(max_Dn) + " < " + str(table_value) + "")

    if(max_Dn < table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")

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
