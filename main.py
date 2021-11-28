from classes import *

pojazd_1 = Pojazd('lambordzini', 'gallardo', 2015, 100, 4.5)
pojazd_2 = Pojazd('mazerati', 'quatroporte', 2018, 300, 3.0)

firma_transportowa = FirmaTransportowa('majkel_dzekson_transport', 'sosnowiec',
                                       123456789, 2, [pojazd_1, pojazd_2])

odcinek_1 = Odcinek('tarnowskie gory', 'sosnowiec', 50.5, False, False)
odcinek_2 = Odcinek('sosnowiec', 'krakow', 70.3, True, True)

# Create a Kurs object
kurs_1 = Kurs()
kurs_1.firma = firma_transportowa
kurs_1.odcinki = [odcinek_1, odcinek_2]
kurs_1.data_kursu = '2020-01-01'
kurs_1.kierowca = 'zbyszek wojcik'
kurs_1.czas_minuty = 30.5
kurs_1.pojazd = kurs_1.firma.pojazdy[0]

# Test of the oblicz_sume_kilometrow method
print(f'Suma kilometrow w kursie: {kurs_1.oblicz_sume_kilometrow()}')

# Test of zwroc_marke_pojazdu method
print(f'Marka pojazdu w kursie: {kurs_1.zwroc_marke_pojazdu()}')

# Print the kurs_1 object
print(kurs_1)
