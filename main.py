from mini_turtle import adelante, abajo, reiniciar

# Script que importa las funciones y dibuja una escalera
print("Dibujando una escalera")
print()

# Reiniciar la posición antes de comenzar
reiniciar()

# Dibujar múltiples escalones para crear una escalera
for i in range(3):
    #print(f"Escalón {i + 1}:")
    adelante()  # Dibuja la línea horizontal
    abajo()     # Dibuja la línea vertical

print("Escalera completada")

# Reiniciar la posición para la escalera inversa
reiniciar()

for i in range(3):
    adelante()  # posición final a la derecha

print()
print("Escalera inversa:")

# escalera inversa
for i in range(3):
    abajo()     # Primero la línea vertical
    adelante()  # Luego la línea horizontal


