#Import
from datetime import datetime

name = 'eesnimi perenimi' #String (str)
age = 10 #Täisarv (integer)
height = 1.80 #Ujukomaarv (float)

print(f'Kasutaja {name.title()} vanuses {age} ja pikkusega {height} meetrit') #f = format. Name.title = teeb esimesed tähed suureks
print('Kasutaja ' + name.title() + ' vanuses ' + str(age) + ' ja pikkusega ' + str(height) + ' meetrit') # alternatiiv eelmisele

birth_year = datetime.now().year - age #Jooksev aasta - vanus
print (birth_year)

name = name.title() #Korrasta nimi ja kasuta sama muutujat
print(name[1])      #Väljund: "e". Annab teise tähe kuna indeksid algavad nullist
print(name[1:5])    #Väljund: "esni"
print(name[6:])     #Väljund: "i perenimi"
print(name[:5])     #Väljund: "Eesni"
print(name[::-1])   #Väljund: "iminereP iminseE"

age = int(input('Sisesta vanus: '))
#age = int(age)
if age > 122 or age < 1:
    print('Vanus on vales vahemikus (1-122)')
elif age < 18:
    print('Alaealine')
elif age < 65:
    print('Tööealine')
elif age < 100:
    print('Pensionär')
else:
    print('Pikaealine')

place = input('Sisesta elukoht: ')
print(f'Sisestati {place}')

if len(place) > 1 and len(place) <= 7:
    print(f'Lühikse nimega koht {place.title()}')
elif len(place) > 7:
    print(f'Pika nimega koht {place.title()}')
else:
    print('Nimi liiga lühike')


#Väljasta muutujate tüübid
print(type(name))
print(type(age))
print(type(height))
print(type(place))