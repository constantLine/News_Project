"""Изменение таблицы токенов (UUID for SQLite)

Revision ID: 135dc88732d7
Revises: 7c561ecb0de4
Create Date: 2024-05-03 19:02:11.836749

"""
from typing import Sequence, Union
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '135dc88732d7'
down_revision: Union[str, None] = '7c561ecb0de4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# Функция upgrade применяет изменения
def upgrade():
    # Изменяем тип столбца token на GUID
    op.alter_column('tokens', 'token', type_=sa.String, nullable=False)
    # Устанавливаем значение по умолчанию для столбца token
    op.execute("ALTER TABLE tokens ALTER COLUMN token SET DEFAULT '{}'".format(str(uuid.uuid4())))


# Функция downgrade отменяет изменения
def downgrade():
    # Возвращаем столбец token к типу UUID
    op.alter_column('tokens', 'token', type_=sa.UUID(as_uuid=False), nullable=False)
