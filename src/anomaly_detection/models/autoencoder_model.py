import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from ..base_model import BaseAnomalyModel

class AutoencoderModel(BaseAnomalyModel):
    def __init__(self, input_dim: int, encoding_dim: int = None, learning_rate: float = 0.001, epochs: int = 50, batch_size: int = 32):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim if encoding_dim is not None else max(1, input_dim // 2)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            Dense(self.encoding_dim, activation='relu', input_shape=(self.input_dim,)),
            Dense(self.input_dim, activation='sigmoid')
        ])
        model.compile(optimizer=Adam(learning_rate=self.learning_rate), loss='mse')
        return model

    def train(self, X: pd.DataFrame):
        X_values = X.values
        self.model.fit(X_values, X_values, epochs=self.epochs, batch_size=self.batch_size, verbose=1)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        X_values = X.values
        reconstructions = self.model.predict(X_values)
        mse = np.mean(np.power(X_values - reconstructions, 2), axis=1)
        return mse
