import sys
sys.path.append(".")
from Rom import Rom


class Register:
    R0=0
    R1=0
    R2=0



    def getvalue(self, value):
        self.value=value
        print (self.value)

    def r0(self):
        self.R0=self.value
        print(self.R0)

    def r1(self):
        self.R1=self.value
        print(self.R1)

    def r2(self):
        self.R2=self.value
        print(self.R2)
