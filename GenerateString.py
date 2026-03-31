class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        # Use None to represent unassigned positions
        res = [None] * total_len
        
        # Step 1: Fill all forced 'T' positions
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return "" # Conflict found
                    res[i + j] = str2[j]
        
        # Step 2: Fill gaps with 'a'
        for i in range(total_len):
            if res[i] is None:
                res[i] = 'a'
        
        # Step 3: Verify 'F' constraints and adjust if necessary
        # Since we only want the lexicographically smallest, if an 'F' index
        # currently matches str2, we must change the LAST character of that 
        # substring to 'b' (if possible) or the smallest available change.
        # However, we must ensure we don't overwrite a 'T' requirement.
        
        def check_at(idx):
            for j in range(m):
                if res[idx + j] != str2[j]:
                    return False
            return True

        for i in range(n):
            if str1[i] == 'F':
                # If it currently matches str2, we must change something
                if check_at(i):
                    # Try to change the last possible character in the m-length window
                    # that wasn't forced by a 'T' index.
                    changed = False
                    for k in range(m - 1, -1, -1):
                        pos = i + k
                        # Check if this specific character was forced by ANY 'T'
                        # A character at 'pos' is forced if str1[pos-j] == 'T' for any 0 <= j < m
                        is_forced = False
                        # We only need to check T's that could cover this position
                        for start_node in range(max(0, pos - m + 1), min(n, pos + 1)):
                            if str1[start_node] == 'T':
                                is_forced = True
                                break
                        
                        if not is_forced:
                            # Change 'a' to 'b' (or 'b' to 'a' if str2 had 'a', 
                            # but 'a' is always our default if not forced)
                            res[pos] = 'b' if str2[k] == 'a' else 'a'
                            changed = True
                            break
                    
                    if not changed:
                        return ""
                        
        return "".join(res)
