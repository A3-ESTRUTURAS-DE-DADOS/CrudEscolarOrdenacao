from extensions import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    ano_letivo = db.Column(db.String(100), nullable=True)

    def init(self, id, nome, idade, endereco, ano_letivo):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.ano_letivo = ano_letivo
    
    def __repr__(self):
        return "<Aluno(id={}, nome={}, idade={}, endereco={}, ano_letivo={})>".format(self.id, self.nome, self.idade, self.endereco, self.ano_letivo)

    def to_dict(aluno):
        return {
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'endereco': aluno.endereco,
            'ano_letivo': aluno.ano_letivo
        }

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    
    def init(self, id, nome):
        self.id = id
        self.nome = nome
        
    def __repr__(self):
        return "<Materia(id={}, nome={})>".format(self.id, self.nome)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }

class Prova(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    
    aluno = db.relationship('Aluno', backref=db.backref('provas', lazy=True))
    materia = db.relationship('Materia', backref=db.backref('provas', lazy=True))
    
    def init(self, id, id_aluno, id_materia, nota):
        self.id = id
        self.id_aluno = id_aluno
        self.id_materia = id_materia
        self.nota = nota
    
    def __repr__(self):
        return "<Prova(id={}, id_aluno={}, id_materia={}, nota={})>".format(self.id, self.id_aluno, self.id_materia, self.nota)
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_aluno': self.id_aluno,
            'id_materia': self.id_materia,
            'nota': self.nota
        }