class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        def dfs(index, path):
            # 끝까지 탐색 시 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위로 반복
            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i + 1, path + j)
                    
        # 예외처리
        if not digits:
            return []
        
        dict = {"2": "abc", "3": "def",
                "4": "ghi", "5": "jkl", "6": "mno",
                "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []
        
        dfs(0, "")
        
        
        return result