class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        freq = [0] * (n + 1)
        C = []
        common_count = 0
        
        for i in range(n):
            # Process element from A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
                
            # Process element from B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1
                
            # Append the count of common elements at this prefix
            C.append(common_count)
            
        return C
        
