from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from routes.route import note

app = FastAPI()
app.include_router(note)

# app.mount("/static", StaticFiles(directory="static"), name="static")


