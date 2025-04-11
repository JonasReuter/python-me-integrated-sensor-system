import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def create_pairplot(data: pd.DataFrame, hue: str = None, title: str = "Pair Plot"):
    """
    Erstellt einen Pairplot (Scatterplot-Matrix) für die Eingabedaten.
    """
    g = sns.pairplot(data, hue=hue)
    g.fig.suptitle(title, y=1.02)
    plt.show()
