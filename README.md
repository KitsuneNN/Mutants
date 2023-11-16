# Mutants

## Información Personal
**Nombre y Apellido:** Nadir Nahuel Quiroga  
**Legajo:** 51623  
**Email:** nadirquiroga@gmail.com

## Descripción del Proyecto
Este proyecto fue asignado por Mercado Libre a través de la facultad regional de Mendoza. El objetivo del proyecto es desarrollar un programa que...

## Resolución
La resolución del problema se llevó a cabo utilizando...

## Código

El código principal del proyecto se encuentra en el archivo `mutants.py`. A continuación, se presenta una descripción general de la estructura del código:

```python
# Aquí va una breve descripción del propósito del código

def is_mutant(dna):
    # Lógica para determinar si el ADN es mutante
    # ...

def solicitar_matriz_al_usuario():
    # Función para solicitar al usuario que complete la matriz de ADN
    # ...

# Solicitar al usuario que complete la matriz
matriz_ingresada = solicitar_matriz_al_usuario()

print("\nMatriz ingresada por el usuario:")
for fila in matriz_ingresada:
    print(fila)

# Comprobar si el ADN es mutante
resultado = is_mutant(matriz_ingresada)
print("\n¿Es mutante?", resultado)
