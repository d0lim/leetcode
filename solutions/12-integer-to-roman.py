class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        place = 1
        while num >= 1:
            result = self.convertPlaceDigitToRoman(num % 10, place) + result
            place += 1
            num //= 10
        return result

    # digit is between 0 to 9
    # place is between 1 to 3 for this problem
    def convertPlaceDigitToRoman(self, digit: int, place: int) -> str:
        if place == 4:
            return 'M' * digit
        elif place == 3:
            return self.convertDigitToRoman(digit, 'M', 'D', 'C')
        elif place == 2:
            return self.convertDigitToRoman(digit, 'C', 'L', 'X')
        elif place == 1:
            return self.convertDigitToRoman(digit, 'X', 'V', 'I')
    
    def convertDigitToRoman(self, digit: int, symbolForTen: str, symbolForFive: str, symbolForOne: str)-> str:
        if digit == 9:
            return symbolForOne + symbolForTen
        elif digit == 4:
            return symbolForOne + symbolForFive
        else:
            if digit >= 5:
                return symbolForFive + symbolForOne * (digit -5)
            else:
                return symbolForOne * digit
