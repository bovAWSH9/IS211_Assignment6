#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment6 refractored_test.py"""

import unittest
from conversions_refactored import *


class TesTemperatureConversions(unittest.TestCase):

    def testConvertCelsiusToKelvin(self):
        print("Testing ConvertCelsiusToKelvin")
        result = convert("Celsius", "Kelvin", 1)
        self.assertEqual(round(result, 2), 274.15)

    def testConvertCelsiusToFahrenheit(self):
        print("Testing ConvertCelsiusToFahrenheit")
        result = convert("Celsius", "Fahrenheit", 1)
        self.assertEqual(round(result, 1), 33.8)

    def testConvertKelvinToCelsius(self):
        print("Testing ConvertKelvinToCelsius")
        result = convert("Kelvin", "Celsius", 1)
        self.assertEqual(round(result, 2), -272.15)

    def testConvertKelvinToFahrenheit(self):
        print("Testing ConvertKelvinToFahrenheit")
        result = convert("Kelvin", "Fahrenheit", 1)
        self.assertEqual(round(result, 2), -457.87)

    def testConvertFahrenheitToCelsius(self):
        print("Testing ConvertFahrenheitToCelsius")
        result = convert("Fahrenheit", "Celsius", 1)
        self.assertEqual(round(result, 2), -17.22)

    def testConvertFahrenheitToKelvin(self):
        print("Testing ConvertFahrenheitToKelvin")
        result = convert("Fahrenheit", "Kelvin", 1)
        self.assertEqual(round(result, 2), 255.93)


class TesDistanceConversions(unittest.TestCase):

    def testConvertMeterToYard(self):
        print("Testing ConvertMeterToYard")
        result = convert("meter", "yard", 1)
        self.assertEqual(round(result, 2), 1.09)

    def testConvertMeterToMile(self):
        print("Testing ConvertMeterToMile")
        result = convert("meter", "mile", 1)
        self.assertEqual(round(result, 1), 0.0)

    def testConvertYardToMeter(self):
        print("Testing ConvertYardToMeter")
        result = convert("yard", "meter", 1)
        self.assertEqual(round(result, 2), 0.91)

    def testConvertYardToMile(self):
        print("Testing ConvertYardToMile")
        result = convert("yard", "mile", 1)
        self.assertEqual(round(result, 2), 0.00)

    def testConvertMileToMeter(self):
        print("Testing ConvertMileToMeter")
        result = convert("mile", "meter", 1)
        self.assertEqual(round(result, 2), 1609.34)

    def testConvertMileToYard(self):
        print("Testing ConvertMileToYard")
        result = convert("mile", "yard", 1)
        self.assertEqual(round(result, 2), 1760.00)


class TestIncompatibleConversions(unittest.TestCase):

    def testInvalidConversions(self):
        for From in ["mile", "yard", "meter"]:
            for To in ["Kelvin", "Fahrenheit", "Celsius"]:
                try:
                    convert(From, To, 1)
                except ConversionNotPossible:
                    pass
                else:
                    self.fail("ConversionNotPossible")


class TestSameUnit(unittest.TestCase):
    def testSameUnites(self):

        for value in range(0, 50):
            x = convert('mile', 'mile', value)
            result = convert('mile', 'mile', x)
            self.assertEqual(value, result)

        for value in range(0, 50):
            x = convert('meter', 'meter', value)
            result = convert('meter', 'meter', x)
            self.assertEqual(value, result)

        for value in range(0, 50):
            x = convert('yard', 'yard', value)
            result = convert('yard', 'yard', x)
            self.assertEqual(value, result)

        for value in range(0, 50):
            x = convert('Celsius', 'Celsius', value)
            result = convert('Celsius', 'Celsius', x)
            self.assertEqual(value, result)

        for value in range(0, 50):
            x = convert('Kelvin', 'Kelvin', value)
            result = convert('Kelvin', 'Kelvin', x)
            self.assertEqual(value, result)

        for value in range(0, 50):
            x = convert('Fahrenheit', 'Fahrenheit', value)
            result = convert('Fahrenheit', 'Fahrenheit', x)
            self.assertEqual(value, result)


if __name__ == "__main__":
    unittest.main()
