class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    # 만들어진 output의 값이 모두 pop 되기 전까지 output 리스트 재작성하지 않음.
    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        # list[-1] = last element
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()