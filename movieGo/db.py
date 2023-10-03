# from flask import current_app, g
# import mysql.connector
#
#
# def get_db():
#     if 'db' not in g:
#         connection_params = {
#             'host': 'localhost',
#             'user': 'root',
#             'password': 'h0hiehhiaf',
#             'database': 'moviego'
#         }
#         g.db = mysql.connector.connect(**connection_params)
#     return g.db
#
#
# def close_db(e=None):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()

