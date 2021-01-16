class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        if n == 1: return True
        n = str(n)
        while True:
            total = 0
            for i in n[::-1]:
                total += int(i)**2
            if total == 1: return True
            elif total in s: return False
            s.add(total)
            n = str(total)
        return False
