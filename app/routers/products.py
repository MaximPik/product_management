from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from product_management.app.database import get_db
from product_management.app.crud import products as ProductCrud
from product_management.app.dto import products as ProductDto

# В этом файле определены маршруты для операций над пользователями
router = APIRouter()

# tags=["user"] — это метка, которая используется для группировки маршрутов в документации

@router.post('/products/')
async def create(data: ProductDto.Product = None, db: Session = Depends(get_db)):
    return ProductCrud.create_product(data, db)

@router.get('/products/{id}')
async def get(id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.get_product(id, db)

@router.get('/products/', response_model=list[ProductDto.Product])
async def get(db:Session=Depends(get_db),
              name: str = None,
              price: float = None,
              category_id: int = None,
              ):
    return ProductCrud.get_products(db=db, name=name, price=price, category_id=category_id)

@router.put('/products/{id}')
async def update(data: ProductDto.Product = None, id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.update_product(data, db, id)

@router.delete('/products/{id}')
async def delete(id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.delete_product(db, id)

@router.post('/category/')
async def create(data: ProductDto.Category = None, db: Session = Depends(get_db)):
    return ProductCrud.create_category(data, db)

@router.get('/category/{id}')
async def get(id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.get_category(id, db)

@router.get('/category/')
async def get(db:Session=Depends(get_db)):
    return ProductCrud.get_categories(db=db)