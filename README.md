# Roman Numeral Converter

This Python project provides a utility to convert Roman numerals into integers. It also checks for invalid Roman numerals (four consecutive identical letters) and prevents such inputs.

## Features

- Converts Roman numerals to integers.
- Detects invalid Roman numerals and shows error messages.
- Prevents more than three consecutive identical numerals ("A", "IIII" are invalid).

## Usage

1. Clone or download the project from GitHub.

```bash
git clone https://github.com/your_username/roman-numeral-converter.git
```

2. Run the project by opening your terminal or command prompt and using the following command:

```bash
python roman_numeral_converter.py
```

3. Example Usage:

```bash
roman_numerals_to_int("IX")  # Output: 9
roman_numerals_to_int(" McMXCViI   ")  # Output: 1997
roman_numerals_to_int("IIII")  # Output: Invalid Roman Numerals!
```
