import sys
sys.path.append(".")
from CU import CU
from RAM import RAM
from Rom import Rom
from Reg import Register
from delay import delay


def main():
    tabla = RAM()
    visual = Rom()
    registros = Rom()
    reloj = Rom()
    operacion = Rom()
    r1= Register()
    delay1=delay()
    delay1.Htz()
    registros.vis()
    visual.vis()
    reloj.vis()
    operacion.vis()




    print ("\n                  Proyecto 1 CPU Simulator                           ")
    print ("*--------------------------------------------------------------------*")
    print ("""      Integrantes:
            - Juan Luis Fernandez
            - Rodrigo Reyes
            - Esteban Samayoa\n
                """)
    delay1.tiempo()
    if visual.v == True:
        print ("*--------------------------------*")
        print ("              RAM                    ")
        tabla.valoress()
    delay1.tiempo()
    if registros.b == True:
        print (f"""
*---------------------------------*
            REGISTROS:
        Primer registro : {r1.R0}
        Segundo registro : {r1.R1}
        Tercer registro : {r1.R2}

    """)
    delay1.tiempo()
    if reloj.c == True:
        print ("*--------------------------------*")
        print (f"""
        Tiempo : {hrtzz.htz}
        """)
    delay1.tiempo()
    if operacion.a == True:
        cu1=CU()
        cu1.operate()


main()
