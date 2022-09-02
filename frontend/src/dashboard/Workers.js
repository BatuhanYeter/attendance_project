import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';

import { useState, useEffect} from 'react';



function preventDefault(event) {
  event.preventDefault();
}



export default function Workers() {
  const [workers, setWorkers] = useState([]);
  const [entrances, setEntrances] = useState([]);
  const [loading, setLoading] = useState(true);
  async function fetchData() {
    await fetch('http://127.0.0.1:8000/workers/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    })
      .then(res => res.json())
      .then(data => {
        setWorkers(data);
        setLoading(false);
      });

      fetch('http://127.0.0.1:8000/entrances/', {
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
        setLoading(false);
      });
  }
  useEffect( ()  =>  {
    fetchData()
  }, []);

  

  return (
    <React.Fragment>
      <Title>Workers</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            {/* <TableCell>Start Date</TableCell> */}
            <TableCell>Name</TableCell>
            <TableCell>Last Name</TableCell>
            <TableCell>TCK</TableCell>
            <TableCell align="right">Age</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {loading === false && (
        workers.length > 0 ? (
            workers.map(function(worker, index) {
              return (
            <TableRow key={worker.id}>
              {/* {worker.createddate !== null ? (
                <TableCell>{format(new Date(worker.createddate), 'dd/MM/yyyy')}</TableCell>
              ): (
                <TableCell>Unknown</TableCell>
              )} */}
              <TableCell>{worker.firstname}</TableCell>
              <TableCell>{worker.lastname}</TableCell>
              <TableCell>{worker.tck}</TableCell>
              <TableCell align="right">{`${worker.age}`}</TableCell>
            </TableRow>
              )})
        ) : (
          <div>No access.</div>
        )


      )}
        </TableBody>
      </Table>
      <Title>Entrances</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Worker Id</TableCell>
            <TableCell>Worker Fullname</TableCell>
            <TableCell>Entrance Date</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {loading === false && (
        entrances.length > 0 ? (
            entrances.map(function(entrance, index) {
              var date = new Date(entrance.createddate)
              return (
            <TableRow key={entrance.id}>
              <TableCell>{entrance.worker.id}</TableCell>
              <TableCell>{`${entrance.worker.firstname} ${entrance.worker.lastname}`}</TableCell>
              {/* <TableCell>{format(date , 'dd/MM/yyyy HH:mm')}</TableCell> */}
              <TableCell>{date.toUTCString()}</TableCell>
            </TableRow>
              )})
        ) : (
          <TableRow>
              <TableCell>No access.</TableCell>
          </TableRow>
        )


      )}
        </TableBody>
      </Table>
      <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        See the entrances
      </Link>
    </React.Fragment>
  );
}