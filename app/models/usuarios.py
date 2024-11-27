from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delate(self)
        db.session.commit()

    def hashear_password(self, password):
        self.password = generate_password_hash(password)


    def verificar_password(self, password):
        return check_password_hash(self.password, password)
    
        

        
