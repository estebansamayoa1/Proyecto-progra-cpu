#CPU Simulator 

Descripcion: El programa simula a un CPU. Gran parte del codigo esta trabajado en clases que son heredadas de otros archivos. Cada archivo tiene una tarea en especifico que representa lo que haria el componente del CPU. Esta conformado de tal forma que simula como funcionaria un CPU en la vida real. 

Partes:
  - Registers: 
    - Almacenan los datos que la instruccion en el ROM le manda. 
  - ALU:
    - Son las operaciones artimeticas o logicas que el CPU puede trabajar. 
  - Memory:
    - Un espacio de memoria para almacenar datos.
  - CU:
    - Es el responsable de buscar las instrucciones, decodificarlas y ejecutarlas. 
    - Tambien lleva un reloj para darle un delay a cada intruccion. 
  - RAM:
    - Accesa de manera rapida a la data y las instrucciones, para poder realizar las instrucciones. 
  - ROM:
    - Guarda la data y las instrucciones. 
  - Clock:
    - Se encarga de controlar el tiempo en que se realiza cada instruccion. 
  - Main:
    - Junta todo y lo corre. 
   
Intrucciones:
  - "0000", OUTPUT, Manda el output del registro al RAM
  - "0001", LOAD_R0, lee la posicion de RAM y lo manda al registro R0
  - "0010", LOAD_R1, lee la posicion de RAM y lo manda al  registro R1
  - "0011", AND, realiza la operacion logica "AND" de dos bits de registros
  - "0100", ILD_R0, ...
  - "0101", STORE_R0, lee la posicion de R0 y la manda al RAM
  - "0110", STORE_R1, lee la posicion de R1 y la manda al RAM
  - "0111", OR, realiza la operacion "OR" de dos bits de registros
  - "1000", ILD_R1, ...
  - "1001", ADD, Suma de dos registros, guardar el resultado dentro de otro registro
  - "1010", SUB, Resta de dos registros, guardar el resultado dentro de otro registro
  - "1011", JUMP, ...
  - "1100", JUMP_NEG, ...
  - "1101", ...
  - "1110", ...
  - "1111", HALT, se acaba el programa
  
 
