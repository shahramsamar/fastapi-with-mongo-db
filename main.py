from fastapi import FastAPI
from .routers.router import MyRouter

app = FastAPI()
app.include_router(MyRouter)

# READ , UPDATE, POST, PUT, PATCH


@app.get("/test")
async def root():
    return {"message": "Hello World", "mongodb_status": "connected"}

@app.get("/name/{name}")
async def say_my_name(name: str):
    return [
        {"message": f"Hello, my name is {name}!"},
        {"message2": f"Hello, my name is {name}!"},
        ]
