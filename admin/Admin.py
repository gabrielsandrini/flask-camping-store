# -*- coding: utf-8 -*-
# from flask_admin import Admin: Ela possui vários recursos para criação 
# de views customizadas para nossa aplicação
from flask_admin import Admin

# Componente dentro do flask_admin para ativar as views em nossa aplicação, baseadas em nossas models.
from flask_admin.contrib.sqla import ModelView
from models.User import User
from models.Product import Product
from models.Order import Order 
from models.OrderStatus import OrderStatus
from models.Permission import Permission
from models.ProductCategory import ProductCategory


def start_views(app, db):
    # Utilização do bootstrap4 por meio do construtor do Admin.
    admin = Admin(app, name='Outdor in tents', template_mode='bootstrap4')
    # Método que é utilizado para criar uma view em nossa aplicação Admin.
    # ModelView: é um recurso do flask_admin que permite a criação Admin, as telas do administrador baseadas na estrutura das models.
    # category é utilizado para agrupar os itens de menus.
    admin.add_view(ModelView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(ModelView(Permission, db.session, "Permissões", category="Usuários"))
    admin.add_view(ModelView(Product, db.session, "Produtos", category="Produtos"))
    admin.add_view(ModelView(ProductCategory, db.session, "Categoria", category="Produtos"))
    admin.add_view(ModelView(Order, db.session, "Compras", category="Compras"))
    admin.add_view(ModelView(OrderStatus, db.session, "Status", category="Compras"))