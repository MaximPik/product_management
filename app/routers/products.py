from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import products as ProductCrud
from app.dto import products as ProductDto
from fastapi import HTTPException

# В этом файле определены маршруты для операций над пользователями
router = APIRouter()

# tags=["user"] — это метка, которая используется для группировки маршрутов в документации

@router.post('/products/', response_model=ProductDto.ProductResponse)
async def create(data: ProductDto.ProductCreate = None, db: Session = Depends(get_db)):
    return ProductCrud.create_product(data, db)

@router.get('/products/{id}', response_model=ProductDto.ProductResponse)
async def get(id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.get_product(id, db)

@router.get('/products/', response_model=list[ProductDto.ProductResponse])
async def get(db:Session=Depends(get_db),
              name: str = None,
              price: float = None,
              category_id: int = None,
              ):
    return ProductCrud.get_products(db=db, name=name, price=price, category_id=category_id)

@router.put('/products/{id}', response_model=ProductDto.ProductResponse)
async def update(data: ProductDto.ProductCreate = None, id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.update_product(data, db, id)

@router.delete('/products/{id}', response_model=dict)
async def delete(id: int=None, db:Session=Depends(get_db)):
    product = ProductCrud.delete_product(db, id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}
    #return ProductCrud.delete_product(db, id)

@router.post('/category/', response_model=ProductDto.CategoryResponse)
async def create(data: ProductDto.CategoryCreate = None, db: Session = Depends(get_db)):
    return ProductCrud.create_category(data, db)

@router.get('/category/{id}', response_model=list[ProductDto.CategoryResponse])
async def get(id: int=None, db:Session=Depends(get_db)):
    return ProductCrud.get_category(id, db)

@router.get('/category/', response_model=list[ProductDto.CategoryResponse])
async def get(db:Session=Depends(get_db)):
    return ProductCrud.get_categories(db=db)