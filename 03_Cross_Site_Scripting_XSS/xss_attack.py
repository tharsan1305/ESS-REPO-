
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data = request.form.get("name", "")
    output = data if "unsafe" in request.form else escape(data)

    return f"""
    <form method="POST">
        <input name="name">
        <button name="unsafe">Unsafe</button>
        <button name="safe">Safe</button>
    </form>
    <h3>{output}</h3>
    """

app.run()
