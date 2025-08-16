from flask import Flask, render_template, request, jsonify

"""
It creates instance of Flask class,
whill will be your WSGI app
"""
app = Flask(__name__)


@app.route("/hi")
def welcome():
    return "Hello"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/user", methods=["GET"])
def user():
    user = {"name": "sudhanshu", "age": "24"}
    return user


@app.route("/book/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    return f"Book {book_id} deleted"


@app.route("/book", methods=["POST"])
def create_book():
    if "name" not in request.json:
        return jsonify("Book name not provided")
    new_book = {"book_name": request.json["name"]}
    return f"Book {request.josn['name']} created"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return f"Hello {request.form['name']}"
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
