import React, { useState, useEffect, Fragment } from 'react';

const Dashboard = () => {
  const [workers, setWorkers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') === null) {
        console.log("This worked")
      window.location.replace('http://localhost:3000/login');
    } else {
        console.log("This worked: fetch")
      fetch('http://127.0.0.1:8000/workers/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(data => {
          console.log(data)
          setWorkers(data);
          setLoading(false);
        });
    }
  }, []);

  return (
    <div>
      {loading === false && (
        workers.length > 0 ? (
            workers.map(function(worker, index) {
              return (
                <div key={worker.id}>
                  <div>{worker.firstname}</div>
                  <div>{worker.lastname}</div>
                  <div>{worker.tck}</div>
                </div>
              
              )
              
            })
        ) : (
          <p>No access.</p>
        )
      )}
    </div>
  );
};

export default Dashboard;