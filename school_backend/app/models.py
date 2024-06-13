from app import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(200), nullable=True)
    ano_letivo = db.Column(db.String(100), nullable=True)

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Prova(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    
    aluno = db.relationship('Aluno', backref=db.backref('provas', lazy=True))
    materia = db.relationship('Materia', backref=db.backref('provas', lazy=True))