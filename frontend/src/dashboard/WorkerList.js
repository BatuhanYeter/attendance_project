import * as React from 'react';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';
import { useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom"

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

export default function WorkerList() {
  const [workers, setWorkers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [id, setId] = useState();
  const navigate = useNavigate();

  async function fetchData() {
    var token = localStorage.getItem('token')
        if (token === null || token.length === 0) {
            console.log("token: "+ token)
            window.location.replace('http://localhost:3000/login');
        } else {
        await fetch('http://127.0.0.1:8000/workers/', {
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

  const onClickHandle = () => {
    window.location.replace('http://localhost:3000/entrance');
  }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell>Workers</StyledTableCell>
            <StyledTableCell align="right">Name</StyledTableCell>
            <StyledTableCell align="right">Last Name</StyledTableCell>
            <StyledTableCell align="right">TCK</StyledTableCell>
            <StyledTableCell align="right">Age</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {loading === false && (
        workers.length > 0 ? (
            workers.map(function(worker, index) {
                return (
                <StyledTableRow key={worker.id}>
                    <StyledTableCell padding="checkbox">
                    <Checkbox
                        color="primary"
                        // indeterminate={numSelected > 0 && numSelected < rowCount}
                        // checked={rowCount > 0 && numSelected === rowCount}
                        // onChange={onSelectAllClick}
                        inputProps={{
                        'aria-label': 'select all',
                        }}
                    />
                    </StyledTableCell>
                    {/* <StyledTableCell component="th" scope="row">
                        {worker.firstname} 
                    </StyledTableCell> */}
                    <StyledTableCell align="right">{worker.firstname}</StyledTableCell>
                    <StyledTableCell align="right">{worker.lastname}</StyledTableCell>
                    <StyledTableCell align="right">{worker.tck}</StyledTableCell>
                    <StyledTableCell align="right">{worker.age}</StyledTableCell>
                </StyledTableRow>
                )})
            ) : (
            <StyledTableRow>
              <TableCell>No access.</TableCell>
            </StyledTableRow>
            ))}
        </TableBody>
      </Table>
      
      <Button
            onClick={()=>navigate("/entrances", {state:{id: 20, title:"aaa"}})}
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            >
            Get Entrances
      </Button>
    </TableContainer>
    
  );
}
