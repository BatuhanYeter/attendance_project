
import './App.css';

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from './auth/Login';
import Logout from './auth/Logout';
import Dashboard from './dashboard/Dashboard';
import Register from './auth/Register';
import WorkerList from './dashboard/WorkerList';
import EntranceList from './dashboard/Entrances';

const App
 = () => {
  return (
    <Router>
      <Routes>
        {/* <Route component={Home} path="/" element={<Home/>} exact /> */}
        <Route component={Login} path="/login" element={<Login/>} />
        <Route component={Logout} path="/logout" element={<Logout/>} />
        <Route component={Register} path="/register" element={<Register/>} />
        <Route component={WorkerList} path="/workers" element={<WorkerList/>} />
        <Route component={EntranceList} path="/entrances" element={<EntranceList/>} />
        <Route component={Dashboard} path="/" element={<Dashboard/>} exact />
      </Routes>
    </Router>
  )
}

export default App
