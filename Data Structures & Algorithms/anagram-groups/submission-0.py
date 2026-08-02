class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strHash = {}

        for elem in strs: 
            hashedElem = "".join(sorted(elem))

            if hashedElem in strHash: 
                strHash[hashedElem].append(elem)
            else: 
                strHash[hashedElem] = [elem]

        final = []
        for value in strHash.values(): 
            final.append(value) 
        
        return final