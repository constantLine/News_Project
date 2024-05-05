import React, { useState } from 'react';
import axios from 'axios';
import "./Login.css";

import { Link, useNavigate } from 'react-router-dom'; // Импортируем компонент Link для перехода на другие страницы


const Login = ({onLogin}) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const response = await axios.post('http://localhost:8000/auth/', formData);

        console.log('Успешная аутентификация', response.data);
        onLogin(response.data.token); // Передаем токен в родительский компонент
        navigate('/');
    } catch (error) {
        setError('Неверная почта или пароль');
    }
};

  return (
    <div className="login-container">
      <h2>Вход</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label htmlFor="username">Почта:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Пароль:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Войти</button>
      </form>
      <p>Еще нет аккаунта? <Link to="/register">Регистрация</Link></p>
    </div>
  );
};

export default Login;

