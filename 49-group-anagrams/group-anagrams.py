class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for i in strs:
            key="".join(sorted(i))
            if key not in d:
                d[key]=[i]
            else:
                d[key].append(i)    
        return list(d.values())