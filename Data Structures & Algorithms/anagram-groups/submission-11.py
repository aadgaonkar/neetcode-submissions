class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        defmap=defaultdict(list)

        for x in strs:
            defmap["".join(sorted(x))].append(x)

        result=[]

        for val in defmap.values():
            result.append(val)
        
        return result


