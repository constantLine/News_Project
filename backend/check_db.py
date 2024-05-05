import sqlite3

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('database/news_db.db')
cursor = conn.cursor()

# Получаем список пользователей
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("Список пользователей:")
for user in users:
    print(user)

# Получаем список новостей
cursor.execute("SELECT * FROM news")
news = cursor.fetchall()

print("\nСписок новостей:")
for item in news:
    print(item)

# Получаем список новостей
cursor.execute("SELECT * FROM tokens")
tokens = cursor.fetchall()

print("\nСписок токенов:")
for item in tokens:
    print(item)

# Закрываем соединение с базой данных
conn.close()
