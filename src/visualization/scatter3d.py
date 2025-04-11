import plotly.express as px
import pandas as pd

def create_scatter3d(data: pd.DataFrame, x: str, y: str, z: str, color: str = None, size: str = None, hover_data: list = None, title: str = "3D Scatter Plot"):
    """
    Erstellt einen 3D-Scatterplot für die Eingabedaten.
    """
    fig = px.scatter_3d(data, x=x, y=y, z=z, color=color, size=size, hover_data=hover_data)
    fig.update_layout(title=title)
    fig.show()
