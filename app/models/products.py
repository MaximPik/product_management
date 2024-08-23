from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

# Создание таблицы Users
class Product(Base):
    __tablename__ = 'products' # Название таблицы
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

class Category(Base):
    __tablename__ = 'categories'  # Название таблицы
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    products = relationship("Product", backref="Category")
