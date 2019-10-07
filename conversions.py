#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment6 conversions.py"""


def convertCelsiusToKelvin(value):
    return round(value + 273.15, 2)


def convertCelsiusToFahrenheit(value):
    return round((value * (9.0 / 5)) + 32, 2)


def convertKelvinToCelsius(value):
    return round(value - 273.15, 2)


def convertKelvinToFahrenheit(value):
    return round((value - 273.15) * (9.0 / 5) + 32, 2)


def convertFahrenheitToCelsius(value):
    return round((value - 32) * (5.0 / 9), 2)


def convertFahrenheitToKelvin(value):
    return round((value - 32) * (5.0 / 9) + 273.15, 2)
