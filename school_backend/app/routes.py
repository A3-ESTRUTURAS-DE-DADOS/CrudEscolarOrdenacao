from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime 
from app.models import Aluno, Materia, Prova

routes = Blueprint('routes', __name__)

@routes.route('/get/alunos/', methods=['GET'])
def get_alunos():
    try:
        alunos = Aluno.query.all()
        
        #OBS: para a ementa da A3, foi usado o bubble sort para ordenar os alunos por id
        n = len(alunos)
        for i in range(n):
            for j in range(0, n-i-1):
                if alunos[j].id > alunos[j+1].id:
                    alunos[j], alunos[j+1] = alunos[j+1], alunos[j]
        
        return jsonify({'Alunos': [aluno.to_dict() for aluno in alunos]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        dataAno = request.json['ano']
        
        aluno = Aluno(nome=dataNome, idade=dataIdade, endereco=dataEndereco, ano_letivo=dataAno)
        
        db.session.add(aluno)
        db.session.commit()
        
        return jsonify(aluno.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].id < R[j].id:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

@routes.route('/get/materias/', methods=['GET'])
def get_materias():
    try:
        materias = Materia.query.all()
        
        #agora ta sendo usado o merge sort para ordenar as materias por id
        merge_sort(materias)
        
        materias_list = [materia.to_dict() for materia in materias]
        return jsonify({'Materias': materias_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        
        return jsonify({'materia': materia.to_dict()}), 201
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


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menor = [x for x in arr[1:] if x.nota <= pivo.nota]
        maior = [x for x in arr[1:] if x.nota > pivo.nota]
        return quick_sort(maior) + [pivo] + quick_sort(menor)

@routes.route('/get/provas/', methods=['GET'])
def get_provas():
    try:
        provas = Prova.query.all()
        
        # por fim, ta sendo usado o quick sort aqui para ordenar por NOTA
        provas_quick = quick_sort(provas)
        
        provas_list = [prova.to_dict() for prova in provas_quick]
        return jsonify({'Provas': provas_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



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
        id_aluno = request.json['id_aluno']
        id_materia = request.json['id_materia']
        nota = request.json['nota']
        
        prova = Prova(id_aluno=id_aluno, id_materia=id_materia, nota=nota)
        
        db.session.add(prova) 
        db.session.commit()
        
        return jsonify({'prova': prova.to_dict()}), 201
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
