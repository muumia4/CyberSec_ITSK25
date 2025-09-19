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

with open(source, 'r', encoding='utf-8') as file: #Loeme sisse open() käuga "source" muutujas oleva väärtuse
   with open(destination, 'w', encoding='utf-8') as dest: #Loob uue faili (või kirjutab üle) 'w'
    contents = csv.reader(file, delimiter=';') #Loome muutuja "contents", avame csv.reader mooduliga "file" muutuja väärtuse ning kirjeldame reavahemärgi 

