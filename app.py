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
class IrisInput(BaseModel)
