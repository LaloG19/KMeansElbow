# Análisis de Clústers con K-Means

Este proyecto realiza un análisis de clústers utilizando el algoritmo K-Means en un dataset de clientes de un centro comercial. El objetivo es segmentar a los clientes en diferentes grupos basados en sus características demográficas y de comportamiento.

## Archivos Incluidos

- `kmeans_clustering.py`: Script principal que realiza el análisis de clústers y genera las visualizaciones.
- `Mall_Customers.csv`: Dataset original de clientes.
- `Mall_Customers_normalized.csv`: Dataset normalizado utilizado para el análisis.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.
- `.gitignore`: Archivo para ignorar archivos innecesarios en el repositorio Git.
- `clusters_3d.html`: Visualización interactiva en 3D de los clústers generados.
- `distribucion_Age.png`, `distribucion_Annual_Income_(k$).png`, `distribucion_Spending_Score_(1-100).png`: Gráficos de barras que muestran la distribución de cada característica por clúster.
- `cluster_stats.csv`: Estadísticas descriptivas de cada clúster.

## Requisitos

- Python 3.7 o superior
- Bibliotecas listadas en `requirements.txt`

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `.\env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Asegúrate de tener `Mall_Customers.csv` en la raíz del proyecto.
2. Ejecuta el script principal:
    ```sh
    python kmeans_clustering.py
    ```
3. Los resultados generados incluirán:
   - Estadísticas descriptivas en `cluster_stats.csv`
   - Visualización 3D interactiva en `clusters_3d.html`
   - Gráficos de barras en archivos PNG (`distribucion_Age.png`, `distribucion_Annual_Income_(k$).png`, `distribucion_Spending_Score_(1-100).png`)

## Visualizaciones

- **Gráfica 3D**: `clusters_3d.html`
- **Gráficos de Barras**:
  - Distribución de Edad: `distribucion_Age.png`
  - Distribución de Ingresos Anuales: `distribucion_Annual_Income_(k$).png`
  - Distribución de Puntaje de Gasto: `distribucion_Spending_Score_(1-100).png`

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
