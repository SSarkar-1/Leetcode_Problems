class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp=dict()
        for index,letter in enumerate(s):
            if letter in mapp:
                if mapp[letter] != t[index]:
                    return False
            else:
                if t[index] in mapp.values():
                    return False
                mapp[letter]=t[index]
        return True