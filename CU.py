import time
import sys
sys.path.append(".")
from ALU import ALU
from RAM import RAM
from Rom import Rom
from Reg import Register
from delay import delay


class CU():
    register=Register()

    ram1=RAM()
    rom1=Rom()
    ram1.upcc()
    ram1.instt()
    delay1=delay()
    delay1.Htz()
    ram1.valoress()



    def operate(self):
        for line in self.ram1.d:
            print("-------------------------------------------------")
            print ("Fetch:")
            print(f"La instrucción es: {self.ram1.d[line]}")
            print("Decode:")
            for j in self.rom1.instructions:
                if self.ram1.d[line][0:4]==j:
                    print (self.rom1.instructions[j])
                    print(self.ram1.d[line][5:10])
                    print ("Execute")
                    if self.rom1.instructions[j]=="LOAD_R0":
                        self.rom1.valores()
                        posicion=int(self.ram1.d[line][5:10])
                        self.register.getvalue(self.rom1.val[posicion])
                        self.register.r0()

                    elif self.rom1.instructions[j]=="LOAD_R1":
                        self.rom1.valores()
                        posicion=int(self.ram1.d[line][5:10])
                        self.register.getvalue(self.rom1.val[posicion])
                        self.register.r1()

                    elif self.rom1.instructions[j]=="OUTPUT":
                        self.register.r1()

                    elif self.rom1.instructions[j]=="ADD":
                        imon=self.ram1.d[line][5:7]
                        meybelyn=self.ram1.d[line][8:10]
                        print(imon)
                        print(meybelyn)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        alu1.suma()

                    elif self.rom1.instructions[j]=="SUB":
                        imon=self.ram1.d[line][5:7]
                        meybelyn=self.ram1.d[line][8:10]
                        print(imon)
                        print(meybelyn)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        alu1.resta()
                    elif self.rom1.instructions[j]=="HALT":
                        exit()

                    elif self.rom1.instructions[j]=="AND":
                        imon=self.ram1.d[line][5:7]
                        meybelyn=self.ram1.d[line][8:10]
                        print(imon)
                        print(meybelyn)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        if alu1.And()==True:
                            print ("La siguiente operación lógica es verdadera")
                        else:
                            print ("La operación es falsa")

                    elif self.rom1.instructions[j]=="OR":
                        imon=self.ram1.d[line][5:7]
                        meybelyn=self.ram1.d[line][8:10]
                        print(imon)
                        print(meybelyn)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        if alu1.OR()==True:
                            print ("La siguiente operación lógica es verdadera")
                        else:
                            print ("La operación es falsa")
                        
            print("-------------------------------------------------")
            self.delay1.tiempo()
 
