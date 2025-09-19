#For Loops

import random #Impordime random numbri mooduli

names = ['Mari', 'Anna', 'Juhan', 'Juss'] #Loon listi

for name in names: #Loop mis prindib välja listi sisu
    print(name)
print()

for x in range(len(names)): #Loop mis väljastab nii palju itemeid kui on "names" listis asju (hetkel 0-3)
    print(names[x], random.randint(1, 122)) #prindib ja lisab suvalise "vanuse" 1 ja 122 vahelt
print()

for x in range(1, 5): #prindib numbrid 1-4 
    print(x, end=' ') #prindib üksteise järgi ja lisab numbrite vahele tühiku
print('\n') #reavahetus

for x in range(0, 10, 2): #Paarisarvud kus 0 on algus, 10 lõpp ja 2 on sammude arv
    print(x, end=' | ')
print('\n')

#While loops
x = 0
while x < len(names):
    print(names[x])
    x += 1


"""
Väljasta listi nimed konsooli iga nimi eraldi real, kuid iga nime ees on järjekorra number.
Järjekorra number agab ühega.
"""

ages = []

for x in range(len(names)):
    ages.append(random.randint(1, 122))
    
    print(str(x + 1) + '. ' + names[x] + ' ' +str(ages[-1]))

print(names)
print(ages)