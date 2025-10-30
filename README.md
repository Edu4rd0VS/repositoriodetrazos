# Análisis de Spotify - Valence vs Energy

## Descripción
Análisis de la relación entre positividad (valence) y energía (energy) en canciones de Spotify.

## Requisitos
Instala las librerías necesarias:
```bash
pip install pandas matplotlib seaborn
```

## Estructura del proyecto
```
repositoriodetrazos/
├── spotify.csv                  # Dataset original
├── tu_archivo.py                # Código de análisis
├── valence_vs_energy.png        # Gráfico generado
├── spotify_analizado.csv        # Resultados
└── README.md                    # Este archivo
```

## Cómo ejecutar
```bash
python tu_archivo.py
```
(Reemplaza `tu_archivo.py` con el nombre real de tu script)

## Archivos generados
- **valence_vs_energy.png**: Gráfico de dispersión mostrando la relación entre valence y energy
- **spotify_analizado.csv**: Dataset procesado con el análisis completo

## Resultados principales
- Promedio de energía en canciones con baja positividad (valence < 0.4)
- Promedio de energía en canciones con alta positividad (valence >= 0.4)
- Correlación entre valence y energy
- Visualización de la distribución de canciones