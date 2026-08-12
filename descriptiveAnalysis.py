"""
Trabajo 1: Lectura de datos y análisis descriptivo
Aprendeizaje Automático y Minería de Datos
Dataset: Bike Sharing (UC Irvine Machine Learning Repository)
Varaible respuesta: cnt (total de alquileres de bicicletas)
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

#visual config 

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# 1. Data and structure charge

print("=" * 70 )
print("1. Carga de los datos")
print("=" * 70 )

"""
El origen del dataset se encuentra en el repository de la UC Irvine y puede ser descargado con este link:
https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip
"""

try:
    df = pd.read_csv("hour.csv")
    print("Dataset cargado con éxito")
except FileNotFoundError:
    print("Archivo no encontrado, descarga el repo en: ")
    print("https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip")
    print("Descomprime el archivo zip en la carpeta del notebook y vuelve a ejecutar")
    exit()


# Testing pipeline