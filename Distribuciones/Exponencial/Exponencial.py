import os
import sys
import math

def main():
    num_rectangulares = []
    cant_num_rectangulares = int(
        input("Ingrese la cantidad de numeros rectangulares: "))
    media_estadistica = int(
        input("Ingrese la media estadistica de la variable aleatoria: "))
    unidad = str(input("Ingrese el tipo de unidades: "))

    for input_rectangulares in range(0, cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=float,
                     condition=lambda x: x > 0,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    x = [None] * len(num_rectangulares)
    tiempo_atencion = 0
    media_calculada = 1 / media_estadistica
    
    for i in range(cant_num_rectangulares):
        x[i] = -media_calculada * math.log(num_rectangulares[i])
        print(f'TA{(i + 1)} = -1 / {media_estadistica} ln({num_rectangulares[i]}) = {round(x[i], 5)} {unidad}')
        tiempo_atencion += x[i]

    promedio_atencion = tiempo_atencion / cant_num_rectangulares

    print(f'Sumatoria total: {round(tiempo_atencion, 5)} {unidad}')
    print(f'Tiempo total de operacion: {round(tiempo_atencion, 5)} {unidad}')
    print(f'Tiempo promedio de atencion: {round(promedio_atencion, 5)} {unidad}')

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
