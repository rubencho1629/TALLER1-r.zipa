from flask import request, redirect, url_for, render_template, flash, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.usuario import Usuario
from .. import app, db


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verificar si el usuario ya existe
        existing_user = Usuario.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"message": "El nombre de usuario ya existe."}), 400

        # Crear nuevo usuario
        new_user = Usuario(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Registro exitoso"}), 201

    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

        user = Usuario.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))  # Redirige al index
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))

    return render_template('login/login.html')


# Ruta para el cierre de sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

# Ruta para el dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('login/dashboard.html', mensaje="¡Bienvenido a tu panel de control!")
