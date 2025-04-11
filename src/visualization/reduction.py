import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def reduce_dimensions_pca(data: pd.DataFrame, n_components: int = 2):
    """
    Führt eine PCA durch und reduziert die Dimensionen.
    """
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(data.values)
    columns = [f"PC{i+1}" for i in range(n_components)]
    return pd.DataFrame(components, columns=columns)

def plot_pca_result(data: pd.DataFrame, title: str = "PCA Result"):
    """
    Plottet ein 2D-Scatterplot der PCA-Komponenten.
    """
    plt.figure(figsize=(8,6))
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha=0.7)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(title)
    plt.show()
