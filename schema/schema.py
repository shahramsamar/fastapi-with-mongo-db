
def my_serializer(todo):
    """Define a function to serialize and deserialize the json values"""
    """We have an ID by Default"""
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "descripttion": todo["description"],
        "isdone": todo["isdone"],
    }

def list_serial(todos):
    """Sometimes we need to return those datas as a list"""
    return [my_serializer(todo) for todo in todos]