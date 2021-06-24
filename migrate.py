# Usado somente para criar o banco sqlite e as migrações dos modelos e sempre que alterar algum modelo, copiar novamente a classe e executar.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from config import app_active, app_config


config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app) 
manager.add_command('db', MigrateCommand)

# ADICIONAR AQUI OS MODELS
# IMPORTANTE, LEMBRAR DAS DEPENDÊNCIAS NA CRIAÇÃO
class Permission(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(45),unique=True, nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=True)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    recovery_code=db.Column(db.String(100),nullable=True) 
    active=db.Column(db.Boolean(),default=1,nullable=False) 
    permission_fk=db.Column(db.Integer,db.ForeignKey(Permission.id),nullable=False)

class ProductCategory(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(45),unique=True, nullable=False)

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(45), nullable=False)
    image_url=db.Column(db.Text(), nullable=True)
    description=db.Column(db.Text(), nullable=True)
    price=db.Column(db.Float(), nullable=False)
    category_fk=db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable=True)
    user_fk = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=True)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 

class OrderStatus(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(15),unique=True, nullable=False)

order_products_table = db.Table('order_products', 
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('qtty', db.Integer, primary_key=True)
)

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    status_fk=db.Column(db.Integer, db.ForeignKey(OrderStatus.id), nullable=True)
    product_fk = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    user_fk = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    quantity=db.Column(db.Integer)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    # db.relationship(Product, secondary=order_products_table, lazy='subquery', backref=db.backref('orders', lazy=True))

if __name__ == '__main__':
    manager.run()