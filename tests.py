#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment6 tests.py"""

import unittest
from conversions import *


class TestCases(unittest.TestCase):

    def testConvertCelsiusToKelvin(self):
        print("Testing ConvertCelsiusToKelvin")
        result = convertCelsiusToKelvin(1)
        self.assertEqual(round(result, 2), 274.15)

    def testConvertCelsiusToFahrenheit(self):
        print("Testing ConvertCelsiusToFahrenheit")
        result = convertCelsiusToFahrenheit(1)
        self.assertEqual(round(result, 1), 33.8)

    def testConvertKelvinToCelsius(self):
        print("Testing ConvertKelvinToCelsius")
        result = convertKelvinToCelsius(1)
        self.assertEqual(round(result, 2), -272.15)

    def testConvertKelvinToFahrenheit(self):
        print("Testing ConvertKelvinToFahrenheit")
        result = convertKelvinToFahrenheit(1)
        self.assertEqual(round(result, 2), -457.87)

    def testConvertFahrenheitToCelsius(self):
        print("Testing ConvertFahrenheitToCelsius")
        result = convertFahrenheitToCelsius(1)
        self.assertEqual(round(result, 2), -17.22)

    def testConvertFahrenheitToKelvin(self):
        print("Testing ConvertFahrenheitToKelvin")
        result = convertFahrenheitToKelvin(1)
        self.assertEqual(round(result, 2), 255.93)


if __name__ == "__main__":
    unittest.main()
