class Solution:
    def calculate(self, s: str) -> int:

        # stack: pending num and ops 
        # num: number being build
        stack = [] 
        num = 0
        ops = '+'
        # think as '0+' + s

        # def compute(a: int, b: int, ops: str) -> int:
            # if ops == '+': 
            #     return a + b
            # if ops == '0':
            #     return a - b
            # if ops == '*':
            #     return a * b
            # if ops == '/':
            #     return int(a / b)
        
        s += '+' # for handling last char
        for char in s:
            if char == ' ':
                continue
            # keep build number
            if char.isdigit():
                num = num*10 + int(char)
                continue
            
            # compute to stack
            if ops == '+':
                stack.append(num)
            if ops == '-':
                stack.append(-1*num)
            if ops == '*':
                stack.append(stack.pop() * num)
            if ops == '/':
                stack.append(int(stack.pop() / num))
            
            num = 0
            ops = char
            
        return sum(stack)
                

# num: 0
# ops: +
# stack: [3,4]

            
