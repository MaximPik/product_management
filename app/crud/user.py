# Взаимодействие с БД
from app.models.users import User
from sqlalchemy.orm import Session
from app.dto import user

# Создать пользователя
def create_user(data: user.User, db: Session):
    new_user = User(name=data.name)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        print(e)

    return new_user

# Получить пользователя
def get_user(id: int, db):
    return db.query(User).filter(User.id==id).first()

# Обновить пользователя
def update_user(data: user.User, db:Session, id: int):
    user = db.query(User).filter(User.id==id).first()
    user.name = data.name
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

# Удалить пользователя
def delete_user(db:Session, id: int):
    user = db.query(User).filter(User.id==id).delete()
    db.commit()
    return user
