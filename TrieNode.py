class TrieNode(object):
    # Using __slots__ reduces memory overhead and improves attribute access speed
    __slots__ = ['children', 'best_idx'] 
    
    def __init__(self, best_idx):
        self.children = {}
        self.best_idx = best_idx

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        # Step 1: Find the absolute best fallback index for an empty suffix match
        # We want the shortest word overall. In a tie, the earlier index wins.
        best_global_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best_global_idx]):
                best_global_idx = i
                
        root = TrieNode(best_global_idx)
        
        # Step 2: Build the Suffix Trie (inserting words in reverse)
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    # Initialize new node with the current word's index
                    curr.children[char] = TrieNode(i)
                
                child = curr.children[char]
                
                # Update best_idx if the current word is strictly shorter.
                # Note: We don't need to explicitly handle index tie-breakers (i < child.best_idx)
                # because we iterate through wordsContainer in increasing order of 'i'. 
                # The first word to reach this node naturally claims the smallest index.
                if len(word) < len(wordsContainer[child.best_idx]):
                    child.best_idx = i
                    
                curr = child
                
        # Step 3: Answer Queries
        ans = []
        for q in wordsQuery:
            curr = root
            for char in reversed(q):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break # Stop when the common suffix ends
            ans.append(curr.best_idx)
            
        return ans
