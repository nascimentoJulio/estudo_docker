import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/task", methods=["POST"])
def index():
    print("ola")
    return "Ola"

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=5000)