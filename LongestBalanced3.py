class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        
        # Helper to find max length for a specific subset of characters
        def solve(chars):
            # map from state (tuple of differences) to first occurrence index
            # State: (count[chars[1]] - count[chars[0]], count[chars[2]] - count[chars[1]], ...)
            lookup = {tuple([0] * (len(chars) - 1)): -1}
            counts = {c: 0 for c in chars}
            
            curr_max = 0
            for i, char in enumerate(s):
                if char not in counts:
                    # Reset if we hit a character not in our target set
                    # Note: For this specific problem, we look for substrings 
                    # containing ONLY these characters or subset of them?
                    # "all distinct characters in the substring appear the same number of times"
                    # This means we should iterate through all 7 possible non-empty subsets.
                    pass 
            # Re-evaluating: The constraint is "all distinct characters in the substring".
            # This is slightly different from "fixed set". 
            # We iterate through all 7 possible combinations of {a, b, c}.
            
        # Let's try a more direct approach:
        # There are only 7 possible subsets of {'a', 'b', 'c'}:
        # {a}, {b}, {c}, {a,b}, {b,c}, {a,c}, {a,b,c}
        subsets = [('a',), ('b',), ('c',), ('a','b'), ('b','c'), ('a','c'), ('a','b','c')]
        
        for subset in subsets:
            target = set(subset)
            # We need a substring where ONLY these characters appear AND their counts are equal
            # Actually, the problem says "all distinct characters IN the substring"
            # So if a substring only has 'a' and 'b', we check if count(a) == count(b).
            # If it has 'a', 'b', and 'c', we check count(a) == count(b) == count(c).
            
            # To handle this, we can use a sliding window or a modified prefix hash.
            # But with N=10^5, an O(7 * N) approach is perfect.
            
            counts = {c: 0 for c in 'abc'}
            # We use a hashmap to store the first time a specific relative difference occurs
            # while ensuring ONLY the target characters have been seen in the current window.
            
            # Let's refine: For a fixed subset, find the longest substring containing 
            # EXACTLY those characters with equal counts.
            last_invalid = -1
            lookup = {tuple([0] * (len(subset) - 1)): -1}
            
            # For 1 char subsets, it's just the count of that char in any contiguous block.
            if len(subset) == 1:
                char = subset[0]
                curr = 0
                for c in s:
                    if c == char:
                        curr += 1
                        max_len = max(max_len, curr)
                    else:
                        curr = 0
                continue

            # For 2 or 3 chars:
            counts = {c: 0 for c in subset}
            diff_map = {tuple([0] * (len(subset) - 1)): -1}
            
            # Tracking indices where any character NOT in subset appeared
            bad_char_idx = -1
            
            running_counts = {c: 0 for c in subset}
            for i, c in enumerate(s):
                if c not in target:
                    # If we hit a char not in our subset, reset
                    bad_char_idx = i
                    running_counts = {char: 0 for char in subset}
                    diff_map = {tuple([0] * (len(subset) - 1)): i}
                else:
                    running_counts[c] += 1
                    # Create a state based on differences
                    # e.g., for {a, b}, state is (count_a - count_b)
                    # e.g., for {a, b, c}, state is (count_a - count_b, count_b - count_c)
                    if len(subset) == 2:
                        state = (running_counts[subset[0]] - running_counts[subset[1]],)
                    else:
                        state = (running_counts['a'] - running_counts['b'], 
                                 running_counts['b'] - running_counts['c'])
                    
                    if state in diff_map:
                        # Check if all characters in the subset have appeared at least once
                        # in the range (diff_map[state] + 1, i)
                        # Actually, the "all distinct characters" rule means if we are
                        # looking for the {a, b} subset, the substring MUST contain a and b.
                        start_idx = diff_map[state]
                        length = i - start_idx
                        
                        # Validation: Does this window contain ONLY and ALL of the subset?
                        # Since we reset on bad_char, we know it only contains subset chars.
                        # We just need to ensure count > 0 for all in subset.
                        is_valid = True
                        for char in subset:
                            # This is the tricky part: we need the count within the specific window
                            # But wait, if counts are equal and > 0, the logic holds.
                            pass
                        
                        # Optimization: Instead of full validation, just ensure the substring 
                        # contains all characters of the subset.
                        # We can track the last seen index of each character.
                        # This is getting complex. Let's simplify.
                        
        # Simplified Logic: 
        # A substring is balanced if:
        # count(a)==count(b) (if c is absent)
        # count(b)==count(c) (if a is absent)
        # count(a)==count(c) (if b is absent)
        # count(a)==count(b)==count(c) (if all present)
        # length of 1 (if only one type present)
        
        # For N=10^5, we can just use the standard "Equal Counts" prefix sum trick 
        # for all combinations of characters.
        
        def get_max_for_subset(chars):
            res = 0
            # map of (diffs) -> first index
            lookup = {tuple([0]*(len(chars)-1)): -1}
            counts = {c: 0 for c in chars}
            
            # To ensure the substring contains EXACTLY these characters, 
            # we track the last time each character was seen.
            last_seen = {c: -1 for c in chars}
            
            # We also need to know when a character NOT in this subset was last seen
            other_chars = [c for c in 'abc' if c not in chars]
            last_other = -1
            
            curr_counts = [0] * len(chars)
            
            for i, c in enumerate(s):
                if c in other_chars:
                    last_other = i
                    # Reset tracking
                    lookup = {tuple([0]*(len(chars)-1)): i}
                    curr_counts = [0] * len(chars)
                    continue
                
                # Update counts for characters in subset
                for idx, char in enumerate(chars):
                    if c == char:
                        curr_counts[idx] += 1
                        last_seen[char] = i
                
                # Calculate differences
                diffs = []
                for j in range(len(chars) - 1):
                    diffs.append(curr_counts[j] - curr_counts[j+1])
                state = tuple(diffs)
                
                if state in lookup:
                    start_idx = lookup[state]
                    # The substring is s[start_idx+1 : i+1]
                    # It contains ONLY chars from our subset.
                    # Does it contain ALL chars from our subset?
                    if all(last_seen[char] > start_idx for char in chars):
                        res = max(res, i - start_idx)
                else:
                    lookup[state] = i
            return res

        final_ans = 0
        # Subsets of size 1
        final_ans = max(final_ans, 1 if n > 0 else 0) # Any single char is balanced
        # Correctly: any sequence of identical chars is balanced. 
        # Example: "aaaa" is balanced (distinct chars: {a}, count: 4).
        temp = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                temp += 1
            else:
                temp = 1
            final_ans = max(final_ans, temp)
            
        # Subsets of size 2 and 3
        for sub in [('a','b'), ('b','c'), ('a','c'), ('a','b','c')]:
            final_ans = max(final_ans, get_max_for_subset(sub))
            
        return final_ans

