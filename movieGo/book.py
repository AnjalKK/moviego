import functools
from movieGo.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/movie', methods=('GET','POST'))
def movie():
    if request.method == 'GET':
        db = get_db()
        error = None
        cursor = db.cursor()
        cursor.execute('SELECT * FROM movie WHERE movieId = 1')
        movieSelected = cursor.fetchone()

        return render_template('movie.html', content=movieSelected)

@bp.route('/slot',)
def slot():
    return render_template('booking.html')

