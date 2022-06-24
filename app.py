from email.policy import default
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#creating a database for our app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
db = SQLAlchemy(app)
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    Author = db.Column(db.String(20), nullable = False, default = 'N/A')
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    
    def __rpr__(self):
        return "Blog Post " + str(self.id)
    
# ---------------testing arguement-----------------
# @app.route('/')
# x = 'name'
# name = f'/home/<string:{x}>'
# ------------------------------
# @app.route('/home/<string:name>') # for single element
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "hello, Mr "+ name + " your id is: "+ str(id)
#making a post or get request
@app.route('/home/onlyget', methods = ['GET'])
def only_get():
    return "this funtion returns only get request"

@app.route('/home/onlypost', methods= ['POST'])
def only_post():
    return "this funtion returns only post request"

#allowing both get and post methods
@app.route('/home/both', methods = ['GET', 'POST'])
def both():
    return "this funtion returns both post and get request"

# ------------WRITING THE FRONTEND --------------
@app.route('/')
def home():
    return render_template('index.html')

#lests create a dummy post and send to our postd.html file
all_post = [
    {
        "title" : "this is our post 1.",
        "contents" : "this is the content of the post yeeeeyyyy....",
        "Author": "caleb chima"
    },
    {
        "title" : "this is our post 2.",
        "contents" : "this is the content of the second post yeeeeyyyy...."
    }
]

#creating a post rout
@app.route('/posts')
def post():
    return render_template('posts.html', posts =  all_post)


if __name__ == "__main__":
    app.run(debug=True)