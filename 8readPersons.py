"""
INPUT:
    csv fail
    Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood

Luua etteantud kasutajatele kasutaja nimi ja eposti aadress
KASUTAJANIMI:
    eesnimi.perenimi
    eesnimes eemaldada tühik / sidekriips (Mari-Liis > Mari Liis)
    eemaldada rõhumärgid ja täpitähed (õüöäšž)
    kasutaja nimi on läbivalt väikeste tähtedega
EPOST
    kasutajanimi@asutus.com
KELLELE TEHA
    Sündinud 1990-1999 k.a
OUTPUT:
    uus csv
    Eesnimi;Perenimi;Isikukood;Kasutajanimi;EPost
"""

import csv
import unicodedata

source = 'data/Persons.csv' #Info algallikas
destination = 'data/Persons_accounts.csv' #Uus väljund
header = 'Eesnimi;Perenimi;Isikukood;Kasutajanimi;EPost' #Uue faili päis
domain = '@asutus.com' #Emaili domeen

def strip_accents(s): #https://stackoverflow.com/questions/517923 Eemaldab rõhumärgid ja täpitähed
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

with open(source, 'r', encoding='utf-8') as file: #Loeme sisse open() käuga "source" muutujas oleva väärtuse ja kirjutame selle muutujasse "file"
   with open(destination, 'w', encoding='utf-8') as dest: #Loob uue faili (või kirjutab üle) 'w' ning paneb selle muutujasse "dest"
    contents = csv.reader(file, delimiter=';') #Loome muutuja "contents", avame csv.reader mooduliga "file" muutuja väärtuse ning kirjeldame reavahemärgi 
    dest.write(header + '\n') #Kirjutame uude faili päise ja reavahetuse
    next(contents) #Alusta lugemsit järgmiselt realt kuna esimene rida CSVs on header

    for row in contents: #Loop kus võtame info "contents" muutujast ja iga leitud element pannakse ajutiselt "row" muutujasse
        date = row[2] #Kuupäev eraldi muutujasse
        year = int(date.split('.')[2]) #Võtame eelnevalt saadud kuupäevast välja aasta
        if year >= 1990 and year <= 1999:
            first_name = row[0] #Eesnimi eraldi muutujasse
            last_name = row[1] #Perenimi eraldi muutujasse
            first_name = first_name.replace(' ','') #Otsime tühikuid ja asendama tühjusega
            first_name = first_name.replace('-','') #otsime sidekriipsu ja asendame tühjusega

            user_name = '.'.join([first_name,last_name]).lower() #Ühendame ees ja perenime, paneme punkti vahele ja muudame väikesteks tähtedeks
            user_name = strip_accents(user_name) #Eemaldame täpitähed ja 
            
            email = user_name + domain #Loome emaili liites kaks muutujat kokku

            new_row = ';'.join(row[:2] + [row[-1], user_name, email]) #Määrame uue faili ridade vormingu (eesnimi;perenimi;isikukood;kasutajanimi;email)
            dest.write(new_row + '\n') #Kirjutame "new_row" alusel read faili ja paneme lõppu reavahetuse märgi
