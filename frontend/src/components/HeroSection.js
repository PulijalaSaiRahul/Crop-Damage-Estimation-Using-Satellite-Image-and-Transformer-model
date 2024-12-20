import React from 'react'
import '../App.css'
import { Button } from './Button'
import './HeroSection.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src='\videos\video-3.mp4' autoPlay loop muted></video>
      <h1>Empowering Agriculture <br></br>through Accurate Loss Estimation</h1>
  
      <div className='hero-btns'>
        <Button className='btns' 
        buttonStyle='btn--outline' 
        buttonSize='btn--large'>
            GET STARTED
        </Button>
        
      </div>
    </div>
  )
}

export default HeroSection
