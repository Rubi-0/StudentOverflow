from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta
from .models.preguntas import Pregunta



def user_register(nombre, email, telefono, password):
    usuario_existente = User.query.filter_by(email=email).first()
    if usuario_existente is not None:
        return{'Error':'El usuario ya esta registrado :c'}, 403
    nuevo_usuario = User(nombre=nombre, email=email, telefono=telefono)
    nuevo_usuario.hashear_password(password=password)

    nuevo_usuario.save()

    return{
        'status': 'usuario registrado',
        'email':email, 
        'telefono': telefono
    }, 200

def user_login(correo, password):
    usuario_existente = User.query.filter_by(email=correo).first()
    if usuario_existente is None:
        return{'Status': 'El correo no esta registrado'}, 500
    if usuario_existente.verificar_password(password = password):
        caducidad = timedelta(minutes=10)
        token_acceso = create_access_token(identity=usuario_existente.nombre)
        return {
            'Status': 'Sesión iniciada',
            'Token': token_acceso
            }, 200
    else:
        return{'Status': 'La contraseña no coinicide'}, 400

def crear_pregunta(usuario_id, titulo, contenido):
    nueva_pregunta = Pregunta(
        titulo=titulo,
        contenido=contenido,
        usuario_id=usuario_id
    )
    nueva_pregunta.save()

    return {
        'status': 'Pregunta creada exitosamente',
        'titulo': titulo,
        'contenido': contenido
    }, 201

