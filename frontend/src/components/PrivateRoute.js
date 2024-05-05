// PrivateRoute.js
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = ({ isAuthenticated }) => {
    // Если пользователь авторизован, возвращаем Outlet для рендеринг дочерних элементов
    // В противном случае возвращаем элемент, который перенаправит на страницу входа
    return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoute;

