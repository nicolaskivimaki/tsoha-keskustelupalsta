from app import app
from flask import render_template, request, redirect
import messages, categories, users
from posts import get_post
from comments import *
from likes import *
from feedback import *
from categories import get_categories_list, get_name, get_posts, new_category

@app.route("/")
def index():
    list = get_categories_list()
    latest_post = messages.get_latest_post()
    return render_template("index.html", count=len(list), categories=list, latest=latest_post)

@app.route("/newcategory", methods=["POST"]) 
def new_category():
    category = request.form["category"]
    if new_category(category):
        return redirect("/")
    else:
        return render_template("error.html", message="Uuden keskustelualueen luominen ei onnistunut")

@app.route('/category/<int:id>', methods=['get'])
def category(id):
    if request.method == 'GET':
        category = get_name(id)
        posts = get_posts(id)
        count = len(posts)
        return render_template('category.html', id=id, category=category, posts=posts, count=count)

@app.route('/category/<int:id>/<int:post_id>', methods=['get'])
def post(id, post_id):
    if request.method == 'GET':
        post = get_post(post_id)
        comments = get_comments(post_id)
        return render_template('post.html', id=id, post_id=post_id, post=post, comments=comments) 

@app.route("/category/<int:id>/send", methods=["POST"]) 
def send(id):
    title = request.form["title"]
    content = request.form["content"]
    if messages.new_post(title, content, id):
        return redirect(f"/category/{id}")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route('/category/<int:id>/<int:post_id>/comment', methods=['post'])
def comment(id, post_id):
    comment = request.form["comment"]
    if new_comment(comment, post_id):
        return redirect(f"/category/{id}/{post_id}")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/feedback")
def feedback():
    feedback_list = get_feedback()
    return render_template("feedback.html", feedback_list=feedback_list)

@app.route("/feedback/send", methods=['post'])
def send_feedback():
    content = request.form["content"]
    if new_feedback(content):
        return redirect("/feedback")
    else:
        return render_template("error.html", message="Palautteen lähetys ei onnistunut")

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