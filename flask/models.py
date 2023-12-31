from jogoteca import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = db.Column(db.String(50), nullable = False)
    categoria = db.Column(db.String(40), nullable = False)
    console = db.Column(db.String(20), nullable = False)

    def __repr__(self) -> str:
        return "<Nome %r>" % self.name

class Usuarios(db.Model):
    nome = db.Column(db.String(20), nullable = False)
    nickname = db.Column(db.String(8), nullable = False, primary_key=True)
    senha = db.Column(db.String(100), nullable = False)

    def __repr__(self) -> str:
        return "<Nome %r>" % self.name