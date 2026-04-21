from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

def train(X, y):
    model.fit(X, y)

def predict(X):
    return model.predict(X)
