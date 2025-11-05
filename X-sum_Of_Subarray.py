from collections import Counter
from sortedcontainers import SortedList

class Solution(object):
    def findXSum(self, nums, k, x):
        n = len(nums)
        freq = Counter()
        self.top = SortedList()   # best x by (-freq, -val)
        self.rest = SortedList()
        self.sumTop = 0
        res = []

        def add_to_top(item):
            # item is a tuple (-freq, -val)
            self.top.add(item)
            f, v = item
            self.sumTop += (-f) * (-v)

        def remove_from_top(item):
            self.top.remove(item)
            f, v = item
            self.sumTop -= (-f) * (-v)

        def add_to_rest(item):
            self.rest.add(item)

        def remove_from_rest(item):
            self.rest.remove(item)

        def remove_item_if_present(item):
            # remove old record from the correct set, without moving it
            # returns True if it was present
            if item in self.top:
                remove_from_top(item)
                return True
            if item in self.rest:
                remove_from_rest(item)
                return True
            return False

        def push_best_from_rest_to_top():
            if not self.rest:
                return
            item = self.rest[0]
            remove_from_rest(item)
            add_to_top(item)

        def push_worst_from_top_to_rest():
            if not self.top:
                return
            item = self.top[-1]
            remove_from_top(item)
            add_to_rest(item)

        def balance():
            # 1) fix ordering: ensure best of rest is not better than worst of top
            while self.top and self.rest and self.rest[0] < self.top[-1]:
                # swap
                best_rest = self.rest[0]
                worst_top = self.top[-1]
                remove_from_rest(best_rest)
                remove_from_top(worst_top)
                add_to_top(best_rest)
                add_to_rest(worst_top)

            # 2) fix size: keep exactly x in top when possible
            while len(self.top) > x:
                push_worst_from_top_to_rest()
            while len(self.top) < x and len(self.rest) > 0:
                push_best_from_rest_to_top()

        def insert_new_item(new_item):
            # place directly based on current worst of top
            if len(self.top) < x:
                # space available: prefer top
                add_to_top(new_item)
            else:
                # compare against worst in top: if better, goes to top
                if not self.top or new_item <= self.top[-1]:
                    add_to_top(new_item)
                else:
                    add_to_rest(new_item)

        def update(num, delta):
            # remove old record of num if present
            if freq[num] > 0:
                old_item = (-freq[num], -num)
                remove_item_if_present(old_item)

            # update freq
            freq[num] += delta
            if freq[num] == 0:
                del freq[num]
            else:
                new_item = (-freq[num], -num)
                insert_new_item(new_item)

            # restore invariants
            balance()

        # build first window
        for i in range(k):
            update(nums[i], 1)
        res.append(self.sumTop)

        # slide window
        for i in range(k, n):
            update(nums[i - k], -1)   # remove left
            update(nums[i], 1)        # add right
            res.append(self.sumTop)

        return res
