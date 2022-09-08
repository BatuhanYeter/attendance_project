import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Title from './Title';

import { useState, useEffect } from 'react';

function preventDefault(event) {
  event.preventDefault();
  window.location.replace('http://localhost:3000/workers')
}

export default function InfoRight() {
    const [workers, setWorkers] = useState([]);
    const date = new Date()
    const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

useEffect(() => {
    fetch('http://127.0.0.1:8080/workers/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    })
      .then(res => res.json())
      .then(data => {
        // console.log(data)
        setWorkers(data);
      
      });
  }, []);
  return (
    <React.Fragment>
      <Title>Recent Workers</Title>
      <Typography component="p" variant="h4">
        {workers.length}
      </Typography>
      <Typography color="text.secondary" sx={{ flex: 1 }}>
        {date.getDate()} {monthNames[date.getMonth()]} {date.getFullYear()}
      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          View Workers
        </Link>
      </div>
    </React.Fragment>
  );
}