# Ejercicio fin evaluacion Módulo 3
## Análisis de Datos de Reservas de Vuelos

Este repositorio contiene el proyecto final de evaluación del módulo 3 del curso de Analista de Datos por Adalab, Promo k. 


## Tabla de Contenidos
1. [Descripción del Ejercicio](#descripción-del-ejercicio)
2. [Objetivos](#objetivos)
3. [Tecnologías Utilizadas](#tecnologias-utilizadas)
4. [Instrucciones para Ejecutar el Ejercicio](#instrucciones-para-ejecutar-el-ejercicio)
5. [Estructura del Ejercicio](#estructura-del-ejercicio)
6. [Resultados y Visualizaciones](#resultados-y-visualizaciones)
7. [Autora](#autora)

## Descripción del Ejercicio

El proyecto realiza un análisis exhaustivo de un conjunto de datos de reservas de vuelos, incluyendo la exploración y limpieza de los datos, 
la visualización de patrones e insights, y la evaluación de diferencias en el número de vuelos reservados según el nivel educativo de los clientes.

Este ejercicio está dividido en tres fases:

**Fase 1:** Exploración y Limpieza de Datos
- Exploración inicial para identificar problemas en los datos.
- Tratamiento de valores nulos y atípicos.
- Unificación de conjuntos de datos y limpieza.

**Fase 2:** Visualización de Datos
Creación de visualizaciones para responder preguntas clave sobre los datos:
- Distribución de vuelos reservados por mes.
- Relación entre distancia de vuelos y puntos acumulados.
- Distribución de clientes por provincia.
- Comparación de salario promedio según nivel educativo.
- Proporción de tipos de tarjetas de fidelidad.
- Distribución de clientes según estado civil y género.
  
**BONUS: Fase 3** Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo
- Análisis de la diferencia en las reservas de vuelos según nivel educativo.
- Aplicación de pruebas estadísticas para determinar la significancia de las diferencias.

## Objetivos

- Análisis Exploratorio de los datos.
- Gestión de nulos.
- Visualización de datos con matplotlib y seaborn.
- Estadística descriptiva e inferencial.
- A/B testing.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **Pandas:** Libreria para la manipulación de datos.
- **Numpy:** Libreria para el cálculo numérico.
- **Matplotlib y Seaborn:** Libreria para la visualización de datos.
- **SciPy:** Libreria para las pruebas estadísticas.
- **Jupyter Notebooks:** Entorno interactivo para la documentación y ejecución de análisis.

## Instrucciones para Ejecutar el Ejercicio

1. Clonar el repositorio
Para clonar este repositorio, usa el siguiente comando: 

git clone [https://github.com/Adalab/bda-modulo-3-evaluacion-final-psainzpc.git](https://github.com/Adalab/bda-modulo-3-evaluacion-final-psainzpc.git)

## Estructura del Ejercicio

El repositorio contiene la siguiente estructura:

**Descripción de la Estructura de Carpetas**

- **`data/`**: Esta carpeta contiene los conjuntos de datos utilizados en el análisis.
  - **`Customer Flight Activity.csv`**: Conjunto de datos con la información sobre los vuelos reservados (incluye columnas como la fecha de reserva, el destino, la distancia del vuelo, etc.).
  - **`Customer Loyalty History.csv`**: Conjunto de datos con la información sobre los clientes (incluye columnas como nivel educativo, tipo de tarjeta de fidelidad, provincia, salario, ciudad, etc.).
  - **`union_tablas.csv`**: union de los conjuntos de datos anteriores con la fase 1 de exploración y limpieza realiza(gestión de nulos, duplicados y tipos de datos).

- **`notebooks`**: un Notebook Jupyter por cada fase para facilitar la evaluación del ejercicio: 
  **`1.exploracion_limpieza.ipynb`**: Notebook que contiene el código para la exploración y limpieza de los datos (fase 1).
  **`1.1.comprobaciones.ipynb`**: Notebook con las comprobaciones realizadas para llevar a cabo los pasos de limpieza de los datos.
  **`2.visualizaciones.ipynb`**: Notebook que contiene el código para llevar a cabo la fase 2 (visualización) con los diferentes gráficos.
  **`3.bonus.ipynb`**: Notebook que contiene el código para llevar a cabo la fase 3 (prueba de hipótesis).

- **`src/`**: Scripts de Python utilizados para el procesamiento y análisis de los datos. 
  - **`soporte.py`**: funciones usadas para el analisis

- **`README.md`**: Este archivo de documentación, que explica el propósito del proyecto, cómo ejecutarlo y su estructura.

## Resultados y Visualizaciones
Durante la fase de exploracion y limpieza, se llevaron a cabo los siguientes cambios: 
- Gestión de datos duplicados por mes.
- Gestión de datos nulos en la columna salario.
- Corrección de valores atípicos. Valor negativo en la columna de salario.
- Cambiar tipo de dato en columnas de cancelacion (de float a int), respetando los nulos de los clientes que siguen activos.

Durante la fase de visualización, se generaron varios gráficos para responder las siguientes preguntas:

1.  ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?
   
Se utilizó un gráfico de lineas para observar la variación mensual durante los 2 diferentes años de los datos.

2. ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los clientes?

Se utilizó un gráfico de dispersión para explorar esta relación.

3. ¿Cuál es la distribución de los clientes por provincia o estado?

Se creó un gráfico de barras (barplot) para ver la distribución geográfica de los clientes.

4. ¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?
   

Se generó un gráfico de barras (barplot) con la media de los salarios por nivel educativo.

5. ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad?

Se realizó un gráfico de pastel para mostrar la distribución de tarjetas.

6. ¿Cómo se distribuyen los clientes según su estado civil y género?

Se utilizó un gráfico de barraspara analizar la distribución de clientes según estas variables.

Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativos:

Los pasos seguidos fueron:
- Preparación de datos: Filtrando el conjunto de datos para incluir solo las columnas necesarias: Flights Booked y Education.
- Análisis Descriptivo: Agrupando los datos por nivel educativo y calculando estadísticas descriptivas.
- Prueba de Hipótesis: Realizando la Prueba de Kruskal-Wallis junto con la prueba post-hoc de Dunn:
  * Los resultados mostraron que sí existen diferencias significativas en las reservas de vuelos entre 2 de los niveles educativos.
  * Entre el resto de niveles educativos no existen diferencias significativas


## Autora
* Patricia Sainz-Pardo Caraballo - Estudiante de Adalab. Curso Analista de Datos. Promo K.
* Perfil de **GitHub**: [@psainzpc](https://github.com/psainzpc)

