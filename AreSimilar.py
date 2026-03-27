class Solution(object):
    def areSimilar(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        # We only need to check the effective shift
        shift = k % n
        
        # If there's no effective shift, it's always true
        if shift == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                # For even rows (left shift): 
                # Original element at j moves to (j - k) % n
                # For odd rows (right shift): 
                # Original element at j moves to (j + k) % n
                
                # However, the matrix is identical ONLY if:
                # mat[i][j] == mat[i][(j + shift) % n]
                # This check works for both directions because 
                # if a row is identical after a shift, it must be periodic.
                if mat[i][j] != mat[i][(j + shift) % n]:
                    return False
                    
        return True
