import os

from flask import render_template, request, session
from flask_session import Session
from sqlalchemy.exc import IntegrityError

from _models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configuring Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
Session(app)


# username = "safoqwame99@gmail.com"
# password = "0277364585"


@app.route('/', methods=["GET", "POST"])
def index():
    if session.get("projects") is not None:
        session["projects"].clear()
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('your_email')
        password = request.form.get('password')
        account = Account(first_name=first_name, last_name=last_name, username=username, pass_code=password)
        db.session.add(account)
        try:
            db.session.commit()
            return render_template('render.html', view='login/index.html', valid=True)
        except IntegrityError as e:
            source = request.host_url
            cause = "Unable To Create Account"
            suggestion = "Please check form data or resubmit form"
            return render_template('error.html', source=source, cause=cause, suggestion=suggestion)
    elif request.method == "GET":
        return render_template('render.html', view='login/index.html', valid=True)


@app.route('/sign_up')
def sign_up():
    return render_template('render.html', view='login/sign_up.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pass")
        account = Account.query.filter_by(username=username).first()
        print(f"username: {account.username} ; password: {account.pass_code}")
        if account.username is None or account.pass_code != password:
            # if request.form.get("username") != username or request.form.get('pass') != password:
            print("Account Invalid")
            return render_template('render.html', view='login/index.html', valid=False,
                                   isPasswordValid="True",
                                   isAccountValid="True",
                                   input=request.form.get("username"))
        else:
            print('Account Valid')
            projects = account.projects
            if session.get("projects") is None:
                session["projects"] = []
            for pro in projects:
                session["projects"].append(pro)
                print(pro)
            return render_template('render.html', view='landing/index.html', home='active',
                                   projects=projects)
    else:
        return render_template('render.html', view='landing/index.html', home='active')


@app.route('/about')
def about():
    return render_template('render.html', view='landing/about.html', about='active')


@app.route('/blog')
def route():
    return render_template('render.html', view='landing/blog.html', blog='active')


@app.route('/contact')
def contact():
    return render_template('render.html', view='landing/contact.html', contact='active')


@app.route('/elements')
def elements():
    return render_template('render.html', view='landing/elements.html')


@app.route('/main')
def mains():
    return render_template('render.html', view='landing/main.html')


@app.route('/package')
def package():
    return render_template('render.html', view='landing/package.html', package='active')


@app.route('/search')
def search():
    return render_template('render.html', view='landing/search.html')


@app.route('/single-blog')
def single_blog():
    return render_template('render.html', view='landing/single-blog.html', )


@app.route('/support')
def support():
    return render_template('render.html', view='landing/Support.html', support='active')


@app.route('/blog')
def blog():
    return render_template('render.html', view='landing/blog.html')


@app.route('/intro')
def intro():
    return render_template('render.html', view='landing/intro.html', home='active')


@app.route('/demo')
def demo():
    return render_template('landing/demoQ.html')


notes = []
code = ''


@app.route('/project', methods=["GET", "POST"])
def project():
    global code
    if request.method == "POST":
        if "form1" in request.form:
            note = request.form.get('note')
            notes.append(note)
            print(notes)
        if 'form2' in request.form:
            code = request.form.get("code")
    return render_template('landing/pro/web.html', notes=notes, code=code)


@app.route('/projects/<string:location>', methods=['GET'])
def projects(location):
    global code
    if request.method == 'POST':
        if "form1" in request.form:
            note = request.form.get('note')
            notes.append(note)
            print(notes)
        elif 'form2' in request.form:
            code = request.form.get("code")
        return render_template('landing/pro/{}'.format(location), notes=notes, code=code)
    else:
        return render_template('landing/pro/{}'.format(location))


@app.route('/gen')
def gen():
    account = Account.query.get(2)
    account.add_project("Web Development", "web.html")
    account.add_project("Staging Pro", "pro_database.html")
    # db.create_all()
    return render_template('error.html', cause="successes")


if __name__ == '__main__':
    app.run()
