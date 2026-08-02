class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMap = {}
        for index, elem in enumerate(nums): 
            numberMap[elem] = index
        
        for index, number in enumerate(nums): 
            want = target - number
            if want in numberMap and numberMap[want] != index: 
                return sorted([index, numberMap[want]])
        
        return []