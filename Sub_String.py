class Solution(object):
    def numberOfSubstrings(self, s):
        
        n = len(s)
        if n == 0:
            return 0

        import math
        B = int(math.sqrt(n)) + 1

        # positions of zeros with sentinels at -1 and n
        zero_pos = [-1]
        for i, ch in enumerate(s):
            if ch == '0':
                zero_pos.append(i)
        zero_pos.append(n)
        Z = len(zero_pos) - 2  # actual zero count (without sentinels)

        ans = 0

        # 1) substrings with zero zeros -> those are contiguous runs of ones
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                length = j - i
                ans += length * (length + 1) // 2
                i = j
            else:
                i += 1

        # 2) substrings with k zeros where 1 <= k <= B
        # iterate all possible blocks of k consecutive zeros
        # zero_pos uses indices: sentinel -1 at idx0, zeros at 1..Z, sentinel n at Z+1
        for k in range(1, B + 1):
            if k > Z:
                break
            need_len = k * k + k  # minimal length (ones + zeros) needed: ones >= k^2 -> len = ones + k >= k^2 + k
            # iterate start index of the zero-block in zero_pos (1-based for actual zeros)
            for start in range(1, Z - k + 2):  # start ranges 1..Z-k+1
                end = start + k - 1
                Lmin = zero_pos[start - 1] + 1
                Lmax = zero_pos[start]
                Rmin = zero_pos[end]
                Rmax = zero_pos[end + 1] - 1
                if Lmin > Lmax or Rmin > Rmax:
                    continue

                # For each possible left L in [Lmin..Lmax], minimal R needed is max(Rmin, L + need_len - 1)
                # Rather than iterate all L in huge ranges, we can compute the first L where R_needed <= Rmax
                # But simple iteration over left choices is fine because either left range is small or Z is small.
                # We'll iterate L but break early when R_needed > Rmax for all larger L.
                # (R_needed increases with L.)
                for L in range(Lmin, Lmax + 1):
                    R_needed = L + need_len - 1
                    R_actual_min = R_needed if R_needed > Rmin else Rmin
                    if R_actual_min > Rmax:
                        # since R_needed increases with L, if current L yields too large R_actual_min,
                        # larger L will only increase R_needed, so we can break the loop on L.
                        if R_needed > Rmax:
                            break
                        else:
                            continue
                    ans += (Rmax - R_actual_min + 1)

        return ans
