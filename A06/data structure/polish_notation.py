from stack import Stack

class PolishNotation:
    
    def calculate(self, string):
        stack=Stack()
        operator=["+", "-", "*", "/"]
        self.string=string
        for i in self.string:
            if i not in operator:
                stack.push(i)
                
            if i in operator:
                b = int(stack.pop())
                a = int(stack.pop())
                
                if i=="+":
                    stack.push(a+b)
                if i=="-":
                    stack.push(a-b)
                if i=="*":
                    stack.push(a*b)
                if i=="/":
                    stack.push(a/b)
              
        return int(stack.pop())
        
p = PolishNotation()

pn = PolishNotation()

assert(pn.calculate("46+") == 10)
assert(pn.calculate("76-") == 1)
assert(pn.calculate("23*") == 6)
assert(pn.calculate("42/") == 2)

assert(pn.calculate("46+7-") == 3)
assert(pn.calculate("46+7-23*-") == -3)
assert(pn.calculate("46+7-23*-343-/+") == 0)