class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
#         ## 1. dfs
#         route = []
        
#         # # 그래프 구성 1
#         # graph = collections.defaultdict(list)
#         # for a, b in tickets:
#         #     graph[a].append(b)
#         # for a in graph:
#         #     graph[a].sort
            
#         # 그래프 구성 2
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)
#         print(graph)
            
#         # 그래프에서 하나씩 꺼낸다.
#         def dfs(a):
#             while graph[a]:
#                 dfs(graph[a].pop(0))
#             route.append(a)
#             print(route)
            
            
#         dfs('JFK')
        
#         return route[::-1]
    
#         ## 2. stack
        
#         graph = collections.defaultdict(list)
#         # 그래프를 뒤집어서 구성
#         for a, b in sorted(tickets, reverse=True):
#             graph[a].append(b)
        
#         route = []
        
#         def dfs(a):
#             while graph[a]:
#                 dfs(graph[a].pop())
#             route.append(a)
            
            
#         dfs('JFK')
        
#         return route[::-1]
    
    
        ## 3. 반복
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성, 막히는 부분에서 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

            
        return route[::-1]