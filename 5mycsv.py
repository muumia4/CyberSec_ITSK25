filename = 'data/Create-MyCSV-v.csv' #Faili asukoht ja nimi millega tegelema hakatakse
column = 0 #Veerg mida kokku liita
total = 0 #Veeru summa

with open(filename, 'r') as f: #Avan faili (with open()) ja loen sisu ('r') ja sellest saab muutuja (as f)
    contents = f.readlines() #Loeb faili sisu muutujasse
    for row in contents: #Loop käib rea haaval faili läbi
        row = row.strip() #Eemalda tühikud ja reavahetus
        item = row.split(';') #Tükelda semikoolonist. .split tekitab alati listi ja töötab ainult str-iga
        if item[column].isdigit(): #Kas kõik itemid muutujas column on numbrid
            total += int(item[column]) #Arvutame kokku eelmises käigus saadud numbrid

    print(total)