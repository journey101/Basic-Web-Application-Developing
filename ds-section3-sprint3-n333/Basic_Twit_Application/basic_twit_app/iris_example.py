import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

MODEL_FILE = os.path.join(os.path.dirname(__file__), "models",
                          "twit_model.pkl")


def create_model():
    X, y = load_iris(return_X_y=True) #twit data로 변경. 

    classifier = LogisticRegression()
    classifier.fit(X, y)

    with open(MODEL_FILE, 'wb') as model_file:
        pickle.dump(classifier, model_file)

    print("Model saved")

def load_model():

    with open(MODEL_FILE, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
        print("Model Loaded")

    return loaded_model


if __name__ == "__main__":
    clf = load_model()

    X, y = load_iris(return_X_y=True) # twit data 로 변경. 
    inputs = X[:, :]
    
    result = clf.predict(inputs)
    print("RESULT :", result)
