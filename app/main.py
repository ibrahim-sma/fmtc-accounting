from fastapi import FastAPI
from app.routes import transactions, auth
from app.database import Base, engine
from app.models import transaction
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.include_router(transactions.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}
