from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                sum += num

        return sum
