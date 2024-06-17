from flask import Blueprint, request, flash, session
from flask import render_template, jsonify, redirect
from extensions import db
import datetime
from app.models import Aluno, Materia, Prova

routes = Blueprint('routes', __name__)

# Arquivo de definição das rotas HTTP

# Rota GET de alunos (retorna todos os alunos de maneira ordenada por id usando o bubblesort)
@routes.route('/get/alunos/', methods=['GET'])
def get_alunos():
    """
    Retorna todos os alunos ordenados por ID usando o algoritmo Bubble Sort.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo a lista de alunos ordenados ou uma mensagem de erro.
    """
    try:
        alunos = Aluno.query.all()

        # Bubble Sort para ordenar os alunos por id
        n = len(alunos)
        for i in range(n):
            for j in range(0, n-i-1):
                if alunos[j].id > alunos[j+1].id:
                    alunos[j], alunos[j+1] = alunos[j+1], alunos[j]

        return jsonify({'Alunos': [aluno.to_dict() for aluno in alunos]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota GET de alunos por ID
@routes.route('/get/alunos/<int:id>', methods=['GET'])
def get_alunos_id(id):
    """
    Retorna o aluno com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID do aluno a ser retornado.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados do aluno ou uma mensagem de erro.
    """
    try:
        query = Aluno.query.filter_by(id=id).first()
        return jsonify(query.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota POST de alunos
@routes.route('/post/alunos/', methods=['POST'])
def post_alunos():
    """
    Cria um novo aluno com os dados fornecidos no corpo da requisição.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados do aluno criado ou uma mensagem de erro.
    """
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

# Rota PUT de alunos
@routes.route('/put/alunos/<int:id>', methods=['PUT'])
def put_alunos(id: int):
    """
    Atualiza os dados do aluno com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID do aluno a ser atualizado.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados do aluno atualizado ou uma mensagem de erro.
    """
    try:
        query = Aluno.query.filter_by(id=id).first()
        query.nome = request.json['nome']
        query.idade = request.json['idade']
        query.endereco = request.json['endereco']
        query.ano_letivo = request.json['ano_letivo']

        db.session.commit()

        return jsonify({'Aluno atualizado': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota DELETE de alunos
@routes.route('/delete/alunos/<int:id>', methods=['DELETE'])
def delete_alunos(id: int):
    """
    Deleta o aluno com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID do aluno a ser deletado.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados do aluno deletado ou uma mensagem de erro.
    """
    try:
        query = Aluno.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()

        return jsonify({'Aluno deletado': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Função de merge sort para ordenar as matérias por ID
def merge_sort(arr):
    """
    Ordena uma lista de objetos Materia pelo atributo ID usando o algoritmo Merge Sort.
    
    Parameters:
    -----------
    arr : list
        Lista de objetos Materia a ser ordenada.
    """
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

# Rota GET de matérias
@routes.route('/get/materias/', methods=['GET'])
def get_materias():
    """
    Retorna todas as matérias ordenadas por ID usando o algoritmo Merge Sort.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo a lista de matérias ordenadas ou uma mensagem de erro.
    """
    try:
        materias = Materia.query.all()

        # Merge Sort para ordenar as matérias por id
        merge_sort(materias)

        materias_list = [materia.to_dict() for materia in materias]
        return jsonify({'Materias': materias_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota GET de matérias por ID
@routes.route('/get/materias/<int:id>', methods=['GET'])
def get_materias_id(id: int):
    """
    Retorna a matéria com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da matéria a ser retornada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da matéria ou uma mensagem de erro.
    """
    try:
        query = Materia.query.filter_by(id=id).first()
        return jsonify(query.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota POST de matérias
@routes.route('/post/materias/', methods=['POST'])
def post_materias():
    """
    Cria uma nova matéria com os dados fornecidos no corpo da requisição.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da matéria criada ou uma mensagem de erro.
    """
    try:
        dataNome = request.json['nome']

        materia = Materia(nome=dataNome)

        db.session.add(materia)
        db.session.commit()

        return jsonify({'materia': materia.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota PUT de matérias
@routes.route('/put/materias/<int:id>', methods=['PUT'])
def put_materias(id: int):
    """
    Atualiza os dados da matéria com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da matéria a ser atualizada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da matéria atualizada ou uma mensagem de erro.
    """
    try:
        query = Materia.query.filter_by(id=id).first()
        query.nome = request.json['nome']

        db.session.commit()

        return jsonify({'Materia atualizada': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota DELETE de matérias
@routes.route('/delete/materias/<int:id>', methods=['DELETE'])
def delete_materias(id: int):
    """
    Deleta a matéria com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da matéria a ser deletada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da matéria deletada ou uma mensagem de erro.
    """
    try:
        query = Materia.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        return jsonify({'Materia deletada': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Função de quick sort para ordenar as provas por nota
def quick_sort(arr):
    """
    Ordena uma lista de objetos Prova pelo atributo nota usando o algoritmo Quick Sort.
    
    Parameters:
    -----------
    arr : list
        Lista de objetos Prova a ser ordenada.
    
    Returns:
    --------
    list
        Lista de objetos Prova ordenada por nota.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menor = [x for x in arr[1:] if x.nota <= pivo.nota]
        maior = [x for x in arr[1:] if x.nota > pivo.nota]
        return quick_sort(maior) + [pivo] + quick_sort(menor)

# Rota GET de provas
@routes.route('/get/provas/', methods=['GET'])
def get_provas():
    """
    Retorna todas as provas ordenadas por nota usando o algoritmo Quick Sort.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo a lista de provas ordenadas ou uma mensagem de erro.
    """
    try:
        provas = Prova.query.all()

        # Quick Sort para ordenar as provas por nota
        provas_quick = quick_sort(provas)

        provas_list = [prova.to_dict() for prova in provas_quick]
        return jsonify({'Provas': provas_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota GET de provas por ID
@routes.route('/get/provas/<int:id>', methods=['GET'])
def get_provas_id(id: int):
    """
    Retorna a prova com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da prova a ser retornada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da prova ou uma mensagem de erro.
    """
    try:
        query = Prova.query.filter_by(id=id).first()
        return jsonify(query.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota POST de provas
@routes.route('/post/provas/', methods=['POST'])
def post_provas():
    """
    Cria uma nova prova com os dados fornecidos no corpo da requisição.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da prova criada ou uma mensagem de erro.
    """
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

# Rota PUT de provas
@routes.route('/put/provas/<int:id>', methods=['PUT'])
def put_provas(id: int):
    """
    Atualiza os dados da prova com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da prova a ser atualizada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da prova atualizada ou uma mensagem de erro.
    """
    try:
        query = Prova.query.filter_by(id=id).first()
        query.id_aluno = request.json['id_aluno']
        query.id_materia = request.json['id_materia']
        query.nota = request.json['nota']

        db.session.commit()

        return jsonify({'Prova atualizada': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota DELETE de provas
@routes.route('/delete/provas/<int:id>', methods=['DELETE'])
def delete_provas(id: int):
    """
    Deleta a prova com o ID especificado.
    
    Parameters:
    -----------
    id : int
        ID da prova a ser deletada.
    
    Returns:
    --------
    response: Flask.Response
        JSON contendo os dados da prova deletada ou uma mensagem de erro.
    """
    try:
        query = Prova.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
        return jsonify({'Prova deletada': query.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
