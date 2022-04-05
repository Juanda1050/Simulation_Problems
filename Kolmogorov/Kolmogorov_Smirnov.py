from curses import keyname
import random
import sys
from prettytable import PrettyTable
from Estadisticos import statistic_table_alfa_10, statistic_table_alfa_5, statistic_table_alfa_1
import os


def main():
    # random_numbers = []
    # n = getInput(prompt="Ingrese la cantidad de numeros aleatorios a generar: ", cast=int,
    #              condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    # alfa = getInput(prompt="Ingrese el valor porcentual de alfa (en entero): ", cast=int,
    #                 condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    # for rnd in range(0, n):
    #     number = round(random.uniform(0, 1), 5)
    #     random_numbers.append(number)
    num_rectangulares = []
    cant_num_rectangulares = int(
        input("Ingrese la cantidad de numeros rectangulares: "))
    alfa = getInput(prompt="Ingrese el valor porcentual de alfa (en entero): ", cast=int,
                    condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")

    for input_rectangulares in range(0, cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=float,
                     condition=lambda x: x > 0,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

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

    if(alfa == 10):
        statisticResult_alfa10(cant_num_rectangulares, alfa, max_Dn)
    elif(alfa == 5):
        statisticResult_alfa5(cant_num_rectangulares, alfa, max_Dn)
    elif(alfa == 1):
        statisticResult_alfa1(cant_num_rectangulares, alfa, max_Dn)


def statisticResult_alfa10(cant_num_rectangulares, alfa, max_Dn):
    key = "alfa"
    res = [val[key]
           for keys, val in statistic_table_alfa_10.items() if key in val]
    statistic_table_value = statistic_table_alfa_10[cant_num_rectangulares].get('dis')

    for key_value in statistic_table_alfa_10:
        if(key_value == cant_num_rectangulares or res == alfa):
            print("Valor mayor de estadisticos calculados:", max_Dn)
            print("Estadistico de tablas:", statistic_table_value)
            print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")

    restartProgram()


def statisticResult_alfa5(cant_num_rectangulares, alfa, max_Dn):
    key = "alfa"
    res = [val[key]
           for keys, val in statistic_table_alfa_5.items() if key in val]
    statistic_table_value = statistic_table_alfa_5[cant_num_rectangulares].get('dis')

    for key_value in statistic_table_alfa_5:
        if(key_value == cant_num_rectangulares or res == alfa):
            print("Valor mayor de estadisticos calculados:", max_Dn)
            print("Estadistico de tablas:", statistic_table_value)
            print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")

    restartProgram()


def statisticResult_alfa1(cant_num_rectangulares, alfa, max_Dn):
    key = "alfa"
    res = [val[key]
           for keys, val in statistic_table_alfa_1.items() if key in val]
    statistic_table_value = statistic_table_alfa_1[cant_num_rectangulares].get('dis')

    for key_value in statistic_table_alfa_1:
        if(key_value == cant_num_rectangulares or res == alfa):
            print("Valor mayor de estadisticos calculados:", max_Dn)
            print("Estadistico de tablas:", statistic_table_value)
            print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")

    restartProgram()


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


def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except IOError:
            print(errorMessage or "Invalid input. Try again.")


if __name__ == '__main__':
    main()
