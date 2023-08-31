class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_gas = 0
        start_pos = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                start_pos = i + 1
                total_gas = 0

        if total_gas < 0:
            return -1
        return start_pos
