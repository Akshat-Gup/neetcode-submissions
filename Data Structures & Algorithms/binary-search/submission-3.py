class Solution:
    def binarySearch(self, p: int, r: int, nums: List[int], target: int) -> int:
        if r < p:
            return -1
        q = (p + r) // 2
        if nums[q] == target:
            return q
        if nums[q] < target:
            return self.binarySearch(q+1, r, nums, target)
        else:
            return self.binarySearch(p, q-1, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)
        