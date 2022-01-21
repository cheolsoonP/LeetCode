class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
#         # index, 값
#         for i, curr in enumerate(temperatures):
#             # 현재 온도가 스택 값보다 높다면 정답
#             # list[-1] => 리스트의 마지막 값.
#             while stack and curr > temperatures[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)
        
#         return answer
                
        
        answer = [0] * len(temperatures)
        stack = []
        
        for i, curr in enumerate(temperatures):
            # 스택에 인덱스 저장, 이전 온도보다 현재 온도가 높을때
            # 현재 index와 stack의 index 차이만큼 answer에 저장
            while stack and curr > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        
        return answer