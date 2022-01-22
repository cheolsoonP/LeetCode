class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        route = []
        graph = collections.defaultdict(list)
        
        # 사전 순서로 하기 위해 정렬
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        def dfs(a):
            
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
                
            return
        
        dfs("JFK")
        return route[::-1]
        
            
    
#         ## 3. 반복
#         graph = collections.defaultdict(list)
#         # 그래프를 뒤집어서 구성
#         for a, b in sorted(tickets):
#             graph[a].append(b)
            
#         route, stack = [], ['JFK']
#         while stack:
#             # 반복으로 스택을 구성, 막히는 부분에서 처리
#             while graph[stack[-1]]:
#                 stack.append(graph[stack[-1]].pop(0))
#             route.append(stack.pop())

            
#         return route[::-1]