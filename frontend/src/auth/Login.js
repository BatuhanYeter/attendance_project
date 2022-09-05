import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import { useEffect, useState } from 'react';

export default function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        var token = localStorage.getItem('token')
        if (token !== null) {
          window.location.replace('http://localhost:3000/');
        } else {
          setLoading(false);
        }
      }, []);

  
      const onSubmit = e => {
        e.preventDefault();
    
        const user = {
          username: username,
          password: password
        };
    
        fetch('http://127.0.0.1:8000/rest-auth/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(user)
        })
          .then(res => res.json())
          .then(data => {
            console.log(data.key)
            if (data.key) {
              localStorage.clear();
              localStorage.setItem('token', data.key);
              window.location.replace('http://localhost:3000/');
            } else {
              setUsername('');
              setPassword('');
              localStorage.clear();
            }
          });
      };
  
    if(loading === false) {
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
            Sign in
          </Typography>
          <Box component="form" onSubmit={onSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              fullWidth
              id="email"
              label="Name"
              autoComplete="email"
              autoFocus
              name='username'
              type='username'
              value={username}
              required
              onChange={e => setUsername(e.target.value)}
            />
            <TextField
              margin="normal"
              fullWidth
              label="Password"
              id="password"
              autoComplete="current-password"
              name='password'
              type='password'
              value={password}
              required
              onChange={e => setPassword(e.target.value)}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
          </Box>
        </Box>
        </Container>
      )
    } 
    
    return (
      <div>No access.</div>
    );
}