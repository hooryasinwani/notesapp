from fastapi import FastAPI
from app.routes.routes import router
from app.database.database import Base, engine
from app.models import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)