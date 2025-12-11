from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = FastAPI()

# Разрешить запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    hours: float
    practice: float
    teamwork: float
    midterm: float

# Загружаем и обучаем модель один раз при старте
csv_path = "Student_Grades_clean.csv"
df = pd.read_csv(csv_path)
X = df[['Hours', 'Practice', 'TeamWork', 'MidTerm']].copy()
# 'Hours' не масштабируем, остальные переводим в 0-100
X['Practice'] = X['Practice'] * 10
X['TeamWork'] = X['TeamWork'] * 10
X['MidTerm'] = X['MidTerm'] * 10
y = df['FinalExam'] * 10
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

@app.post("/predict")
def predict(data: StudentData):
    features = [[data.hours, data.practice, data.teamwork, data.midterm]]
    prediction = model.predict(features)[0]
    return {"prediction": round(prediction, 2)}
