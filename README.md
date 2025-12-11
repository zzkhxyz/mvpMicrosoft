# CRM & Student Score Prediction MVP

![Project Banner](https://via.placeholder.com/800x200.png?text=CRM+MVP)

## 🚀 Project Overview

This project is a **Minimum Viable Product (MVP)** developed for the **Microsoft Imagine Cup 2026**.  
It combines a **React frontend** and a **Python ML model** to predict students' final exam scores based on study habits and performance factors.

The goal is to provide a **simple, interactive tool** for students and educators to visualize how study time, practice, teamwork, and mid-term results affect final scores.

---

## ✨ Features

- **Student Score Prediction**: Lightweight ML model predicts final exam scores.  
- **Interactive Frontend**: Users input study hours, practice, teamwork, and mid-term scores to get predictions instantly.  
- **No Database Needed**: All data runs locally — simple setup.  
- **Educational Insights**: Helps understand which factors impact performance the most.

---

## 🛠 Technologies Used

- Frontend: React, Vite  
- Backend / ML: Python, scikit-learn, pandas, numpy  
- Visualization: matplotlib / seaborn (optional)  
- Version Control: Git & GitHub

---

## 📂 Project Structure

crmformvp/
│
├─ src/ # React frontend components
│ ├─ App.jsx
│ └─ main.jsx
│
├─ index.html # Main HTML page
├─ package.json # Frontend dependencies & scripts
├─ requirements.txt # Python dependencies
├─ model.py # ML model logic
└─ README.md # Project documentation


---

## ⚡ Getting Started

### Frontend (React)

1. Install dependencies:

    bash
npm install

    Run development server:

npm run dev

Open in browser:

http://localhost:5173/

Backend / ML (Python)

Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

    install dependencies:

pip install -r requirements.txt

    Run the Python script:

python model.py

🎮 How to Use

    Open the frontend in your browser.

    Enter Hours of Study, Practice, Teamwork, Mid-term Score, etc.

    Click Predict to see the estimated final score.

    Use the insights to improve study strategies.

⚠️ Limitations & Future Improvements
Current Limitations

    Small dataset reduces model accuracy.

    Lightweight ML model; no neural networks.

    No database — data is not stored.

    Python backend and React frontend are loosely integrated.

    No user authentication or profiles.

Future Improvements

    Expand dataset for better predictions.

    Implement advanced ML models (neural networks, ensemble methods).

    Add database integration to store historical data.

    Fully integrate backend and frontend via API.

    Improve UI/UX with charts, graphs, and responsive design.

    Add authentication and user profiles.

🤝 Contribution

This is an MVP project. Contributions are welcome to improve:

    UI/UX of the frontend

    ML model accuracy

    Visualization and analytics
