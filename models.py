"""
Definição dos modelos do banco de dados.

Este arquivo contém as classes [Usuario](http://_vscodecontentref_/10) e [Receita](http://_vscodecontentref_/11), que representam as tabelas
do banco de dados. Ambas as classes utilizam SQLAlchemy para mapear os modelos.
"""

from app import db

class Usuario(db.Model):
    """
    Modelo que representa a tabela `usuarios`.

    Atributos:
        id (int): Identificador único do usuário.
        nome (str): Nome do usuário.
        email (str): E-mail único do usuário.
        data_de_nascimento (date): Data de nascimento do usuário (opcional).
    """
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    data_de_nascimento = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Receita(db.Model):
    """
    Modelo que representa a tabela `receitas`.

    Atributos:
        id (int): Identificador único da receita.
        titulo (str): Título da receita.
        descricao (str): Descrição detalhada da receita.
        usuario_id (int): Chave estrangeira que referencia o usuário.
        usuario (Usuario): Relacionamento com o modelo [Usuario](http://_vscodecontentref_/12).
    """
    __tablename__ = 'receitas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('receitas', lazy=True))

    def __repr__(self):
        return f'<Receita {self.titulo}>'