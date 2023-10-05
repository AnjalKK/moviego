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
