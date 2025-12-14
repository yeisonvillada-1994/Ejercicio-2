from mini_turtle import Tortuga

print("Dibujando una escalera")
print()

# crear la primera tortuga
t1 = Tortuga()

# dibujar escalera normal
for i in range(3):
    t1.adelante()
    t1.abajo()

print("Escalera completada")

# resetear la tortuga
t1.reiniciar()

for i in range(3):
    t1.adelante()

print()
print("Escalera inversa:")

# hacer escalera al reves
for i in range(3):
    t1.abajo()
    t1.adelante()

print()
print("Probando que dos tortugas no interfieren:")

# crear dos tortugas distintas
t2 = Tortuga()
t3 = Tortuga()

print("Tortuga 2:")
t2.adelante()
t2.abajo()

print("Tortuga 3:")
for i in range(2):
    t3.adelante()
    t3.abajo()



