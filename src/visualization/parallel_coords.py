import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

def create_parallel_coordinates(data: pd.DataFrame, class_column: str = None, title: str = "Parallel Coordinates Plot"):
    """
    Erstellt einen Parallel Coordinates Plot zur Darstellung mehrerer Dimensionen.
    """
    plt.figure(figsize=(10,6))
    if class_column:
        parallel_coordinates(data, class_column, colormap=plt.get_cmap("Set2"))
    else:
        data_copy = data.copy()
        data_copy["dummy"] = "Daten"
        parallel_coordinates(data_copy, "dummy", colormap=plt.get_cmap("Set2"))
    plt.title(title)
    plt.xlabel("Variablen")
    plt.ylabel("Wert")
    plt.show()
