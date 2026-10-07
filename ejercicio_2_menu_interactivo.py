# Ejercicio 2 para el Prelab 3

# Menu con la opción inicial

print("--- MENÚ DE CONTROL DEL ROBOT ---")
print("A. Mover a la derecha")
print("B. Mover a la izquierda")
print("C. Mover hacia frente")
print("D. Mover hacia atrás")
print("E. Apagar\n")

# Bucle continuo 

while True:
    comando = input("Ingrese un código de comando (A, B, C, D, E): ").strip().upper()

    match comando:
        case "A":
            print("El robot se despalzo a la derecha.")
        case "B":
            print("El robot se despalzo a la izquierda.")
        case "C":
            print("El robot se despalzo hacia frente.")
        case "D":
            print("El robot se despalzo hacia atrás.")
        case "E":
            print("Apagando el robot. Programa finalizado.")
            break
        case _:
            print("Comando no válido. Por favor, ingrese A, B, C, D o E.")