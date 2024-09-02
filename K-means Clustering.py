import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
import imageio.v2 as imageio
import numpy as np

frecuencia_de_compra = ['Alta', 'Media', 'Baja']
tipo_de_producto = ['Electrónica', 'Ropa', 'Hogar', 'Alimentos']
ubicacion_geografica = ['Norte', 'Sur', 'Este', 'Oeste']
edad = ['18-24', '25-34', '35-44', '45-54', '55+']

np.random.seed(42)
num_registros = 30000
data = {
    'Frecuencia_de_compra': np.random.choice(frecuencia_de_compra, num_registros),
    'Tipo_de_producto': np.random.choice(tipo_de_producto, num_registros),
    'Ubicacion_geografica': np.random.choice(ubicacion_geografica, num_registros),
    'Edad': np.random.choice(edad, num_registros),
    'Año': np.random.choice([2015, 2016, 2017, 2018], num_registros)
}
df = pd.DataFrame(data)

categorical_features = ['Frecuencia_de_compra', 'Tipo_de_producto', 'Ubicacion_geografica', 'Edad']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ]
)

X = preprocessor.fit_transform(df)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.toarray())

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

n_clusters = 8
kmeans = KMeans(n_clusters=n_clusters, random_state=42, init='random', max_iter=1, n_init=1)

filenames = []
for i in range(300):
    kmeans.fit(X_scaled)
    labels = kmeans.predict(X_scaled)

    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, s=50, cmap='viridis', alpha=0.7, marker='o')

    centers = kmeans.cluster_centers_
    centers_pca = pca.transform(scaler.transform(centers))
    plt.scatter(centers_pca[:, 0], centers_pca[:, 1], c='red', s=200, alpha=0.75, marker='X',
                label='Centros de Clusters')

    plt.colorbar(scatter, label='Cluster')
    plt.title(f'Iteración {i + 1}')
    plt.xlabel('Componente PCA 1')
    plt.ylabel('Componente PCA 2')
    plt.legend()
    filename = f'kmeans_iter_{i}.png'
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))  # Leer las imágenes
imageio.mimsave('kmeans_evolution.gif', images, duration=0.5)

print("GIF generado con éxito.")
