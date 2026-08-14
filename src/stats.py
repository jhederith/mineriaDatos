import matplotlib.pyplot as plt
import os

def analizar_distribuciones(df):
    """Genera estadísticas descriptivas y exactamente 2 gráficos de distribución."""
    os.makedirs("outputs", exist_ok=True)
    
    print("\n" + "="*50)
    print(" 2. ANÁLISIS DE DISTRIBUCIONES (UNIVARIADO) ")
    print("="*50)
    print(f" - Media de alquileres (cnt): {df['cnt'].mean():.2f}")
    print(f" - Mediana de alquileres (cnt): {df['cnt'].median():.2f}")
    print(f" - Asimetría (Skewness) de cnt: {df['cnt'].skew():.2f} (Sesgo positivo)")

    # Configuración de estilo
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfico de distribución 1: Variable respuesta 'cnt'
    axes[0].hist(df['cnt'], bins=50, color='steelblue', edgecolor='black', alpha=0.75)
    axes[0].axvline(df['cnt'].mean(), color='red', linestyle='dashed', linewidth=2, label=f"Media: {df['cnt'].mean():.1f}")
    axes[0].axvline(df['cnt'].median(), color='green', linestyle='dashed', linewidth=2, label=f"Mediana: {df['cnt'].median():.1f}")
    axes[0].set_title('Distribución de cnt (Total de alquileres)')
    axes[0].set_xlabel('Alquileres por hora (cnt)')
    axes[0].set_ylabel('Frecuencia')
    axes[0].legend()

    # Gráfico de distribución 2: Temperatura ('temp')
    axes[1].hist(df['temp'], bins=40, color='coral', edgecolor='black', alpha=0.75)
    axes[1].axvline(df['temp'].mean(), color='darkred', linestyle='--', linewidth=2, label=f"Media: {df['temp'].mean():.2f}")
    axes[1].set_title('Distribución de la Temperatura (temp)')
    axes[1].set_xlabel('Temperatura normalizada')
    axes[1].set_ylabel('Frecuencia')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('outputs/01_distribuciones.png', dpi=200)
    plt.close()
    print("[INFO] Gráficos de distribución guardados en outputs/01_distribuciones.png")