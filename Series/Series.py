
def main():
    num_rectangulares = []
    cant_num_rectangulares = int(
        input("Ingrese la cantidad de numeros rectangulares: "))
    alfa = int(input("Ingrese el porcentaje de alfa: "))
    subintervalo = int(
        input("Ingrese la cantidad de subinvertalos bidimensionales: "))
    for input_rectangulares in range(cant_num_rectangulares):
        n = getInput(prompt="[" + str(input_rectangulares + 1) + "]: ",
                     cast=str,
                     errorMessage="Numero incorrecto. Intenta de nuevo")
        num_rectangulares.append(n)

    FEi = float(cant_num_rectangulares - 1) / (pow(subintervalo, 2))
    pairs_num = []

    for previous, current in zip(num_rectangulares, num_rectangulares[1:]):
        pairs_num.append([previous, current])

    new_l = [(float(x[0]), float(x[1])) for x in pairs_num]
    intervalo_matriz = float(1) / subintervalo

    a = []
    b = []
    c = []
    d = []

    [a.append(x) for x in new_l if x[0] < intervalo_matriz and x[1] < intervalo_matriz]
    [b.append(x) for x in new_l if x[0] > intervalo_matriz and x[1] < intervalo_matriz]
    [c.append(x) for x in new_l if x[0] < intervalo_matriz and x[1] > intervalo_matriz]
    [d.append(x) for x in new_l if x[0] > intervalo_matriz and x[1] > intervalo_matriz]

    [print("La coordenada", x, "está en A con índice", a.index(x)) for x in new_l if x in a]
    [print("La coordenada", x, "está en B con índice", b.index(x)) for x in new_l if x in b]
    [print("La coordenada", x, "está en C con índice", c.index(x)) for x in new_l if x in c]
    [print("La coordenada", x, "está en D con índice", d.index(x)) for x in new_l if x in d]

    print("FEi =", cant_num_rectangulares, "- 1 /(",subintervalo,")² =",FEi)

    Xo = ((pow(subintervalo, 2)) / (cant_num_rectangulares - 1)) * (pow((len(a) - FEi), 2) + pow((len(b) - FEi), 2) + pow((len(c) - FEi), 2) + pow((len(d) - FEi), 2))

    print("Xo² =", round(Xo, 5))
    

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
