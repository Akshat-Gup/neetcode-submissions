class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            seen[num] = i
    
        for i in range(n):
            num = nums[i]
            pair = target - num
            if pair in seen and seen[pair] != i:
                return [i, seen[pair]]
