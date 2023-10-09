from movieGo.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta

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
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM movie where movieId = {movie_id}")
        movieSelected = cursor.fetchone()
        db.close()
        return render_template('movie.html', content=movieSelected, movie_id=movie_id)


@bp.route('/movie/<int:movie_id>/show', methods=('GET', 'POST'))
def slot(movie_id):
    if request.method == 'GET':
        movie_show_datetime = request.args.get('datetime')
        if movie_show_datetime is None:
            current_datetime = datetime.utcnow()
            target_times = [10, 14, 18]
            nearest_target_time = None
            for target_time in target_times:
                target_datetime = current_datetime.replace(hour=target_time, minute=0, second=0, microsecond=0)
                if target_datetime > current_datetime:
                    nearest_target_time = target_datetime
                    break
            if nearest_target_time is None:
                next_day = current_datetime + timedelta(days=1)
                nearest_target_time = next_day.replace(hour=target_times[0], minute=0, second=0, microsecond=0)
            formatted_datetime = nearest_target_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
            movie_show_datetime = formatted_datetime

        input_datetime = datetime.strptime(movie_show_datetime, '%a, %d %b %Y %H:%M:%S GMT')
        mysql_datetime_str = input_datetime.strftime('%Y-%m-%d %H:%M:%S')
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT date_time FROM movie_show WHERE movie_id = {movie_id}")
        date = cursor.fetchall()
        cursor.execute(f"SELECT movie_show_id FROM movie_show WHERE date_time = '{mysql_datetime_str}'")
        movie_show = cursor.fetchone()
        movie_show_id = movie_show['movie_show_id']
        cursor.execute(f"SELECT * FROM seat WHERE movie_show_id = {movie_show_id}")
        seats = cursor.fetchall()
        db.close()
        return render_template('booking.html', content=seats, movie_id=movie_id, dates=date)

    if request.method == 'POST':
        data = request.get_json()
        selected_seats = data.get("selectedSeats", [])
        seatNumbers = [int(seat_id[1:]) - 1 for seat_id in selected_seats]
        print(seatNumbers)
        movie_show_datetime = request.args.get('datetime')
        if movie_show_datetime is None:
            current_datetime = datetime.utcnow()
            target_times = [10, 14, 18]
            nearest_target_time = None
            for target_time in target_times:
                target_datetime = current_datetime.replace(hour=target_time, minute=0, second=0, microsecond=0)
                if target_datetime > current_datetime:
                    nearest_target_time = target_datetime
                    break
            if nearest_target_time is None:
                next_day = current_datetime + timedelta(days=1)
                nearest_target_time = next_day.replace(hour=target_times[0], minute=0, second=0, microsecond=0)
            formatted_datetime = nearest_target_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
            movie_show_datetime = formatted_datetime
        input_datetime = datetime.strptime(movie_show_datetime, '%a, %d %b %Y %H:%M:%S GMT')
        mysql_datetime_str = input_datetime.strftime('%Y-%m-%d %H:%M:%S')
        print(mysql_datetime_str)
        # Execute the SQL query to update the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT movie_show_id FROM movie_show WHERE date_time = '{mysql_datetime_str}'")
        movie_show = cursor.fetchone()
        print(movie_show)
        movie_show_id = movie_show[0]
        cursor.execute(f"UPDATE seat SET is_reserved = 1 WHERE seat_number IN ({','.join(map(str, seatNumbers))}) AND "
                       f"movie_show_id = {movie_show_id}")
        db.commit()
        db.close()
        return redirect('/book/payment')


@bp.route('/payment', methods=('GET', 'POST'))
def payment():
    print("rediredcted")
    if request.method == 'GET':
        return render_template('bill.html')


@bp.route('/confirm', methods=('GET', 'POST'))
def confirmation():
    if request.method == 'GET':
        return render_template('bookingconfirmation.html')
