class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규 표현식을 통해 문자열이 아닌 것들은 제거
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        