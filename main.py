import json

app = Flask(__name__)


def novo_usuario():
    if request.method == 'POST':
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        # Aqui você pode adicionar a lógica para salvar o usuário no banco de dados
        # Por exemplo, você pode usar SQLAlchemy ou outro ORM para persistir os dados

        return jsonify({'message': 'Usuário criado com sucesso!'}), 201

    return jsonify({'message': 'Método não permitido'}), 405