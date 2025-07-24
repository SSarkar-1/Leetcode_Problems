class Solution:
    def isValid(self, s: str) -> bool:
        d={'(': ')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                
                elif d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False