# 1. Single Roman Numerals
# 2. Additive Roman Numerals
# 3. Subtractive Roman Numerals
# 4. Roman Numerals with both addition and subtraction within same number
# 5. Handling invalid inputs

# Define Roman Numerals
def_roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]

# Conversion of single Roman Numerals
def convert_single_roman_numeral_to_int(roman_numeral):
    match roman_numeral:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
    return 0

# Checking is valid Roman Numerals
def is_valid_roman_numerals(roman_numerals):
    # Invalid Roman Numerals
    for roman_numeral in roman_numerals:
        if roman_numeral not in def_roman_numerals:
            return False
    # Four consecutive identical Roman Numerals
    for i in range(len(roman_numerals) - 3):
        if(roman_numerals[i] == roman_numerals[i+1] == roman_numerals[i+2] == roman_numerals[i+3]):
            return False
    return True

# Convert Roman Numerals to Integer
def convert_roman_numerals_to_int(roman_numerals):
    # Check space and lowercase in Roman Numerals
    roman_numerals = roman_numerals.strip()
    roman_numerals = roman_numerals.upper()
    # Check is valid Roman Numerals
    if not is_valid_roman_numerals(roman_numerals):
        print("Invalid Roman Numerals!")
        return None

    # Converting
    total = 0
    prev_val = 0
    
    for roman_numeral in reversed(roman_numerals):
        current_val = convert_single_roman_numeral_to_int(roman_numeral)
        if current_val < prev_val:
            total -= current_val
        else:
            total += current_val
        prev_val = current_val
    
    print(total)


# Example
convert_roman_numerals_to_int(" McMXCViI   ")