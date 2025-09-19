filename = 'data/Persons.csv' #Töödeldava faili asukoht
count = 0 #Loon muutuja leitud kasutajate arvu näitamiseks
phrase = input('Sisesta otsitav fraas (min. 2 märki): ') #Küsime kasutajalt otsitavat fraasi ja lisame selle muutujasse "phrase"

if len(phrase.strip()) > 1: #Kui "phrase" muutuja pikkus on suurem kui 1 (koristame ära ka tühikud)
    phrase = phrase.strip().lower() #Korrastan otsingu fraasi võttes ära tühikud ja reavahetused ning muudame kõik tähed väikseks
    file = open(filename, 'r', encoding='utf-8') #Avame faili lugemiseks
    contents = file.readlines()[1:] #Loeme alates teisest reast
    file.close() #Sulge fail
    for row in contents: #Käime listi rea haaval läbi
        row = row.strip() #Korrastame kõik read
        if phrase in row.lower():
            print(row)
            count += 1 #Suurenda "count" loendurit ühe võrra
    print(f'Leiti {count} nime.')
else:
    print('Otsingu fraas liiga lühike!')