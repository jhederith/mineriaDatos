# Taller de Minería de Datos

Este proyecto es parte del **taller de minería de datos**.  
Se hace uso de **GitHub** y de la **colaboración en la nube** para aplicar buenas prácticas de programación, trabajo en equipo y control de versiones.

## Autores

- Jhederith Quitian Diaz
- Esteban Quitian Diaz
- Oscar Beltran

## Contexto del proyecto

El proyecto realiza una carga y análisis descriptivo inicial del dataset **Bike Sharing** de UC Irvine.  
Archivo principal actual:

- `descriptiveAnalysis.py`

Fuente del dataset:

- https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip

## Clonación del repositorio

```bash
git clone https://github.com/jhederith/mineriaDatos.git
cd mineriaDatos
```

## Requisitos

Se recomienda usar **Python 3.9+**.

Librerías necesarias:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Instalación rápida:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Ejecución del proyecto

1. Descarga el dataset desde el enlace de UC Irvine.
2. Descomprime el archivo zip.
3. Copia `hour.csv` dentro de la carpeta raíz del proyecto (`mineriaDatos`).
4. Ejecuta el script:

```bash
python descriptiveAnalysis.py
```

> Si `hour.csv` no está en la raíz del proyecto, el script mostrará un mensaje de error indicando cómo descargarlo.

---

Este README es una base inicial; en futuras iteraciones se ampliará con más detalles del flujo de trabajo y mejoras del proyecto.
