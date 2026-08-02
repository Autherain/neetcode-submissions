class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None: 
            return False
        
        map = {}
        
        for element in nums: 
            map[element] = map.get(element, 0) + 1

            if map[element] > 1:
                return True
        
        return False