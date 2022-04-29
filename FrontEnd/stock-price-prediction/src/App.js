import React from 'react'
import {BrowserRouter as Router, Switch ,Route} from 'react-router-dom';
import Header from './Components/Header';
import Home from './Pages/Home';
import Introduction from './Pages/Introduction';
import Predictions from './Pages/Predictions';
import WorkSpace from './Pages/WorkSpace';


function App() {
  return (
    <Router>
    <Header/>
      <div className="App">
        <Switch>
          <Route path="/Home" component={Home}/>
          <Route path="/Predictions" component={Predictions}/>
          <Route path="/Introduction" component={Introduction}/>
          <Route path="/WorkSpace" component={WorkSpace}/>
          <Route path="/" component={Home}/>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
