import sys
import math
import re

def value_validator(value_to_check): #program przyjmuje ulamki zarowno w formie dziesietnej, z przecinkiem i kropka
    type_of_fractioning = re.compile(r'\/|\,|\.')
    rege = type_of_fractioning.search(value_to_check)
    if rege:
        if rege.group() == '/':
            match_before = re.match(r'^([^/]*)', value_to_check)
            if match_before:
                up_frac = float(match_before.group(1))
            match_after = re.search(r'/(.*)$', value_to_check)
            if match_after:
                down_frac = float(match_after.group(1))
            value_to_check_float = float(up_frac/down_frac)
            return value_to_check_float
        elif rege.group() == '.':
            value_to_check_float = float(value_to_check)
            return value_to_check_float
        elif rege.group() == ',':
            value_to_check = value_to_check.replace(',', '.')
            value_to_check_float = float(value_to_check)
            return value_to_check_float
    else:
        int_check = re.compile(r'^\d+$|^-\d+$')
        int_check_result = bool(int_check.match(value_to_check))
        if int_check_result:
            value_to_check_float = float(value_to_check)
            return value_to_check_float
        else:
            raise ValueError('Podana wartosc nie jest integerem ani wartoscia ulamkowa')

def expo_calc(base_corrected, exp_corrected): #funk do unit testow
    return round(pow(base_corrected, exp_corrected), 3)

def expo_menu():
    while True:
        try:
            base = input('Podaj podstawe potegi: \n')
            base_corrected = value_validator(base)
            exp = input('wykladnik potegi: \n')
            exp_corrected = value_validator(exp)
            result = expo_calc(base_corrected, exp_corrected)
            return result
        except ValueError:
            print('Zarowno podstawa jak i wykladnik potegi musza byc liczbami')
            continue  

def mins_calc(user_time_corrected): #funk do unit testow
    return round(user_time_corrected * 60)    

def mins_menu():
    while True:
        try:
            user_time = input('Podaj ulamek godziny do obliczenia na minuty: \n')
            user_time_corrected = value_validator(user_time)
            result = mins_calc(user_time_corrected)
            return result
        except ValueError as e:
            print(e)

def distance_calc(dist_value_corrected,user_choice_dist): #funk do unit testow
    conversion_value = 1.609344
    if user_choice_dist == '1':
        result_value = round(dist_value_corrected/conversion_value, 3)
        return ('milach to ' + str(result_value))
    elif user_choice_dist == '2':
        result_value = round(dist_value_corrected * conversion_value, 3)
        return ('kilometrach to ' + str(result_value))

def distance_menu():
    while True:
        try:
            user_choice_dist = input('1. kilometry -> mile\n2. mile -> kilometry\n')
            if user_choice_dist not in ['1','2']:
                print('wybierz z dostepnych.')
                user_choice_dist = input('1. kilometry -> mile\n2. mile -> kilometry\n')
                continue
            dist_value = input('Podaj wartosc ktora chcesz przeliczyc:\n')
            dist_value_corrected = value_validator(dist_value)
            result = distance_calc(dist_value_corrected,user_choice_dist)
            return result
        except ValueError as e:
            print(e)

def divide_calc(num_1_corrected, num_2_corrected): #funk do unit testow
    return round(num_1_corrected/num_2_corrected, 2) #poprawione mnozenie na dzielenie

def divide_menu():
    while True:
        try:
            num_1 = input('Podaj liczbe do podzielenia: \n')
            num_1_corrected = value_validator(num_1)
            num_2 = input('Podaj liczbe przez ktora dzielisz: \n')
            num_2_corrected = value_validator(num_2)
            if num_2 == '0':
                raise ValueError
            else:
                result = divide_calc(num_1_corrected, num_2_corrected)
                return result
        except ValueError:
            print('Obie wartosci musza byc liczbami i mianownik nie moze byc zerem')
            continue

if __name__ == '__main__':
    while True:
        print('\nKalkulator wita. Wybierz jedną z opcji:')
        print('1. potegowanie')
        print('2. przeliczanie ulamkow na minuty')
        print('3. mile <=> kilometry')
        print('4. dzielenie z zaokragleniem')
        print('"end" zeby zamknac program')

        user_choice = input('Podaj dzialanie:\n')

        if user_choice not in ['1','2','3','4','end']: #zapomnialem ze switch istnieje xD
            print('Wybierz poprawne dzialanie')
            continue
        if user_choice == 'end':
            print('Papa')
            sys.exit()

        print("Wybrano opcje: ", user_choice)

        if user_choice == '1':
            power = expo_menu()
            print('Wynik to:\n', power)

        elif user_choice == '2':
            time_output = mins_menu()
            print('Podany czas to: ', time_output, 'minut')
        
        elif user_choice == '3':
            km_miles = distance_menu()
            print('Wartosc w ', km_miles)

        elif user_choice == '4':
            division_results = divide_menu()
            print('Wynik dzielenia wynosi: ', division_results)