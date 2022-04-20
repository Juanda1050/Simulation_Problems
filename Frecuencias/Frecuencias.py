import os
import sys
import pandas as pd


def main():
    # Print title
    print('Prueba Estadística de Frecuencias', "\n")

    # Inputs
    num_rectangulares = []
    cant_num_rectangulares = getInput(prompt="Ingrese la cantidad de numeros rectangulares: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    alfa = getInput(prompt="Ingrese el porcentaje de alfa: ",
                    cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    subintervalo = getInput(prompt="Ingrese la cantidad de subinvertalos: ",
                            cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    for input_rectangulares in range(0, cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=float,
                     condition=lambda x: x > 0,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    FEi = cant_num_rectangulares / subintervalo

    # List ranges in Alphabet
    listAlphabet = list(map(chr, range(65, 65 + subintervalo)))

    # Ranges
    ranges = []
    sumai = 0
    while sumai < 1:
        ranges.append(sumai)
        sumai += 1 / subintervalo
    ranges.append(1)

    # Put numbers in ranges
    counters = []
    for x in range(subintervalo):
        count = len([y for y in num_rectangulares if y >
                    ranges[x] and y <= ranges[x+1]])
        counters.append(count)
    
    print("\n")
    for i in range(len(ranges)):
        for j in range(cant_num_rectangulares):
            if (num_rectangulares[j] > ranges[i] and num_rectangulares[j] <= ranges[i + 1]):
                print(f'[{j + 1}] = {num_rectangulares[j]} {listAlphabet[i]}')

    # Dataframe for data
    print("\n")
    rtd = []
    try:
        [rtd.append(str(ranges[x])+"-"+str(ranges[x + 1]))
         for x in range(len(ranges))]
    except:
        pass
    fo = []
    [fo.append(FEi) for x in range(subintervalo)]
    df = pd.DataFrame([fo, counters, rtd],
                      columns=listAlphabet, index=["FEi", "FOi", " "])
    print(df, "\n")

    # Table calculations
    df1 = pd.read_csv(
        "https://raw.githubusercontent.com/Davvii1/X-2DistributionTableCSV/main/DistribucionX2.csv", index_col=0, header=0)
    tdata = df1.loc[(subintervalo - 1), str(alfa / 100)]

    # Sum of FO-FE
    sumax = 0
    print(f'FEi = {cant_num_rectangulares} / {subintervalo} = {FEi}')
    print(f'Xo² = 1 / {FEi}', end='[')
    for x in range(subintervalo):
        sumax += (counters[x] - FEi) * (counters[x] - FEi)
        print(f'({counters[x]} - {FEi})²', end='')
        if x != subintervalo - 1:
            print(" + ", end='')
    print("]\n")
    x0t2 = (1 / FEi) * sumax

    print(f'Xo² = {x0t2}')
    print("X²", alfa / 100, ",", subintervalo - 1, ":", tdata)
    print(f'Xo² < X²α, n - 1 \n{x0t2} < {tdata}')

    # Evaluate Xot² with table
    if x0t2 < tdata:
        print("Los numeros son aceptados")
    else:
        print("Los numeros no son aceptados")

    # Restart for .exe
    restartProgram()


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
