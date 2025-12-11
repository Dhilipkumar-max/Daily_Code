class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        # Build min/max per column (y) and per row (x)
        col_min = {}  # y -> min x
        col_max = {}  # y -> max x
        row_min = {}  # x -> min y
        row_max = {}  # x -> max y

        for x, y in buildings:
            if y not in col_min:
                col_min[y] = x
                col_max[y] = x
            else:
                if x < col_min[y]:
                    col_min[y] = x
                if x > col_max[y]:
                    col_max[y] = x

            if x not in row_min:
                row_min[x] = y
                row_max[x] = y
            else:
                if y < row_min[x]:
                    row_min[x] = y
                if y > row_max[x]:
                    row_max[x] = y

        covered = 0
        for x, y in buildings:
            # there must be at least one building with smaller x (above)
            # and at least one with larger x (below) in same column y
            col_condition = (col_min[y] < x < col_max[y])
            # and at least one building with smaller y (left)
            # and at least one with larger y (right) in same row x
            row_condition = (row_min[x] < y < row_max[x])

            if col_condition and row_condition:
                covered += 1

        return covered
