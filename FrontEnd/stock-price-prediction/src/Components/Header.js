import React, {useState, useEffect} from 'react'
import { Link, withRouter } from 'react-router-dom'
import Hamburger from './Hamburger'
import '../Scss/Header.css'

const Header = ({history}) => {
    const [state, setState] = useState({
        initial: false,
        clicked: null,
        menuName: "menu"
    });

    //state for disabled button
    const [disabled, setDisabled] = useState(false);

    //useeffect for page changes
    useEffect(() => {
        //listen  for page changes
        history.listen(() => {
            setState({clicked: false, menuName: "menu"})
        })
    })

    const handleMenu = () =>{

        disableMenu();

        if (state.initial === false) {
            setState({
                initial: null,
                clicked: true,
                menuName: "Close",
                styles: {
                    color: "#000000"
                }
            });
        } else if (state.clicked === true) {
            setState({
                clicked: !state.clicked,
                menuName: "Menu"
            });
        } else if(state.clicked === false) {
            setState({
                clicked: !state.clicked,
                menuName: "Close",
                styles: {
                    color: "#000000"
                }
            });
        }
    };

    //Determine if our menu button should be disabled
    const disableMenu = () => {
        setDisabled(!disabled);
        setTimeout(() => {
            setDisabled(false);
        }, 1200);
    };

    return (
        <header>
            <div className='container'>
                <div className='wrapper'>
                    <div className='inner-header'>
                        <div className='logo'>
                        <div className='nav-logo'><Link to='/Home'>SMPSA</Link></div>
                        </div>
                        <div className='menu'>
                            <button disabled={disabled} onClick={handleMenu}>Menu</button>
                        </div>
                    </div>
                </div>
            </div>
            <Hamburger state={state}/>
        </header>
    )
}

export default withRouter(Header)
