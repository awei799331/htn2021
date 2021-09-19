import React, { useEffect, useState } from 'react';
import { slide as Menu } from 'react-burger-menu';

import { navStyles } from './styles';

function Home() {
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
        isOpen={true}
        itemListClassName={ "nav-button" }
      >
        <a id="home" href="/">Home</a>
        <a id="about" href="/about">About</a>
        <a id="contact" href="/contact">Contact</a>
      </Menu>
      <main id="page-wrap">
        <p>
          {lat} {lon}
        </p>
        <iframe
          title='joemama'
          width="1280"
          height="720"
          src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk&mode=walking&origin=351+Tealby+Cres&destination=351+Tealby+Cres&waypoints=362+King+St+N|462+Albert+St"
        >
        </iframe>
      </main>
    </div>
  );
}

export default Home;