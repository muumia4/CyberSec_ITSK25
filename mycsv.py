filename = 'data/Create-MyCSV-v.csv'
column = 0 #Veerg mida kokku liita
total = 0 #Veeru summa

with open(filename, 'r') as f: #Avan faili (with open()) ja loen sisu ('r') ja sellest saab muutuja (as f)
    contents = f.readlines() #Loeb faili sisu muutujasse
    print(contents)