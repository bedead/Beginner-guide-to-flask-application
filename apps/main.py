# @author Satyam Mishra

# importing Flask

from flask import Blueprint, render_template

# Blueprint Configuration adding to main app
main = Blueprint(
    'main', __name__,
)

@main.route("/")
def home():
    # you can return using this command:
    return render_template("home.html")

# same way you can create multiple points

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
