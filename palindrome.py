class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        charac=s[:n//2]
        if n%2==0:
            s=charac.sort()+charac.sort(reverse=True)
            return "".join(s)
        else:
            s=charac.sort()+s[n//2]+charac.sort(reverse=True)+s[n//2]
            return "".join(s)


    