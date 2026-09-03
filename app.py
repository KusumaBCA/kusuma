from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "lav", "email": "abc@gmail.com"},
    {"id": 2, "name": "ma", "email": "123@gmail.com"},
    {"id": 3, "name": "hemu", "email": "lav@gmail.com"},
    {"id": 4, "name": "meenu", "email": "145@gmail.com"},
    {"id": 5, "name": "kav", "email": "def@gmail.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "success": True,
        "message": "data retrieved successfully",
        "count": len(users),
        "data": users
    }), 200


@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    for user in users:
        if user["id"] == uid:
            return jsonify({
                "success": True,
                "message": "data is found successfully",
                "data": user
            }), 200

    return jsonify({
        "success": False,
        "message": "data not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)