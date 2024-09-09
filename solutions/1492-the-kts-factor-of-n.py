import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        square_root = math.sqrt(n)
        factors = set()
        for i in range(1, math.floor(square_root) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)

        return list(sorted(factors))[k - 1] if(len(factors) >= k) else -1
