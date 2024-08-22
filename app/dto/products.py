from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    category_id: int

class Category(BaseModel):
    name: str