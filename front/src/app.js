import React from 'react';
import {createRoot} from 'react-dom/client';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import PrivateRoute from './utils/PrivateRoute';
import {AuthProvider} from './context/AuthContext';

import SignInOutContainer from './containers/index';
import RegisterContainer from './containers/register';
import StudentPage from './containers/studentPage';
import {createTheme, ThemeProvider} from '@mui/material/styles';

import './styles/style.css';
import ExercisesTeacherPage from './containers/ExercisesTeacherPage';
import ClassroomsTeacherPage from './containers/ClassroomsTeacherPage';

const theme = createTheme({
  palette: {
    tertianary: {
      light: '#ADE6FF',
      main: '#1698f9',
      dark: '#1670F9',
      contrastText: '#fff',
    },
    secondary: {
      light: '#FFD290',
      main: '#f9a429',
      dark: '#D78E32',
      contrastText: '#fff',
    },
    primary: {
      light: '#fff',
      main: '#fff',
      dark: '#fff',
      contrastText: '#000',
    },
  },
});

const App = () => {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
          <Route component={SignInOutContainer} path="/" exact />
          <Route component={RegisterContainer} path="/register" />
          <PrivateRoute
            component={ExercisesTeacherPage}
            userType="TEACHER"
            path="/teacher/exercises"
          />
          <PrivateRoute
            component={ClassroomsTeacherPage}
            userType="TEACHER"
            path="/teacher/classrooms"
          />
          <PrivateRoute userType="STUDENT" path="/student">
            <ThemeProvider theme={theme}>
              <StudentPage />
            </ThemeProvider>
          </PrivateRoute>
        </AuthProvider>
      </Router>
    </div>
  );
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
