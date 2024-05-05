import sqlalchemy

from .users import users_table

metadata = sqlalchemy.MetaData()


news_table = sqlalchemy.Table(
    "news",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.Text()),
    sqlalchemy.Column("likes", sqlalchemy.Integer, nullable=False, default=0),
    sqlalchemy.Column("media_url", sqlalchemy.String, nullable=True),
)

categories_table = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
)


news_categories_table = sqlalchemy.Table(
    "news_categories",
    metadata,
    sqlalchemy.Column("news_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("news.id"), primary_key=True),
    sqlalchemy.Column("category_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"), primary_key=True),
)
