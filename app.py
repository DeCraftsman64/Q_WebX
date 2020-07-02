import os

from flask import Flask, render_template, request, jsonify
from jinja2 import Template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('render.html', view='login/index.html')


@app.route('/home')
def home():
    return render_template('render.html', view='landing/render.html', home='active')


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


if __name__ == '__main__':
    app.run()
