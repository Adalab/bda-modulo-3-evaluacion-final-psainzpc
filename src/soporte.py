import pandas as pd
import numpy as np
from scipy.stats import shapiro, levene
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency
#import scipy.stats as stats
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest

from IPython.display import display

def exploracion(df):
    '''
    Realiza una exploración inicial de un DataFrame de pandas proporcionando información 
    sobre los datos nulos, duplicados, tipos de datos, valores únicos y estadísticas descriptivas.

    Esta función imprime un resumen con:
    - El número de filas y columnas del DataFrame.
    - El porcentaje de valores nulos y no nulos por columna.
    - El tipo de dato de cada columna.
    - El número de valores únicos en cada columna.
    - El número total de registros duplicados y su porcentaje respecto al total de filas.
    - Las columnas que contienen datos nulos y las que no contienen datos nulos.
    - Comprueba si si tiene columnas categóricas y numéricas, y si las tiene devuelve Estadísticas descriptivas.

    Parámetros:
    ----------
    df : pandas.DataFrame
        El DataFrame que se desea explorar.

    Retorna:
    --------
    df_info : pandas.DataFrame
        Un DataFrame con la siguiente información para cada columna:
        - '% nulos': Porcentaje de valores nulos.
        - '% no_nulos': Porcentaje de valores no nulos.
        - 'tipo_dato': Tipo de dato de la columna.
        - 'num_valores_unicos': Número de valores únicos en la columna.'''

    df_info = pd.DataFrame()

    df_info["% nulos"] = round(df.isna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["% no_nulos"] = round(df.notna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["tipo_dato"] = df.dtypes
    df_info["num_valores_unicos"] = df.nunique()

    print(f"""El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.
    Tiene {df.duplicated().sum()} datos duplicados, lo que supone un porcentaje de {round(df.duplicated().sum()/df.shape[0], 2)}% de los datos.

    Hay {len(list(df_info[(df_info["% nulos"] != "0.0%")].index))} columnas con datos nulos, y son: 
    {list(df_info[(df_info["% nulos"] != "0.0%")].index)}

    y sin nulos hay {len(list(df_info[(df_info["% nulos"] == "0.0%")].index))} columnas y son: 
    {list(df_info[(df_info["% nulos"] == "0.0%")].index)}


    A continuación tienes un detalle sobre los datos nulos y los tipos y número de datos:""")
    
    display(df_info.head())

    print("Principales estadísticos de las columnas categóricas:")
    categorial_columns = df.select_dtypes(include="O")
    if not categorial_columns.empty:
        display(categorial_columns.describe().T)
    else:
        print("No hay columnas categóricas en el DataFrame.")

    print("Principales estadísticos de las columnas numéricas:")
    numeric_columns = df.select_dtypes(exclude="O")
    if not numeric_columns.empty:
        # Asegurarse de que las columnas numéricas estén en el tipo adecuado
        numeric_columns = numeric_columns.apply(pd.to_numeric, errors='coerce')  # Forzar conversión a numérico
        display(numeric_columns.describe().T)
    else:
        print("No hay columnas numéricas en el DataFrame.")

    return df_info

def convertir_int(df, columna):
    """
    Convierte una columna de un DataFrame a tipo entero, manteniendo los valores nulos.

    Esta función intenta convertir los valores de una columna específica de un DataFrame
    al tipo de dato `Int64` de pandas, que es un tipo entero que permite valores nulos
    (representados como `<NA>`). Si ocurre un error durante la conversión, la función
    devolverá `np.nan` para indicar que la conversión falló.

    Args:
        df (pd.DataFrame): El DataFrame que contiene la columna a convertir.
        columna (str): El nombre de la columna que se desea convertir a tipo entero.

    Returns:
        None: Si la conversión es exitosa, la columna se actualiza en el DataFrame y no retorna nada.
        np.nan: Si ocurre un error en la conversión (por ejemplo, si los datos no pueden ser convertidos), retorna `np.nan`."""

    try: 
        df[columna]= df[columna].astype('Int64')
        return
    
    except:
        return np.nan

def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.
    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.
    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """
    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")