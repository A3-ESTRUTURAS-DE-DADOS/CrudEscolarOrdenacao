from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime
from flask_login import login_user, login_required, current_user, logout_user

routes = Blueprint('routes', __name__)

