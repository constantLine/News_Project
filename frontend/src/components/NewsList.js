// NewsList.js
import React from 'react';


// Компонент для отображения одной новости
const NewsItem = ({ news }) => {
  return (
    <div className="news-item">
      <h2>{news.title}</h2>
      <p>{news.content}</p>
    </div>
  );
};
const NewsList = ({ newsList }) => {
  return (
    <div className="news-list">
      {newsList.map((news, index) => (
        <NewsItem key={index} news={news} />
      ))}
    </div>
  );
};

export default NewsList;
