import React, { useRef, useEffect } from 'react'
import '../Scss/Home.css'
import { GraphModel } from '../Models/ModelsExport'
import gsap from 'gsap'
import {Link} from 'react-router-dom'

const Home = () => {

  let homeOne = useRef(null);
  let homeTwo = useRef(null);

  const staggerText = (node) => {
    gsap.from(node, {
        duration:0.8,
        y: 200,
        delay: 1.5,
        ease: "circ.out",
        opacity: 0,
        stagger: {
            amount: 0.3
        },
    });
  } 

  const fadeIn = (node) =>{
    gsap.from(node,{
      duration: 1,
      delay: 1,
      ease: "circ.out",
      opacity:0
    });
  }

  useEffect(() => {
    staggerText(homeOne);
    fadeIn(homeTwo)
})
  
  return (
    <div className='home_container'>
        <h1 ref={el => (homeOne = el)} className='home_title'>MAKING YOUR TRADING SMOOTHER.</h1>
        <div ref={el => (homeTwo = el)} className='home_canvas'>
            <GraphModel/>
        </div>
        <Link to='/Introduction' className='get_started_button'>Get Started</Link>
        <div className='home_decor_one'>TRADING</div>
    </div>
  )
}

export default Home