class Solution(object):
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        p = [[1] * m for _ in range(n)]
        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                pref = (pref * grid[i][j]) % MOD
                
        # Backward pass: calculate suffix products and combine with prefixes
        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Multiply the stored prefix product by the running suffix product
                p[i][j] = (p[i][j] * suff) % MOD
                # Update the running suffix product for the previous cell
                suff = (suff * grid[i][j]) % MOD
                
        return p
