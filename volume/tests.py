import unittest
import math
from volume_calc import objetosc_szescianu, objetosc_prostopadloscianu, objetosc_graniastoslupa, objetosc_stozka

class TestStringMethods(unittest.TestCase):

#test objetosc szczescianu
    def test_obj_szescianu_true(self):
        a = 2
        result_expected = math.pow(a, 3)
        result_real = objetosc_szescianu(a)
        self.assertEqual(result_expected, result_real)

    def test_obj_szescianu_false(self):
        a = 2
        result_expected = math.pow(a, 2)
        result_real = objetosc_szescianu(a)
        self.assertNotEqual(result_expected, result_real)
    
#test objetosc prostopadloscianu

    def test_obj_prostopadloscianu_true(self):
        a = 2
        b = 3
        c = 4
        result_expected = a*b*c
        result_real = objetosc_prostopadloscianu(a,b,c)
        self.assertEqual(result_expected, result_real)
    
    def test_obj_prostopadloscianu_false(self):
        a = 2
        b = 3
        c = 4
        result_expected = a/b/c
        result_real = objetosc_prostopadloscianu(a,b,c)
        self.assertNotEqual(result_expected, result_real)

#test objetosc graniastoslupa

    def test_obj_graniastos_true(self):
        pole_podstawy = 2
        wysokosc_graniastoslupa = 3
        result_expected = pole_podstawy * wysokosc_graniastoslupa
        result_real = objetosc_graniastoslupa(pole_podstawy, wysokosc_graniastoslupa)
        self.assertEqual(result_expected, result_real)

    def test_obj_graniastos_false(self):
        pole_podstawy = 2
        wysokosc_graniastoslupa = 3
        result_expected = pole_podstawy ** wysokosc_graniastoslupa
        result_real = objetosc_graniastoslupa(pole_podstawy, wysokosc_graniastoslupa)
        self.assertNotEqual(result_expected, result_real)

#test objetosc stozka

    def test_obj_stozka_true(self):
        promien_podstawy = 2
        wysokosc_stozka = 3
        result_expected = (1/3) * math.pi * math.pow(promien_podstawy, 2) * wysokosc_stozka
        result_real = objetosc_stozka(wysokosc_stozka, promien_podstawy,)
        self.assertAlmostEqual(result_expected, result_real)

    def test_obj_stozka_false(self):
        promien_podstawy = 2
        wysokosc_stozka = 3
        result_expected = 1/3 * math.pow(promien_podstawy, 2) * wysokosc_stozka
        result_real = objetosc_stozka(promien_podstawy, wysokosc_stozka)
        self.assertNotEqual(result_expected, result_real)


#test results: obj stozka zle liczona, promien nie do kwadratu