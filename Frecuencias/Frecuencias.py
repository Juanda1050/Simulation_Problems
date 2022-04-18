import os
import sys
import pandas as pd
from termcolor import colored


def main():
    # Print title
    title = colored('𝙿𝚛𝚞𝚎𝚋𝚊 𝙴𝚜𝚝𝚊𝚍í𝚜𝚝𝚒𝚌𝚊 𝚍𝚎 𝙵𝚛𝚎𝚌𝚞𝚎𝚗𝚌𝚒𝚊𝚜', 'green', attrs=['blink'])
    print(title, "\n")

    # Inputs
    num_rectangulares = []
    cant_num_rectangulares =  getInput(prompt="Ingrese la cantidad de numeros rectangulares: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    alfa =  getInput(prompt="Ingrese el porcentaje de alfa: ",
                                      cast=int, condition=lambda x: x > 0, errorMessage="Numero incorrecto. Intenta de nuevo")
    subintervalo =  getInput(prompt="Ingrese la cantidad de subinvertalos: ",
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
        count = len([y for y in num_rectangulares if y > ranges[x] and y <= ranges[x+1]])
        counters.append(count)

    # Dataframe for data
    rtd = []
    try:
        [rtd.append(str(ranges[x])+"-"+str(ranges[x + 1])) for x in range(len(ranges))]
    except:
        pass
    fo = []
    [fo.append(FEi) for x in range(subintervalo)]
    df = pd.DataFrame([fo, counters, rtd], columns = listAlphabet, index = ["FEi", "FOi", " "])
    print(df)


    # Table calculations
    df1 = pd.read_csv("https://raw.githubusercontent.com/Davvii1/X-2DistributionTableCSV/main/DistribucionX2.csv", index_col=0, header =0)
    tdata = df1.loc[(subintervalo - 1), str(alfa / 100)]

    # Sum of FO-FE
    sumax = 0
    for x in range(subintervalo):
        sumax += (counters[x] - FEi) * (counters[x] - FEi)
    x0t2 = (1 / FEi) * sumax

    print("FEi =", FEi)
    print("X0^2 =", x0t2)
    print("X^2", alfa / 100, ",", subintervalo - 1, ":", tdata)

    # Evaluate x0t2 with table
    if x0t2 < tdata:
        print("Los numeros son aceptados")
    else:
        print("Los numeros no son aceptados")

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