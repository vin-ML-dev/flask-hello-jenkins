from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello world from jenkins!!!"


if __name__ == "__main__":
   #port = int(os.environ.get("PORT", 5000))
   app.run(host='23.23.65.192', port="5000")
