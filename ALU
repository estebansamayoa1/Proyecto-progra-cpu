from IC import IC
import IC



class ALU():
    def __init__(self, inputA, inputB):
        self.inputA = inputA 
        self.inputB = inputB

    def suma(self):

        result = self.inputA + self.inputB
        print ("la respuesta de la suma es: ")
        print (result)
        
        if (result < 0):
            return "negative"

        if (result == 0):
            return "zero"

        elif(result <= 15 ):
            return "Es la respuesta"

        if (result > 15 and result % 2):
            return "Overflow es impar igual 15"
        else:
            return "Overflow es par igual 14"

    def resta(self):

        result = self.inputA - self.inputB
        print ("la respuesta de la resta es: ")
        print (result)
        
        if (result < 0):
            return "negative"

        if (result == 0):
            return "zero"

        elif(result <= 15 ):
            return "Es la respuesta"

        if (result > 15 and result % 2):
            return "Overflow es impar igual 15"
        else:
            return "Overflow es par igual 14"

    def OR(self):

        if (self.inputA < 15 and self.inputA > 0 or self.inputB > 0 and self.inputB < 15 ):
            return "True"
        else:
            return "False"

    def And(self):

        if (self.inputA < 15 and self.inputA > 0 and self.inputB > 0 and self.inputB < 15):
            return "True"
        else:
            return "False"

    def Not(self):

        if (self.inputA <= 15 and self.inputB <= 15 or self.inputA >= 0 and self.inputB >= 0):
            return "False"
        else:
            return "True"
