class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        count = 0
        
        for i, x in enumerate(s):
            if x in t:
                t=t[t.find(x)+1:]
                count+=1
                    
                
        if count == len(s):
            return True
        else:
            return False