import random
from datetime import datetime

input = 'data/andmed.txt'                                               #Fail mille algul loome ja siis loeme
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')                     #Lisan hetkeaja muutujasse ja määran vormingu

def calc():                                                             #Funktsioon arvutab ja kuvab summa(int), keskmise(float) ja suurima arvu(int)
    total = 0                                                           #Loome muutuja summa arvutamiseks
    count = 0                                                           #Loome loenduri, et lugeda kokku listi üksused
    for number in numbers:
        total += number                                                 #Arvutame summa
        count += 1                                                      #Tõstame loendurit ühe võrra
        average = total / count                                         #Arvutame keskmise
        largest = max(numbers)                                          #Leiame suurima arvu
    print(f'Summa: {total}')
    print(f'Keskmine: {average:.2f}')                                   #Kuvame kaks komakohta
    print(f'Suurim arv: {largest}')

with open(input, 'w', encoding='utf-8') as destination:                 #Tekitame faili
    destination.write(str(date) + '\n')                                 #Lisame faili kuupäeva ja reavahetuse
    for n in range(20):                                                 #Tekitame loopi
        destination.write(str(random.randint(1,100)) + ' ')             #Genereerime numbrid, muudame stringiks ja kirjutame need faili ning lisame tühikud vahele

with open(input, 'r', encoding='utf-8') as file:                        #Avame eelnevalt loodud faili
    numbers = [int(x) for x in file.readlines()[1].strip().split(' ')]  #Lisame muutujasse loodud failist teise rea numbrijadaga, eemaldame läbu ja eraldame tühikust

print(f'Failist loetud arvud: {numbers}')                               #Kuvame numrbid
calc()                                                                  #Kutsume eelnevalt loodud funktsiooni
