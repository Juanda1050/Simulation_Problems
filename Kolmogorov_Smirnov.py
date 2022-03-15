from curses import keyname
import random
from prettytable import PrettyTable
from Estadisticos import statistic_table_alfa_10, statistic_table_alfa_5, statistic_table_alfa_1

def main():
    random_numbers = []
    n = getInput(prompt="Ingrese la cantidad de numeros aleatorios a generar: ", cast=int,
                 condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    alfa = getInput(prompt="Ingrese el valor porcentual de alfa (en entero): ", cast=int,
                 condition=lambda x: x > 0, errorMessage="El valor debe ser mayor a cero. Intenta de nuevo.")
    for rnd in range(0, n):
        number = round(random.uniform(0, 1), 5)
        random_numbers.append(number)
        
    random_numbers.sort(key=float)

    Fx = [None] * len(random_numbers)
    Dn = [None] * len(random_numbers)
    header_list = ["i", "Xi", "F(Xi)", "Dn = max|Fx(i) - Xi|"]
    table = PrettyTable(header_list)

    for i in range(len(random_numbers)):
        Fx[i] = float(i + 1) / n
        Dn[i] = abs(Fx[i] - random_numbers[i])
        table.add_row([str(i + 1), str(random_numbers[i]), str(Fx[i]), str(round(Dn[i], 5))])

    max_Dn = max(Dn)
    print(table)

    if(alfa == 10):
        statisticResult_alfa10(n, alfa, max_Dn)
    elif(alfa == 5):
        statisticResult_alfa5(n, alfa, max_Dn)
    elif(alfa == 1):
        statisticResult_alfa1(n, alfa, max_Dn)


def statisticResult_alfa10(n, alfa, max_Dn):
    key = "alfa"
    res = [val[key] for keys, val in statistic_table_alfa_10.items() if key in val]
    statistic_table_value = statistic_table_alfa_10[n].get('dis')

    for k, v in statistic_table_alfa_10.items():
        if(k == n and res[k] == alfa):
                print("Valor mayor de estadisticos calculados:", round(max_Dn, 5))
                print("Estadistico de tablas:", statistic_table_value)
                print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")


def statisticResult_alfa5(n, alfa, max_Dn):
    key = "alfa"
    res = [val[key] for keys, val in statistic_table_alfa_5.items() if key in val]
    statistic_table_value = statistic_table_alfa_5[n].get('dis')

    for k, v in statistic_table_alfa_5.items():
        if(k == n and res[k] == alfa):
                print("Valor mayor de estadisticos calculados:", round(max_Dn, 5))
                print("Estadistico de tablas:", statistic_table_value)
                print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")


def statisticResult_alfa1(n, alfa, max_Dn):
    key = "alfa"
    res = [val[key] for keys, val in statistic_table_alfa_1.items() if key in val]
    statistic_table_value = statistic_table_alfa_1[n].get('dis')

    for k, v in statistic_table_alfa_10.items():
        if(k == n and res[k] == alfa):
                print("Valor mayor de estadisticos calculados:", round(max_Dn, 5))
                print("Estadistico de tablas:", statistic_table_value)
                print("" + str(max_Dn) + " < " + str(statistic_table_value) + "")

    if(max_Dn < statistic_table_value):
        print("Los numeros son aceptados.")
    else:
        print("Los numeros no son aceptados.")


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
