#ProyectoConArreglos
# Creamos variables e inicializamos con sus respectivos valores
# Creamos un Arreglo vacio
# Creamos una variable que pida y almacene un dato que al mismo tiempo funciona como operador para decidir las veces que se ejecutar el ciclo FOR
# Se piden datos en la variable Edad y se almacenan justo despues se crea un acumulado para ser imprimido mas adelante
# Se crean condiciones que determinan que variable es mayor o menor
# Justo despues se calculan los porcentajes y promedios de dichas variables ya mencionadas

Contador = 0
Sumadora = 0
CantidadMenoresEdad = 0
Menor = 0
Mayor = 0
PromedioEdades = 0
Porcentaje = 0

print("ESTUDIANTE: ANDREW ECHEVERRIA\n")

ListadoEdades = []

N = int(input("Cantidad Estudiantes...  "))

for i in range(N):
    Edad = int(input("Escriba su edad... "))
    Sumadora = Sumadora + Edad

    if Edad >= 18:
        Contador = Contador + 1

    if i == 1:
        Mayor = Edad
        Menor = Edad

    if Edad > Mayor:
        Mayor = Edad

    if Edad < Menor:
        Menor = Edad

    ListadoEdades.append(Edad)


PromedioEdades = Sumadora / N
Porcentaje = Contador * 100 / N
CantidadMenoresEdad = N - Contador

print("El Valor del Promedio de Edades es: "+(str(PromedioEdades)))
print("El Valor del Porcentaje de Edades es: "+(str(Porcentaje)))
print("La Cantidad de Menores de Edad son: ", CantidadMenoresEdad)
print("El Valor de Edad Mas Alto es: ", Mayor)
print("El Valor de Edad Mas Bajo es: ", Menor)
