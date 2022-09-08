import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import * as React from 'react';
import Chart from './Chart';
import InfoRight from './InfoRight';
import Workers from './Workers';

import { useEffect, useState } from 'react';
// Generate Sales Data
function createData(time, amount) {
  return { time, amount };
}
function DashboardContent() {
  let [morningShift, setMorningShiftEntrances] = useState(0);
  let [eveningShift, setEveningShiftEntrances] = useState(0);
  let [nightShift, setNightShiftEntrances] = useState(0);
  let [chartData, setChartData] = useState([]);
  useEffect(() => {
    async function fetchChartData() {
      await fetch('http://127.0.0.1:8080/entrances/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    }) 
      .then(res => res.json())
      .then(data => {
        var shiftMor = 0;
        var shiftEve = 0;
        var shiftNig = 0;
  
        var midday = 0;
        var evening = 0;
  
        
        data.map(function(entrance, index) {
          const date = new Date(entrance.createddate).getUTCHours()
          
          console.log(index + "------->" + date)
          if (date >= 7 && date <= 9) {
              shiftMor += 1;
          } else if (date >= 9 && date <= 16) {
              midday += 1;
          } else if (date >= 16 && date <= 18) {
              shiftEve += 1;
          } else if (date >= 18 && date <= 23) {
              evening += 1;
          } else {
              shiftNig += 1;
          }
          console.log("mrng shift: "+ shiftMor)
          // {format(new Date(entrance.createddate), 'dd/MM/yyyy')}
        })
        async function setAll() {
          setMorningShiftEntrances(shiftMor)
          setEveningShiftEntrances(shiftEve)
          setNightShiftEntrances(shiftNig)
        }
        
        setAll()

        const cntShiftToChart = [ 
          createData('00:00 - 07:00', 0),
          createData('07:00 - 09:00', morningShift),
          createData('09:00 - 16:00', midday),
          createData('16:00 - 18:00', eveningShift),
          createData('18:00 - 23:00', evening),
          createData('23:00 - 24:00', nightShift),
        ];
        console.log(cntShiftToChart[1])
        setChartData(cntShiftToChart)
      });
    }


    var token = localStorage.getItem('token')
    if (token.length === 0) {
      console.log("Token null: " + token)
      window.location.replace('http://localhost:3000/login');
    } else {
      console.log("Token is not null: " + token)
      fetchChartData()
      console.log("---===" + chartData[1])
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
             {chartData.length > 0 && (
            <Chart chartData={chartData} />)}
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