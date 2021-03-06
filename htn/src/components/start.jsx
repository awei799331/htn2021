import React, { useState } from 'react';
import { useHistory } from 'react-router';
import NavBar from './navbar';
import { Button, TextField } from '@mui/material';
import { withStyles } from '@mui/styles';
import styled from 'styled-components';
import axios from 'axios';

const CssTextField = withStyles({
  root: {
    '& label.Mui-focused': {
      color: '#FFD100',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: '#FFD100',
    },
    '& .MuiOutlinedInput-root': {
      color: 'white',
      '& fieldset': {
        borderColor: 'white',
      },
      '&:hover fieldset': {
        borderColor: 'white',
      },
      '&.Mui-focused fieldset': {
        borderColor: '#FFD100',
      },
    },
    '& .MuiInputLabel-root': {
      color: 'white'
    },
  },
})(TextField);

function Start() {
  const history = useHistory();
  const [locStatus, setLocStatus] = useState(-1);
  const [distance, setDistance] = useState(0);
  const [lat, setLat] = useState(null);
  const [lon, setLon] = useState(null);
  const [showError, setShowError] = useState(false);

  const getLocation = () => {
    navigator.geolocation.getCurrentPosition(position => {
      console.log(lat, lon);
      setLat(position.coords.latitude);
      setLon(position.coords.longitude);
      setLocStatus(1);
    }, error => {
      setLocStatus(0);
    }
    );
  };

  const planRoute = async () => {
    if (lat === null || lon === null) {
      setShowError(true);
      return;
    }
    let actualDistance = Math.abs(distance);
    try {
      let response = await axios.post(`${process.env.REACT_APP_BACKEND}/get-route`, {
        length: actualDistance,
        latitude: lat,
        longitude: lon
      });
      console.log(response.data);
      window.localStorage.setItem('mapEmbed', response.data.path_url);
      window.localStorage.setItem('waypointImgs', JSON.stringify(response.data.img_url));
      history.push('/route');
    } catch (e) {
      console.log(e);
    }
  }

  return (
    <div id="outer-container">
      <NavBar />
      <main id="page-wrap" className="main-page">
        <MainWrapper>
          <h2>
            Select an origin:
          </h2>
            <Button 
              variant="outlined"
              onClick={getLocation}
            >
              Use Current Location
            </Button>
          <p>
            {
              locStatus === 1 ? 'Location found!' :
              locStatus === 0 ? 'Error: location access denied' :
              ''
            }
          </p>
          <h2>
            Select a run length:
          </h2>
          <CssTextField
            required
            id="outlined"
            label="Distance (km)"
            onChange={e => setDistance(e.target.value)}
            type="number"
            defaultValue={0}
          />
          <Button 
            variant="outlined"
            onClick={planRoute}
          >
            Plan Route
          </Button>
          <p>
            {
              showError === true ? 'Please enable location and check your distance input!' : ''
            }
          </p>
        </MainWrapper>
      </main>
    </div>
  );
}

const MainWrapper = styled.div`
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  padding: 10vh 5vw 0;

  > * {
    margin: 10px !important;
  }
`;

export default Start;