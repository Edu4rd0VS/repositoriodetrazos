print("Hola mundo!") 
import pandas as pd

# Cargar los datos
df = pd.read_csv('spotify.csv')

# Verificar columnas
print("Columnas disponibles:", df.columns)

# Analizar valence y energy
subset = df[['valence', 'energy']]
print("\n=== Estadísticas generales ===")
print(subset.describe())

# Canciones con baja valence (< 0.4)
baja_valence = df[df['valence'] < 0.4]
alta_valence = df[df['valence'] >= 0.4]

print("\nPromedio de energía (baja valence):", baja_valence['energy'].mean())
print("Promedio de energía (alta valence):", alta_valence['energy'].mean())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv('spotify.csv')

# Verificar columnas
print("Columnas disponibles:", df.columns)

# Analizar valence y energy
subset = df[['valence', 'energy']]
print("\n=== Estadísticas generales ===")
print(subset.describe())

# Canciones con baja valence (< 0.4)
baja_valence = df[df['valence'] < 0.4]
alta_valence = df[df['valence'] >= 0.4]
print("\nPromedio de energía (baja valence):", baja_valence['energy'].mean())
print("Promedio de energía (alta valence):", alta_valence['energy'].mean())

# ==== NUEVAS VISUALIZACIONES ====

# 1. Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['valence'], df['energy'], alpha=0.5, c='blue')
plt.xlabel('Valence (Positividad)')
plt.ylabel('Energy (Energía)')
plt.title('Relación entre Valence y Energy en Spotify')
plt.grid(True, alpha=0.3)
plt.savefig('valence_vs_energy.png')
plt.show()

# 2. Correlación
correlation = df['valence'].corr(df['energy'])
print(f"\n=== Correlación ===")
print(f"Correlación entre valence y energy: {correlation:.3f}")

# 3. Guardar resultados
df.to_csv('spotify_analizado.csv', index=False)
print("\n✅ Análisis completado. Archivos guardados.")