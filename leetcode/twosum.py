# URL: https://leetcode.com/problems/two-sum/discussion/
from typing import List, Tuple


def twoSum(nums: List[int], target: int) -> tuple[int, int]:
    value = [0, 0]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                value = [i, j]
    return value

print(twoSum([0, 1, 2, 3, 4, 5], 2))
