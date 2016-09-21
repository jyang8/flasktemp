from flask import Flask

app = Flask(__name__)

@app.route("/")
def msgOne():
    return "Welcome!"

@app.route("/pg01")
def msgTwo():
    return "Filling up flask..."

@app.route("/pg02")
def msgThree():
    return "Goodbye!"

if __name__ == "__main__":
    app.run()
