class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = {}
        for i in range(len(numbers)):
            num = numbers[i]
            remaining_number = target - num
            if remaining_number in right and remaining_number != i+1:
                return [right[remaining_number], i+1]
            elif num not in right:
                right[num] = i+1
        
            
