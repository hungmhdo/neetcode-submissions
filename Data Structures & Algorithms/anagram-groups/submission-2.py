class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            sortedStrs[sortedS].append(s)
        
        return list(sortedStrs.values())