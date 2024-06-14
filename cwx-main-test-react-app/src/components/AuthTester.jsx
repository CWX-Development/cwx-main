import React, { useState } from 'react';
import axios from 'axios';

const AuthTester = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    const url = 'http://localhost:8080/auth/login';

    const data = {
      email,
      password,
    };
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Parse the JSON response
      })
      .then((data) => {
        console.log('Success:', data); // Handle the JSON response data
      })
      .catch((error) => {
        console.error('Error:', error); // Handle errors
      });
  };

  const handleSignup = async () => {
    try {
      const response = await axios.post(
        'http://localhost:8080/auth/signup',
        new URLSearchParams({ email, password }).toString(),
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );
      const { token } = response.data;
      console.log(response.data);
      localStorage.setItem('token', token);
      setError('');
    } catch (error) {
      setError('Signup failed. Please try again.');
      console.error('Signup error:', error);
    }
  };

  return (
    <div>
      <h2>Login / Signup</h2>
      <form>
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="button" onClick={handleLogin}>
          Login
        </button>
        <button type="button" onClick={handleSignup}>
          Signup
        </button>
        {error && <p>{error}</p>}
      </form>
    </div>
  );
};

export default AuthTester;
