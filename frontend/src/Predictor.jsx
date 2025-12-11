import React, { useState } from "react";
import axios from "axios";
import "./Predictor.css";

const Predictor = () => {
  const [hours, setHours] = useState(5);
  const [practice, setPractice] = useState(2);
  const [teamwork, setTeamwork] = useState(1);
  const [midterm, setMidterm] = useState(3);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/predict", {
        hours,
        practice,
        teamwork,
        midterm
      });
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
      alert("Ошибка при предсказании!");
    }
    setLoading(false);
  };

  return (
    <div className="predictor-container">
      <h1>Student Final Exam Predictor</h1>
      <div className="input-group">
        <label>Hours of Study</label>
        <input type="number" value={hours} onChange={e => setHours(parseFloat(e.target.value))} min="0" max="24" />
      </div>
      <div className="input-group">
        <label>Practice Score</label>
        <input type="number" value={practice} onChange={e => setPractice(parseFloat(e.target.value))} min="0" max="100" step="0.1" />
      </div>
      <div className="input-group">
        <label>Team Work Score</label>
        <input type="number" value={teamwork} onChange={e => setTeamwork(parseFloat(e.target.value))} min="0" max="100" step="0.1" />
      </div>
      <div className="input-group">
        <label>Mid-Term Score</label>
        <input type="number" value={midterm} onChange={e => setMidterm(parseFloat(e.target.value))} min="0" max="100" step="0.1" />
      </div>
      <button className="predict-btn" onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict Final Exam"}
      </button>
      {prediction !== null && (
        <div className="result-card">
          <h2>Predicted Final Exam Score</h2>
          <p>{prediction.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
};

export default Predictor;
