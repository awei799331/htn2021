import { reveal as Menu } from 'react-burger-menu';

import { navStyles } from './styles';

function NavBar() {
  return (
    <Menu
      pageWrapId={"page-wrap"}
      outerContainerId={"outer-container"}
      styles={navStyles}
      isOpen={false}
    >
      <p id="title-nav">cacheXplore</p>
      <a id="home" className="nav-button" href="/">Home</a>
      <a id="about" className="nav-button" href="/start">Start</a>
      <a id="contact" className="nav-button" href="/contact">Contact</a>
    </Menu>
  )
}

export default NavBar;