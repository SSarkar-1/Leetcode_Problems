class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        s2=""
        for i in range(len(s1)):
            if (s[i].isalnum()==True):
              s2+=s1[i]
        return s2==s2[::-1]