import sys
sys.path.append(".")
from ALU import ALU
from Rom import Rom
from Reg import Register
from delay import delay

class RAM():
    instructions=open('machinecode.cpufm', 'r')
    upcode=[]
    rom1=Rom()




    def upcc(self):
        for line in self.instructions:
            if not line.lower().startswith(";"):
                self.upcode.append(line)

    def instt(self):
        rom1=Rom()
        self.d={}
        for i in range(len(self.upcode)):
            self.d["instruccion{0}".format(i)]=self.upcode[i]

    def valoress(self):
        self.rom1.valores()
        for i in range (len(self.rom1.val)):
            print ("            --------                        ")
            print(f"            {i} || {self.rom1.val[i]}       ")
