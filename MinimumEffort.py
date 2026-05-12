class Solution(object):
    def minimumEffort(self, tasks):
        # Sort tasks based on the difference between minimum and actual energy descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            # If our running current_energy is less than the minimum required for this task,
            # we must "top up" our starting initial_energy by the deficit.
            if current_energy < minimum:
                initial_energy += (minimum - current_energy)
                current_energy = minimum  # Update current energy to match the requirement
                
            # Perform the task, deducting the actual energy used
            current_energy -= actual
            
        return initial_energy
