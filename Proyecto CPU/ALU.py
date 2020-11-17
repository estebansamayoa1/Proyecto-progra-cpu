
class ALU():
    def __init__(self, inputA, inputB, result):
        #self.zero = zero
        #self.overflow = overflow
        #self.negative = negative
        self.inputA = inputA
        self.inputB = inputB
        self.result=result

    def suma(self):
        result = self.inputA + self.inputB
        self.result=result
        print (f"La respuesta de la suma es: {self.result}")


    def numero(self):
        if (self.result < 0):
            print ("negative")

        elif (self.result == 0):
            print ("zero")

        elif(self.result <= 15 ):
            print ("Es la respuesta")

        elif (self.result > 15 and self.result % 2):
            print ("Overflow es impar igual 15")
        else:
            print ("Overflow es par igual 14")

    def resta(self):

        self.result = self.inputA - self.inputB
        print ("la respuesta de la resta es: ")
        print (self.result)
        return self.result

        if (self.result < 0):
            print("negative")

        if (self.result == 0):
            print("zero")

        elif(self.result <= 15 ):
            print("Es la respuesta")

        if (self.result > 15 and result % 2):
            print("Overflow es impar igual 15")
        else:
            print ("Overflow es par igual 14")

    def OR(self):

        if (self.inputA > 0 or self.inputB > 0 ):
            return True
        else:
            return False

    def And(self):

        if (self.inputA > 0 and self.inputB > 0):
            return True
        else:
            return False
