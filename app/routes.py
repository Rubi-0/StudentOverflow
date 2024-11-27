from flask_restful import Resource
from flask import request, render_template, make_response
from .methods import user_register
from .methods import user_login
from .methods import crear_pregunta
from flask_jwt_extended import jwt_required, get_jwt_identity



class HolaMundo(Resource):
    def get(self):
        pagina = render_template('index.html')
        respuesta = make_response(pagina) 
        return respuesta
    def post(self):
        return{'Mensaje':'Hola mundo desde post'}
    

class Registro(Resource):
    def get(self):
        pagina = render_template('registro.html')
        respuesta = make_response(pagina)
        return respuesta
    
    def post(self):
        user_info = request.form
        username = user_info.get('nombre')
        email = user_info.get('correo')
        password = user_info.get('password')
        telefono = user_info.get('telefono')

        respuesta, status = user_register(username, email, telefono, password)
    
        return respuesta, status
    
    
class login(Resource):
    def get(self):
        pagina = render_template('login.html')
        respuesta = make_response(pagina) 
        return respuesta       
    def post(self):
        user_info = request.form
        username = user_info.get('nombre')
        email = user_info.get('correo')
        password = user_info.get('password')
        respuesta, status = user_login(email, password)
        return respuesta, status
     
class Restringido(Resource):
    @jwt_required()
    def get(self):
        pagina = render_template('restringido.html')
        respuesta = make_response(pagina)

        return respuesta
class Logout(Resource):
    def get(self):
        pagina = render_template('login.html')
        respuesta = make_response(pagina)
        return respuesta   
class Preguntar(Resource):
    @jwt_required()
    def get(self):
        pagina = render_template('pregunta.html')
        respuesta = make_response(pagina)
        return respuesta
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        pregunta_info = request.form
        titulo = pregunta_info.get('titulo')
        contenido = pregunta_info.get('contenido')
        respuesta, status = crear_pregunta(user_id, titulo, contenido)
        return respuesta, status
    





class APIRoutes:
    def init_api(self, api):
        api.add_resource(HolaMundo, '/')
        api.add_resource(Registro, '/registro')
        api.add_resource(login, '/login')
        api.add_resource(Restringido, '/restringido')
        api.add_resource(Logout, '/logout')
        api.add_resource(Preguntar, '/preguntar')

