import os
import sys
import math
from prettytable import PrettyTable


def main():
    # Print title
    print('Generador Congruencial Multiplicativo', "\n")

    # Inputs
    multiplicativa = getInput(prompt="a = ",
                              cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    semilla = getInput(prompt="Xo = ",
                       cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    modulo = getInput(prompt="m = ",
                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    pe = 0

    # Obtain power
    if((modulo % 10) == 0):
        exponente = math.log10(modulo)
        int_exponente = int(exponente)

        if(exponente >= 5):
            pe = 5 * pow(10, exponente - 2)
            print("p.e. = 5ₓ₁₀" + superi(str(int_exponente)) + " = " + str(int(pe)))
        elif(exponente < 5):
            print("p.e. = m.c.m. λ(5" + superi(str(int_exponente)) +
                  "), λ(2" + superi(str(int_exponente)) + ")")
            lambda_5 = lambda_cinco(exponente)
            lambda_2 = lambda_dos(exponente)

            pe = mcm(lambda_5, lambda_2)

            print("p.e. = m.c.m (" + str(int(lambda_5)) +
                  ", " + str(int(lambda_2)) + ")")
            print("p.e. = " + str(int(pe)) + " p.e.")
    else:
        pe = modulo / 4
        print("p.e. = " + str(modulo) + " / 4 = " + str(int(pe)) + " p.e.")

    header_list = ["n", "X₀", "aX₀ mod m", "Xn + 1", "Números Rectangulares"]
    table = PrettyTable(header_list)

    aux_semilla = semilla
    n = 1

    while True:
        solucion = (multiplicativa * semilla) / modulo
        semilla_generada = (multiplicativa * semilla) % modulo
        num_rectangulares = semilla_generada / modulo
        table.add_row([str(n), str(semilla), str(round(solucion, 5)) + " + " + str(semilla_generada) + " / " + str(modulo),
                      str(semilla_generada), str(semilla_generada) + " / " + str(modulo) + " = " + str(round(num_rectangulares, 5))])
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

    # Restart for .exe
    restartProgram()


def lambda_cinco(exponente):
    solucion = 4 * pow(5, exponente - 1)
    print("λ(5" + superi(str(int(exponente))) + ") = 5" +
          superi(str(int(exponente))) + superi(' - 1') + "(4) = " + str(int(solucion)))
    return solucion


def lambda_dos(exponente):
    solucion = 0
    if (exponente == 0):
        solucion = 1
    elif (exponente == 1):
        solucion = 2
    elif (exponente > 1):
        solucion = pow(2, exponente - 2)

    print("λ(2" + superi(str(int(exponente))) + ") = 2" +
          superi(str(int(exponente))) + superi(' - 2') + "(4) = " + str(int(solucion)))
    return solucion


def mcd(a, b):
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a


def mcm(a, b): return (a * b) / mcd(a, b)


def superi(x):
    normal = "0123456789-"
    s = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"
    res = x.maketrans(''.join(normal), ''.join(s))
    return x.translate(res)


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
