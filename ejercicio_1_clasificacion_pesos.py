# Ejercicio 1 del Prelab 3

pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]
piezas_validas = 0

for peso in pesos_piezas:
    if peso <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif 1 <= peso <= 13:
        print("Pieza Ligera aprobada.")
        piezas_validas += 1
    elif peso > 13:
        print("Pieza Pesada aprobada.")
        piezas_validas += 1

print(f"\nTotal de piezas válidas aprobadas: {piezas_validas}")

