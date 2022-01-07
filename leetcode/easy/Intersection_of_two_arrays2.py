class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_counter = collections.Counter(nums1)
        result = []
        for n2 in nums2:
            if n2 in n1_counter and n1_counter[n2]:
                result.append(n2)
                n1_counter[n2] -= 1
        return result
