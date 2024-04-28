from area_calc import trojkat, kwadrat, prostkat, romb

# Lista do przechowywania błędów
bledy = []

# Sprawdzenie funkcji pola trójkąta
wysokosc = 3
podstawa = 6
oczekiwany_wynik = 0.5 * podstawa * wysokosc
wynik_pola = trojkat(podstawa, wysokosc)

try:
    assert wynik_pola == oczekiwany_wynik
except AssertionError:
    bledy.append("Błąd: Pole trójkąta nie zostało obliczone poprawnie")

# Sprawdzenie funkcji pola kwadratu
dlugosc_boku_kwadratu = 2
oczekiwany_wynik = dlugosc_boku_kwadratu * dlugosc_boku_kwadratu
wynik_pola = kwadrat(dlugosc_boku_kwadratu)

try:
    assert wynik_pola == oczekiwany_wynik
except AssertionError:
    bledy.append("Błąd: Pole kwadratu nie zostało obliczone poprawnie")

# Sprawdzenie funkcji pola prostokąta
dlugosc_bok_a = 3  
dlugosc_bok_b = 6  
oczekiwany_wynik = dlugosc_bok_a * dlugosc_bok_b
wynik_pola = prostkat(dlugosc_bok_a, dlugosc_bok_b)

try:
    assert wynik_pola == oczekiwany_wynik
except AssertionError:
    bledy.append("Błąd: Pole prostokąta nie zostało obliczone poprawnie")

# Sprawdzenie funkcji pola rombu
bok_a = 3  
bok_b = 6
wysokosc_rombu = 5  
oczekiwany_wynik = 0.5 * (bok_a + bok_b) * wysokosc_rombu
wynik_pola = romb(bok_a, bok_b, wysokosc_rombu)

try:
    assert wynik_pola == oczekiwany_wynik
except AssertionError:
    bledy.append("Błąd: Pole rombu nie zostało obliczone poprawnie")

if bledy:
    for blad in bledy:
        print(blad)
else:
    print("Wszystkie pola zostały obliczone poprawnie.")