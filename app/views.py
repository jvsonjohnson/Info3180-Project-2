import os
from app import app
from . import db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

###
# Routing.
###


class RegisterForm(FlaskForm):
    firstname = StringField("", validators=[DataRequired()])
    lastname = StringField("", validators=[DataRequired()])
    username = StringField("", validators=[DataRequired()])
    password = PasswordField(
        "", [validators.DataRequired(), validators.Length(max=70)])
    email = StringField("", validators=[DataRequired(), Email()])
    location = StringField("", validators=[DataRequired()])
    biography = StringField("", validators=[DataRequired()])
    photo = FileField(validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])


class Users(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(120))
    email = db.Column(db.String(120))
    location = db.Column(db.String(120))
    biography = db.Column(db.String(255))
    profile_photo = db.Column(db.String(255))
    joined_on = db.Column(db.String(255))

    def __init__(self, first_name, last_name, gender, email, location,
                 biography, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = paswword
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on


@app.route("/api/users/register", methods=["POST"])
def register():

    form = RegisterForm()
    if request.method == "POST" and uform.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.profile_photo.data
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        joined = format_date_joined()

        new_user = Users(firstname, lastname, username, password,
                         email, location, biography, profile_photo, joined)

        db.session.add(new_user)
        db.session.commit()

    return render_template("index.html", form=form)


'''
@app.route("/api/auth/login", methods=["POST"])
def login():
    username = form.username.data
    password = form.username.data


@app.route("/api/auth/logout", methods=["GET"])
def logout():


@app.route("/api/users/{user_id}/posts", methods=["GET"])
def viewposts():


@app.route("/api/users/{user_id}/posts", methods=["POST"])
def createposts():


@app.route("/api/users/{user_id}/follow", methods=["POST"])
def follow():


@app.route("/api/posts", methods=["GET"])
def posts():


@app.route("/api/posts/{post_id}/like", methods=["POST"])
def like():
'''


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    Because we use HTML5 history mode in vue-router we need to configure our
    web server to redirect all routes to index.html. Hence the additional route
    "/<path:path".

    Also we will render the initial webpage and then let VueJS take control.
    """
    return render_template('index.html')


def format_date_joined():
    import datetime
    now = datetime.datetime.now()  # today's date
    date_joined = now  # a specific date
    return date_joined.strftime("%B %V, %Y")


def get_uploaded_images():
    import os
    rootdir = os.getcwd()
    print(rootdir)
    ilist = []
    for subdir, dirs, files in os.walk(rootdir + r'\app\static\uploads'):
        for file in files:
            ilist.append(file)

    return ilist


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
