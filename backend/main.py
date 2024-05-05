from fastapi import FastAPI
from os import environ
from sqlalchemy import select, desc
import databases
from models.users import users_table
from models.news import news_table
from routes import users, news
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Разрешаем CORS для всех доменов на всех маршрутах
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(news.router)

SQLALCHEMY_DATABASE_URL = "sqlite:///database/news_db.db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get("/")
async def read_root():
    # изменим роут таким образом, чтобы он брал данные из БД
    query = (
        select(

                news_table.c.id,
                news_table.c.created_at,
                news_table.c.title,
                news_table.c.content,
                news_table.c.likes,
                news_table.c.media_url,
                news_table.c.user_id,
                users_table.c.name.label("name"),

        )
        .select_from(news_table.join(users_table))
        .order_by(desc(news_table.c.created_at))
    )
    return await database.fetch_all(query)
