import pandas as pd

# Inputs
N = int(input("Cantidad de numeros a ingresar: "))
alfa = int(input("Valor en porcentaje de alfa: "))
n = int(input("Cantidad de subintervalos: "))

numbers = []
for x in range(N):
    an = input("["+str(x+1)+"]: ")
    numbers.append(float(an))

fe = N/n

# List ranges in Alphabet
listAlphabet = list(map(chr, range(65, 65+n)))

# Ranges
ranges = []
sumai = 0
while sumai < 1:
    ranges.append(sumai)
    sumai += 1/n
ranges.append(1)

# Put numbers in ranges
counters = []
for x in range(n):
    count = len([y for y in numbers if y > ranges[x] and y <= ranges[x+1]])
    counters.append(count)

# Dataframe for data
rtd = []
try:
    [rtd.append(str(ranges[x])+"-"+str(ranges[x+1])) for x in range(len(ranges))]
except:
    pass
fo = []
[fo.append(fe) for x in range(n)]
df = pd.DataFrame([fo, counters, rtd], columns = listAlphabet, index = ["FEi", "FOi", " "])
print(df)


# Table calculations
df1 = pd.read_csv("https://raw.githubusercontent.com/Davvii1/X-2DistributionTableCSV/main/DistribucionX2.csv", index_col=0, header =0)

tdata = df1.loc[(n-1), str(alfa/100)]

# Sum of FO-FE
sumax = 0
for x in range(n):
    sumax += (counters[x] - fe) * (counters[x] - fe)
x0t2 = (1/fe) * sumax

print("FEi =", fe)
print("X0^2 =", x0t2)
print("X^2", alfa/100, ",", n-1, ":", tdata)

# Evaluate x0t2 with table
if x0t2 < tdata:
    print("Los numeros son aceptados")
else:
    print("Los numeros no son aceptados")