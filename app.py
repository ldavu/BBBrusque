from flask import Flask, render_template, request
from usuarios import usuarios

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar se o usuário existe e se a senha está correta
        if username in usuarios and usuarios[username] == password:
            # Se o login for bem-sucedido, renderizar a página multicameras.html
            return render_template('multicameras.html', username=username)
        else:
            # Se o login falhar, exibir uma mensagem de erro
            error = 'Usuário ou senha inválidos. Por favor, tente novamente.'
            return render_template('login.html', error=error)

    # Se a solicitação for GET ou se o login falhar, renderizar o formulário de login
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
