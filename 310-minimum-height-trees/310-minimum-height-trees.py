class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 1:
            return [0]
        
        # 그래프 만들기 
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        # 리프 노드는 해당 키의 값이 1개인 것
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
            
        # 리프 노드를 삭제해 나간다. 루트를 남기기 위해서
        while n > 2:
            n -= len(leaves) # 최종 길이 - 리프노드 수
            new_leaves = [] 
            for leaf in leaves: 
                neighbor = graph[leaf].pop() 
                graph[neighbor].remove(leaf) 
                
                # 리프 노드를 제거했을때 새로운 리프노드 찾음
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
        
        return leaves