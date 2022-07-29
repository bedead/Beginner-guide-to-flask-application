# importing Flask 
from flask import Flask, render_template

# this is name for your app (it can be anything)
name = "Medium blog example"
app = Flask(name)

# To specify route in which particular html file will be passed.
# "/" is root directory
@app.route("/")
def home():
    # you can type complete html inside quotes.
    return "<h1>This is a Home app.</h1>"
    
    # you can return using this command:
    # return render_template(html file name)

# same way you can create multiple points
@app.route("/about")
def about():
    return "<h1>This is About Page.</h1>"

@app.route("/contact")
def contact():
    return "<h1>This is Contact Page.</h1>"

# you can use directly run the flask server be running the app.py file
if __name__=="__main__":
    # debug should be True if website is under development
    # and False in other cases
    app.run(debug=True)

