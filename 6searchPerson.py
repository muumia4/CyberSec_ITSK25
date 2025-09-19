import csv #csv failide töötlemiseks mõeldud pakett

filename = 'data/Persons.csv' #Töödeldava faili asukoht
count = 0 #Loon muutuja leitud kasutajate arvu näitamiseks
phrase = input('Sisesta otsitav fraas (min. 2 märki): ') #Küsime kasutajalt otsitavat fraasi ja lisame selle muutujasse "phrase"

if len(phrase) > 1: #Kui "phrase" muutuja pikkus on suurem kui 1
#    pass #Testimiseks mõeldud käsk mis jätab plokki vahele
    with open(filename, 'r', encoding='utf-8') as f: #Siis ava "filename" muutujas kirjeldatud fail, loe seda, muuda encoding ja salvesta muutujasse "f"
        contents = csv.reader(f, delimiter=';') #Loome muutuja "contents", avame csv.reader mooduliga "f" muutuja väärtuse ning kirjeldame reavahemärgi 
        for row in contents: #Käime listi rea haaval läbi
            phrase = phrase.lower() #Tee väiketähtedeks, et välistada tõstutundlikus otsingus
            first_name = row[0].lower() #Tee väiketähtedeks eesnimi, et välistada tõstutundlikus otsingus
            last_name = row[1].lower() #Tee väiketähtedeks perenimi, et välistada tõstutundlikus otsingus
            if phrase in first_name or phrase in last_name:
                print(';'.join(row)) #Tee list str-iks
                count += 1

        print(f'Leiti {count} nime')

else:
    print('Otsitav fraas on liiga lühike')