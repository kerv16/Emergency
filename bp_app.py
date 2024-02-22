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


@app.route("/emeregency/get_all_status",methods=["POST","GET"])
def get_all_status():
	_file = open(c.JSON_PATH,"r")
	_data = json.loads(_file.read())
	return jsonify(_data)



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