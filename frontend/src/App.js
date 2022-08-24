
import './App.css';

import React, { useEffect, useState } from 'react'

import { BrowserRouter as Router, Route, Routes, useNavigate } from "react-router-dom";
import Login from './Login';
import Home from './Home';
import Navbar from './Navbar';
import Logout from './Logout';
import Dashboard from './Dashboard';
const App
 = () => {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route component={Home} path="/" element={<Home/>} exact />
        <Route component={Login} path="/login" element={<Login/>} />
        <Route component={Login} path="/logout" element={<Logout/>} />
        <Route component={Dashboard} path="/dashboard" element={<Dashboard/>} />
      </Routes>
    </Router>
  )
}

export default App
