import unittest
import sys
import math
import re

from math_calc import mins_calc, distance_calc, expo_calc, divide_calc, value_validator

class TestStringMethods(unittest.TestCase):
    #test expo
    def test_good_expo(self):
        base_corrected = 2
        exp_corrected = 2
        expo_result_expected = round(pow(base_corrected, exp_corrected), 3)
        expo_result_real = expo_calc(base_corrected, exp_corrected)

        self.assertEqual(expo_result_expected, expo_result_real)

    def test_bad_expo(self):
        base_corrected = 2
        exp_corrected = 3
        expo_result_expected = base_corrected * exp_corrected
        expo_result_real = expo_calc(base_corrected, exp_corrected)

        self.assertNotEqual(expo_result_expected, expo_result_real)

    #test mins
    def test_good_mins(self):
        user_time_corrected = 2
        mins_result_expected = round(user_time_corrected * 60)
        mins_result_real = mins_calc(user_time_corrected)

        self.assertEqual(mins_result_expected, mins_result_real)

    def test_bad_mins(self):
        user_time_corrected = 2
        mins_result_expected = round(user_time_corrected / 60)
        mins_result_real = mins_calc(user_time_corrected)

        self.assertNotEqual(mins_result_expected, mins_result_real)

    #test distance
    def test_good_case1_distance(self):
        dist_value_corrected = 2
        user_choice_dist = '1'
        conversion_value = 1.609344
        dist_result_expected = round(dist_value_corrected/conversion_value, 3)
        dist_result_real = distance_calc(dist_value_corrected,user_choice_dist)

        self.assertEqual(dist_result_expected, dist_result_real)

    def test_bad_case1_distance(self):
        dist_value_corrected = 2
        user_choice_dist = '1'
        conversion_value = 1.609344
        dist_result_expected = round(dist_value_corrected*conversion_value, 3)
        dist_result_real = distance_calc(dist_value_corrected,user_choice_dist)

        self.assertNotEqual(dist_result_expected, dist_result_real)

    def test_good_case2_distance(self):
        dist_value_corrected = 2
        user_choice_dist = '2'
        conversion_value = 1.609344
        dist_result_expected = round(dist_value_corrected*conversion_value, 3)
        dist_result_real = distance_calc(dist_value_corrected,user_choice_dist)

        self.assertEqual(dist_result_expected, dist_result_real)

    def test_bad_case2_distance(self):
        dist_value_corrected = 2
        user_choice_dist = '2'
        conversion_value = 1.609344
        dist_result_expected = round(dist_value_corrected/conversion_value, 3)
        dist_result_real = distance_calc(dist_value_corrected,user_choice_dist)

        self.assertNotEqual(dist_result_expected, dist_result_real)


    #test dividie
    def test_good_divide(self):
        num_1_corrected = 2
        num_2_corrected = 2
        dividie_result_expected = round(num_1_corrected/num_2_corrected, 2)
        divide_result_real = divide_calc(num_1_corrected, num_2_corrected)
        self.assertEqual(dividie_result_expected, divide_result_real)

    def test_bad_divide(self):
        num_1_corrected = 2
        num_2_corrected = 2
        dividie_result_expected = round(num_1_corrected-num_2_corrected, 2)
        divide_result_real = divide_calc(num_1_corrected, num_2_corrected)

        self.assertNotEqual(dividie_result_expected, divide_result_real)