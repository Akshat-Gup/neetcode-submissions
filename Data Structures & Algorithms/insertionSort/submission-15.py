# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        outputarr = []
        for i in range(len(pairs)):
            j = i
            while True:
                if pairs[j].key < pairs[j-1].key and j > 0:
                    temp = pairs[j-1]
                    pairs[j-1] = pairs[j]
                    pairs[j] = temp
                    j -=1
                else:
                    break
            outputarr.append(pairs[:])
        
        return outputarr
    
                


