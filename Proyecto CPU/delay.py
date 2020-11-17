import time
import sys
sys.path.append(".")
from Rom import Rom

class delay:
    rom1=Rom()
    h = rom1.reloj()
    htz = 0

    def Htz(self):
        print (self.h)
        self.htz=1/self.h
        

    def tiempo(self):
        time.sleep(self.htz)
