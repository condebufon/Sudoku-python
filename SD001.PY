import string
import random

# Definición de la función para inicializar el tablero. Esta función crea un tablero vacío y llena cada celda con un número aleatorio.

def init(m, n, nivel):
    tablero = [[0] * n for _ in range(m)]

    for i in range(0, m, 3):
        for j in range(0, n, 3):
            bloque = random.sample(range(1, 10), 9)
            for k, num in enumerate(bloque):
                fila = i + k // 3
                columna = j + k % 3
                tablero[fila][columna] = num

    if nivel == 1:
        for i in range(m):
            for j in range(n):
                if (i * n + j + 1) % 7 == 0:
                    tablero[i][j] = 0
    elif nivel == 2:
        for i in range(m):
            for j in range(n):
                if (i * n + j + 1) % 4 == 0:
                    tablero[i][j] = 0
    elif nivel == 3:
        for i in range(m):
            for j in range(n):
                if (i * n + j + 1) % 2 == 0:
                    tablero[i][j] = 0

    return tablero

#Definición de la función para generar dificultad
def seleccionar_dificultad():
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

    nivel = int(input("Ingrese el número correspondiente al nivel: "))

    if nivel < 1 or nivel > 3:
        print("Opción inválida. Intente nuevamente.")
        seleccionar_dificultad()

    return nivel

#Definición de la función para póder remplaza casillas por filas y columnas
def set_valor(tablero):
  f = -1
  while f < 0 or f > 9:
      letra = input("Ingrese la letra de la fila: \n")
      f = ord(letra.upper()) - ord('A')

  c = -1
  while c < 0 or c > 9:
      c = int(input("Ingrese el número de la columna: \n"))

  v = -1
  while v < 0 or v > 9:
      v = int(input("Ingrese el número de su selección: \n"))

  tablero[f][c] = v

  return tablero

#Definición de la función para imprimir el tablero. Esta función muestra visualmente el tablero en la consola.

def print_board(tablero):
  bar="--------------------------"
  indice_fila= string.ascii_uppercase

  print("   ",end="")
  for j in range(len(tablero[0])):
    if (j) % 3==0 and j>0:
      print(" |", end="")
    print("",j, end="")  
  print()

  for i in range(len(tablero)):
    if (i) % 3==0:
      print(bar)
    print(indice_fila[i], end="")

    for j in range(len(tablero[i])):
      if (j) % 3==0: #j>0:
        print(" |", end="")
      print("",tablero[i][j], end="")  
    print()

  print(bar)


#Solicitar al usuario los valores de m y n
m = int(input("Ingrese el número de filas (múltiplos de 3): \n"))
n = int(input("Ingrese el número de columnas (múltiplos de 3): \n"))

print("\n para poder Jugar remplace todos los 0 por los numeros que son para completar el sudoku. \n")

# Llamada a la función para seleccionar el nivel de dificultad
nivel_dificultad = seleccionar_dificultad()

# Llamada a la función para inicializar el tablero con el nivel de dificultad seleccionado
tablero = init(m, n, nivel_dificultad)
# Llamada a la función para imprimir el tablero
print_board(tablero)
set_valor(tablero)
print_board(tablero)
