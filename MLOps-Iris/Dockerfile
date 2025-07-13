FROM python:3.10

WORKDIR /app

COPY ./App ./App
COPY requirements.txt .
COPY App/model.joblib /app/App  

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]




