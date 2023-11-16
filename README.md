# Mutants

## Información Personal
**Nombre y Apellido:** Nadir Nahuel Quiroga  
**Legajo:** 51623  
**Email:** nadirquiroga@gmail.com

## Descripción del Proyecto
Este proyecto fue asignado por Mercado Libre a través de la facultad regional de Mendoza. El objetivo del proyecto es desarrollar un programa que Magneto reclute la mayor cantidad de mutantes para poder luchar contra los X-Mens. Desarrollando un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.
Para que un individuo sea conciderado mutante deve tener al menos 2 grupos de cuatro letras (A,T,C,G) en forma de columna, fila y diagonal.

## Resolución
Para resolver el problema, se implementó una lógica que verifica la presencia de dos o más secuencias de cuatro letras iguales consecutivas en un conjunto de ADN. Esto se logró explorando la matriz en direcciones horizontal, vertical y diagonal. La validación de la entrada del usuario asegura que la matriz de ADN sea válida antes de realizar la verificación mutante.

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
```
###Instrucciones para ejecutar el programa:
**Asegúrate de tener Python instalado en tu sistema.
**Ejecuta el programa utilizando el comando python mutants.py.
**Sigue las instrucciones para completar la matriz de ADN.
## ¿Cómo Correrlo?

**Requisitos Previos:**
- Asegúrate de tener Python instalado en tu sistema.

**Pasos para Ejecutar el Programa:**
1. Descarga el archivo `Mutants.py` desde el repositorio.
2. Abre una terminal o línea de comandos en el directorio donde se encuentra el archivo `Mutants.py`.
3. Ejecuta el siguiente comando para iniciar el programa:
   ```bash
   python Mutants.py

