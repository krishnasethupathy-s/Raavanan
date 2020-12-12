import { useEffect } from 'react';
import Container from '@material-ui/core/Container';
import Paper from '@material-ui/core/Paper';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { green } from '@material-ui/core/colors';

import { BrowserRouter as Router } from 'react-router-dom';
import Routes from './routes/Routes';

import { useSelector } from 'react-redux';

import useDarkTheme from './hooks/useDarkTheme';

import Loader from './components/Loader/Loader';
import Navbar from './components/navbar/Navbar';
import Footer from './components/Footer/Footer';

// import { dark, light } from './theme';

import ReactGA from 'react-ga';
import { Helmet } from 'react-helmet';

import { useStyles } from './AppStyle';

import Logo from './asserts/raavanan logo.png';

function App() {
  const classes = useStyles();
  const [theme] = useDarkTheme();
  const { loading } = useSelector((state) => state.appUi);

  const darkTheme = createMuiTheme({
    palette: {
      type: 'dark',
    },
  });

  const lightTheme = createMuiTheme({
    palette: {
      primary: {
        main: green[600],
      },
    },
  });

  useEffect(() => {
    ReactGA.initialize('G-LH9KB8TXPW');
    ReactGA.pageview(window.location.pathname + window.location.search);
  }, []);

  return (
    <>
      <Helmet>
        <title>இராவணன் அங்காடி | முகப்பு</title>
        <meta
          name="keywords"
          content="ravanan,raavanan, ravanan store, raavanan store, phone case,photo frame,mugs,cups,stickers,tamil Dhesiyam, ntk, naam tzhamilar, seeman,valluvar, raavananstore "
        />
        <meta property="og:title" content="Raavanan Store , இராவணன் அங்காடி" />
        <meta property="og:image" content={Logo} />
        <meta
          property="og:description"
          content="Raavanan Store , இராவணன் அங்காடி"
        />
      </Helmet>
      <ThemeProvider theme={theme === 'light' ? lightTheme : darkTheme}>
        <Router>
          <Paper>
            {loading && <Loader />}
            <Navbar />
            <Container className={classes.root}>
              <Routes />
            </Container>
            <Footer />
          </Paper>
        </Router>
      </ThemeProvider>
    </>
  );
}

export default App;
