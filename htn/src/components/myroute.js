import React, { useState } from 'react';
import NavBar from './navbar';
import styled from 'styled-components';

function MyRoute() {
  const [routeUrl, setRouteUrl] = useState(window.localStorage.getItem('mapEmbed') || null);

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
              height: '75vh',
              width: '95%'
            }}
            src={routeUrl}
          >
          </iframe>
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