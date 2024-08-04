import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//Switch is replced by Routes
import Navbar from './components/Navbar';
import Home from './components/pages/Home';
import SignUp from './components/pages/SighUp';
import About from './components/pages/About';

function App() {
  return (
    <>
    <Router>
      <Navbar/>
      <Routes>
        <Route path='/' exact Component={Home}/>
        <Route path='/about' Component={About}/>
        <Route path='/sign-up' Component={SignUp}/>
      </Routes>
    </Router>
    </>
  );
}

export default App;
