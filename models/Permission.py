# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 

from config import app_config, app_active 

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Permission(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  description=db.Column(db.String(45),unique=True, nullable=False)
  
  def __repr__(self):
    return '%s' % (self.description)