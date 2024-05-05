import sqlite3
from datetime import datetime
import uuid

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('database/news_db.db')
cursor = conn.cursor()

# Добавляем 5 пользователей
for i in range(5):
    email = f"user{i + 1}@example.com"
    name = f"User{i + 1}"
    hashed_password = "password123"  # В реальном приложении следует хэшировать пароли
    cursor.execute("INSERT INTO users (email, name, hashed_password) VALUES (?, ?, ?)", (email, name, hashed_password))
    user_id = cursor.lastrowid

    # Если это первый пользователь, делаем его администратором
    if i == 0:
        cursor.execute("INSERT INTO administrators (user_id) VALUES (?)", (user_id,))

# Добавляем 10 новостей, используя ID первого пользователя
for i in range(10):
    user_id = 1  # ID первого пользователя (администратора)
    created_at = datetime.now()  # Текущая дата и время
    title = f"Новость {i + 1}"  # Заголовок новости
    content = f"Содержание новости {i + 1}"  # Содержание новости
    likes = i*2
    # SQL запрос для вставки новости
    query = "INSERT INTO news (user_id, created_at, title, content, likes) VALUES (?, ?, ?, ?, ?)"

    # Выполняем запрос с данными для вставки
    cursor.execute(query, (user_id, created_at, title, content, likes))

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()
