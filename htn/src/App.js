import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/home';
import Start from './components/start';
import './App.css';
import { ThemeProvider, createTheme } from '@mui/material';

const theme = createTheme({
  components: {
    // Name of the component
    MuiButton: {
      styleOverrides: {
        // Name of the slot
        outlined: {
          color: 'white',
          borderColor: 'white',
          ":hover": {
            color: '#FFD100',
            borderColor: '#FFD100'
          }
        }
      }
    }
  }
});

function App() {
  return (
    <>
      <ThemeProvider theme={theme}>
        <Router>
          <Switch>
            <Route exact path="/" component={ Home } />
            <Route exact path="/start" component={ Start } />
          </Switch>
        </Router>
      </ThemeProvider>
    </>
  );
}

export default App;
