#Reto5
posicion_x = 0        # posición acumulada de la tortuga
pasos_h = 0               # pasos horizontales fijos
pasos_v = 0               # pasos verticales fijos

# Entradas del usuario
pasos_h = int(input("Ingrese pasos hacia adelante: "))
pasos_v = int(input("Ingrese pasos hacia abajo: "))


def adelante():
    global posicion_x, pasos_h
    # imprimir escalón horizontal
    print(" " * posicion_x , end="")
    print("-" * pasos_h + ">")
    # actualizar posición horizontal acumulada
    posicion_x += pasos_h


def abajo():
    global posicion_x, pasos_v

    # líneas verticales alineadas al final del escalón
    for i in range(pasos_v):
        print(" " * posicion_x + "|")

    # punta final abajo
    print(" " * posicion_x + "v")
    
    
def reiniciar():
    global posicion_x
    posicion_x = 0


#for i in range(3):
#    adelante()
#    abajo()
