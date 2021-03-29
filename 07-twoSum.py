from typing import List

class Solutions:
    def two_sums1(self, nums :List[int], target : int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sums2(self, nums : List[int], target : int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

    def two_sums3(self, nums: List[int], target : int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return[i, nums_map[target - num]]

    def two_sums4(self, nums: List[int], target : int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target - num]]
            nums_map[num] = i

b = Solutions()
print(b.two_sums1([4,2,3,1,5], 7))
print(b.two_sums2([4,2,3,1,5], 7))
print(b.two_sums3([4,2,3,1,5], 7))
print(b.two_sums4([4,2,3,1,5], 7))

print(b.two_sums1([1,2,3,4,5], 20))
print(b.two_sums2([1,2,3,4,5], 20))
print(b.two_sums3([1,2,3,4,5], 20))
