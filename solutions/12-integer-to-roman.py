class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        place = 1
        while num >= 1:
            result = self.convertDigitToRoman(num % 10, place) + result
            place += 1
            num //= 10
        return result

    # digit is between 0 to 9
    # place is between 1 to 3 for this problem
    def convertDigitToRoman(self, digit: int, place: int) -> str:
        if place == 4:
            return 'M' * digit
        elif place == 3:
            if digit == 9:
                return 'CM'
            elif digit == 4:
                return 'CD'
            else:
                if digit >= 5:
                    return 'D' + 'C' * (digit - 5)
                else:
                    return 'C' * digit
        elif place == 2:
            if digit == 9:
                return 'XC'
            elif digit == 4:
                return 'XL'
            else:
                if digit >= 5:
                    return 'L' + 'X' * (digit - 5)
                else:
                    return 'X' * digit
        elif place == 1:
            if digit == 9:
                return 'IX'
            elif digit == 4:
                return 'IV'
            else:
                if digit >= 5:
                    return 'V' + 'I' * (digit - 5)
                else:
                    return 'I' * digit
