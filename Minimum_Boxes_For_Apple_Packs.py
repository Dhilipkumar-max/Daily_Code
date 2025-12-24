class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        # Step 1: Calculate the total number of apples
        total_apples = sum(apple)
        
        # Step 2: Sort capacities in descending order to use the biggest boxes first
        capacity.sort(reverse=True)
        
        boxes_used = 0
        
        # Step 3: Iterate through the boxes and subtract their capacity from total_apples
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            
            # Step 4: If all apples are accounted for, return the count
            if total_apples <= 0:
                return boxes_used
        
        return boxes_used
