from fastapi import APIRouter
from ..models.todo import Todo
from ..configurations.database import collection_name
from ..schema.schema import list_serial
from bson import ObjectId


MyRouter = APIRouter()


@MyRouter.get("/")
async def get_todos_list():
    todos = list_serial(collection_name.find())
    # todos = list_serial(collection_name.find().limit(10))
    return todos

