import './App.css';
import axios from 'axios';
/* This allows us to use the axios library to make HTTP requests to our backend. */
import { useEffect, useState } from 'react';


function App() {
  
  const [people, setPeople] = useState([]);

/* The useState hook is used to store the data that we get back from our backend. */
  useEffect(() => {
    axios.get('/api').then(response => setPeople(response.data));

}, []);

/* The useEffect hook is used to make a request to our backend when the component is rendered. */
return people.map((p, index) => {
  return <p key={index}>{p.id} {p.name} {p.age}</p>
})
}

export default App;
