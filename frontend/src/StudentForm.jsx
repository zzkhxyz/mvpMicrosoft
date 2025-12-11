import React, { useState } from "react";

const inputStyle = {
  width: "100%",
  padding: "8px 12px",
  border: "1px solid #d0d7de",
  borderRadius: 6,
  fontSize: 16,
  background: "#f6f8fa",
  marginBottom: 16,
  color: "#24292f"
};
const labelStyle = {
  fontWeight: 500,
  marginBottom: 4,
  color: "#24292f",
  fontSize: 15
};
const buttonStyle = {
  width: "100%",
  padding: "10px 0",
  background: "#2da44e",
  color: "#fff",
  border: "none",
  borderRadius: 6,
  fontWeight: 600,
  fontSize: 16,
  cursor: "pointer",
  marginTop: 8,
  boxShadow: "0 1px 4px rgba(27,31,35,0.04)"
};

const StudentForm = ({ onPredict, loading, result }) => {
  const [hours, setHours] = useState(5);
  const [practice, setPractice] = useState(20);
  const [teamwork, setTeamwork] = useState(10);
  const [midterm, setMidterm] = useState(30);

  const handleSubmit = (e) => {
    e.preventDefault();
    onPredict({ hours, practice, teamwork, midterm });
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: 8 }}>
      <div>
        <label style={labelStyle}>Часы учебы за день (0–24)</label>
        <input style={inputStyle} type="number" min={0} max={24} value={hours} onChange={e => setHours(Number(e.target.value))} required />
      </div>
      <div>
        <label style={labelStyle}>Оценка за практику (0–100)</label>
        <input style={inputStyle} type="number" min={0} max={100} value={practice} onChange={e => setPractice(Number(e.target.value))} required />
      </div>
      <div>
        <label style={labelStyle}>Оценка за командную работу (0–100)</label>
        <input style={inputStyle} type="number" min={0} max={100} value={teamwork} onChange={e => setTeamwork(Number(e.target.value))} required />
      </div>
      <div>
        <label style={labelStyle}>Оценка за промежуточный экзамен (0–100)</label>
        <input style={inputStyle} type="number" min={0} max={100} value={midterm} onChange={e => setMidterm(Number(e.target.value))} required />
      </div>
      <button style={buttonStyle} type="submit" disabled={loading}>
        {loading ? "Предсказание..." : "🔮 Предсказать итоговый балл"}
      </button>
      {result && (
        <div style={{ marginTop: 18, color: "#0969da", fontSize: 17, textAlign: "center" }}>
          Ожидаемый итоговый балл студента: <b>{result}</b> из 100
        </div>
      )}
    </form>
  );
};

export default StudentForm;
