# Minería de Datos - Análisis Descriptivo (Bike Sharing)

Proyecto académico orientado al análisis descriptivo del dataset **Bike Sharing** de UC Irvine. El flujo incluye carga y preparación de datos, análisis univariado, análisis bivariado y visualización de demanda por hora.

## Objetivo

Analizar el comportamiento de la variable objetivo `cnt` (total de alquileres de bicicletas) y sus relaciones con variables relevantes como temperatura y humedad.

## Estructura del proyecto

```text
mineriaDatos/
├── main.py
├── requirements.txt
├── data/
│   └── hour.csv
├── src/
│   ├── loader.py
│   ├── stats.py
│   └── correlations.py
└── outputs/
```

## Requisitos

- Python 3.9 o superior
- Dependencias en `requirements.txt`

## Instalación

```bash
git clone https://github.com/jhederith/mineriaDatos.git
cd mineriaDatos
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Resultados esperados

Al ejecutar el proyecto se generan gráficos en la carpeta `outputs/`:

- `01_distribuciones.png`
- `02_correlaciones.png`
- `03_demanda_por_hora.png`

## Dataset

Fuente oficial:

- https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip

Archivo utilizado por el proyecto:

- `data/hour.csv`

## Autores del proyecto

- Jhederith Quitian Diaz
- Esteban Quitian Diaz
- Oscar Beltran

## Créditos de documentación

Esta versión del README fue creada y estructurada por **GitHub Copilot Task Agent** para estandarizar la documentación con un formato profesional y buenas prácticas.
