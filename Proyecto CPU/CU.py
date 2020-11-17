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
            self.delay1.tiempo()
            print("Decode:")
            for j in self.rom1.instructions:
                if self.ram1.d[line][0:4]==j:
                    print (self.rom1.instructions[j])
                    print(self.ram1.d[line][5:10])
                    self.delay1.tiempo()
                    print ("Execute:")
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
                        print(self.register.r1())


                    elif self.rom1.instructions[j]=="ADD":
                        a=self.ram1.d[line][5:7]
                        b=self.ram1.d[line][8:10]
                        print(a)
                        print(b)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        alu1.suma()
                        self.register.getvalue(alu1.result)
                        self.register.r1()

                    elif self.rom1.instructions[j]=="SUB":
                        a=self.ram1.d[line][5:7]
                        b=self.ram1.d[line][8:10]
                        print(a)
                        print(b)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        alu1.resta()

                    elif self.rom1.instructions[j]=="HALT":
                        exit()

                    elif self.rom1.instructions[j]=="AND":
                        a=self.ram1.d[line][5:7]
                        b=self.ram1.d[line][8:10]
                        print(a)
                        print(b)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        if alu1.And()==True:
                            print ("La siguiente operación lógica es verdadera")
                        else:
                            print ("La operación es falsa")

                    elif self.rom1.instructions[j]=="OR":
                        a=self.ram1.d[line][5:7]
                        b=self.ram1.d[line][8:10]
                        print(a)
                        print(b)
                        alu1=ALU(self.register.R0,self.register.R1, 0)
                        if alu1.OR()==True:
                            print ("La siguiente operación lógica es verdadera")
                        else:
                            print ("La operación es falsa")

                    elif self.rom1.instructions[j]=="STORE_R0":
                        rom1=Rom()
                        rom1.valores()
                        self.rom1.val[line][8:10]=self.register.R0
                        print (self.rom1.val[line][8:10])

                    elif self.rom1.instructions[j]=="STORE_R0":
                        rom1=Rom()
                        rom1.valores()
                        self.rom1.val[line][8:10]=self.register.R1
                        print (self.rom1.val[line][8:10])

                    elif self.rom1.instructions[j]=="ILD_R0":
                        self.rom1.valores()
                        posicion=int(self.ram1.d[line][5:10])
                        self.register.getvalue(self.rom1.val[posicion])
                        self.register.r0()

                    elif self.rom1.instructions[j]=="ILD_R1":
                        self.rom1.valores()
                        posicion=int(self.ram1.d[line][5:10])
                        self.register.getvalue(self.rom1.val[posicion])
                        self.register.r1()

                    elif self.rom1.instructions[j]=="LOAD_R2":
                        self.rom1.valores()
                        posicion=int(self.ram1.d[line][5:10])
                        self.register.getvalue(self.rom1.val[posicion])
                        self.register.r2()

                    elif self.rom1.instructions[j]=="LOAD_R3":
                        pass




            print("-------------------------------------------------")
            self.delay1.tiempo()
