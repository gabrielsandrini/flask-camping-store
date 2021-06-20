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
    description=db.Column(db.Text(), nullable=True)
    price=db.Column(db.Float(), nullable=False)
    category_fk=db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable=False)

    category=relationship(ProductCategory)
