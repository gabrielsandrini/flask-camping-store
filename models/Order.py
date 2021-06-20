# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para permitir relacionamento entre as classes
from sqlalchemy.orm import relationship 
from models.OrderStatus import OrderStatus 

from config import app_config, app_active 
from models.Product import Product

config = app_config[app_active]
db = SQLAlchemy(config.APP)


order_products_table = db.Table('order_products', 
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('qtty', db.Integer, primary_key=True)
)

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    status_fk=db.Column(db.Integer, db.ForeignKey(OrderStatus.id))
    #products_fk=db.relationship(Product, secondary=order_products_table, lazy='subquery', backref=db.backref('orders', lazy=True))
    product_fk = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    
    status = relationship(OrderStatus)
    product = relationship(Product)
    #products = relationship(Product)
    def init_db():
        db.create_all()

    if __name__ == '__main__':
        init_db()