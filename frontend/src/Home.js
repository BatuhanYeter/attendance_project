import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useEffect } from 'react'
import jwtDecode from 'jwt-decode';

const Home = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    const [workers, setWorkers] = useState([]);
    const fetchWorkers = async () => {
        const response = await fetch('http://127.0.0.1:8000/workers/', {
          method: "GET",
          headers: {
            "Content-Type":"application/json",
            "Authorization": "Basic " + btoa(`${username}:${password}`)
          },
        })

        if (response.status === 200) {
            const data = await response.json()
            console.log(data)
            setUsername(localStorage.getItem("username"))
            setPassword(localStorage.getItem("password"))
            
            } else {
                alert("Something went wrong!")
            }
        }
    
  const navigate = useNavigate()


  useEffect(() => {
    console.log("usename: " + username)
    console.log("password: " + password)
    if (username === "") {
        // navigate("/login")
    } else {
        fetchWorkers()
    }
  }, [username])

  return (
    <div>

    {workers.length > 0 ? (
          workers.map(function(worker, index) {
            return (
              <div>
                <div>{worker.firstname}</div>
                <div>{worker.lastname}</div>
                <div>{worker.tck}</div>
              </div>
            
            )
            
          })
      ) : (
        <p>No access.</p>
      )}
      </div>
  )
}

export default Home