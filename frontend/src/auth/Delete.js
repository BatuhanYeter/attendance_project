import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { useState, useEffect } from 'react';

export default function Delete() {
    useEffect(() => {
        // if(errors !== "") console.log(errors)

        var token = localStorage.getItem('token')
        if (token === null || token.length === 0) {
            console.log("token: "+ token)
            window.location.replace('http://localhost:3000/login');
        } 
    }, [])
    const [workerId, setWorkerId] = useState(null)
    
    const handleChange = (e) => {
        setWorkerId(e.target.value);
    };
    

    const handleSubmit = async (e) => {
        if(workerId !== null) {
            await fetch(`http://127.0.0.1:8000/workers/${workerId}/`, {
                method: 'DELETE',
                headers: {
                  Authorization: `Token ${localStorage.getItem('token')}`
                }
              })
              .then((res) => {
                if(res.status === 301) {
                    alert("Delete success!")
                    window.location.replace('http://localhost:3000/');
                }
              })
              .catch((err) => alert(err));
        } else {
            alert("Please enter an ID!")
        }
    } 
        
    
  return (
      <Container component="main" maxWidth="md">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Delete A Worker
          </Typography>
          <Box component="form" noValidate onSubmit={(e) => handleSubmit(e)} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  onChange={(e) => {
                    handleChange(e);
                }}
                  value={workerId}
                  name="workerId"
                  required
                  fullWidth
                  id="workerId"
                  label="Worker ID"
                  autoFocus
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Delete
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/" variant="body2">
                  Return to Dashboard
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        
      </Container>
  );
}