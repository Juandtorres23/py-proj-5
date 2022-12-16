"""Server for movie ratings app."""
from flask import (Flask, 
                    render_template, 
                    request, 
                    flash, 
                    session, 
                    redirect)
from jinja2 import StrictUndefined

from model import connect_to_db, db

import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    ''' View Homepage.'''

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    ''' View all movies. '''

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)