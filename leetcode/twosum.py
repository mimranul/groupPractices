# URL: https://leetcode.com/problems/two-sum/discussion/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                value = [i, j]
    return value


def twoSumSolution2(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap and hashmap[compliment] != i:
            value = [hashmap[compliment], i]
    return value

def twoSumSolution3(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i, element in enumerate(nums):
        comliment = target - element
        if comliment in hashmap and hashmap[comliment] != i:
            value = [hashmap[comliment], i]
    return value


given_list = [0, 1, 2, 3, 7, 6]
target = 5

print(twoSum(given_list, target))
print(twoSumSolution2(given_list, target))
print(twoSumSolution3(given_list, target))
