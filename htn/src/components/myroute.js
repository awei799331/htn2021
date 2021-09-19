import React, { useState, useEffect } from 'react';
import NavBar from './navbar';
import styled from 'styled-components';

function MyRoute() {
  const [routeUrl, setRouteUrl] = useState(window.localStorage.getItem('mapEmbed') || null);
  const [images, setImages] = useState([]);

  const updateStorage = () => {
    if (window.localStorage.getItem('mapEmbed') !== '') {
      setRouteUrl(window.localStorage.getItem('mapEmbed'));
    } 
    if (window.localStorage.getItem('waypointImgs') !== '') {
      let images_for_gallery = []
      const image_array = JSON.parse(window.localStorage.getItem('waypointImgs'));
      setImages(image_array);
    }
  }

  useEffect(() => {
    updateStorage();
  }, []);

  return (
    <div id="outer-container">
      <NavBar />
      <main id="page-wrap" className="main-page">
        <MainWrapper>
          <h2>
            Your route: 
          </h2>
          <iframe
            title='joemama'
            style={{
              height: '60vh',
              width: '95%'
            }}
            src={routeUrl}
          >
          </iframe>
          <h2>
            Your waypoints:
          </h2>
          {
            images.map((item, index) => {
              console.log(item)
              return <img alt={`street view ${index}`} style={{width:'90%'}} src={item} key={index} />
            })
          }
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

export default MyRoute;