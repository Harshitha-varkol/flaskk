
from flask import *
from flask_sqlalchemy import SQLALchemy
app.config['SQLALCHEMY_DATEBASE_URL']='sqlite://mydb.db'
db=SQLALchemy(app)

app=Flask(__name__)

# @app.route("/user/<name>")
# def info(name):
#     return render_template("index.html",name=name)

# @app.route("/")
# def display():
#     return "this is programming language"
# @app.route("/")
# def display():
#     return render_template("index.html")

# @app.route("/get",methods=["GET"])
# def get():
#     name=request.args.get("name")
#     password=request.args.get("password")
#     if name=="harshitha" and password=="harshi":
#         return f"welcome {name}"
#     else:
#         return f"invalid {name}"



@app.route("/get",methods=["POST"])
def post():
    name=request.form.get("name")
    password=request.form.get("password")
    return f"{name},{password}"


@app.route("/")
def display():
    return render_template("index.html")
 





if __name__=="__main__":
    app.run(debug=True)





