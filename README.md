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

- **Frontend**: React, Vite  
- **Backend / ML**: Python, scikit-learn, pandas, numpy  
- **Visualization**: matplotlib / seaborn (optional)  
- **Version Control**: Git & GitHub

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

```bash
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

    Install dependencies:

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

    Small Dataset: The ML model is trained on a very limited dataset, which can reduce prediction accuracy.

    Simplified ML Model: Uses a lightweight model; advanced techniques like neural networks are not implemented.

    No Database Integration: All data runs locally; historical data cannot be stored or analyzed.

    Frontend-Backend Separation: The Python ML logic is separate from the React frontend; integration is basic.

    No User Authentication: Anyone can input data; there is no security or user management.

Future Improvements

    Larger Dataset: Incorporate more student data to improve model accuracy and reliability.

    Advanced ML Models: Explore neural networks or ensemble methods for better predictions.

    Database Integration: Store user inputs and predictions for historical analysis.

    Full Integration: Connect Python backend API with React frontend for seamless interaction.

    UI/UX Enhancements: Add charts, graphs, and responsive design for better visualization.

    Authentication & User Profiles: Allow users to save their data and track progress over time.

🤝 Contribution

This is an MVP project. Contributions are welcome to improve:

    UI/UX of the frontend

    ML model accuracy

    Charts, graphs, and visual analytics
