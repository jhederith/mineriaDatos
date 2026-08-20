import pandas as pd
from sklearn.model_selection import train_test_split

def cargar_y_preparar_datos(ruta_csv="hour.csv"):
    """Carga el dataset, verifica nulos y realiza la partición de datos."""
    try:
        df = pd.read_csv(ruta_csv)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo en {ruta_csv}. Asegúrate de descargarlo.")
        exit(1)

    # Tratamiento de valores faltantes (según pautas de la actividad)
    missing_count = df.isnull().sum().sum()
    if missing_count > 0:
        print(f"[AVISO] Se encontraron {missing_count} valores nulos. Aplicando imputación...")
        df.fillna(df.median(numeric_only=True), inplace=True)
    else:
        print("[INFO] No se encontraron valores faltantes en el dataset.")

    # Selección de datos y eliminación de variables para evitar data leakage
    # (Se eliminan 'casual' y 'registered' porque suman 'cnt', además de identificadores)
    cols_to_drop = ['cnt', 'casual', 'registered', 'instant', 'dteday']
    X = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    y = df['cnt']

    # División 80% modelización, 20% validación
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, shuffle=True
    )

    print(f"[INFO] Dataset cargado: {df.shape[0]} registros totales.")
    print(f"[INFO] Conjunto de entrenamiento: {len(X_train)} obs. | Validación: {len(X_test)} obs.")
    
    return df, X_train, X_test, y_train, y_test

