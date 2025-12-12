class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        # Sort events by timestamp (int) first.
        # If timestamps are equal, prioritize 'OFFLINE' (0) over 'MESSAGE' (1).
        # This ensures status updates are processed before messages at the same time.
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        
        mentions = [0] * numberOfUsers
        
        # Tracks the timestamp when a user will be back online.
        # Initialized to 0, implying everyone is online at start.
        back_online_time = [0] * numberOfUsers
        
        for event in events:
            kind, time_str, content = event
            timestamp = int(time_str)
            
            if kind == "OFFLINE":
                user_id = int(content)
                # User becomes offline for 60 units.
                # They are back online exactly at timestamp + 60.
                back_online_time[user_id] = timestamp + 60
                
            elif kind == "MESSAGE":
                if content == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif content == "HERE":
                    for i in range(numberOfUsers):
                        # User is online if the current message time is >= their return time
                        if back_online_time[i] <= timestamp:
                            mentions[i] += 1
                            
                else:
                    # Handle specific IDs like "id0 id1 id0"
                    # Split string by spaces to get tokens
                    ids = content.split()
                    for token in ids:
                        # Slice string to skip 'id' and convert remainder to int
                        # e.g., "id12" -> 12
                        user_id = int(token[2:])
                        mentions[user_id] += 1
                        
        return mentions
