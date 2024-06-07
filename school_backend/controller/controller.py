from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime

routes = Blueprint('routes', __name__)

@routes.route('/teste', methods=['GET'])
def teste():
    return render_template('teste.html')

@routes.route('/school', methods=['GET'])
def get_all():
    return jsonify({'message': 'Hello World'})

@routes.route('/school/{id}', methods=['GET'])
def get_by_id(id: int):
    return jsonify({'message': 'Hello World'})