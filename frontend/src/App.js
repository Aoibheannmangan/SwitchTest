import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [form, setForm] = useState({ en_volume: "", dol: "", weight: ""});
  const [result, setResult] = useState(null);

  const handleFormChange = (e) => {
    setForm({...form, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://127.0.0.1:5000/calculate',
      {
        en_volume: Number(form.en_volume),
        dol: Number(form.dol),
        weight: parseFloat(form.weight)
      });
    setResult(res.data);
  };
  return(
    <div className='App'>
      <h2>SPN Calculator</h2>
      <div className="calculator-container">
        <div className="form-wrapper">
          <div className="calculator-card">
            <form onSubmit={handleSubmit}>
              <div className='input-group'>
                <label>EN Volume: </label>
                <input
                  name="en_volume"
                  type="number"
                  value={form.en_volume}
                  onChange={handleFormChange}
                  placeholder='EN Volume (mL)'
                />
              </div>
              <div className='input-group'>
                <label>Day of Life: </label>
                <input
                  name="dol"
                  type="number"
                  value={form.dol}
                  onChange={handleFormChange}
                  placeholder='Day of Life (Days)'
                />
              </div>
              <div className='input-group'>
                <label>Weight: </label>
                <input 
                  name="weight"
                  type="number"
                  value={form.weight}
                  onChange={handleFormChange}
                  placeholder='Weight (kg)'
                />
              </div>
              <button type="submit" className="calculate-button">Calculate</button>
            </form>
            {result && (
              <div>
                {"message" in result ? (
                  <h3>{result.message}</h3>
                ) : (
                  <>
                    <p><strong>CSPN Type:</strong> {result.cspn_type}</p>
                    <p><strong>Aqueous Volume: </strong> {result.target_a} mL (min: {result.min_a}, max: {result.max_a} )</p>
                    <p><strong>Lipid Volume: </strong>{result.target_l}</p>
                    <p><strong>Total SPN Volume: </strong>{result.target_total}</p>
                  </>
                )}
              </div>
            )}
            <p className="warning-text">Aim to provide target SPN volumes. Min SPN volumes meet lower end of nutrition recommendations. Do not exceed max SPN volumes.</p>
          </div>
          </div>
        </div>
      </div>
  )
};


