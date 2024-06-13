from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime

routes = Blueprint('routes', __name__)

alunos = [
    {
        'id': 1,
        'nome': 'João',
        'idade': 20,
        'endereço': 'Rua 1',
        'anoLetivo': 2021
    },
    {
        'id': 2,
        'nome': 'Maria',
        'idade': 21,
        'endereço': 'Rua 2',
        'anoLetivo': 2021
    },
    {
        'id': 3,
        'nome': 'José',
        'idade': 22,
        'endereço': 'Rua 3',
        'anoLetivo': 2021
    }
]

materias = [
    {
        'id': 1,
        'nome': 'Matemática',
    },
    {
        'id': 2,
        'nome': 'Português',
    },
    {
        'id': 3,
        'nome': 'História',
    }
]

provas = [
    {
        'id': 1,
        'aluno_id': ''.join(str(alunos[0]['id'])),
        'nota': 8,
    },
    {
        'id': 2,
        'aluno_id': ''.join(str(alunos[1]['id'])),
        'nota': 9,
    },
    {
        'id': 3,
        'aluno_id': ''.join(str(alunos[2]['id'])),
        'nota': 10,
    }
]

@routes.route('/get/alunos/', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@routes.route('/get/alunos/<int:id>', methods=['GET'])
def get_alunos_id(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return jsonify(aluno)
        else:
            return jsonify({'message': 'Aluno não encontrado'})
        
@routes.route('/post/alunos/', methods=['POST'])
def post_alunos():
    return jsonify({'message': 'Hello World'})

@routes.route('/delete/alunos/{id}', methods=['DELETE'])
def delete_alunos(id: int):
    return jsonify({'message': 'Hello World'})


#rotas para materias
@routes.route('/get/materias/', methods=['GET'])
def get_materias():
    return jsonify(materias)

@routes.route('/get/materias/{id}', methods=['GET'])
def get_materias_id(id: int):
    return jsonify({'message': 'Hello World'})

@routes.route('/post/materias/', methods=['POST'])
def post_materias():
    return jsonify({'message': 'Hello World'})

@routes.route('/delete/materias/{id}', methods=['DELETE'])
def delete_materias(id: int):
    return jsonify({'message': 'Hello World'})


#rotas para provas
@routes.route('/get/provas/', methods=['GET'])
def get_provas():
    return jsonify(provas)

@routes.route('/get/provas/{id}', methods=['GET'])
def get_provas_id(id: int):
    return jsonify({'message': 'Hello World'})

@routes.route('/post/provas/', methods=['POST'])
def post_provas():
    return jsonify({'message': 'Hello World'})

@routes.route('/delete/provas/{id}', methods=['DELETE'])
def delete_provas(id: int):
    return jsonify({'message': 'Hello World'})
