from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
db = SQLAlchemy(app)

class User(db.Model):
  sno = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(200), nullable=False)
  password = db.Column(db.String(250), nullable=False)
  datetime = db.Column(db.DateTime, default=datetime.utcnow)

# creating db if it's not created
with app.app_context():
  db.create_all()

@app.route('/' , methods = ["GET", 'POST'])
def home():
  extend_base = request.args.get('extend', 'false').lower() == 'true'
  all_user = User.query.all()
  if request.method == 'POST':
    # Handle form submission
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Login received: {username}"
  return render_template('home.html', name="Doxa", extend_base=extend_base)

@app.route('/about')

def about():
  return render_template('about.html')

@app.route('/art1')

def art1():
  return render_template('page2.html')

@app.route('/disabledform')
def dlogin():
  return render_template('disabledfieldset.html')

@app.route('/login', methods = ["GET", 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    print(username)
    new_user = User(
      username = username,
      password = password
    )
    db.session.add(new_user)
    db.session.commit()
  return render_template('loginform.html')


'''
@app.route('/about')

def about():
  return "hell"

@app.route('/about')

def about():
  return "hell"

@app.route('/about')

def about():
  return "hell"

@app.route('/about')

def about():
  return "hell"

@app.route('/about')

def about():
  return "hell"


@app.route('/about')

def about():
  return "hell"


@app.route('/about')

def about():
  return "hell"

@app.route('/about')

def about():
  return "hell"

  '''

if __name__ == "__main__":
  app.run(debug=True) # during deployment we remove the inner value. done only during development to see live change