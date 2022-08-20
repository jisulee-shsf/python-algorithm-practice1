from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        pair = []

        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum
