from sklearn.base import BaseEstimator, TransformerMixin

class selectionFiture(BaseEstimator, TransformerMixin):
    list_drop = ['RestingECG']
    def __init__(self, drop_columns = list_drop):
        self.drop_columns = drop_columns
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(self.drop_columns, axis=1)