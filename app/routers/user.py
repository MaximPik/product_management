from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from product_management.app.database import get_db
from product_management.app.crud import user as UserCrud
from product_management.app.dto import user as UserDto

# В этом файле определены маршруты для операций над пользователями
router = APIRouter()

# tags=["user"] — это метка, которая используется для группировки маршрутов в документации

@router.post('/')
async def create(data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserCrud.create_user(data, db)


@router.get('/{id}')
async def get(id: int=None, db:Session=Depends(get_db)):
    return UserCrud.get_user(id, db)

@router.put('/{id}')
async def update(data: UserDto.User = None, id: int=None, db:Session=Depends(get_db)):
    return UserCrud.update_user(data, db, id)

@router.delete('/{id}')
async def delete(id: int=None, db:Session=Depends(get_db)):
    return UserCrud.delete_user(db, id)