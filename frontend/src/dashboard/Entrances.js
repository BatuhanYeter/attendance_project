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



export default function EntranceList(props) {
  const [entrances, setEntrances] = useState([]);
  const [loading, setLoading] = useState(true);

  const location = useLocation();

  const [workerId, setWorkerId] = useState(location.state.id)
  
  

  async function fetchData() {
    var token = localStorage.getItem('token')
    console.log("id: " + workerId)
    if (token === null) {
            console.log("token: "+ token)
            window.location.replace('http://localhost:3000/login');
        } else {
            console.log("trying to get: "+ workerId)
            await fetch(`http://127.0.0.1:8080/entrances/${workerId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token ${localStorage.getItem('token')}`
            }})
      .then(res => res.json())
      .then(data => {
        setEntrances(data);
        setLoading(false);
      });
    }}

  useEffect( ()  =>  {
    if(workerId) {
        fetchData()
    } else {
        window.location.replace('http://localhost:3000/workers');
    }
    
  }, []);
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell>Worker Id</StyledTableCell>
            <StyledTableCell align="right">Worker Full Name</StyledTableCell>
            <StyledTableCell align="right">Entrance Date</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {loading === false && (
        entrances.length > 0 ? (
            entrances.map(function(entrance, index) {
                var date = new Date(entrance.createddate)
                return (
                <StyledTableRow key={entrance.id}>
                    <StyledTableCell>{entrance.worker.id}</StyledTableCell>
                    <StyledTableCell align="right">{`${entrance.worker.firstname} ${entrance.worker.lastname}`}</StyledTableCell>
                    <StyledTableCell align="right">{date.toUTCString()}</StyledTableCell>
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
