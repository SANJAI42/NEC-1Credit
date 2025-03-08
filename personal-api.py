from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Sanjai J"


@app.route("/registerNumber")
def register_number():
    return "22IT042"

@app.route("/department")
def department():
    return "IT(Information Technology)"

if _name__ == "__main__":
    app.run(debug =True)
