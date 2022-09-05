import { useTheme } from '@mui/material/styles';
import * as React from 'react';
import { Label, Line, LineChart, ResponsiveContainer, XAxis, YAxis } from 'recharts';
import Title from './Title';

import { useEffect, useState } from 'react';

// Generate Sales Data
function createData(time, amount) {
  return { time, amount };
}




export default function Chart() {
  const theme = useTheme();
  const [entrances, setEntrances] = useState([]);
  const [morningShift, setMorningShiftEntrances] = useState(0);
  const [eveningShift, setEveningShiftEntrances] = useState(0);
  const [nightShift, setNightShiftEntrances] = useState(0);
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);

async function fetchData() {
  await fetch('http://127.0.0.1:8000/entrances/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${localStorage.getItem('token')}`
    }
  })
    .then(res => res.json())
    .then(data => {
      // console.log(data)
      setEntrances(data);
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
        
        // {format(new Date(entrance.createddate), 'dd/MM/yyyy')}
      })
      setMorningShiftEntrances(shiftMor)
      setEveningShiftEntrances(shiftEve)
      setNightShiftEntrances(shiftNig)
      
      const cntShiftToChart = [ 
        createData('00:00 - 07:00', 0),
        createData('07:00 - 09:00', morningShift),
        createData('09:00 - 16:00', midday),
        createData('16:00 - 18:00', eveningShift),
        createData('18:00 - 23:00', evening),
        createData('23:00 - 24:00', nightShift),
      ];
      setChartData(cntShiftToChart)
      setLoading(false)
    });
}

useEffect(() => {
  if (localStorage.getItem('token') === null) {
    // console.log("This worked")
    window.location.replace('http://localhost:3000/login');
  } else {
      // console.log("This worked: fetch")
      fetchData()
      console.log(chartData)
  }
}, []);

  return (
    <React.Fragment>
      <Title>Today</Title>
      {loading === false && (
      <ResponsiveContainer>
          <LineChart
          data={chartData}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <XAxis
            dataKey="time"
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          />
          <YAxis
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          >
            <Label
              angle={270}
              position="left"
              style={{
                textAnchor: 'middle',
                fill: theme.palette.text.primary,
                ...theme.typography.body1,
              }}
            >
              Number of Workers
            </Label>
          </YAxis>
          <Line
            isAnimationActive={false}
            type="monotone"
            dataKey="amount"
            stroke={theme.palette.primary.main}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
      )}
    </React.Fragment>
  );
}