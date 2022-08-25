import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Title from './Title';

import { useState, useEffect } from 'react';

function preventDefault(event) {
  event.preventDefault();
}

export default function InfoRight() {
    const [workers, setWorkers] = useState([]);
    const date = new Date()
    const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

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
        //   setLoading(false);
        });
    }
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