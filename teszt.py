print('')
print('Írj be két számot: ')
elsoSzam = int(input('Elso szám: '))
masodikSzam = int(input('Masodik szam: '))
print('Két szám összege: ', elsoSzam + masodikSzam)
print('')
szamSor = [3, 5, 11, 4, 15, 9]
print(len(szamSor))
osszeg = (sum(szamSor))
print(szamSor)
print('Összeg: ',osszeg)
atlag = (osszeg/(len(szamSor)))
print('Átlag: ',atlag)
min1 = min(szamSor)
max1 = max(szamSor)
print('Minimum: ', min1, 'Maximum: ', max1)
vizsgalat = False
for valtozo in szamSor:
    if valtozo == 9:
        vizsgalat = True
if vizsgalat == True:
    print('Tartalmaz 9 es számiot')
else:
    print('Nem tartalmaz 9 es számot')        
import random
szamLista = []
for i in range(10):
    szamLista.append(random.randrange(1,10))

for i in szamLista:
    print(i)
print('')