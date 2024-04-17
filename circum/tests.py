import math
from circum_calc import obwod_kola, obwod_kwadratu, obwod_prostokata, obwod_trojkata


# Sprawdzenie funkcji obwod_kola
promien = 2
oczekiwany_wynik = 4 * math.pi
wynik_obwodu = obwod_kola(promien)

assert wynik_obwodu == oczekiwany_wynik, "Błąd: Obwód koła nie został obliczony poprawnie"



# Sprawdzenie funkcji obwod_kwadratu
dlugosc_boku = 6  # Przykładowa długość boku kwadratu
oczekiwany_wynik = 4 * dlugosc_boku
wynik_obwodu = obwod_kwadratu(dlugosc_boku)

assert wynik_obwodu == oczekiwany_wynik, "Błąd: Obwód kwadratu nie został obliczony poprawnie"



#Sprawdzenie obwodu prostokata 

dlugosc_bok_a = 4  
dlugosc_bok_b = 6  
oczekiwany_wynik = 2 * dlugosc_bok_a + 2 * dlugosc_bok_b
wynik_obwodu = obwod_prostokata(dlugosc_bok_a, dlugosc_bok_b)

assert wynik_obwodu == oczekiwany_wynik, "Błąd: Obwód prostokąta nie został obliczony poprawnie"


# Sprawdzenie funkcji obwodu trójkąta

dlugosc_boku_a = 3 
dlugosc_boku_b = 4  
dlugosc_boku_c = 5  
oczekiwany_wynik = dlugosc_boku_a + dlugosc_boku_b + dlugosc_boku_c
wynik_obwodu = obwod_trojkata(dlugosc_boku_a, dlugosc_boku_b, dlugosc_boku_c)

assert wynik_obwodu == oczekiwany_wynik, "Błąd: Obwód trójkąta nie został obliczony poprawnie"
