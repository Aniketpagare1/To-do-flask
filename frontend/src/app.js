import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ToDoList from './components/ToDolist';
import ProFeature from './components/Profeature';
import Login from './components/login';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Keycloak login logic (simulated)
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <Router>
      <div>
        {isLoggedIn ? (
          <Switch>
            <Route path="/" exact component={ToDoList} />
            <Route path="/pro" component={ProFeature} />
          </Switch>
        ) : (
          <Login setIsLoggedIn={setIsLoggedIn} />
        )}
      </div>
    </Router>
  );
}

export default App;
