# URL: https://leetcode.com/problems/two-sum/discussion/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    value = [0, 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                value = [i, j]
    return value


def twoSumSolution2(nums: List[int], target: int) -> List[int]:
    value = [0, 0]
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap and hashmap[compliment] != i:
            value = [hashmap[compliment], i]
    print(hashmap)
    return value


given_list = [0, 1, 2, 3, 7, 6]
target = 5

print(twoSum(given_list, target))
print(twoSumSolution2(given_list, target))
