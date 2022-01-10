class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        # index, 값
        for i, curr in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답
            # list[-1] => 리스트의 마지막 값.
            while stack and curr > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        
        return answer
                