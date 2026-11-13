from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    return f"<h2>Hello {name}</h2>"

if __name__ == "__main__":
    app.run(debug=False)
