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
        for c in s:
            current = roman_int_map[c]
            if prev < current:
                    total += (current - prev * 2)
            
            else:
                total += current

            prev = current
        
        return total

print(Solution().romanToInt("XLIX"))