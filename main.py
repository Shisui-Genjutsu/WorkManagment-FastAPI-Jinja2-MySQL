from fastapi import FastAPI
import models
from database import engine
from starlette.staticfiles import StaticFiles
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)

