import * as React from 'react';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useState, useEffect} from 'react';
import { useLocation } from "react-router-dom";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));



export default function DeletedWorkersList() {
  const [workers, setWorkers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  

  async function fetchData() {
    var token = localStorage.getItem('token')
    if (token === null) {
            console.log("token: "+ token)
            window.location.replace('http://localhost:3000/login');
        } else {
            await fetch(`http://127.0.0.1:8000/deleted-workers/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token ${localStorage.getItem('token')}`
            }})
      .then(res => res.json())
      .then(data => {
        setWorkers(data);
        setLoading(false);
      });
    }}

  useEffect( ()  =>  {
    fetchData()
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell>Worker's Old Id</StyledTableCell>
            <StyledTableCell>Full Name</StyledTableCell>
            <StyledTableCell>Deleted Date</StyledTableCell>
            <StyledTableCell>TCK</StyledTableCell>
            <StyledTableCell>Address</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {loading === false && (
        workers.length > 0 ? (
            workers.map(function(worker, index) {
                var date = new Date(worker.deletedate)
                console.log(worker)
                return (
                <StyledTableRow key={worker.id}>
                    <StyledTableCell>{worker.old_id}</StyledTableCell>
                    <StyledTableCell >{`${worker.firstname} ${worker.lastname}`}</StyledTableCell>
                    <StyledTableCell>{date.toUTCString()}</StyledTableCell>
                    <StyledTableCell>{worker.tck}</StyledTableCell>
                    <StyledTableCell>{worker.addressid.name}</StyledTableCell>
                </StyledTableRow>
                )})
            ) : (
            <StyledTableRow>
              <TableCell>No access.</TableCell>
            </StyledTableRow>
            ))}
        </TableBody>
      </Table>
    </TableContainer>
    
  );
}
