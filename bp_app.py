from datetime import date, datetime
from flask import Blueprint, render_template, request, session, redirect, jsonify, Response,send_file
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os, random, json, shutil, base64, sys, warnings, csv, xlrd
from werkzeug.utils import secure_filename
from flask_cors import CORS,cross_origin

import pandas as pd
from tqdm import tqdm

app = Blueprint("emeregency",__name__,template_folder='pages')
rapid_mysql = mysql(*c.DB_CRED)

# JSON_PATH = "assets/response/devices.json"
# app = Flask(__name__)

@app.route("/emeregency")
@app.route("/emeregency/dashboard")
def dashboard():
	return render_template('ft_index.html')


@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/emeregency/get_all_status",methods=["POST","GET"])
def get_all_status():
	all_users = {}
	# _file = open(c.JSON_PATH,"r")
	# _data = _file.read()
	for fname in os.listdir(c.JSON_PATH):
		_file = open(c.JSON_PATH+fname,"r")
		_data = json.loads(_file.read())
		all_users[fname] = _data
	return jsonify(all_users)
	# return jsonify(_data)


@app.route("/emeregency/set_users/<name>",methods=["POST","GET"])
def set_users(name):
	user = {}
	for key in request.form:
		user[key] = request.form[key]

	_file = open(c.JSON_PATH+name,"w")
	_data = _file.write(json.dumps(user))
	_file.close()

	return "DONE"

@app.route("/dl/<file_>",methods=["POST","GET"])
def download_file(file_):
	# today = str(datetime.today()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_")
	# def_name = "{}_{}".format(today,file_)
	def_name = file_
	return send_file(file_, as_attachment=True,download_name=def_name)




# ======================================
_data_struct = [
	{
		"name" : "",
		"device" : "",
		"latlong" : "",
		"num" : "",
		"emer_num" : "",
		"accel" : "",
		"gyro" : "",
		"axis" : "",
		"status" : ""
	}
]