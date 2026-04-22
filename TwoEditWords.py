class Solution(object):
    def twoEditWords(self, queries, dictionary):
        result = []
        for query in queries:
            for target in dictionary:
                edits = 0
                for i in range(len(query)):
                    if query[i] != target[i]:
                        edits += 1
                    if edits > 2:
                        break
                if edits <= 2:
                    result.append(query)
                    break
                    
        return result
