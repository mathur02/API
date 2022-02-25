from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

# from cricket.user_manager import UserManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:farcry1234@localhost/cricketer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from cricket import routes