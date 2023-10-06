import functools
import mysql.connector
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from movieGo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        userName = request.form.get('name')
        userContact = request.form.get('phonenumber')
        userEmail = request.form.get('email')
        userPassword = request.form.get('password')

        db = get_db()
        error = None

        if not userName:
            error = 'Name is required.'
        elif not userContact:
            error = 'Phone Number is required.'
        elif not userEmail:
            error = 'Email Id is required.'
        elif not userPassword:
            error = 'Password is required.'

        if error is None:
            try:
                cursor = db.cursor()
                cursor.execute("INSERT INTO user(userName, userContact, userEmail, userPassword) VALUES (%s,%s,%s,%s)",
                               (userName, userContact, userEmail, generate_password_hash(userPassword)))
                db.commit()
                cursor.close()
                db.close()
            except mysql.connector.errors.IntegrityError:
                error = f"User {userEmail} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)

    return render_template('register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        print(username)
        db = get_db()
        print(db)
        error = None
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM user WHERE userEmail = '{username}'")
        userSelected = cursor.fetchone()
        print(userSelected)
        if userSelected is None:
            error = 'Incorrect username.'
        elif not check_password_hash(userSelected[4], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = userSelected[0]
            return redirect(url_for('book.slot'))
        print(error)
        flash(error)

    return render_template('login.html')
