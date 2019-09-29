#In The Name Of God
class Conversion:

    # Constructor to initialize the class variables
    def __init__(self):
        self.top = -1
        # This array is used a stack
        self.operandArray = []
        self.operatorArray = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def opearnadPeek(self):
        return self.operandArray[-1]
    
    def opearatorPeek(self):
         return self.operatorArray[-1]

    # Pop the element from the stack
    def operandPop(self):
        return self.operandArray.pop()
    
    def operatorPop(self):
        return self.operatorArray.pop()

    def isOperand(self, ch):
        return ch.isalpha()


    def infixCalculator(self,inputString , withInput , inputX):
        tokens = []
        for char in inputString:
            tokens.append(char)
            
        for token in tokens :
            if ( token.isalpha() ):
                if(withInput == True):
                    self.operandArray.append(inputX)
            if (token.isdigit() ):
                self.operandArray.append(int(token))
            numericKey = self.precedence.keys()
            
            if( token in numericKey):
                self.operatorArray.append(token)
        
        
       
        print(self.operandArray)
        print(self.operatorArray)
        
    
    











#=============================================================================
converte = Conversion()
converte.infixCalculator("-H7e/l5l6o+",False,2)




