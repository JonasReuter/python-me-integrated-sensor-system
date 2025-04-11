import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
from ..base_model import BaseAnomalyModel

class AutoencoderModel(BaseAnomalyModel):
    def __init__(self, input_dim, encoding_dim=3, epochs=10, batch_size=32):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.epochs = epochs
        self.batch_size = batch_size
        self.autoencoder = self._build_model()
    
    def _build_model(self):
        input_layer = Input(shape=(self.input_dim,))
        encoded = Dense(self.encoding_dim, activation="relu")(input_layer)
        decoded = Dense(self.input_dim, activation="sigmoid")(encoded)
        model = Model(inputs=input_layer, outputs=decoded)
        model.compile(optimizer=Adam(), loss="mse")
        return model

    def train(self, X):
        self.autoencoder.fit(X, X, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
    
    def predict(self, X):
        reconstructions = self.autoencoder.predict(X)
        errors = np.mean(np.square(X - reconstructions), axis=1)
        return errors
