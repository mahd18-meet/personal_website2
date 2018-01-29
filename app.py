from flask import Flask, render_template, request, redirect , url_for
from flask.ext.sqlalchemy import SQLAlchemy


from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
heroku = Heroku(app)    
db = SQLAlchemy(app)
    
# Create our database model
class Links(db.Model):
    __tablename__ = "links"
    id = db.Column( db.Integer, primary_key=True)
    user = db.Column(db.String(120), unique=False)
    original_link = db.Column(db.String(120), unique=False)
    shortened_link = db.Column(db.String(350),unique =True)
    def __init__(self, user,original_link,shortened_link):
        self.user = user
        self.original_link = original_link
        self.shortened_link = shortened_link

    def __repr__(self):
        return '<User %r, original link %r , shortened link %r>' % (self.user, self.original_link, self.shortened_link)

db.create_all()
# Set "homepage" to index.html

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random strin



def random_letters():
    shortened_link = ""
    if request.form['spl'] == "":
        
        shortened_link= my_random_string()
        
    else:
        shortened_link = request.form['spl']

    return shortened_link



@app.route('/' , methods=['GET', 'POST'])
def home():

    if request.method == "GET":
        #show the webpage
        
        return render_template('home.html') 
    elif request.method=="POST":
        

        
        shortened_link=random_letters()
        
        link= Links(request.form['user'],request.form['original_link'],shortened_link)
        db.session.add(link)



        
        
        db.session.commit()

        

        
        
        
        

        
        return render_template('home.html' ,shortened_link=shortened_link )


@app.route('/link/<link>')
def submit(link):   
    link=Links.query.filter_by(shortened_link=link).first()
    x = link.original_link
    return render_template('gtl.html' ,link=x)


   





if __name__ == '__main__':
    app.debug = True
    app.run()