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
import { createTheme } from '@mui/material/styles';
import { useState, useEffect } from 'react';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';


const theme = createTheme();

export default function Register() {
    useEffect(() => {
        // if(errors !== "") console.log(errors)

        var token = localStorage.getItem('token')
        if (token === null || token.length === 0) {
            console.log("token: "+ token)
            window.location.replace('http://localhost:3000/login');
        } else {
            console.log("token: "+ token)
            fetch('http://127.0.0.1:8000/address/', {
                method: 'GET',
                headers: {
                  'Content-Type': 'application/json',
                }
              })
                .then(res => res.json())
                .then(data => {
                    setAddressData(data)
                });
        }
    }, [])
    const [errors, setErrors] = useState("")
    const [addressData, setAddressData] = useState([])
    const [selectedAddress, setSelectedAddress] = useState("")
    const [selectedImage, setSelectedImage] = useState(null);
    const [data, setWorkerData] = useState({
        firstname: "",
        lastname: "",
        age: "",
        address: 1,
        tck: "",
        email: "",
        phonenumber: "",
        photourl: ""
    });
    function createMyModelEntry (data) {
        var form_data = new FormData();
        console.log("address"+ data.address)
        for(const name in data) {
            console.log(name+" "+data[name])
            form_data.append(name, data[name]);
          }
        form_data.append("address", selectedAddress)
        return form_data
    };
    const handleChange = ({ currentTarget: input }) => {
        var newData = { ...data };
        newData[input.name] = input.value;
        setWorkerData(newData);
    };
    
    const handleImageChange = (e) => {
        var newData = { ...data };
        newData["photourl"] = e.target.files[0];
        setWorkerData(newData);
    };

    const handleAddressChange = (event) => {
        console.log("changed to: " + event.target.value)
        setSelectedAddress(event.target.value)
        data["address"] = event.target.value
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        var form_data = createMyModelEntry(data)
        // console.log("url" + form_data.get("photourl"))
        await fetch('http://127.0.0.1:8000/workers/', {
            method: 'POST',
            headers: {
              Authorization: `Token ${localStorage.getItem('token')}`
            },
            body: form_data
          })
          .then((res) => {
            if(res.status === 201) {
                alert("Register success!")
                window.location.replace('http://localhost:3000/');
            }
          })
          .catch((err) => alert(err));
        };
    
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
            Register New Worker
          </Typography>
          <Box component="form" noValidate onSubmit={(e) => handleSubmit(e)} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  onChange={(e) => {
                    handleChange(e);
                }}
                  autoComplete="given-name"
                  value={data.firstname}
                  name="firstname"
                  required
                  fullWidth
                  id="firstName"
                  label="First Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  onChange={(e) => {
                    handleChange(e);
                }}
                  required
                  fullWidth
                  value={data.lastname}
                  id="lastname"
                  label="Last Name"
                  name="lastname"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  onChange={(e) => {
                    handleChange(e);
                }}
                  id="email"
                  value={data.email}
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  onChange={(e) => {
                    handleChange(e);
                }}
                  fullWidth
                  value={data.tck}
                  name="tck"
                  label="TCK"
                  id="tck"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  onChange={(e) => {
                    handleChange(e);
                }}
                  fullWidth
                  value={data.age}
                  name="age"
                  label="Age"
                  id="age"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  value={data.phonenumber}
                  onChange={(e) => {
                    handleChange(e);
                }}
                  fullWidth
                  name="phonenumber"
                  label="Phone Number"
                  id="phone"
                />
              </Grid>
              <Grid item xs={12}>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                onChange={handleAddressChange}
                value={selectedAddress}
                name="address"
                autoWidth
                label="Address"
                >
                {addressData.length > 0 ? (
                    addressData.map(function(address, index) {
                    return (    
                        <MenuItem key={index} value={address.id}>{address.name}</MenuItem>
                    )}))
                    : (
                <MenuItem key={"def"} value=""><em>None</em></MenuItem>
                  )}
                </Select>
              </Grid>
              <Grid item xs={12}>
              {selectedImage && (
                    <div>
                    <img alt="not fount" width={"250px"} src={URL.createObjectURL(selectedImage)} />
                    <br />
                    <button onClick={(e) => {
                            handleImageChange(e);
                        }}>Remove</button>
                    </div>
                )}
                <br />
                
                <br /> 
                <input
                    type="file"
                    name="photourl"
                    onChange={(e) => {
                        handleImageChange(e);
                        setSelectedImage(e.target.files[0])
                    }}
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Register
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