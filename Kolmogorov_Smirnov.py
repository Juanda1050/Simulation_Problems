import random
from prettytable import PrettyTable

def main():
    random_numbers = []
    n = getInput(prompt="Ingrese la cantidad de numeros aleatorios a generar: ", cast=int,
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
    print("Valor mayor de estadisticos calculados", round(max_Dn, 5))


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
