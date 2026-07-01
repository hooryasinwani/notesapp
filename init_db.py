from app.database.database import engine, Base
from app.models import models

Base.metadata.create_all(bind=engine)