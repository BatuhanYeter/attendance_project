import React from 'react'
import jwt_decode from "jwt-decode";
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    const navigate = useNavigate()

    const loginAdmin = async (username, password) => {
        const response = await fetch("http://127.0.0.1:8000/workers/", 
        {
          method: "GET",
          headers: {
            "Content-Type":"application/json",
            "Authorization": "Basic " + btoa(`${username}:${password}`)
          },
        }) 
        const data = await response.json()
        if (response.status === 200) {
            
            console.log(data)
            localStorage.setItem("username", username)
            localStorage.setItem("password", password)
            // setToken(jwt_decode(data.access))
            
            navigate("/")
        } else {
            alert("Something went wrong!")
        }
    }
    const handleSubmit = (event) => {
        event.preventDefault();
        loginAdmin(username, password)
      }

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <label>Username:
            <input 
                type="text" 
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            </label>
            <label>Password:
            <input 
                type="password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            </label>
            <input type="submit" />
        </form>
    </div>
  )
}

export default Login