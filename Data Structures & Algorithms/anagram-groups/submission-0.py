class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in sortedStrs:
                sortedStrs[sortedS] = [s]
            else:
                sortedStrs[sortedS].append(s)
        
        groupAnagrams = []
        for key in sortedStrs:
            groupAnagrams.append(sortedStrs[key])
        
        return groupAnagrams