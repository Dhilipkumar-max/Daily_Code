class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]

        def merge(node, left, right):
            p_left = tree_prod[left]
            p_right = tree_prod[right]
            c_left = tree_cnt[left]
            c_right = tree_cnt[right]

            tree_prod[node] = (p_left * p_right) % k
            
            c_node = tree_cnt[node]
            for i in range(k):
                c_node[i] = c_left[i]
            
            for i in range(k):
                if c_right[i]:
                    target = (p_left * i) % k
                    c_node[target] += c_right[i]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree_prod[node] = rem
                tree_cnt[node][rem] = 1
                return
            mid = (l + r) // 2
            left, right = 2 * node, 2 * node + 1
            build(left, l, mid)
            build(right, mid + 1, r)
            merge(node, left, right)

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k
                tree_prod[node] = rem
                for i in range(k):
                    tree_cnt[node][i] = 0
                tree_cnt[node][rem] = 1
                return
            mid = (l + r) // 2
            left, right = 2 * node, 2 * node + 1
            if idx <= mid:
                update(left, l, mid, idx, val)
            else:
                update(right, mid + 1, r, idx, val)
            merge(node, left, right)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node]
            mid = (l + r) // 2
            left, right = 2 * node, 2 * node + 1
            if qr <= mid:
                return query(left, l, mid, ql, qr)
            if ql > mid:
                return query(right, mid + 1, r, ql, qr)
            
            p_left, c_left = query(left, l, mid, ql, qr)
            p_right, c_right = query(right, mid + 1, r, ql, qr)
            
            res_p = (p_left * p_right) % k
            res_c = list(c_left)
            for i in range(k):
                if c_right[i]:
                    target = (p_left * i) % k
                    res_c[target] += c_right[i]
            return res_p, res_c

        build(1, 0, n - 1)

        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, c_res = query(1, 0, n - 1, start, n - 1)
            ans.append(c_res[x])

        return ans
