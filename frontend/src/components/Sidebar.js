import React from 'react';

const Sidebar = () => {
    return (
        <aside className="sidebar">
            <div className="widget">
                <h3>Популярные категории</h3>
                <ul>
                    <li><a href="#">Технологии</a></li>
                    <li><a href="#">Наука</a></li>
                    <li><a href="#">Искусство</a></li>
                </ul>
            </div>
            <div className="widget">
                <h3>Ссылки</h3>
                <ul>
                    <li><a href="#">О нас</a></li>
                    <li><a href="#">Контакты</a></li>
                </ul>
            </div>
        </aside>
    );
};

export default Sidebar;
