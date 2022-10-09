from app import app
from flask import render_template, request, redirect
import messages, categories, users
from categories import get_categories_list, get_name, get_posts

@app.route("/")
def index():
    categories.create_categories()
    list = get_categories_list()
    latest_post = messages.get_latest_post()
    return render_template("index.html", count=len(list), categories=list, latest=latest_post)

@app.route('/category/<int:id>', methods=['get'])
def category(id):
    if request.method == 'GET':
        category = get_name(id)
        posts = get_posts(id)
        count = len(posts)
        return render_template('category.html', id=id, category=category, posts=posts, count=count)

@app.route("/send", methods=["POST"])
def send():
    title = request.form["title"]
    content = request.form["content"]
    if messages.new_post(title, content):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")