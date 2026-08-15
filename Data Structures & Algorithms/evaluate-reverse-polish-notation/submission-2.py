import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []
        for t in tokens:
            if t in operators:
                #print(f"t is an operator: {t}")
                second = int(stack.pop())
                #print(f"second is: {second}")
                first = int(stack.pop())
                #print(f"first is: {first}")
                #print(f"operator is: {t}")
                calcul = operators[t](first, second)
                #print(f"calcul is: {calcul}")
                stack.append(calcul)
            else:
                stack.append(t)
                #print (f"This is the current stack: {stack}") 
                
        return int(stack.pop())