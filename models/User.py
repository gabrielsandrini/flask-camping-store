# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para permitir relacionamento entre as classes Usuario e Perfil
from sqlalchemy.orm import relationship   
from models.Permission import Permission

from config import app_config, app_active 

# Biblioteca adicionada para criptografia de senha
from passlib.hash import pbkdf2_sha256


config = app_config[app_active]
db = SQLAlchemy(config.APP)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    recovery_code=db.Column(db.String(100),nullable=True) 
    active=db.Column(db.Boolean(),default=1,nullable=False) 
    permission_fk=db.Column(db.Integer,db.ForeignKey(Permission.id),nullable=False)
    
    # Adicionado para permitir a relação entre a classe Usuário e a classe Perfil.
    permission = relationship(Permission)

    # Adicionado para exibir da forma que é definida na chamada do objeto da classe.
    # É a forma que será exibido no campo de relacionamento.
    def __repr__(self):
        return '%s - %s' % (self.id, self.username)


    # Métodos adicionados para configuração posterior
    def get_usuario_by_email(self, email): 
        try:
           res = db.session.query(User).filter(User.email == email).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res

    def get_usuario_by_id(self, user_id): 
        try:
           res = db.session.query(User).filter(User.id == user_id).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res

    def update_usuario(self, obj): 
        # Método para atualizar o usuário 
        return ' '

    # Adicionando os métodos para criptografia de senha
    # Metodo de conversão de senha de string para string criptografada
    def hash_password(self, password): 
        try:
            return pbkdf2_sha256.hash(password) 
        except Exception as e:
            print("Erro ao tentar criptografar a senha %s" % e) 

    # Método para atualizar senha
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    # Método para verificar se a senha informada é igual a que está no banco de dados
    def verify_password(self, password_no_hash, password_database): 
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False

    def get_all(self):
        try:
            res = db.session.query(User).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res

    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True
        

    @property
    def is_anonymous(self):
        return False
    
    
    def get_id(self):
        return str(self.id)
        
