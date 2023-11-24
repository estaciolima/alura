from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioLogin
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    form = FormularioLogin()

    proximo = request.args.get('proximo')
    proximo = '/' if proximo == None else proximo
    return render_template('login.html', proximo=proximo, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioLogin(request.form)

    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['usuario_logado'] = form.nickname.data
        flash(f'{session["usuario_logado"]} logado com sucesso')
        proximo = request.form["proximo"]
        return redirect(proximo)
    else:
        flash('Usuario nao logado!')
        proximo = request.form["proximo"]
        return redirect(url_for('login', proximo=proximo))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))