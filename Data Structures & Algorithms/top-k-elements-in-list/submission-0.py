class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = {}
        freq = [[] for i in range(len(nums)+1)]

        for integer in nums: 
            num[integer] = num.get(integer, 0) + 1
        
        for key, value in num.items(): 
            freq[value].append(key)

        res = []
        for listElem in reversed(freq): 
            for subElem in listElem: 
                res.append(subElem)
                if len(res) == k: 
                    return res
        
        return []
      

