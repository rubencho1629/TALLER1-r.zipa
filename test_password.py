from werkzeug.security import check_password_hash
from app import app
from app.models.usuario import Usuario

# Reemplaza "admin_user" y "admin_pass" por el usuario y contraseña que estás probando
username = "admin_user"
password = "admin_pass"

# Inicializar la aplicación en el contexto de Flask
with app.app_context():
    # Buscar el usuario en la base de datos
    user = Usuario.query.filter_by(username=username).first()

    if user:
        # Verificar la contraseña
        password_correct = check_password_hash(user.password, password)
        print("Contraseña correcta:", password_correct)  # Esto debería imprimir "True" si la contraseña es correcta
    else:
        print("Usuario no encontrado")
