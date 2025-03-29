from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/connect")
# def connect(name: str):
folders = os.listdir("./assets/")
print(folders)
# if name in folders:
#     return {"status": "connected"}
# else:
#     return {"status": "not connected"}