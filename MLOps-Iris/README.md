# 🌿 MLOps Iris Classifier

This is a complete MLOps project for classifying Iris flowers using a machine learning model. The project includes model training, REST API (FastAPI), GUI with Streamlit, and deployment using Docker.

---

## 📌 Project Features

- Trains a `RandomForestClassifier` on the classic Iris dataset
- Saves the model using `.joblib`
- FastAPI backend for predictions (`/predict` endpoint)
- Streamlit-based user interface
- Dockerized for portability and deployment

---

## 🧠 Dataset Information

The dataset used is the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris), which contains 150 samples of iris flowers from three different species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

Each sample includes:
- Sepal length
- Sepal width
- Petal length
- Petal width

