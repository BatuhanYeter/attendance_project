
import './App.css';

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from './auth/Login';
import Logout from './auth/Logout';
import Dashboard from './dashboard/Dashboard';

const App
 = () => {
  return (
    <Router>
      <Routes>
        {/* <Route component={Home} path="/" element={<Home/>} exact /> */}
        <Route component={Login} path="/login" element={<Login/>} />
        <Route component={Login} path="/logout" element={<Logout/>} />
        <Route component={Dashboard} path="/" element={<Dashboard/>} exact />
      </Routes>
    </Router>
  )
}

export default App
