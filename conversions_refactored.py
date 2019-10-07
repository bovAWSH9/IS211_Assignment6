#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment6 conversions_refactored.py"""

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    if fromUnit == "meter":
        if toUnit == "yard":
            ret_value = round(value * 1.0936, 3)
            return ret_value
        elif toUnit == "mile":
            ret_value = round(value / 1609.344, 3)
            return ret_value
        elif toUnit == "meter":
            return value

    elif fromUnit == "mile":
        if toUnit == "meter":
            ret_value = round(value * 1609.344, 3)
            return ret_value
        elif toUnit == "yard":
            ret_value = round(value * 1760.0, 3)
            return ret_value
        elif toUnit == "mile":
            return value

    elif fromUnit == "yard":
        if toUnit == "meter":
            ret_value = round(value * 0.9144, 3)
            return ret_value
        elif toUnit == "mile":
            ret_value = round(value / 1760.0, 3)
            return ret_value
        elif toUnit == "yard":
            return value

    elif fromUnit == "Celsius":
        if toUnit == "Kelvin":
            ret_value = round(value + 273.15, 2)
            return ret_value
        elif toUnit == "Fahrenheit":
            ret_value = round(value * (9.0 / 5.0) + 32, 2)
            return ret_value
        elif toUnit == "Celsius":
            return value

    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            ret_value = round((value - 32) * (5.0 / 9.0), 2)
            return ret_value
        elif toUnit == "Kelvin":
            ret_value = round((value + 459.67) * (5.0 / 9.0), 2)
            return ret_value
        elif toUnit == "Fahrenheit":
            return value

    elif fromUnit == "Kelvin":
        if toUnit == "Fahrenheit":
            ret_value = round((value * (9.0 / 5.0)) - 459.67, 2)
            return ret_value
        elif toUnit == "Celsius":
            ret_value = round(value - 273.15, 2)
            return ret_value
        elif toUnit == "Kelvin":
            return value

    if fromUnit in ["meter", "yard", "mile"] and toUnit in ["Celsius", "Fahrenheit", "Kelvin"]:
        raise ConversionNotPossible("")

    if fromUnit in ["Celsius", "Fahrenheit", "Kelvin"] and toUnit in ["meter", "yard", "mile"]:
        raise ConversionNotPossible("")
