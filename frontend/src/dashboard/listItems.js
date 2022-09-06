import AssignmentIcon from '@mui/icons-material/Assignment';
import BarChartIcon from '@mui/icons-material/BarChart';
import DashboardIcon from '@mui/icons-material/Dashboard';
import LogoutIcon from '@mui/icons-material/Logout';
import PeopleIcon from '@mui/icons-material/People';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import PersonRemoveIcon from '@mui/icons-material/PersonRemove';
import * as React from 'react';


export const mainListItems = (
  <React.Fragment>
    <ListItemButton onClick={() => window.location.replace('http://localhost:3000/')}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </ListItemButton>
    <ListItemButton onClick={() => window.location.replace('http://localhost:3000/register')}>
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Add Worker" />
    </ListItemButton>
    <ListItemButton onClick={() => window.location.replace('http://localhost:3000/delete')}>
      <ListItemIcon>
        <PersonRemoveIcon />
      </ListItemIcon>
      <ListItemText primary="Delete A Worker" />
    </ListItemButton>
    <ListItemButton onClick={() => window.location.replace('http://localhost:3000/workers')}>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <ListItemText primary="Workers" />
    </ListItemButton>
    <ListItemButton onClick={() => window.location.replace('http://localhost:3000/logout')}>
      <ListItemIcon>
        <LogoutIcon />
      </ListItemIcon>
      <ListItemText primary="Sign Out" />
    </ListItemButton>
  </React.Fragment>
);

export const secondaryListItems = (
  <React.Fragment>
    <ListSubheader component="div" inset>
      Extract Reports
    </ListSubheader>
    <ListItemButton>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Current month" />
    </ListItemButton>
    <ListItemButton>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Last month" />
    </ListItemButton>
  </React.Fragment>
);