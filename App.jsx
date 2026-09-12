// App.jsx
import { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // URL pointing directly to the FastAPI local server
    fetch('http://localhost:8000/api/data')
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React Front-End</h1>
      <p>Backend says: <strong>{message}</strong></p>
    </div>
  );
}

export default App;