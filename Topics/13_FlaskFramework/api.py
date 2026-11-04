## PUT and DELETE
## Working with API's

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in To-Do List
items = [
    {"id": 1, "name": "Item1", "description": "This Is Item1"},
    {"id": 2, "name": "Item2", "description": "This Is Item2"},
]


@app.route("/")
def home():
    return "Welcome to Sample To-Do List App"


# GET :- Retrive All Items.
@app.route("/item", methods=["GET"])
def get_items():
    return jsonify(items)


# GET :- Retrive Specific Item By ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item Not Found"})
    return jsonify(item)


# POST :- Create New Task
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"error": "Item Not Found"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"],
    }
    items.append(new_item)
    return new_item


# PUT
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item Not Found"})
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item)


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item Deleted"})


if __name__ == "__main__":
    app.run(debug=True)
