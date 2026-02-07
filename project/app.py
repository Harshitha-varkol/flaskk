from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Correct database path (matches your instance folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    qualification = db.Column(db.String(40))
    address = db.Column(db.String(40))


# Create tables
with app.app_context():
    db.create_all()


# Home page
@app.route('/')
def home():
    return render_template("index.html")


# Create user
@app.route("/create", methods=["POST"])
def create():
    name = request.form.get('name')
    age = int(request.form.get('age'))   # FIXED
    qualification = request.form.get('qualification')
    address = request.form.get('address')

    user = User(
        name=name,
        age=age,
        qualification=qualification,
        address=address
    )

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template("success.html")


# View all users
@app.route("/view")
def view():
    data = User.query.all()
    return render_template("view.html", data=data)


# Edit user
@app.route("/edit/<int:id>")
def edit(id):
    user = db.session.get(User, id)   # FIXED modern way
    return render_template("edit.html", data=user)


# Update user
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    user = db.session.get(User, id)

    if user:
        user.name = request.form.get('name')
        user.age = int(request.form.get('age'))   # FIXED
        user.qualification = request.form.get('qualification')
        user.address = request.form.get('address')
        db.session.commit()

    return redirect('/view')


# Delete user
@app.route("/delete/<int:id>")
def delete(id):
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/view")


if __name__ == "__main__":
    app.run(debug=True)

























































































































































































# from flask import *
# from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'

# db=SQLAlchemy(app)

# class User(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(30))
#     age=db.Column(db.Integer)
#     qualification=db.Column(db.String(40))
#     address=db.Column(db.String(40))


# with app.app_context():
#     db.create_all()


# @app.route("/create",methods=["POST"])
# def create():
#     if request.method=="POST":

#         id=request.form.get('id')
#         name=request.form.get('name')
#         age=request.form.get('age')
#         qualification=request.form.get('qualification')
#         address=request.form.get('address')
#         new_create=User(id=id,name=name,age=age,qualification=qualification,address=address)
#         db.session.add(new_create)
#         db.session.commit()
         
#         # return redirect('/')
#         return redirect(url_for('success'))



# ##index page
# @app.route('/')
# def home():
#     return render_template("index.html") 


# ##details page
# @app.route('/details')
# def details():
#     return render_template("details.html")

# ##success
# @app.route('/success')
# def success():
#     return render_template("success.html")

# ##view
# @app.route("/view")
# def view():
#     data = User.query.all()   # replace YourModel with your table class name
#     return render_template("view.html", data=data)

# ##getting the data to edit
# @app.route("/edit/<int:id>")
# def edit(id):
#     data=User.query.get_or_404(id)
#     return render_template("edit.html",data=data)

# # updating the data
# # @app.route('/update/<int:id>',methods=['POST'])
# # def update(id):
# #     user = User.query.get(id)
# #     User.id=request.form['id']
# #     User.name=request.form['name']
# #     User.age=request.form['age']
# #     User.qualification=request.form['qualification']
# #     User.address=request.form['address']
# #     db.session.commit()
# #     return redirect('/edit')

# @app.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     user = User.query.get(id)

#     if user:
#         user.name = request.form.get('name')
#         user.age = request.form.get('age')
#         user.qualification = request.form.get('qualification')
#         user.address = request.form.get('address')

#         db.session.commit()

#     return redirect('/view')   # go back to table page
# ##delete
# @app.route("/delete/<int:id>")
# def delete(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect("/view")   # go back to table page

    
# if __name__=="__main__":
#     app.run(debug=True)