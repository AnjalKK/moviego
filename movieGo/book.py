import functools
from movieGo.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/movieList', methods=('GET', 'POST'))
def movielist():
    if request.method == 'GET':
        db = get_db()
        error = None
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM movie')
        movieSelected = cursor.fetchall()
        db.close()
        return render_template('index.html', content=movieSelected)


@bp.route('/movie/<int:movie_id>', methods=('GET', 'POST'))
def movie(movie_id):
    if request.method == 'GET':
        db = get_db()
        error = None
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM movie where movieId = {movie_id}")
        movieSelected = cursor.fetchone()
        db.close()
        return render_template('movie.html', content=movieSelected)


@bp.route('/slot', )
@login_required
def slot():
    return render_template('booking.html')
