"""class Solution:
    def minCost(self, nums, cost):
        totals = []

        for i in range(len(nums)):
            total = 0

            for j in range(len(nums)):
                total += abs(nums[i] - nums[j]) * cost[j]

            totals.append(total)

        return min(totals)"""
class Solution:
    def minCost(self, nums, cost):
        total_weight = sum(cost)
        pairs = sorted(zip(nums, cost))

        current_weight = 0

        for value, weight in pairs:
            current_weight += weight

            if current_weight * 2 >= total_weight:
                weighted_median = value
                break

        total_cost = 0

        for i in range(len(nums)):
            total_cost += (
                abs(nums[i] - weighted_median) * cost[i]
            )

        return total_cost
