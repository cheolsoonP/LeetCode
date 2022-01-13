class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         ## ****`
#         results = []
#         prev_elements = []
        
#         def dfs(elements):
            
#             if len(elements) == 0:
#                 results.append(prev_elements[:])
            
            
#             # 순열 생성 재귀 호출
#             for e in elements:
#                 next_elements = elements[:]
#                 next_elements.remove(e)
                
#                 prev_elements.append(e)
#                 dfs(next_elements)
#                 prev_elements.pop()
        
#         dfs(nums)
#         return results
    
            
        # 2. itertool 사용 - 라이브러리 
        # 구현의 효율성, 성능을 위해 사용했다.  
        return list(map(list, itertools.permutations(nums)))