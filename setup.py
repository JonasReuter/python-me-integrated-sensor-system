from setuptools import setup, find_packages

setup(
    name='python-me-integrated-sensor-system',
    version='0.1.0',
    description='Integriertes System für Anomalieerkennung, Visualisierung und Datenintegration mit GSV Messverstärker Integration',
    author='Jonas Reuter',
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
        'joblib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)