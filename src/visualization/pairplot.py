import matplotlib.pyplot as plt
import pandas as pd

def create_pairplot(df: pd.DataFrame, title: str = "Pairplot"):
    # Erzeugen Sie einen Scatter-Matrix-Plot
    pd.plotting.scatter_matrix(df, figsize=(8, 8), diagonal='hist')
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()
