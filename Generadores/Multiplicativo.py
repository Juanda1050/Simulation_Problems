import os
import sys
import math 
from prettytable import PrettyTable


def main():
    multiplicativa = int(input("a = "))
    semilla = int(input("Xo = "))
    modulo = int(input("m = "))
    pe = 0

    if((modulo % 10) == 0):
        exponente = math.log10(modulo)
        int_exponente = int(exponente)

        if(exponente >= 5):
            pe = 5 * pow(10, exponente - 2)
            print("p.e. = 5x10^"+ str(int_exponente) + " = " + pe)
        elif(exponente < 5):
            print("p.e. = m.c.m. λ(5^" + str(int_exponente) + "), λ(2^" + str(int_exponente) + ")")
            lambda_5 = lambda_cinco(exponente)
            lambda_2 = lambda_dos(exponente)

            pe = mcm(lambda_5, lambda_2)

            print("p.e. = m.c.m (" + str(int(lambda_5)) + ", " + str(int(lambda_2)) +")")
            print("\np.e. = " + str(int(pe)))
    else:
        pe = modulo / 4
        print("\np.e. = " + str(modulo) + " / 4 = " + str(int(pe)))

    header_list = ["n", "X₀", "aX₀ mod m", "Xn + 1" , "Números Rectangulares"]
    table = PrettyTable(header_list)

    aux_semilla = semilla
    n = 1

    while True:
        solucion = (multiplicativa * semilla) / modulo
        semilla_generada = (multiplicativa * semilla) % modulo
        num_rectangulares = semilla_generada / modulo
        table.add_row([str(n), str(semilla), str(round(solucion, 5)) + " + " + str(semilla_generada) + " / " + str(modulo), str(semilla_generada), str(semilla_generada) + " / " + str(modulo) + " = " + str(round(num_rectangulares, 5))])
        semilla = semilla_generada
        n += 1
        if(semilla_generada == aux_semilla):
            break
        elif (n > pe):
            break
        else:
            continue

    print(table)

    if(aux_semilla == semilla_generada and n - 1 == modulo):
        print("Generador Congruencial Multiplicativo Confiable")
    else:
        print("Generador Congruencial Multiplicativo No Confiable")

    restartProgram()


def lambda_cinco(exponente):
    solucion = 4 * pow(5, exponente - 1)
    print("λ(5^" + str(int(exponente)) + ") = 5^" + str(int(exponente)) + "- 1 (4)")
    return solucion

def lambda_dos(exponente):
    solucion = 0
    if (exponente == 0): 
        solucion = 1
    elif (exponente == 1):
        solucion = 2
    elif (exponente > 1):
        solucion = pow(2, exponente - 2)
    
    print("λ(2^" + str(int(exponente)) + ") = 2^" + str(int(exponente)) + "- 2 (4)")
    return solucion

def mcd(a, b):
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

mcm = lambda a, b: (a * b) / mcd(a, b)


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