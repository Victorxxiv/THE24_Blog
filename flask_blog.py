from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '190badb1c44ce2be4b4942a0ca958d51'

posts = [
    {
        'author': 'Victor Mwendwa',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 02, 2024'
    },
    {
        'author': 'Ragnar Rock',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 03, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')

app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)