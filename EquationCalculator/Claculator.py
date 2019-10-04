


class Calculator :

    def __init__(self, expression , inputX):
        self.length = len(expression)
        self.operatorStack = []
        self.operandStack = []
        self.expr = expression
        self.expr.replace(" ","")
        self.operatorsList = {'+' , '-' , '/' , '*' , '^'}
        self.operatorPrecedences = { "+" : 1 , "-": 1 , "/" : 3 , "*" : 3 , "^" : 4 ,"(" :5 , ")":5}
        self.x = inputX
        #print("Expression : {%s} \n Len : {%d} \n input : {%d} \n " %(self.expr , len(self.expr) , self.x))

    def operandAction(self,operand, input1 , input2):

        if(operand == "+"):
            return (input1 + input2)
        elif (operand == '-'):
            return (input2 - input1)
        elif (operand == '/'):
            return (input2 / input1)
        elif (operand == '*'):
            return (input2 * input1)
        elif (operand == '^'):
            return (input2 ** input1)

    def simpleFunctionCalculator(self):
        for character in self.expr:
            if ( character in self.operatorsList):
                if ( len(self.operatorStack) > 0):
                    if ( ( (character == '*') or (character == '/') ) and ( (self.operatorStack[-1] == '+')  or  (self.operatorStack[-1] == '-') ) ):
                        self.operatorStack.append(character)

                    elif (( (character == '+') or (character == '-') ) and ( (self.operatorStack[-1] == '*')  or  (self.operatorStack[-1] == '/') ) ):

                        if(len(self.operandStack) > 0):
                            a = self.operandStack.pop()
                            b = self.operandStack.pop()
                            result = self.operandAction(self.operatorStack.pop(), b , a)
                            self.operandStack.append(result)
                            self.operatorStack.append(character)
                    else:
                        self.operatorStack.append(character)
                else :
                    self.operatorStack.append(character)
            elif ( character == '('):
                self.operatorStack.append(character)
            elif(character == ')'):
                stackTop = self.operatorStack.pop()
                while ( stackTop != '('):
                    a = self.operandStack.pop()
                    b = self.operandStack.pop()
                    result = self.operandAction(stackTop, b, a)
                    self.operandStack.append(result)
                    stackTop = self.operatorStack.pop()

            elif ( character.isalpha() == True ):
                self.operandStack.append(self.x)

            elif ( character.isdigit() == True):
                self.operandStack.append(int(character))

        if (len(self.operatorStack) > 0):
            operator = self.operatorStack.pop()
            a = self.operandStack.pop()
            b = self.operandStack.pop()
            result = self.operandAction(operator, b, a)
            self.operandStack.append(result)

        return self.operandStack.pop()

def main():
    expr = "(x+2)^3"
    cal = Calculator(expr, 1)
    print(cal.simpleFunctionCalculator())
main()






