import os

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

username = "safoqwame99@gmail.com"
password = "0277364585"


@app.route('/', methods=["GET"])
def index():
    return render_template('render.html', view='login/index.html', valid=True)


@app.route('/sign_up')
def sign_up():
    return render_template('render.html', view='login/sign_up.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("username") != username or request.form.get('pass') != password:
            return render_template('render.html', view='login/index.html', valid=False,
                                   isAccountValid="True",
                                   isPasswordValid="True",
                                   input=request.form.get("username"))
        else:
            return render_template('render.html', view='landing/index.html', home='active')
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
def project():
    return render_template('tester.html')


if __name__ == '__main__':
    app.run()
