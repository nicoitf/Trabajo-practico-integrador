def es_bisiesto(anio):
    """Devuelve True si el año es bisiesto, False si no lo es"""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def ordenar_burbuja(lista):
    """Ordena la lista usando el algoritmo de burbuja"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# 1. Solicitar cantidad de personas
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de personas: "))
        if cantidad > 0:
            break
        else:
            print("Debe ingresar un número mayor a 0.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# 2. Pedir años de nacimiento con validación
anios = []
for i in range(cantidad):
    while True:
        anio = input(f"Ingrese el año de nacimiento de la persona {i+1}: ")
        if anio.isdigit() and len(anio) == 4:
            anios.append(int(anio))
            break
        else:
            print("Año inválido. Debe ser un número de 4 dígitos.")

# 3. Ordenar usando burbuja
anios_ordenados = ordenar_burbuja(anios.copy())
print("Años ordenados de menor a mayor:", anios_ordenados)

# 4. Mostrar cuáles años son bisiestos
bisiestos = [anio for anio in anios_ordenados if es_bisiesto(anio)]

print("\nVerificando años bisiestos:")
if bisiestos:
    print("Los siguientes años son bisiestos:", bisiestos)
else:
    print("Ninguno de los años ingresados es bisiesto.")
