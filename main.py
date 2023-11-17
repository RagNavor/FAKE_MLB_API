from fastapi import FastAPI
from config.database import Session, engine, Base


app = FastAPI()
app.title = "FAKE_MLB_API"
Base.metadata.create_all(bind=engine)
