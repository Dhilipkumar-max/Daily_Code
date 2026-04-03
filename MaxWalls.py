import bisect

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        n = len(robots)
        # Sort robots by their positions and keep distances aligned
        rd = sorted(zip(robots, distance))
        R = [x[0] for x in rd]
        D = [x[1] for x in rd]
        
        # Identify walls at robot positions; these are always destroyed
        robot_set = set(R)
        walls_at_robots_count = 0
        filtered_walls = []
        
        for w in walls:
            if w in robot_set:
                walls_at_robots_count += 1
            else:
                filtered_walls.append(w)
        
        # Sort remaining walls for binary search range queries
        filtered_walls.sort()
        W = filtered_walls
        
        # Helper to count walls in [a, b)
        def count_L(a, b):
            if a >= b: return 0
            return bisect.bisect_left(W, b) - bisect.bisect_left(W, a)

        # Helper to count walls in (a, b]
        def count_R(a, b):
            if a >= b: return 0
            return bisect.bisect_right(W, b) - bisect.bisect_right(W, a)

        # dp0: Max walls in previous gaps where current robot fires Left
        # dp1: Max walls in previous gaps where current robot fires Right
        
        # Robot 0 firing Left covers walls in [R0 - D0, R0)
        dp0 = count_L(R[0] - D[0], R[0])
        # Robot 0 firing Right covers nothing in the non-existent gap to its left
        dp1 = 0
        
        for i in range(n - 1):
            # Interval between R[i] and R[i+1]
            # end_i: How far R[i] bullet goes Right (blocked by R[i+1])
            end_i = min(R[i] + D[i], R[i+1])
            # start_next: How far R[i+1] bullet goes Left (blocked by R[i])
            start_next = max(R[i+1] - D[i+1], R[i])
            
            size_A = count_R(R[i], end_i)      # Walls hit by R[i] firing Right
            size_B = count_L(start_next, R[i+1]) # Walls hit by R[i+1] firing Left
            
            # If ranges overlap or touch, they cover all walls in the gap (R[i], R[i+1])
            if end_i >= start_next:
                size_union = count_R(R[i], R[i+1])
            else:
                size_union = size_A + size_B
            
            # If R[i+1] fires Left:
            # - If R[i] fired Left: R[i+1] adds size_B to the total
            # - If R[i] fired Right: R[i+1] completes the union in the current gap
            next_dp0 = max(dp0 + size_B, dp1 + size_union)
            
            # If R[i+1] fires Right:
            # - If R[i] fired Left: current gap is empty (0 added)
            # - If R[i] fired Right: R[i] adds size_A to the total
            next_dp1 = max(dp0, dp1 + size_A)
            
            dp0, dp1 = next_dp0, next_dp1
            
        # Final step: Robot n-1 firing Right can hit walls in (R[n-1], R[n-1] + D[n-1]]
        a_last = count_R(R[n - 1], R[n - 1] + D[n - 1])
        
        return max(dp0, dp1 + a_last) + walls_at_robots_count
