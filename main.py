from classes.dieta import Dieta
from classes.osoba import *
from classes.zamowienie import Zamowienie


dieta_1 = Dieta(1, 'Spalacz fetu max', 30.501111, 1200)
dieta_2 = Dieta(2, 'Bodybuilder 3000', 60, 4000)

dietetyk_1 = Dietetyk('Majkel', 'Dzekson', 997123666,
                      'Dietetyk sportowy',  '13-02-2013')

pacjent_1 = Pacjent('Tina', 'Turner', 777132111, 1939,
                    'Waniliowa 23, 41-200 Sosnowiec')

zamowienie_1 = Zamowienie()
zamowienie_1.pacjent = pacjent_1
zamowienie_1.dietetyk = dietetyk_1
zamowienie_1.diety = [dieta_1, dieta_2]
zamowienie_1.data_zamowienia = '15-01-2022'

# Test of the oblicz_wartosc_zamowienia method
print(f'Wartosc zamowienia: {zamowienie_1.oblicz_wartosc_zamowienia()}')

# Test of the oblicz_kalorycznosc_zamowienia method
print(f'Kalorycznosc zamowionej diety: '
      f'{zamowienie_1.oblicz_kalorycznosc_zamowienia()}')

# Print the zamowienie_1 object
print(zamowienie_1)
