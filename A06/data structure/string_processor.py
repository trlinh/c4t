from stack import * #import tat ca tu file stack.py
# from stack import Stack #import class Stack trong file stack.py

class StringProcessor:
    def reverse(self, string):
        stack = Stack()
        res=""
        
        self.string=string
        for i in self.string:
            stack.push(i)
        while not stack.is_empty():

            res +=stack.pop()
        return res

    def binary_string(self, integer):
        stack=Stack()
        self.integer=integer
        res=""
        while self.integer>0:
            r=self.integer%2
            self.integer=self.integer//2
            stack.push(r)
        while not stack.is_empty():
            res +=str(stack.pop())
        return res

    def is_valid(self, open_bracket, close_bracket):
        if open_bracket== "(":
            if close_bracket==")":
                return True
            return False
        if open_bracket== "[":
            if close_bracket=="]":
                return True
            return False
        if open_bracket== "{":
            if close_bracket=="}":
                return True
            return False

    def is_balanced(self, bracket):
        stack=Stack()
        open_bracket=["(", "[", "{"]
        close_bracket=[")", "]", "}"]
        for i in bracket:
            if i in open_bracket:
                stack.push(i)
            elif i in close_bracket:
                if stack.is_empty():
                    return False
                temp = stack.pop()
                if not self.is_valid(temp,i):
                    return False
        return stack.is_empty()


        
        


s=StringProcessor()
# print(s.reverse("qwert"))
# print(s.binary_string(17))
print(s.is_balanced("()"))

#2*5*7+3*4=257**34*+
#(1+2)*(3+4)=12+34+*
#1+2*3+4+5*6=123*456*+++