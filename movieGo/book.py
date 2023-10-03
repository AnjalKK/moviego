import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/slot')
def register():
    return render_template('booking.html')

