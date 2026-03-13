from flask import Flask, render_template, request
from form import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        return "Register Successful"
    return render_template("register.html", form=form)


app.run(debug=True)
