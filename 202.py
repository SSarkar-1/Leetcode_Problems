class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.squ(n)

            if n==1 :
                return True
        return False

    def squ(self,n):
        op=0
        while(n>0):
            op+=(n%10)*(n%10)
            n=n//10
        return op
        
