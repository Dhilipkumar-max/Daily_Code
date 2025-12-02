class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        from collections import defaultdict
        ycount = defaultdict(int)

        # Count points per y-coordinate
        for x, y in points:
            ycount[y] += 1

        # Compute number of horizontal segments for each y
        seg = []
        for y in ycount:
            c = ycount[y]
            if c >= 2:
                seg.append(c * (c - 1) // 2)

        if len(seg) < 2:
            return 0

        # Total = sum over all pairs seg[i] * seg[j]
        total_sum = sum(seg) % MOD
        result = 0

        for s in seg:
            total_sum = (total_sum - s) % MOD
            result = (result + s * total_sum) % MOD

        return result % MOD
