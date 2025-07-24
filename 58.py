class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s)-1,0,-1):
            while(s[i]!=' '):
                c+=1
            if(c>0):
                break
        return c
                
        