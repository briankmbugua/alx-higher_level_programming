#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) == str):
        index = len(roman_string) - 1
        digits = []
        symbols = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                }
        value = symbols[roman_string[index]]
        while index >= 0:
            symbol = roman_string[index]

            if symbols[roman_string[index - 1]] < symbols[symbol] and index != 0:
                digits.append(symbols[symbol] - symbols[roman_string[index - 1]])
                index -= 2
            elif symbols[roman_string[index - 1]] >= symbols[symbol] and index != 0:
                digits.append(symbols[symbol])
                value = symbols[symbol]
                index -= 1
            elif index == 0:
                digits.append(symbols[symbol])
                break
        return sum(digits)
    else:
        return 0
