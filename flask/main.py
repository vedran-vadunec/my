
from flask import Flask
app=Flask(__name__)

@app.route("/")
def test():
    return ("Hello World!!")
@app.route("/about")
def about():
    return ("Ovo je about stranica!")
@app.route("/hello/<user_id>")
def hello(user_id):
    return("Hello {0}".format(user_id))

if __name__ == '__main__':
    app.run(debug=True)