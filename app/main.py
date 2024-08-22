import uvicorn
from fastapi import FastAPI
from product_management.app.database import SessionLocal, Base, engine
from product_management.app.routers import user as UserRouter
from product_management.app.routers import products as ProductRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")
app.include_router(ProductRouter.router)

if __name__=='__main__':
    # reload=True - режим автоматической перезагрузки
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, workers=2)
