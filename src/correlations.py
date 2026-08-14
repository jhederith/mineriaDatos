import matplotlib.pyplot as plt
import numpy as np
import os

def analizar_correlaciones(df):
    """Calcula correlaciones de Pearson y genera exactamente 2 gráficos de correlación."""
    os.makedirs("outputs", exist_ok=True)

    print("\n" + "="*50)
    print(" 3. ANÁLISIS DE CORRELACIONES (BIVARIADO) ")
    print("="*50)

    # Cálculo de correlaciones con cnt
    numeric_df = df.select_dtypes(include=[np.number])
    correlations = numeric_df.corr()['cnt'].drop('cnt').sort_values(key=abs, ascending=False)
    
    print(" Principales correlaciones con 'cnt':")
    for var, corr in list(correlations.items())[:5]:
        print(f"   - {var:12s}: {corr:+.3f}")

    # Configuración de gráficos
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfico de correlación 1: Temperatura vs cnt
    axes[0].scatter(df['temp'], df['cnt'], alpha=0.2, s=10, color='navy')
    z1 = np.polyfit(df['temp'], df['cnt'], 1)
    p1 = np.poly1d(z1)
    x_line1 = np.linspace(df['temp'].min(), df['temp'].max(), 100)
    axes[0].plot(x_line1, p1(x_line1), "r--", linewidth=2, label=f"r = {correlations['temp']:.3f}")
    axes[0].set_title('Temperatura vs Demanda (cnt)')
    axes[0].set_xlabel('Temperatura (temp)')
    axes[0].set_ylabel('Alquileres (cnt)')
    axes[0].legend()

    # Gráfico de correlación 2: Humedad vs cnt
    axes[1].scatter(df['hum'], df['cnt'], alpha=0.2, s=10, color='darkgreen')
    z2 = np.polyfit(df['hum'], df['cnt'], 1)
    p2 = np.poly1d(z2)
    x_line2 = np.linspace(df['hum'].min(), df['hum'].max(), 100)
    axes[1].plot(x_line2, p2(x_line2), "r--", linewidth=2, label=f"r = {correlations['hum']:.3f}")
    axes[1].set_title('Humedad vs Demanda (cnt)')
    axes[1].set_xlabel('Humedad (hum)')
    axes[1].set_ylabel('Alquileres (cnt)')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('outputs/02_correlaciones.png', dpi=200)
    plt.close()
    print("[INFO] Gráficos de correlación guardados en outputs/02_correlaciones.png")