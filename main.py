from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import mysql.connector

conexao = mysql.connector.connect(

    host = 'localhost',
    user='root',
    password='1234',
    database='catalogo',
)

app = Flask('Catalogo')
app.config ['JSON_SORT_KEYS']=False
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

login_manager = LoginManager(app)
login_manager.login_view = 'LoginPage'

class Usuario(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email = %s", (user_id,))
    usuario_data = cursor.fetchone()
    if usuario_data:
        usuario = Usuario()
        usuario.id = usuario_data['email']
        return usuario
    return None


@app.route('/', methods=['GET', 'POST'])
def HomePage ():

     return render_template('index.html')


@app.route('/catalogo', methods=['GET', 'POST'])
def Catalogo():
    if request.method == 'POST':
        # Se o método for POST, significa que o formulário foi enviado
        cursor = conexao.cursor()

        # Obter o termo de pesquisa do formulário
        termo_pesquisa = request.form['termo_pesquisa']

        # Consultar o banco de dados para jogos que contenham o termo de pesquisa no nome
        query = "SELECT * FROM jogos WHERE nome_do_jogo LIKE %s "
        cursor.execute(query, ('%' + termo_pesquisa + '%',))
        resultados = cursor.fetchall()

        return render_template('catalogo.html', jogos=resultados, termo_pesquisa=termo_pesquisa)

    # Se o método for GET, exibir a página principal sem resultados de pesquisa
    return render_template('catalogo.html', jogos=None, termo_pesquisa=None)

@app.route('/jogoTeste', methods=['GET', 'POST'])
def PaginaJogo():
     return render_template('paginaJogo.html')

@app.route('/login', methods=['GET', 'POST'])
def LoginPage():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email = %s AND senha = %s", (email, senha))
        usuario_data = cursor.fetchone()

        if usuario_data:
            usuario = Usuario()
            usuario.id = email
            login_user(usuario)
            return redirect (url_for('Catalogo'))

    return render_template('login.html')


@app.route('/registro', methods=['GET', 'POST'])
def RegistroPage():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmarSenha']

        if senha != confirmar_senha:
            mensagem_erro = "As senhas não coincidem."
            return render_template('registro.html', mensagem_erro=mensagem_erro)

        cursor = conexao.cursor()

         # Verifica se o e-mail já está cadastrado
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        if cursor.fetchone():
            mensagem_erro = "Este e-mail já está cadastrado."
            return render_template('registro.html', mensagem_erro=mensagem_erro)

        # Insere o novo usuário no banco de dados
        cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conexao.commit()

        mensagem_sucesso = "Registro bem-sucedido! Faça login para continuar."
        return render_template('registro.html', mensagem_sucesso=mensagem_sucesso)

    return render_template('registro.html', mensagem_erro=None, mensagem_sucesso=None)


@app.route('/logout')
@login_required
def LogoutPage():
    logout_user()
    return redirect(url_for('LoginPage'))

if __name__ == "__main__":
    app.run(debug=True)