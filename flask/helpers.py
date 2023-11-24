import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    submit = SubmitField('Salvar')

class FormularioLogin(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    submit = SubmitField('Login')

def encontra_imagem(id):
    for nome_arquivo in os.listdir(app.config["UPLOADS_PATH"]):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    
    return "capa_padrao.jpg"

def deleta_imagem(id):
    arquivo = encontra_imagem(id)
    if arquivo != "capa_padrao.jpg":
        os.remove(os.path.join(app.config["UPLOADS_PATH"], arquivo))