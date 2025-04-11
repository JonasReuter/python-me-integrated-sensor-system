from setuptools import setup, find_packages

setup(
    name='integrated_system',
    version='0.1.0',
    description='Integriertes System für Anomalieerkennung, Visualisierung und Datenintegration mit GSV Messverstärker Integration',
    author='Your Name',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'pyyaml',
        'plotly',
        'tensorflow',
        'fastapi',
        'uvicorn',
        'kafka-python',
        'sqlalchemy',
        'pymongo',
        'elasticsearch',
        # ggf. weitere Bibliotheken (z.B. für MLflow, Optuna, Dash, etc.)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)