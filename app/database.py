from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Прописываем конфигурацию БД

SQLALCHEMY_URL = "sqlite:///./marketplace.db" # Место хранения хранения БД

#{'check_same_thread': False} - позволяет использовать одно подключение из нескольких потоков
engine = create_engine(SQLALCHEMY_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Создание базового класса для декларативного определения моделей
Base = declarative_base()

# Генератор для создания и возвращения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()