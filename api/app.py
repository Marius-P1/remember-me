from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

from src.agenda import Agenda, Event, create_agenda, add_event_to_agenda, remove_event_from_agenda, get_agenda

# Load environment variables from .env file
load_dotenv()
port = os.getenv("PORT")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/connect")
def connect(request: Request):
    name = request.state.my_name
    print(f"Connecting to {name}")
    folders = os.listdir("./assets/")
    if name in folders:
        print(f"Folder {name} already exists.")
    else:
        os.mkdir(f"./assets/{name}")
        print(f"Created folder: {name}")
        create_agenda(name)
    return {"message": f"Connected to {name}"}

@app.get("/agenda")
def get_agenda_route(request: Request):
    name = request.state.my_name
    agenda : Agenda = get_agenda(name)
    if agenda:
        return {"agenda": agenda}
    else:
        return {"error": "Agenda not found"}

@app.post("/agenda")
def add_event_route(request: Request, event: Event):
    name = request.state.my_name
    agenda = get_agenda(name)
    if agenda:
        add_event_to_agenda(name, event)
        return {"message": "Event added successfully"}
    else:
        return {"error": "Agenda not found"}

@app.delete("/agenda")
def remove_event_route(request: Request, event_name: str):
    name = request.state.my_name
    agenda = get_agenda(name)
    if agenda:
        remove_event_from_agenda(name, event_name)
        return {"message": "Event removed successfully"}
    else:
        return {"error": "Agenda not found"}




@app.middleware("http")
async def check_headers(request: Request, call_next):
    """
    Middleware to check for the presence of the 'My-Name' header.
    If the header is not present, return a 400 Bad Request response.
    """
    if "My-Name" not in request.headers:
        return JSONResponse(status_code=400, content={"message": "Missing My-Name"})
    # If the header is present, get him and set it in the request state
    my_name = request.headers["My-Name"]

    request.state.my_name = my_name
    response = await call_next(request)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(port))

