from databases import Database


SQLALCHEMY_DATABASE_URL = "sqlite:///database/news_db.db"
database = Database(SQLALCHEMY_DATABASE_URL)