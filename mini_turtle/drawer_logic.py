pasos_h = int(input("Ingrese pasos hacia adelante: "))
pasos_v = int(input("Ingrese pasos hacia abajo: "))

class Tortuga:
    def __init__(self):
        # Inicializar la posición
        self.posicion_x = 0
    
    def adelante(self):
        # mover horizontal
        print(" " * self.posicion_x, end="")
        print("-" * pasos_h + ">")
        self.posicion_x += pasos_h
    
    def abajo(self):
        # bajar vertical
        for i in range(pasos_v):
            print(" " * self.posicion_x + "|")
        print(" " * self.posicion_x + "v")
    
    def reiniciar(self):
        # volver al inicio
        self.posicion_x = 0
