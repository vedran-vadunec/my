
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/<greeting>")
def template_test():
    return render_template("template.html",my_string=greeting)


if __name__ == '__main__':
    app.run(debug=True)