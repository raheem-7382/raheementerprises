from flask import Flask,render_template,request,flash,redirect,url_for,session
from flask_bcrypt import generate_password_hash,check_password_hash
from database import User

app = Flask(__name__)
app.secret_key = "raheem"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form["x"]
        email = request.form["y"]
        password = request.form["z"]
        password = generate_password_hash(password)
        User.create(name=name,email=email,password=password)
        flash("Account created successfully")
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form["x"]
        password = request.form["y"]
        try:
            user = User.get(User.email==email)
            hashed_password = user.password
            if check_password_hash(hashed_password,password):
                flash("Logged in successfully")
                session["logged_in"] = True
                session["name"] = user.name
                session["id"] = user.id
                return redirect(url_for("dashboard"))
            else:
                flash("Wrong email or password")
        except User.DoesNotExist:
            flash("No such user registered")

    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if not session["logged_in"]:
        return redirect(url_for("login"))
    users = User.select()
    return render_template("dashboard.html",fetched_users = users)

@app.route('/delete/<int:id>')
def my_delete(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    User.delete().where(User.id == id).execute()
    flash("User deleted successfully")
    return redirect(url_for("dashboard"))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def my_update(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    #     Select user you want to update
    user = User.get(User.id == id)

    if request.method == "POST":
        name = request.form["x"]
        email = request.form["y"]
        password = request.form["y"]
        # Start updating user values
        user.name = name
        user.email = email
        user.password = password

        # Return the user values back to database
        user.save()
        flash("User updated successfully")
        return redirect(url_for("dashboard"))
    return render_template("update.html", selected_user=user)


@app.route('/inventory')
def inventory():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("products.html")

@app.route('/shoes')
def shoes():
    return render_template("shoes.html")

@app.route('/hoodies')
def hoodies():
    return render_template("hoodies.html")

@app.route('/scarves')
def scarves():
    return render_template("scarves.html")

@app.route('/blankets')
def blankets():
    return render_template("blankets.html")

@app.route('/pull_necks')
def pull_necks():
    return render_template("pull_necks.html")

@app.route('/marvins')
def marvins():
    return render_template("marvins.html")

if __name__ == '__main__':
    app.run()
