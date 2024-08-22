# Файл для конфигурации тестовой БД и клиента
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from product_management.app.database import Base, get_db
from product_management.app.main import app
from fastapi.testclient import TestClient

# Прописываем конфигурацию БД

SQLALCHEMY_TEST_URL = "sqlite:///./test.db" # Место хранения хранения БД

#{'check_same_thread': False} - позволяет использовать одно подключение из нескольких потоков
test_engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={'check_same_thread': False})

TestSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=test_engine)

# Создание тестовой БД
@pytest.fixture(scope='function')
def db_session():
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)

# Создание тестового клиента
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    # Подмена зависимости get_db, чтобы использовать тестовую базу данных
    app.dependency_overrides[get_db] = override_get_db
    # Создание тестового клиента
    with TestClient(app) as client:
        yield client
    # Восстановление оригинальной зависимости после тестов
    app.dependency_overrides[get_db] = get_db