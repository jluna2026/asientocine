# Crear matriz 3x4 de asientos (0 = libre, 1 = reservado)
asientos = [[0 for _ in range(4)] for _ in range(3)]

# Pedir al usuario la fila y columna del asiento a reservar
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[f][c] = 1

# Mostrar el estado de la sala
print("\nEstado de la sala:")
for i in range(3):  # filas
    for j in range(4):  # columnas
        print(asientos[i][j], end=" ")
    print()  # salto de línea al final de cada fila