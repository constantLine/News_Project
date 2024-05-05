import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Routes, useNavigate } from 'react-router-dom';
import axios from 'axios';
import "./App.css"
import NewsList from './components/NewsList'; // Импортируем компонент NewsList
import Login from './components/Login'; // Импортируем компонент страницы авторизации
import AddNews from './components/AddNews'; // Импортируем компонент страницы добавления новости
import Register from "./components/Register";
import Sidebar from "./components/Sidebar";
import PrivateRoute from "./components/PrivateRoute";



const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [authToken, setAuthToken] = useState('');
  const [newsList, setNewsList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get('http://localhost:8000/posts/');
        setNewsList(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Ошибка при получении новостей:', error);
      }
    };

    fetchNews();

    return () => {
      // Очистка каких-либо ресурсов, если это необходимо
    };
  }, []);
 const handleLogin = (token) => {
    setIsAuthenticated(true);
    setAuthToken(token);
  };

  return (
    <Router>
      <div className="app">
        <header className="header">
          <div className="container">
            <h1 className="logo">Новости</h1>
            <nav className="nav">
              <ul>
                <li><Link to="/">Главная</Link></li>
                <li><Link to="/add-news">Добавить новость</Link></li>
                {isAuthenticated ? (
                  <li><Link to="/add-news">Добавить новость</Link></li>
                ) : (
                  <li><Link to="/login">Войти</Link></li>
                )}
              </ul>
            </nav>

          </div>
        </header>

        <Routes>
            <Route path="/login" element={<Login onLogin={handleLogin}/>} />
            <Route path="/add-news" element={<AddNews authToken={authToken} />} />
            <Route path="/" element={
                <div className="main-content">
                    <Sidebar />
                    <NewsList newsList={newsList} />
                </div>
            } />
            <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
