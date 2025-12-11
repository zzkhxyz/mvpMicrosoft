import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import streamlit as st

# Установить светлую тему
st.set_page_config(page_title="Student Final Exam Predictor", page_icon="📊", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #f3f6fb;
    }
    .stButton>button {
        background-color: #0078d4;
        color: white;
        border-radius: 6px;
        font-size: 16px;
        padding: 8px 16px;
        border: none;
    }
    .stTextInput>div>input, .stNumberInput>div>input {
        background-color: #fff;
        border: 1px solid #c7e0f4;
        border-radius: 6px;
        font-size: 16px;
        padding: 6px 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Student Final Exam Predictor")
st.write("""
Добро пожаловать! Этот сервис поможет вам предсказать итоговый балл студента за экзамен на основе его активности и промежуточных результатов. Просто заполните форму ниже и нажмите кнопку — результат появится сразу!
""")

st.header("Введите данные студента:")
hours = st.number_input(
    "Часы учебы за день (0–24)", min_value=0.0, max_value=24.0, value=5.0, help="Сколько часов студент занимается в день?"
)
practice = st.number_input(
    "Оценка за практику (0–100)", min_value=0.0, max_value=100.0, value=20.0, help="Суммарный балл за практические задания."
)
teamwork = st.number_input(
    "Оценка за командную работу (0–100)", min_value=0.0, max_value=100.0, value=10.0, help="Суммарный балл за работу в команде."
)
midterm = st.number_input(
    "Оценка за промежуточный экзамен (0–100)", min_value=0.0, max_value=100.0, value=30.0, help="Баллы за midterm экзамен."
)

df = pd.read_csv("Student_Grades_clean.csv")  
X = df[['Hours', 'Practice', 'TeamWork', 'MidTerm']].copy()
# X['Hours'] не масштабируем
X['Practice'] = X['Practice'] * 10  # если максимум 10
X['TeamWork'] = X['TeamWork'] * 10  # если максимум 10
X['MidTerm'] = X['MidTerm'] * 10  # если максимум 10
y = df['FinalExam'] * 10  # переводим в шкалу 0-100

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

st.header("Результат предсказания:")
st.write(f"Среднеквадратичная ошибка модели: **{mse:.2f}** (чем меньше, тем лучше)")

if st.button("🔮 Предсказать итоговый балл"):
    prediction = model.predict([[hours, practice, teamwork, midterm]])[0]
    st.success(f"Ожидаемый итоговый балл студента: **{prediction:.2f}** из 100")
    st.info("Результат основан на данных прошлых студентов и может отличаться от реального.")
