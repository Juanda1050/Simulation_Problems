import os
import sys
from prettytable import PrettyTable


def main():
    multiplicativa = int(input("a = "))
    semilla = int(input("Xo = "))
    aditiva = int(input("c = "))
    modulo = int(input("m = "))

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


if __name__ == '__main__':
    main()
