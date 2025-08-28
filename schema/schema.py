
def my_serializer(todo) -> dict:
    """Define a function to serialize and deserialize"""
    """We have an ID by Default"""
    return {
        "id": str(todo["id"]),
        "name": todo["name"],
        "descripttion": todo["description"],
        "isdone": todo["isdone"],
    }

def list_serial(todos) -> list:
    """Sometimes we need to return those datas as a list"""
    return [my_serializer(todo) for todo in todos]