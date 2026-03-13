from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from form import RegisterForm, LoginForm
from model.user import db, User   # make sure user.py is in same folder

app = Flask(__name__)

app.config['SECRET_KEY'] = 'superman'
app.config['SQLALCHEMY_DATABASE_URI'] = \
'postgresql://postgres:Mayankhenry123%2A@127.0.0.1:5432/test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ================= REGISTER =================
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# ================= LOGIN =================
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        return "Invalid credentials"
    return render_template('login.html', form=form)


# ================= DASHBOARD =================
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)



# ================= LOGOUT =================
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



# ================= DELETE ACCOUNT =================
@app.route('/delete_account', methods=["POST"])
@login_required
def delete_account():
    user = User.query.get(current_user.id)
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('register'))


# ================= UPDATE EMAIL =================
@app.route('/update_email', methods=["GET", "POST"])
@login_required
def update_email():
    form = RegisterForm()
    user = User.query.get(current_user.id)

    if form.validate_on_submit():
        user.email = form.email.data
        db.session.commit()
        return redirect(url_for('dashboard'))

    form.email.data = user.email
    return render_template('update_email.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
     