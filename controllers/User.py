from models.User import User

class UserController():
    # Método construtor da classe UserController.
    def __init__(self):
        # Inicializa uma instância de User().
        self.usuario_model = User()

    # Método que será utilizado para ligar a rota de login com a Model de Usuário
    def login(self, email, password):
        # Recebe os dados de e-mail e salva no atributo da Model de Usuário.
        self.usuario_model.email = email

        # Verifica se o usuário existe no banco de dados e atribui a resultado.
        resultado = self.usuario_model.get_usuario_by_email(email)

        # Caso o usuário exista o resultado não será None
        if resultado is not None: 
            # Verifica se a senha que o usuário enviou, agora convertido em hash, é igual a senha que foi pega no banco de dados para esse usuário.
            res = self.usuario_model.verify_password(password, resultado.password)

            # Se forem a mesma, retorna True.
            if res:
                return resultado
            else:
                return {}
        return {}

        def recuperar(email): 
            # Criado somente para exemplificar a recuperação de senha por email. 
            # Rota do app.py: @app.route('/recuperar-senha/', methods=['POST']) 
            return ''

    def list(self):
        return self.usuario_model.get_all()

    def find_one(self, user_id):
        return self.usuario_model.get_usuario_by_id(user_id)
