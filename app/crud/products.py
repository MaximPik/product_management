# Взаимодействие с БД
from product_management.app.models.products import Product, Category
from sqlalchemy.orm import Session
from product_management.app.dto import products
from sqlalchemy.orm import joinedload

# Создать продукт
def create_product(data: products.Product, db: Session):
    new_product = Product(name=data.name,
                          description=data.description,
                          price=data.price,
                          category_id=data.category_id)
    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    except Exception as e:
        print(e)

    return new_product

# Получить продукт
def get_product(id: int, db):
    return db.query(Product).filter(Product.id==id).first()

# Получить продукт
def get_products(db:Session,
                name: str = None,
                price: float = None,
                category_id: int = None,
                ):
    query = db.query(Product)
    if name:
        query = query.filter(Product.name == name)
    if price:
        query = query.filter(Product.price == price)
    if category_id:
        query = query.filter(Product.category_id == category_id)

    return query.all()

# Обновить продукт
def update_product(data: products.Product, db:Session, id: int):
    product = db.query(Product).filter(Product.id==id).first()
    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.category_id = data.category_id
    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as e:
        print(e)
    return product

# Удалить продукт
def delete_product(db:Session, id: int):
    product = db.query(Product).filter(Product.id==id).delete()
    db.commit()
    return product

# Создать категорию
def create_category(data: products.Category, db: Session):
    new_category = Category(name=data.name)
    try:
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
    except Exception as e:
        print(e)

    return new_category

# Получить категорию
def get_category(category_id: int, db):
    return db.query(Product).options(joinedload(Product.Category)).filter(Product.category_id == category_id).all()

# Получить все категории
def get_categories(db:Session):
    return db.query(Category).all()