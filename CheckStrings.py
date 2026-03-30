class Solution(object):
    def checkStrings(self, s1, s2):
        # Compare characters at even indices
        even_s1 = sorted(s1[0::2])
        even_s2 = sorted(s2[0::2])
        
        # Compare characters at odd indices
        odd_s1 = sorted(s1[1::2])
        odd_s2 = sorted(s2[1::2])
        
        return even_s1 == even_s2 and odd_s1 == odd_s2
