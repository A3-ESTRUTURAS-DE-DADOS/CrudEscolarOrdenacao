from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime 
from app.models import Aluno, Materia, Prova

routes = Blueprint('routes', __name__)

@routes.route('/get/alunos/', methods=['GET'])
def get_alunos():
    try:
        query = Aluno.query.order_by(Aluno.id).all()
        return jsonify({'Alunos': [Aluno.to_dict(aluno) for aluno in query]}, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/get/alunos/<int:id>', methods=['GET'])
def get_alunos_id(id):
    try:
        query = Aluno.query.filter_by(id=id).first()
        return jsonify(query)
    except Exception as e:
        return jsonify({'error': str(e)})
        
@routes.route('/post/alunos/', methods=['POST'])
def post_alunos():
    try:
        dataNome = request.json['nome']
        dataIdade = request.json['idade']
        dataEndereco = request.json['endereco']
        dataAno = request.json['ano_letivo']
        
        aluno = Aluno(nome=dataNome, idade=dataIdade, endereco=dataEndereco, ano_letivo=dataAno)
        
        db.session.add(aluno)
        db.session.commit()
        
        return jsonify({'Aluno criado': Aluno.to_dict(aluno)}, 201)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/put/alunos/<int:id>', methods=['PUT'])
def put_alunos(id: int):
    try:
        query = Aluno.query.filter_by(id=id).first()
        query.nome = request.json['nome']
        query.idade = request.json['idade']
        query.endereco = request.json['endereco']
        query.ano_letivo = request.json['ano_letivo']
        
        db.session.commit()
        
        return jsonify({'Aluno atualizado': Aluno.to_dict(query) }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/delete/alunos/{id}', methods=['DELETE'])
def delete_alunos(id: int):
    try:
        query = Aluno.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        
        return jsonify({'Aluno deletado': query }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})


#rotas para materias
@routes.route('/get/materias/', methods=['GET'])
def get_materias():
    try:
        query = Materia.query.order_by(Materia.id).all()
        return jsonify({'Materias': [Materia.to_dict(materia) for materia in query]}, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/get/materias/<int:id>', methods=['GET'])
def get_materias_id(id: int):
    try:
        query = Materia.query.filter_by(id=id).first()
        return jsonify(query, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/post/materias/', methods=['POST'])
def post_materias():
    try:
        dataNome = request.json['nome']
        
        materia = Materia(nome=dataNome)
        
        db.session.add(materia)
        db.session.commit()
        
        return jsonify({'Materia criada': Materia.to_dict(materia)}, 201)
    
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/put/materias/<int:id>', methods=['PUT'])
def put_materias(id: int):
    try:
        query = Materia.query.filter_by(id=id).first()
        query.nome = request.json['nome']
        
        db.session.commit()
        
        return jsonify({'Materia atualizada': Materia.to_dict(query) }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/delete/materias/<int:id>', methods=['DELETE'])
def delete_materias(id: int):
    try:
        query = Materia.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        return jsonify({'Materia deletada': query }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})


#rotas para provas
@routes.route('/get/provas/', methods=['GET'])
def get_provas():
    try:
        query = Prova.query.order_by(Prova.id).all()
        return jsonify({'Provas': [Prova.to_dict(prova) for prova in query]}, 200)
    except:
        return jsonify({'error': str(e)})

@routes.route('/get/provas/<int:id>', methods=['GET'])
def get_provas_id(id: int):
    try:
        query = Prova.query.filter_by(id=id).first()
        return jsonify(query, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/post/provas/', methods=['POST'])
def post_provas():
    try:
        data = request.json
        id_aluno = data['id_aluno']
        id_materia = data['id_materia']
        nota = data['nota']
        
        prova = Prova(id_aluno=id_aluno, id_materia=id_materia, nota=nota)
        
        db.session.commit()
        
        return jsonify({'Nota de prova atualizada': prova.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes.route('/put/provas/<int:id>', methods=['PUT'])
def put_provas(id: int):
    try:
        query = Prova.query.filter_by(id=id).first()
        query.id_aluno = request.json['id_aluno']
        query.id_materia = request.json['id_materia']
        query.nota = request.json['nota']
        
        db.session.commit()
        
        return jsonify({'Prova atualizada': Prova.to_dict(query) }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/delete/provas/<int:id>', methods=['DELETE'])
def delete_provas(id: int):
    try:
        query = Prova.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        return jsonify({'Prova deletada': query }, 200)
    except Exception as e:
        return jsonify({'error': str(e)})
