
import './App.css';

import React, { useEffect, useState } from 'react'

import { BrowserRouter as Router, Route, Routes, useNavigate } from "react-router-dom";
import Login from './Login';
import Home from './Home';

const App
 = () => {
  return (
    <Router>
      <Routes>
        <Route component={Login} path="/login" element={<Login/>} />
        <Route component={Home} path="/" element={<Home/>} exact />
      </Routes>
    </Router>
  )
}

export default App
