from werkzeug.security import generate_password_hash
from app import db, app
from app.models.usuario import Usuario, Role

# Inicializa la aplicación
with app.app_context():
    # Verificar si el rol 'admin' existe; si no, lo crea
    admin_role = Role.query.filter_by(nombre='admin').first()
    if not admin_role:
        admin_role = Role(nombre='admin')
        db.session.add(admin_role)
        db.session.commit()
        print("Rol 'admin' creado con éxito.")
    else:
        print("Rol 'admin' ya existe.")

    # Verificar si el usuario ya existe
    existing_user = Usuario.query.filter_by(username="admin_user").first()
    if existing_user:
        print("El usuario 'admin_user' ya existe.")
    else:
        # Crear un nuevo usuario con el rol de 'admin' y una contraseña encriptada
        nuevo_admin = Usuario(
            username="admin_user",
            password=generate_password_hash("admin_pass"),  # Cambia "admin_pass" a la contraseña que prefieras
            role=admin_role
        )
        db.session.add(nuevo_admin)
        db.session.commit()
        print("Usuario 'admin_user' creado con éxito.")
