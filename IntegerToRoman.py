class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        res = ""
        for sym, val in reversed(symList):
            if num // val:             #if num//val exists ie val < num 
                count = num // val     # count will be initial quotient ie for 15 it will be 15//10 = 1 i.e X
                res += sym * count     # X * 1  1 FROM ABOVE LINE
                num = num % val        # MAKE NUM AS THE REMAINDER AND NOW FIND THE SYMBOL FOR IT, I.E FOR 15 % 10 = 5 
        return res                     # 5 // 5 = 1 SO SYM*COUNT -> V * 1 SO RES = XV