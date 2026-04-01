class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        # Bundle the data together: [position, health, direction, original_index]
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
            
        # Sort robots strictly by their starting positions (left to right)
        robots.sort(key=lambda x: x[0])
        
        stack = []
        
        for robot in robots:
            # If the robot is moving Right, push it to the stack
            if robot[2] == 'R':
                stack.append(robot)
            else:
                # The robot is moving Left. It will collide with any 'R' robots in the stack
                survived = True
                while stack and stack[-1][2] == 'R':
                    top_robot = stack[-1]
                    
                    if top_robot[1] == robot[1]:
                        # Both have the same health; both are destroyed
                        stack.pop()
                        survived = False
                        break
                    elif top_robot[1] > robot[1]:
                        # The 'R' robot (in stack) has more health; 'L' robot is destroyed
                        top_robot[1] -= 1
                        survived = False
                        break
                    else:
                        # The 'L' robot (current) has more health; 'R' robot is destroyed
                        stack.pop()
                        robot[1] -= 1
                        # The 'L' robot continues moving left, so we loop again
                        
                # If the 'L' robot survived all collisions, add it to the stack
                if survived:
                    stack.append(robot)
                    
        # Restore the original order of the surviving robots using their original index
        stack.sort(key=lambda x: x[3])
        
        # Return only the healths of the surviving robots
        return [robot[1] for robot in stack]
