class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic=dict()
        words=s.split()
        if len(pattern)!=len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]]!=words[i]:
                    return False
            else:
                if words[i] in dic.values():
                    return False
                dic[pattern[i]]=words[i]
        return True
        
