from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    return render_template_string(
        "<h2>Hello {{ name }}</h2>", name=name
    )

if __name__ == "__main__":
    app.run(port=5001, debug=False)
