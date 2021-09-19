import React, { useEffect, useState } from 'react';
import { slide as Menu } from 'react-burger-menu';

import { navStyles } from './styles';

function MapRoute() {
  const [lat, setLat] = useState(null);
  const [lon, setLon] = useState(null);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(position => {
      setLat(position.coords.latitude);
      setLon(position.coords.longitude);
    });
  }, []);

  return (
    <div id="outer-container">
      <Menu
        pageWrapId={"page-wrap"}
        outerContainerId={"outer-container"}
        styles={navStyles}
        isOpen={false}
      >
        <p>cacheXplore</p>
        <a id="home" className="nav-button" href="/">Home</a>
        <a id="about" className="nav-button" href="/about">About</a>
        <a id="contact" className="nav-button" href="/contact">Contact</a>
      </Menu>
      <main id="page-wrap" className="main-page">
        <h1> 
          cacheXplore
        </h1>
        <p>
          {lat} {lon}
        </p>
        <iframe
          title='joemama'
          src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk&mode=walking&origin=351+Tealby+Cres&destination=351+Tealby+Cres&waypoints=362+King+St+N|462+Albert+St"
        >
        </iframe>
      </main>
    </div>
  );
}

export default MapRoute;