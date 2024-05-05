import hashlib
import random
import string
from datetime import datetime, timedelta
from sqlalchemy import and_

from models.database import database
from models.users import tokens_table, users_table
from schemas import users as user_schema
import uuid

def get_random_string(length=12):
    """ Генерирует случайную строку, использующуюся как соль """
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = None):
    """ Хеширует пароль с солью """
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def validate_password(password: str, hashed_password: str):
    """ Проверяет, что хеш пароля совпадает с хешем из БД """
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed


async def get_user_by_email(email: str):
    """ Возвращает информацию о пользователе """
    query = users_table.select().where(users_table.c.email == email)
    return await database.fetch_one(query)


async def get_user_by_token(token: str):
    """ Возвращает информацию о владельце указанного токена """
    query = tokens_table.join(users_table).select().where(
        and_(
            tokens_table.c.token == token,
            tokens_table.c.expires > datetime.now()
        )
    )
    return await database.fetch_one(query)


from schemas.users import TokenBase  # Подставьте правильный путь к модели TokenBase


async def create_user_token(user_id: int):
    """ Создает токен для пользователя с указанным user_id """
    token_value = str(uuid.uuid4())
    expires = datetime.now() + timedelta(weeks=2)

    query = (
        tokens_table.insert()
        .values(expires=expires, user_id=user_id, token=token_value)
        .returning(tokens_table.c.token, tokens_table.c.expires)
    )

    token_record = await database.fetch_one(query)

    # Создаем объект TokenBase для возвращения
    token_data = dict(token=str(token_record.token), expires=token_record.expires, token_type="bearer")
    token_base = TokenBase(**token_data)

    return token_base


async def create_user(user: user_schema.UserCreate):
    """ Создает нового пользователя в БД """
    salt = get_random_string()
    hashed_password = hash_password(user.password, salt)
    query = users_table.insert().values(
        email=user.email, name=user.name, hashed_password=f"{salt}${hashed_password}"
    )
    user_id = await database.execute(query)
    token = await create_user_token(user_id)
    #token_dict = {"token": token["token"], "expires": token["expires"]}

    return {**user.dict(), "id": user_id, "is_active": True, "token": token}