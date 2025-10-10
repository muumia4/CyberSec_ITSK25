src = "output.txt"

#Kuvan faili sisu
with open(src, "r", encoding="utf-8") as f:
    content = f.read()
print("Maatriks:\n" + content)

#Loen sisse maatriksi
with open(src, "r", encoding="utf-8") as f:
    rows = f.readlines()
    print("Rea summad:")

#Korrastan ja loon veergude jaoks tühja listi
rowCount = 0
firstRow = rows[0].strip().split()
columnTotal = [0] * len(firstRow)

firstValue = int(firstRow[0])
minValue = firstValue
maxValue = firstValue

#Korrastan info
for row in rows:
    row = row.strip()
    numbers = row.split()

    #Arvutan rea summad
    rowTotal = 0
    rowCount += 1

    for i in range(len(numbers)):
        value = int(numbers[i])
        rowTotal += value
        columnTotal[i] += value

        #Jälitan suurimat ja väikseimat arvu
        if value < minValue:
            minValue = value
        if value > maxValue:
            maxValue = value

    print("Rida " + str(rowCount) + ": " + str(rowTotal))

#Arvutan veeru summad
print("\nVeeru summad:")
for x in range(len(columnTotal)):
    print("Veerg " + str(x + 1) + ": " + str(columnTotal[x]))

#Kuvan suurima ja väikseima arvu
print("\nSuurim arv: ", maxValue)
print("Väikseim arv: ", minValue)
