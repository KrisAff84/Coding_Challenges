"""
The goal of this version is to provide checks to determine if the input string is a valid
roman numeral string. Still working out some kinks
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev = 0
        prev_lt = 0
        repeat_num = 0
        for c in s:
            if c not in roman_int_map:
                raise ValueError(f'Invalid roman numeral character: {c}')
            
            current = roman_int_map[c]
            if prev < current:
                total += (current - prev * 2)
                prev_lt += 1

                # Prevents more than one subtracting numeral
                # Prevents additional larger numeral after subtracting numeral
                if repeat_num > 0 or prev_lt > 2:
                    raise ValueError('Invalid roman numeral string')
        
            else:
                total += current

                if current == prev:
                    repeat_num += 1
                else:
                    repeat_num = 0

                # Prevents more than 3 of the same character in a row
                # Prevents additional less than or equal numeral after subtracting numeral
                if repeat_num > 2 or prev_lt > 1:
                    raise ValueError('Invalid roman numeral string')

            prev = current 

        return total

print(Solution().romanToInt("XLIX")) 
