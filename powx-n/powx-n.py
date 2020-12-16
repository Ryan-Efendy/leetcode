class Solution:
    '''
    Fast Exponentiation or exponentiation by squaring: https://www.youtube.com/watch?v=L8W38-iPdWE
    x^n = (x^2)^(n/2) if n is even
    x^n = x*(x^2)^*(n-1//2) if n is odd
    '''
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n < 0: return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, (n-1)//2)
