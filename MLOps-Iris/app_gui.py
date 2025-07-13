import streamlit as st
import requests

st.title("🌸 پیش‌بینی گل زنبق")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

if st.button("پیش‌بینی"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    res = requests.post("http://localhost:8000/predict", json=data)
    if res.status_code == 200:
        pred = res.json()["prediction"]
        label = ["Setosa", "Versicolor", "Virginica"][pred]
        st.success(f"🌼 گونه گل: {label}")
    else:
        st.error("❌ خطا در پیش‌بینی")
