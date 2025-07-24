class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=""
        s1=strs[0]
        s2=strs[-1]
        for i in range(min(len(s1),len(s2))):
            if(s1[i]==s2[i]):
                s+=s1[i]
            else:
                return s
        return s
                       