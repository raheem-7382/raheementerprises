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
                return redirect(url_for("products_dash"))
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

@app.route('/bathings')
def bathings():
    return render_template("bathings.html")

@app.route('/products_dash')
def products_dash():
    return render_template("products_dash.html")

@app.route('/clothings')
def clothings():
    return render_template("clothings.html")


@app.route('/skirts')
def skirts():
    return render_template("skirts.html")

@app.route('/shirts')
def shirts():
    return render_template("tshirts.html")

@app.route('/trousers')
def trousers():
    return render_template("trousers.html")

@app.route('/dresses')
def dresses():
    return render_template("dresses.html")

@app.route('/feedings')
def feedings():
    return render_template("feedings.html")

@app.route('/diapers')
def diapers():
    return render_template("diapers.html")

@app.route('/equipments')
def equipments():
    return render_template("p_equipments.html")

@app.route('/wipes')
def wipes():
    return render_template("wipes.html")

@app.route('/care')
def care():
    return render_template("care.html")

@app.route('/formula')
def formula():
    return render_template("formula.html")

@app.route('/tubs')
def tubs():
    return render_template("tubs.html")

@app.route('/seats')
def seats():
    return render_template("potty_seat.html")

@app.route('/thermo')
def thermo():
    return render_template("thermo.html")

@app.route('/hammocks')
def hammocks():
    return render_template("hammocks.html")

@app.route('/b_seats')
def b_seats():
    return render_template("b_seats.html")

@app.route('/tidies')
def tidies():
    return render_template("tidies.html")

@app.route('/touch')
def touch():
    return render_template("touch.html")

@app.route('/bags')
def bags():
    return render_template("bags.html")

@app.route('/mats')
def mats():
    return render_template("mats.html")

@app.route('/toys')
def toys():
    return render_template("toys.html")

@app.route('/feeds')
def feeds():
    return render_template("feedings.html")

@app.route('/bibs')
def bibs():
    return render_template("bibs.html")

@app.route('/bottles')
def bottles():
    return render_template("bottles.html")

@app.route('/soothers')
def soothers():
    return render_template("soothers.html")

@app.route('/chairs')
def chairs():
    return render_template("chairs.html")

@app.route('/h_chairs')
def h_chairs():
    return render_template("seats.html")

@app.route('/pampers')
def pampers():
    return render_template("pampers.html")

@app.route('/huggies')
def huggies():
    return render_template("huggies.html")

@app.route('/angels')
def angels():
    return render_template("little_angels.html")

@app.route('/rascal')
def rascal():
    return render_template("rascal.html")

@app.route('/fred')
def fred():
    return render_template("fred.html")

@app.route('/p_mats')
def p_mats():
    return render_template("p_mats.html")

@app.route('/gym')
def gym():
    return render_template("gym.html")

@app.route('/btoys')
def btoys():
    return render_template("btoys.html")

@app.route('/walkers')
def walkers():
    return render_template("walkers.html")

@app.route('/ptoys')
def ptoys():
    return render_template("ptoys.html")

@app.route('/aveeno')
def aveeno():
    return render_template("aveeno.html")

@app.route('/l_angels')
def l_angels():
    return render_template("l_angels.html")

@app.route('/w_huggies')
def w_huggies():
    return render_template("w_huggies.html")

@app.route('/w_pampers')
def w_pampers():
    return render_template("w_pampers.html")

@app.route('/water')
def water():
    return render_template("water.html")

@app.route('/aveeno_c')
def aveeno_c():
    return render_template("aveeno_c.html")

@app.route('/dove')
def dove():
    return render_template("dove.html")

@app.route('/infa')
def infa():
    return render_template("infa.html")

@app.route('/e45')
def e45():
    return render_template("e45.html")

@app.route('/jj')
def jj():
    return render_template("jj.html")

@app.route('/cocoa')
def cocoa():
    return render_template("cocoa.html")

@app.route('/aptamil')
def aptamil():
    return render_template("aptamil.html")

@app.route('/sma')
def sma():
    return render_template("sma.html")

@app.route('/cow')
def cow():
    return render_template("cow.html")

@app.route('/kenda')
def kenda():
    return render_template("kenda.html")

@app.route('/hipp')
def hipp():
    return render_template("hipp.html")

@app.route('/mammy')
def mammy():
    return render_template("mammy.html")

if __name__ == '__main__':
    app.run()
