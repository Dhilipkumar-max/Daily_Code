class Solution(object):
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7

        # Collect positions of seats
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        total_seats = len(seats)

        # Invalid cases
        if total_seats == 0 or total_seats % 2 != 0:
            return 0

        # Only one section → only 1 way
        if total_seats == 2:
            return 1

        ways = 1

        # Process gaps between seat-pairs
        for i in range(1, total_seats // 2):
            left = seats[2*i - 1]
            right = seats[2*i]
            plants_between = right - left - 1
            ways = (ways * (plants_between + 1)) % MOD

        return ways
