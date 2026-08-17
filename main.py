"""
Trabajo 1: Lectura de datos y análisis descriptivo
Aprendeizaje Automático y Minería de Datos
Dataset: Bike Sharing (UC Irvine Machine Learning Repository)
Varaible respuesta: cnt (total de alquileres de bicicletas)
Autores:
   - Esteban Quitian @quitian07
   - Oscar Beltran @oscarbeltran12
   - Jhederith Quitian @jhederith
"""

import sys
import os
from tabulate import tabulate


# Inclusión del directorio src en el path para no tener problemas al importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from loader import cargar_y_preparar_datos
from stats import analizar_distribuciones
from correlations import analizar_correlaciones, demanda_por_hora

def main():
    print("=" * 70)
    print(" PIPELINE DE ANÁLISIS DESCRIPTIVO - BIKE SHARING (UNIR)")
    print("=" * 70)

    """
    el pipelin consiste en 4 pasos:
    1. Cargar y estructurar datos
    2. Análisis de Distribuciones (Ejecuta estadísticas y genera los 2 gráficos univariados)
    3. Análisis de Correlaciones (Calcula coeficientes y genera los 2 gráficos bivariados)
    4. Demanda por hora (Genera un gráfico de demanda por hora)
    """
    # 1. Cargar y estructurar datos
    df, X_train, X_test, y_train, y_test = cargar_y_preparar_datos("data/hour.csv")

    # Mostrar información inicial en consola usando formato ASCII con tabulate
    print("\n[INFO] Vista previa del dataset (Primeras 3 filas):")
    print(tabulate(df[['season', 'hr', 'temp', 'hum', 'cnt']].head(3), headers='keys', tablefmt='psql'))

    # 2. Análisis de Distribuciones (Ejecuta estadísticas y genera los 2 gráficos univariados)
    analizar_distribuciones(df)

    # 3. Análisis de Correlaciones (Calcula coeficientes y genera los 2 gráficos bivariados)
    analizar_correlaciones(df)

    #4. Demanda por hora (Genera un gráfico de demanda por hora)
    demanda_por_hora(df)

    print("\n" + "=" * 70)
    print(" Proceso completado con éxito.")
    print(" Los gráficos se han creado y exportado a la carpeta /outputs.")
    print("=" * 70)

if __name__ == "__main__":
    main()