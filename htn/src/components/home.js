import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import NavBar from './navbar';

function Home() {

  return (
    <div id="outer-container">
      <NavBar />
      <main id="page-wrap" className="main-page flex">
        <h1 id="title-text"> 
          cacheXplore
        </h1>
        <Stack style={{margin:'5px 0'}} spacing={2} direction="row">
          <Button variant="outlined">Log In</Button>
          <Button variant="outlined">Register</Button>
        </Stack>
      </main>
    </div>
  );
}

export default Home;