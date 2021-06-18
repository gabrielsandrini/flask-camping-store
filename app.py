# Ao inserir esta primeira linha (# -*- coding: utf-8 -*-) no arquivo, estamos indicando que o mesmo deve utilizar a codificação utf-8, no caso para nosso idioma que possui acentos.

# -*- coding: utf-8 -*-

# É importado da biblioteca flask, a classe Flask.
from flask import Flask
from flask import render_template, request

# É importado do arquivo config.py, as variáveis app_config, app_active que app_config: possui as configurações e o tipo de ambiente a ser utilizado (Desenvolvimento, Teste ou Producao). E app_active: possui as configurações de qual ambiente está sendo utilizado por meio da variável de ambiente FLASK_ENV.
from config import app_config, app_active

# A variável config recebe a atribuição do ambiente ativo.
config = app_config[app_active] 

# Método create_app que recebe como argumento com todas as configurações da aplicação.
def create_app(config_name):

    # A variável app recebe uma instância de Flask, passando a configuração da localização dos templates. Pode 
    # receber diversas configurações.
    app = Flask(__name__, template_folder='templates')

    # O atributo secret_key da aplicação app, recebe a configuração da chave secreta do arquivo config.py, por meio da variável config e atributo SECRET.
    app.secret_key = config.SECRET 

    # Efetua o carregamento do arquivo config.py
    app.config.from_object(app_config[config_name]) 
    app.config.from_pyfile('config.py')

    # Primeira rota a ser criada. A rota principal root.
    # Quando se cria duas ou mais rotas seguidas antes do método, isso indica ao navegador que qualquer uma delas acessa o método a seguir. Neste exemplo tanto http://localhost:8000/ e http://localhost:8000/login/ acessam o médtodo index(). Que retorna uma string.
    @app.route('/') 
    def index():
        return render_template("home.html")

    @app.route('/produto')
    def produto():
        return render_template("produto.html")

    # Retorno do método create_app(). Retorna a instância do app criada.
    return app