import uvicorn
from fastapi import FastAPI
from app.database import SessionLocal, Base, engine
from app.routers import user as UserRouter
from app.routers import products as ProductRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")
app.include_router(ProductRouter.router)

if __name__=='__main__':
    # reload=True - режим автоматической перезагрузки
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=2)
