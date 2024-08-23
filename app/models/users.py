from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

# Создание таблицы Users
class User(Base):
    __tablename__ = 'users' # Название таблицы
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

