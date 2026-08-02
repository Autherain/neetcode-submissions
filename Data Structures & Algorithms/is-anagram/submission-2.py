class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap= {}
        for elem in s :
            sMap[elem] = sMap.get(elem,0) + 1

        tMap = {}
        for elem in t :
            tMap[elem] = tMap.get(elem,0) + 1

        return tMap == sMap