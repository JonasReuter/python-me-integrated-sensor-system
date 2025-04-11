from sklearn.svm import OneClassSVM
from ..base_model import BaseAnomalyModel

class OneClassSVMModel(BaseAnomalyModel):
    def __init__(self, kernel="rbf", gamma="scale", nu=0.05):
        self.model = OneClassSVM(kernel=kernel, gamma=gamma, nu=nu)
    
    def train(self, X):
        self.model.fit(X)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def decision_function(self, X):
        return self.model.decision_function(X)
