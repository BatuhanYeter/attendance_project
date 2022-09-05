import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import { createTheme } from '@mui/material/styles';
import * as React from 'react';
import Chart from './Chart';
import InfoRight from './InfoRight';
import Workers from './Workers';

import { useEffect } from 'react';


const mdTheme = createTheme();

function DashboardContent() {
  
  useEffect(() => {
    var token = localStorage.getItem('token')
    if (token === null) {
      console.log("Token null: " + token)
      window.location.replace('http://localhost:3000/login');
    } else {
      console.log("Token is not null: " + token)
    }
  }, []);
  return (
      <Grid container spacing={3}>
        {/* Chart */}
        <Grid item xs={12} md={8} lg={9}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
              height: 240,
            }}
          >
            <Chart />
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={4} lg={3}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
              height: 240,
            }}
          >
            <InfoRight />
          </Paper>
        </Grid>
        
        <Grid item xs={12}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
            <Workers />
          </Paper>
        </Grid>
      </Grid>
            
  );
}

export default function Dashboard() {
  return <DashboardContent />;
}