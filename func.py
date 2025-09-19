#"""------------FUNKTSIOONID-----------------------------------------------------
def welcome(): #Väljastab staatilise tervitusteksti
    print('Tere')

welcome()
#"""-----------------------------------------------------------------------------
#"""-----------------------------------------------------------------------------
def welcome_name(name): #Tagastab sõnumi koos nimega
    return f'Tere, {name}'

print(welcome_name('Tiit'))


kukimuki = welcome_name('Kukimuki')
print(kukimuki)
#"""-----------------------------------------------------------------------------
#"""-----------------------------------------------------------------------------
def division(numb1, numb2):
    """
    Teostab kahe arvu jagamise
    Argumendid:
        numb1 (float): Jagatav arv
        numb2 (float): Jagaja (ei tohi olla null)

    Returns:
        float: Jagatise väärtus
    """
    if numb2 != 0:
        return numb1 / numb2
    return -1

a = 100
b = 20
print(division(a, b))
print(division(a, 0))
#"""-----------------------------------------------------------------------------
#"""-----------------------------------------------------------------------------
def introduce(name, age=25):
    """Loob tutvustava lause

    :param name: Isiku nimi
    :type name: str
    :param age: Isiku vanus (vaikimisi 25)
    :type age: int, valikuline
    :return: Tekstiline tutvustus vormis
            'Tema on <nimi> ja ta on <vanus> aastane!'
    :rtype: str
    """
    return f'Tema on {name} ja ta on {age} aastane!'

print(introduce('Jaak'))
print(introduce('Juhan', 34))
print(introduce(123,124))
#"""-----------------------------------------------------------------------------
#"""-----------------------------------------------------------------------------
#Loo list viie nimega. Väljasta kolme nime tervitus.

names = ['Juss','Jaan','Juku','Juhan','Joosep']
for name in names: 
    print(welcome_name(name))
#"""-----------------------------------------------------------------------------