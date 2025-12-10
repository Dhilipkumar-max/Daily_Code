from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        # If any computer i>0 has complexity <= complexity[0], impossible.
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        # Otherwise every ordering of the remaining n-1 computers works:
        ans = 1
        for k in range(1, n):   # multiply 1 * 2 * ... * (n-1)
            ans = (ans * k) % MOD
        return ans
