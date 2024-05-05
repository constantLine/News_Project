import React, { useState } from 'react';
import axios from 'axios';
import "./AddNews.css";


const AddNews = ({authToken}) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState('');

  const handleAddNews = async (e) => {
    e.preventDefault();
    try {
      console.log(authToken)
      const response = await axios.post('http://localhost:8000/posts/', {
        title: title,
        content: content,
        likes: 1
      }, {
        headers: {
          Authorization: `Bearer ${authToken}` // Передаем токен аутентификации в заголовке запроса
        }
      });
      // Обработка успешного добавления новости
      console.log('Новость успешно добавлена', response.data);
    } catch (error) {
      setError('Что-то пошло не так. Попробуйте еще раз.');
    }
  };

  return (
    <div className="add-news-container">
      <h2>Добавить новость</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleAddNews}>
        <div className="form-group">
          <label htmlFor="title">Заголовок:</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="content">Содержание:</label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
          />
        </div>
        <button type="submit">Добавить новость</button>
      </form>
    </div>
  );
};

export default AddNews;

