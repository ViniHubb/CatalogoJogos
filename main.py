from flask import Flask , make_response, jsonify, request, render_template

import mysql.connector

conexao = mysql.connector.connect(

    host = 'localhost',
    user='root',
    password='1234',
    database='catalogo',
)

app = Flask('Catalogo')
app.config ['JSON_SORT_KEYS']=False

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

@app.route('/login', methods=['GET', 'POST'])
def LoginPage():
    
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


if __name__ == "__main__":
    app.run(debug=True)