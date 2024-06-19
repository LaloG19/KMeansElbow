import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px

# Cargar el archivo CSV con los datos normalizados
X = pd.read_csv('Mall_Customers_normalized.csv')

# Verificar la carga correcta de datos
print("Datos cargados correctamente:")
print(X.head())

# Número óptimo de clústers basado en la regla del codo
k_optimo = 4

# Entrenar el modelo K-Means con el número óptimo de clústers
kmeans = KMeans(n_clusters=k_optimo, init='k-means++', n_init=10, max_iter=200, tol=0.0001, random_state=111)
kmeans.fit(X)

# Añadir las etiquetas de los clústers al DataFrame original
X['cluster'] = kmeans.labels_

# Describir las estadísticas de cada clúster
cluster_stats = X.groupby('cluster').mean()
print("Estadísticas de cada clúster:")
print(cluster_stats)

# Guardar las estadísticas en un archivo CSV
cluster_stats.to_csv('cluster_stats.csv')

# Crear gráficos de barras para cada característica
features = ['Age', 'Spending Score (1-100)', 'Annual Income (k$)']
for feature in features:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='cluster', y=feature, data=X)
    plt.title(f'Distribución de {feature} por Clúster')
    plt.xlabel('Clúster')
    plt.ylabel(feature)
    plt.savefig(f'distribucion_{feature.replace(" ", "_")}.png')
    plt.show()

# Visualizar los clústers en un gráfico 3D interactivo
fig = px.scatter_3d(X, x='Age', y='Spending Score (1-100)', z='Annual Income (k$)', color='cluster', title='Clusters de Clientes')
fig.show()
fig.write_html("clusters_3d.html")
