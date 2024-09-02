# Análisis de Clustering K-Means con Visualización

Este repositorio contiene un script en Python que realiza un análisis de clustering usando el algoritmo K-Means y visualiza la evolución de los clusters a lo largo de las iteraciones. El script genera un archivo GIF que muestra cómo cambian los clusters durante el proceso de ajuste del algoritmo.

## Contenido del Repositorio

- `kmeans_clustering.py`: El script principal que realiza el clustering y genera la visualización en formato GIF.
- `clientes.csv`: Un archivo CSV con un conjunto de datos de ejemplo (solo se generará si se incluye la generación de datos).

## Descripción del Script

El script realiza los siguientes pasos:

1. **Generación de Datos de Ejemplo**:

   - Genera un conjunto de datos con 30,000 registros con las siguientes características:
     - `Frecuencia_de_compra`: Alta, Media, Baja
     - `Tipo_de_producto`: Electrónica, Ropa, Hogar, Alimentos
     - `Ubicacion_geografica`: Norte, Sur, Este, Oeste
     - `Edad`: 18-24, 25-34, 35-44, 45-54, 55+
     - `Año`: 2015, 2016, 2017, 2018
     

2. **Preprocesamiento**:
   - Se utiliza OneHotEncoding para convertir las características categóricas en variables dummy.
   - Se escalan los datos usando `StandardScaler`.

3. **Clustering con K-Means**:
   - Se aplica el algoritmo K-Means con un número fijo de clusters (3 en este caso).
   - Se ajusta el modelo durante 10 iteraciones para observar la evolución de los clusters.

4. **Visualización**:
   - Se utiliza PCA (Análisis de Componentes Principales) para reducir la dimensionalidad de los datos a 2 dimensiones para la visualización.
   - Se generan imágenes de cada iteración mostrando la dispersión de los datos y los centros de los clusters.
   - Se combinan las imágenes en un archivo GIF que muestra la evolución de los clusters.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `imageio` 

Puedes instalar estas dependencias usando pip:

    pip install pandas numpy matplotlib seaborn scikit-learn imageio;
# Cómo Ejecutar el Script
**Clonar el Repositorio:**

    git clone https://github.com/GustavoGamarra95/K_means_Clustering
    cd K_means_Clustering

**Ejecutar el Script:**
    
    python kmeans_clustering.py

Este comando generará el archivo kmeans_evolution.gif en el directorio actual.

# Resultados
El script generará un archivo GIF (kmeans_evolution.gif) que muestra cómo cambian los clusters en cada iteración del algoritmo K-Means. Este archivo puede ser visualizado con cualquier reproductor de GIF para observar la evolución del clustering.

# Contribuciones
Las contribuciones al proyecto son bienvenidas. Si encuentras errores o tienes sugerencias, siéntete libre de abrir un "issue" o enviar una "pull request".

# Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
