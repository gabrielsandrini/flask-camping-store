# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para permitir relacionamento entre as classes
from sqlalchemy.orm import relationship 
from models.OrderStatus import OrderStatus 

from config import app_config, app_active 
from models.Product import Product
from models.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)


""" order_products_table = db.Table('order_products', 
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('qtty', db.Integer, primary_key=True)
) """

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    status_fk=db.Column(db.Integer, db.ForeignKey(OrderStatus.id), nullable=True)
    #products_fk=db.relationship(Product, secondary=order_products_table, lazy='subquery', backref=db.backref('orders', lazy=True))
    quantity=db.Column(db.Integer)
    product_fk = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    user_fk = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 
    
    status = relationship(OrderStatus)
    product = relationship(Product)
    user = relationship(User)
    #products = relationship(Product)

    def __repr__(self):
        return '%s - %s' % (self.id, self.product - self.user - self.date_created)

    def save(self):
        try:
            db.session.add(self) 
            db.session.commit() 
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    
    
