import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [result, setResult] = useState(null);

  const handleDemo = async () => {
    const response = await fetch('/api/demo');
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="App">
      <header className="header">
        <h1>Zorgstart Demo</h1>
        <p>Van ontslag naar levenslang thuis blijven</p>
      </header>
      <main className="main">
        <div className="card">
          <h2>Architectuur</h2>
          <ul>
            <li>Backend: FastAPI (Python)</li>
            <li>Frontend: React + TypeScript + Vite</li>
          </ul>
          <button onClick={handleDemo}>Test Demo</button>
          {result && (
            <div className="result">
              <pre>{JSON.stringify(result, null, 2)}</pre>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
