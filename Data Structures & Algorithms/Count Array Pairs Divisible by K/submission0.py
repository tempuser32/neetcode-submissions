"""
class Solution:
    def countPairs(self, nums, k):
        pairs = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and (nums[i] * nums[j]) % k == 0:
                    pairs.append((i, j))

        print(pairs)
        return len(pairs)
        """
from collections import defaultdict
from math import gcd


class Solution:
    def countPairs(self, nums, k):
        gcd_count = defaultdict(int)
        answer = 0

        for num in nums:
            current_gcd = gcd(num, k)

            for previous_gcd, frequency in gcd_count.items():
                if (current_gcd * previous_gcd) % k == 0:
                    answer += frequency

            gcd_count[current_gcd] += 1

        return answer
