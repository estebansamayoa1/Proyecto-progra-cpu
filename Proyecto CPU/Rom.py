import yaml

class Rom:
    instructions={
    "0000":"OUTPUT",
    "0001":"LOAD_R0",
    "0010":"LOAD_R1",
    "0011":"AND",
    "0100":"ILD_R0",
    "0101":"STORE_R0",
    "0110":"STORE_R1",
    "0111":"OR",
    "1000":"ILD_R1",
    "1001":"ADD",
    "1010":"SUB",
    "1011":"JUMP",
    "1100":"JUMP_NEG",
    "1111":"HALT"
    }
    bios = open ("bios.yaml")
    bo = yaml.load (bios, Loader = yaml.FullLoader)
    v=0

    def __init__(self):
        pass

    def valores(self):
        self.val = self.bo["RAM"]["data"]
        return self.val

    def reloj(self):
        f = self.bo["clock"]
        return f

    def vis (self):
        self.v = self.bo["visualization"]["RAM"]
        self.b = self.bo["visualization"]["Registers"]
        self.c = self.bo["visualization"]["Clock"]
        self.a = self.bo["visualization"]["ALU"]
