from datetime import datetime

from models.database import database
from models.news import news_table
from models.users import users_table
from schemas import news as news_schema
from sqlalchemy import desc, func, select


async def create_post(post: news_schema.NewsModel, user):
    query = (
        news_table.insert()
        .values(
            title=post.title,
            content=post.content,
            created_at=datetime.now(),
            likes=1,
            user_id=user["id"],
        )
        .returning(
            news_table.c.id,
            news_table.c.title,
            news_table.c.content,
            news_table.c.created_at,
            news_table.c.likes,
        )
    )
    news = await database.fetch_one(query)

    # Convert to dict and add user_name key to it
    news = dict(zip(news, news.values()))
    news["user_name"] = user["name"]
    return news


async def get_post(post_id: int):
    query = (
        select(

                news_table.c.id,
                news_table.c.created_at,
                news_table.c.title,
                news_table.c.content,
                news_table.c.user_id,
                users_table.c.name.label("user_name"),

        )
        .select_from(news_table.join(users_table))
        .where(news_table.c.id == post_id)
    )
    return await database.fetch_one(query)


async def get_posts(page: int):
    #max_per_page = 10
    #offset1 = (page - 1) * max_per_page
    query = (
        select(

                news_table.c.id,
                news_table.c.created_at,
                news_table.c.title,
                news_table.c.content,
                news_table.c.user_id,
                #users_table.c.name.label("user_name"),

        )
        .select_from(news_table)#.join(users_table))
        .order_by(desc(news_table.c.created_at))
        #.limit(max_per_page)
        #.offset(offset1)
    )
    return await database.fetch_all(query)


async def get_posts_count():
    query = select(func.count()).select_from(news_table)
    return await database.fetch_val(query)


async def update_post(post_id: int, post: news_schema.NewsModel):
    query = (
        news_table.update()
        .where(news_table.c.id == post_id)
        .values(title=post.title, content=post.content)
    )
    return await database.execute(query)
