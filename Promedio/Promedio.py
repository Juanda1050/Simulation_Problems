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