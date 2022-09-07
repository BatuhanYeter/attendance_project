import { useTheme } from '@mui/material/styles';
import * as React from 'react';
import { Label, Line, LineChart, ResponsiveContainer, XAxis, YAxis } from 'recharts';
import Title from './Title';

import { useEffect, useState } from 'react';



export default function Chart(props) {
  const theme = useTheme();
  let [chartData, setChartData] = useState([])
  
  
  useEffect(() => {
    const fetchData = async () => {
      console.log("fetched data: ", props.chartData)
      let data = await props.chartData
      console.log("let data: ", data)
      setChartData(data)
      console.log("chart data: ", chartData)
    }

    fetchData()
  }, [chartData]);

  console.log(chartData)
  return (
    <React.Fragment>
      <Title>Today</Title>
      {/* {chartData.length > 0 && ( */}
      <ResponsiveContainer>
      {/* {chartData.length > 0 && ( */}
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
        {/* )} */}
      </ResponsiveContainer>
    </React.Fragment>
  );
}