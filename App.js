import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [inputs, setInputs] = useState({
    age: '',
    hypertension: '',
    heart_disease: '',
    smoking_history: '',
    bmi: '',
    HbA1c_level: '',
    blood_glucose_level: ''
  });
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/react/', inputs);
      setResult(response.data.result);
      setError('');
    } catch (error) {
      console.error('Error:', error);
      setError('Failed to process data. Please try again.');
    }
  };

  return (
    <div className="container">
      <h2>Diabetes Prediction</h2>
      <h1>Input Form</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Age:
          <input type="number" name="age" value={inputs.age} onChange={handleChange} />
        </label>
        <br />
        <label>
          Hypertension:
          <input type="number" name="hypertension" value={inputs.hypertension} onChange={handleChange} />
        </label>
        <br />
        <label>
          Heart Disease:
          <input type="number" name="heart_disease" value={inputs.heart_disease} onChange={handleChange} />
        </label>
        <br />
        <label>
          Smoking History:
          <input type="number" name="smoking_history" value={inputs.smoking_history} onChange={handleChange} />
        </label>
        <br />
        <label>
          BMI:
          <input type="number" name="bmi" value={inputs.bmi} onChange={handleChange} />
        </label>
        <br />
        <label>
          HbA1c Level:
          <input type="number" name="HbA1c_level" value={inputs.HbA1c_level} onChange={handleChange} />
        </label>
        <br />
        <label>
          Blood Glucose Level:
          <input type="number" name="blood_glucose_level" value={inputs.blood_glucose_level} onChange={handleChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      {error && <p className="error">{error}</p>}
      <h2> Result</h2>
      <p>{result}</p>
    </div>
  );
};

export default App;
