class Solution:

    memory = {1: 1, 2: 2}


    def climbStairs(self, n: int) -> int:
        if self.memory.get(n):
            return self.memory[n]
        
        self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memory[n]
