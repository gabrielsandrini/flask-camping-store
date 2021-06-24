# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

# Adicionado para permitir relacionamento entre as classes
from sqlalchemy.orm import relationship 

from config import app_config, app_active 
from models.ProductCategory import ProductCategory

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(45), nullable=False)
    image_url=db.Column(db.Text(), nullable=True)
    description=db.Column(db.Text(), nullable=True)
    price=db.Column(db.Float(), nullable=False)
    category_fk=db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable=True)
    # date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    # last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True) 

    category=relationship(ProductCategory, lazy='subquery')

    def __repr__(self):
        return '%s - %s' % (self.id, self.title)

    def get_all(self):
        try:
            res = db.session.query(Product).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res       


    def get_by_title(self, title):
        try:
           res = db.session.query(Product).filter(Product.title.like('%'+title+'%')).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res       


    def get_by_id(self, product_id): 
        try:
           res = db.session.query(Product).filter(Product.id == product_id).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res       
    
    def get_by_category(self, category_id):
        try:
           res = db.session.query(Product).filter(Product.category_fk == category_id).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close() 
            return res