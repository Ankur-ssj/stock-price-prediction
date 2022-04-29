import React, {useEffect, useState} from 'react'
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';
import msftinitialdata from '../static/msftstatic/msftinitialdata.png'
import msftlstmfinalgraph from '../static/msftstatic/msftlstmfinalgraph.png'
import micorsoft_logo from '../Images/microsoft_logo.png'
import msfacf from '../static/msftstatic/msfacf.png'
import msftacf from '../static/msftstatic/msftacf.png'
import msftpacf from '../static/msftstatic/msftpacf.png'
import msftresidual from '../static/msftstatic/msftresidual.png'
import msftarimavsgraph from '../static/msftstatic/msftarimavsgraph.png'
import msftlr from '../static/msftstatic/msftlr.png'
import '../Scss/Prediction.css'

const Predictions = () => {
    const [data, setData] = useState([])

    const getData = async () =>{
        if(data.length === 0){
            const response  = await fetch(`http://127.0.0.1:5000/api/microsoft`);
            setData(await response.json());
            console.log(data);
        }
    }

    useEffect(()=> {
        getData();
    }, [getData]);

  return (
    <>
        <div className="msft">
            <div className="msft_section">
                <div className='msft_header'>
                    <img src={micorsoft_logo} alt="msft" className='msft_logo' />
                    <div className="micorsoft_header">Microsoft</div>
                </div>
                <img src={msftinitialdata} alt="msft" className='msftinitialgraph'/>
                <div className='msft_lstm_section'>
                    <p className='msft_lstm_header'>Closing price predicted by LSTM model.</p>
                    <img src={msftlstmfinalgraph} className="msft_lstm_graph" alt="msft"/>
                    <p className='msft_lstm_data'>Next seven day closing price:</p>
                    <div className="msft_lstm_value">Next 7 days price: {data?.msftlstmdata ? data?.msftlstmdata : <Backdrop
                        sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
                        open>
                        <CircularProgress color="inherit" />
                        </Backdrop>}
                    </div>
                </div>

                <div className='msft_arima_section'>
                    <p className='msft_arima_header'>Closing price predicted by Arima model.</p>
                    <p className='msft_arima_og_header'>Arima Original</p>
                    <img className='ogacf' src={msfacf} alt="msft"/>
                    <p className='msft_arima_acf_header'>Arima ACF Plot</p>
                    <img className='acf' src={msftacf} alt="msft"/>
                    <p className='msft_arima_pacf_header'>Arima PACF Plot</p>
                    <img className='pacf' src={msftpacf} alt="msft"/>
                    <p className='msft_arima_residual_header'>Arima Residual</p>
                    <img className='residual' src={msftresidual} alt="msft"/>
                    <p className='msft_arima_final_header'>Arima Result</p>
                    <img className='arimafinalgraph' src={msftarimavsgraph} alt="msft"/>
                    <div className="msft_arima_value">Next 7 days price: {data?.msftarimadata ? data?.msftarimadata : <Backdrop
                        sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
                        open>
                        <CircularProgress color="inherit" />
                        </Backdrop>}
                    </div>
                </div>

                <div className='msft_lr_section'>
                    <p className='msft_lr_header'>Closing price predicted by Linear Regression model</p>
                    <img className='msft_lr_graph' src={msftlr} alt="msft"/>
                    <div className="msft_lr_value">Next 7 days price: {data?.msftlrdata ? data?.msftlrdata : <Backdrop
                        sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
                        open>
                        <CircularProgress color="inherit" />
                        </Backdrop>}
                    </div>
                </div>
            </div>
        </div>
    </>
  )
}

export default Predictions