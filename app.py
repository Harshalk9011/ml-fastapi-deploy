from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = FastAPI(title="Iris Flower Classifier API")

# Load and train model
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)
class_names = iris.target_names.tolist()

# Input validation with ranges (based on iris dataset stats)
class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, lt=10)
    sepal_width: float = Field(..., gt=0, lt=10)
    petal_length: float = Field(..., gt=0, lt=10)
    petal_width: float = Field(..., gt=0, lt=10)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Flower Classification API!"}

@app.post("/predict")
def predict_species(data: IrisInput):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)[0]
    predicted_class = class_names[prediction]
    return {
        "prediction": int(prediction),
        "species": predicted_class
    }
