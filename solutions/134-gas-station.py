class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_cost = sum(cost)
        sum_gas = sum(gas)

        if sum_cost > sum_gas:
            return -1

        current = 0
        start = 0

        # We can assume that there is always an unique answer.
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1

        return start
