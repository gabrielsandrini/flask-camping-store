# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

from config import app_config, app_active 

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class ProductCategory(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  description=db.Column(db.String(45),unique=True, nullable=False)

  def __repr__(self):
    return '%s - %s' % (self.id, self.description)

  def get_all(self):
    try:
        res = db.session.query(ProductCategory).all()
    except Exception as e:
        res = []
        print(e)
    finally:
        db.session.close() 
        return res       