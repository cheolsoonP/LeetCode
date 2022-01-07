class Solution:
    def isPalindrome(self, s: str) -> bool:
#         # 1. use deque
#         strs: Deque = collections.deque()
        
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
        
        
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
        
#         return True
                
        
        # 2. use slicing
        s = s.lower()
        # 정규 표현식을 통해 문자열이 아닌 것들은 제거
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        