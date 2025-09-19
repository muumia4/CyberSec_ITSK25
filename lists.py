#Listid

places = [] #Tühi list

places.append('Kehtna') #.append = lisa lõppu
places.append('Rapla')
places[1:1] = ['Tallinn', 'Pärnu'] #Lisa Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisab lõppu
places.insert(2, 'Are') #Lisab Tallinna ja Pärnu vahele
print(places)

places.remove('Rapla') #Kustutab esimese leitud
places.pop(6) #Kustutab indeksi järgi
del places[2] #Kustutab indexi järgi
print(places)

places.append('Rapla') #Lisa Rapla lõppu 
places.insert(3, 'Rapla') #ja pärast Pärnut
print(places)

place = places[-1] #Muutuja saab väärtuseks listi viimase elemendi
index = places.index(place) #Mitmes element on esimene Rapla
count = places.count(place) #Mitu Raplat on kokku listis

print(index, count)

if place in places: #Kas Rapla on nimekirjas?
    print(f'{place} on nimekirjas')
else:
    print('Ei ole nimekirjas')

list_copy = places.copy() #Tee listist koopia
list_list = list(places) #Tee listist koopia (alternatiiv viis)

list_copy.sort() #A-Z
list_list.sort(reverse=True) #Z-A

print(list_copy)
print(list_list)

new_sorted_list = sorted(places, reverse=False) #Loob uue sorteeritud listi A>Z 
print(new_sorted_list)

new_sorted_list.clear() #Tühjenda listi sisu

print(places[len(places)-1]) #Prindi viimane item


print(places[2][2].upper()) #Places listi kolmanda itemi kolmas täht suurelt

keskmine = places[2] #Eelmine aga kolme reaga
keskmine = keskmine.upper()
print(keskmine[2])