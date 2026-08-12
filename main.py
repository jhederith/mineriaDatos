import sys
import os
from tabulate import tabulate

# Inclusión del directorio src en el path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from loader import cargar_y_preparar_datos
from stats import analizar_distribuciones
from correlations import analizar_correlaciones

def main():
    print("=" * 70)
    print(" PIPELINE DE ANÁLISIS DESCRIPTIVO - BIKE SHARING (UNIR)")
    print("=" * 70)

    # 1. Cargar y estructurar datos
    df, X_train, X_test, y_train, y_test = cargar_y_preparar_datos("hour.csv")

    # Mostrar información inicial en consola usando formato ASCII con tabulate
    print("\n[INFO] Vista previa del dataset (Primeras 3 filas):")
    print(tabulate(df[['season', 'hr', 'temp', 'hum', 'cnt']].head(3), headers='keys', tablefmt='psql'))

    # 2. Análisis de Distribuciones (Ejecuta estadísticas y genera los 2 gráficos univariados)
    analizar_distribuciones(df)

    # 3. Análisis de Correlaciones (Calcula coeficientes y genera los 2 gráficos bivariados)
    analizar_correlaciones(df)

    print("\n" + "=" * 70)
    print(" [EXITO] Proceso completado con éxito.")
    print(" Los gráficos limpios han sido exportados a la carpeta /outputs para tu PDF.")
    print("=" * 70)

if __name__ == "__main__":
    main()