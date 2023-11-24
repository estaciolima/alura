from jogoteca import app, db
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Jogos
from helpers import encontra_imagem, deleta_imagem, FormularioJogo, FormularioLogin
import time

@app.route('/')
def index():
    jogos = Jogos.query.order_by(Jogos.id)
    return render_template("lista.html", titulo="Jogoteca", jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo='novo'))
    
    form = FormularioJogo()

    return render_template("novo.html", titulo="Novo jogo", form=form)

@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    
    if Jogos.query.filter_by(nome=nome).first():
        flash('Esse jogo ja existe!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    arquivo.save(f'{app.config["UPLOADS_PATH"]}/capa{novo_jogo.id}-{time.time()}.jpg')

    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory("uploads", nome_arquivo)



@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo='editar'))
    
    jogo = Jogos.query.filter_by(id=id).first()
    capa = encontra_imagem(id)

    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console

    return render_template("editar.html", titulo="Editar jogo", id=jogo.id, capa=capa, form=form)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    id = request.form["id"]
    jogo = Jogos.query.filter_by(id=id).first()
    jogo.nome = request.form["nome"]
    jogo.categoria = request.form["categoria"]
    jogo.console = request.form["console"]

    arquivo = request.files['arquivo']
    deleta_imagem(id)
    arquivo.save(f'{app.config["UPLOADS_PATH"]}/capa{jogo.id}-{time.time()}.jpg')

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo='editar'))
    
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()

    flash("Jogo deletado com sucesso!")

    return redirect(url_for("index"))

