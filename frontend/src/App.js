
import './App.css';

import React, { useEffect, useState } from 'react'

const App
 = () => {
  const [workers, setWorkers] = useState([]);
  const [errors, setErrors] = useState("");

  useEffect(() => {
    const fetchWorkers = () => {
      fetch('http://127.0.0.1:8000/workers/')
      .then(response => response.json())
      .then(data => 
        setWorkers(data)
      )
    }
    fetchWorkers();
  }, [])
  
  return (
    <div>
        {workers.map(function(worker, index) {
          return (
            <div>
              <div>{worker.firstname}</div>
              <div>{worker.lastname}</div>
              <div>{worker.tck}</div>
            </div>
          
          )
          
        })}
    </div>
  )
}

export default App
