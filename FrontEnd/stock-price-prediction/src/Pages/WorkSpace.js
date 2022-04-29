import React from 'react'
import '../Scss/Workspace.css'
import microsoft_logo from '../Images/microsoft_logo.png'
import apple_logo from '../Images/apple_logo.png'
import icici_logo from '../Images/icici_logo.png'
import infosys_logo from '../Images/infosys_logo.png'
import tcs_logo from '../Images/tcs_logo.png'
import reliance_logo from '../Images/reliance_logo.png'
import amazon_logo from '../Images/amazon_logo.png'
import sbi_logo from '../Images/sbi_logo.png'
import google_logo from '../Images/google_logo.png'
import { Link } from 'react-router-dom'


const WorkSpace = () => {
  return (
    <>
        <div className='worspace_container'>
        <div className='workspace_header'>WORK SPACE</div>
        <p className='workspace_subheader'>Select a company for prediction.</p>
        <div className='card_wrapper'>
            <Link>
                <div className='card_one'>
                    <img className='company_logo msft_logo' src={microsoft_logo} alt="msft"/>
                </div>
            </Link>
            <div className='card_two'>
                <img className='company_logo' src={apple_logo} alt="msft"/>
            </div>
            <div className='card_three'>
                <img className='company_logo icici' src={icici_logo} alt="msft"/>
            </div>
            <div className='card_four'>
                <img className='company_logo' src={google_logo} alt="msft"/>
            </div>
            <div className='card_five'>
                <img className='company_logo' src={tcs_logo} alt="msft"/>
            </div>
            <div className='card_six'>
                <img className='company_logo reliance' src={reliance_logo} alt="msft"/>
            </div>
            <div className='card_seven'>
                <img className='company_logo' src={amazon_logo} alt="msft"/>
            </div>
            <div className='card_eight'>
                <img className='company_logo' src={sbi_logo} alt="msft"/>
            </div>
            <div className='card_nine'>
                <img className='company_logo infosys' src={infosys_logo} alt="msft"/>
            </div>
        </div>
        </div>
    </>
  )
}

export default WorkSpace