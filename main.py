from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import mysql.connector, os
from flask import jsonify


conexao = mysql.connector.connect(

    host = 'localhost',
    user='root',
    password='143786',
    database='catalogo',
)

app = Flask('Catalogo')
app.config ['JSON_SORT_KEYS']=False
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

login_manager = LoginManager(app)
login_manager.login_view = 'LoginPage'

class Usuario(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome



@login_manager.user_loader
def load_user(user_id):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (user_id,))
    usuario_data = cursor.fetchone()
    if usuario_data:
        usuario = Usuario(id=usuario_data['email'], nome=usuario_data['nome'])
        return usuario
    return None


@app.route('/', methods=['GET', 'POST'])
def HomePage ():

     return render_template('index.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def Catalogo():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM jogos ORDER BY id DESC LIMIT 10")
    resultados = cursor.fetchall()

    if request.method == 'POST':
        # Se o método for POST, significa que o formulário foi enviado
        cursor = conexao.cursor()

        # Obter o termo de pesquisa do formulário
        termo_pesquisa = request.form['termo_pesquisa']

        # Consultar o banco de dados para jogos que contenham o termo de pesquisa no nome
        query = "SELECT * FROM jogos WHERE nome LIKE %s "
        cursor.execute(query, ('%' + termo_pesquisa + '%',))
        resultados = cursor.fetchall()

        return render_template('catalogo.html', jogos=resultados, termo_pesquisa=termo_pesquisa)

    # Se o método for GET, exibir a página principal sem resultados de pesquisa
    return render_template('catalogo.html', jogos=resultados, termo_pesquisa=None)

@app.route('/jogo', methods=['GET', 'POST'])
def PaginaJogo():
    jogo_id = request.args.get('id', default=None, type=int)
    jogo_info = None
    analises_com_nomes = None
    media_notas = 0.0
    menssagem = 1

    if jogo_id is not None:
        cursor = conexao.cursor()
        query_jogo = "SELECT * FROM jogos WHERE id = %s"
        cursor.execute(query_jogo, (jogo_id,))
        jogo_info = cursor.fetchone()

        query_analises = """
        SELECT analises.nota, analises.comentario, usuarios.nome, usuarios.email
        FROM analises 
        JOIN usuarios ON analises.email_usuario = usuarios.email 
        WHERE analises.id_jogo = %s;
        """
        cursor.execute(query_analises, (jogo_id,))
        analises_com_nomes = cursor.fetchall()

        if current_user.is_authenticated:
            for analiseAtual in analises_com_nomes:
                if current_user.id in analiseAtual:
                    menssagem = 0

        if analises_com_nomes != []:
            query_media = "SELECT AVG(nota) FROM analises WHERE id_jogo = %s"
            cursor.execute(query_media, (jogo_id,))
            media_notas = round(cursor.fetchone()[0], 1)

    if request.method == "POST":
        nota = request.form['nota']
        comentario = request.form['comentario']
        email = request.form['email']

        cursor = conexao.cursor()
        query_user = "SELECT * FROM analises WHERE email_usuario = %s AND id_jogo = %s"
        cursor.execute(query_user, (email,jogo_id))
        if cursor.fetchone():
            menssagem = 0
        else:
            cursor.execute("INSERT INTO analises (nota, comentario, id_jogo, email_usuario) VALUES (%s, %s, %s, %s)", (nota, comentario, jogo_id, email))
            conexao.commit()

    if jogo_info:
        return render_template('paginaJogo.html',
            menssagem=menssagem,
            jogo=jogo_info, 
            analises=analises_com_nomes,
            nota=media_notas
        )
    else:
        return "Jogo não encontrado", 404

@app.route('/login', methods=['GET', 'POST'])
def LoginPage():
    menssagem = ""
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        menssagem = "Email ou senha incorretos"

        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario_data = cursor.fetchone()

        if usuario_data:
            usuario = Usuario(id=usuario_data['email'], nome=usuario_data['nome'])
            login_user(usuario)
            return redirect (url_for('Catalogo'))

    return render_template('login.html', menssagem=menssagem)


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
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            mensagem_erro = "Este e-mail já está cadastrado."
            return render_template('registro.html', mensagem_erro=mensagem_erro)

        # Insere o novo usuário no banco de dados
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conexao.commit()

        mensagem_sucesso = "Registro bem-sucedido! Faça login para continuar."
        return render_template('registro.html', mensagem_sucesso=mensagem_sucesso)

    return render_template('registro.html', mensagem_erro=None, mensagem_sucesso=None)


@app.route('/admin', methods=['GET', 'POST'])
def Admin():
    cursor = conexao.cursor()

    if request.method == 'POST':
        # Se o formulário de pesquisa for enviado, realiza a pesquisa e exibe os resultados
        if 'termo_pesquisa' in request.form:
            termo_pesquisa = request.form['termo_pesquisa']
            query = "SELECT * FROM jogos WHERE nome LIKE %s"
            cursor.execute(query, ('%' + termo_pesquisa + '%',))
            resultados = cursor.fetchall()
            return render_template('admin.html', jogos=resultados, termo_pesquisa=termo_pesquisa)
        
        elif 'nome' in request.form:
            nome = request.form['nome']
            classificacao = request.form['classificacao']
            ano_lancamento = request.form['ano_lancamento']
            genero = request.form['genero']
            modo_de_jogo = request.form['modo_de_jogo']
            plataforma = request.form['plataforma']
            publicadoras = request.form['publicadoras']
            descricao = request.form['descricao']
            imagem = request.files['imagem']
            # Se houver um ID, trata-se de uma edição
            if 'jogo_id' in request.form:
                if imagem.filename != "":
                    jogo_id = request.form['jogo_id']
                    query_caminho = "SELECT imagem FROM jogos WHERE id=%s"
                    cursor.execute(query_caminho, (jogo_id,))
                    caminho_imagem = cursor.fetchone()
                    os.remove(caminho_imagem[0])
                    
                    nome_imagem = str("static/img/jogos/" + imagem.filename)
                    imagem.save(nome_imagem)
                    query = "UPDATE jogos SET nome=%s, classificacao=%s, ano_lancamento=%s, genero=%s, modo_de_jogo=%s, plataforma=%s, publicadoras=%s, descricao=%s, imagem=%s WHERE id=%s"
                    cursor.execute(query, (nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao, nome_imagem, jogo_id))
                    mensagem_sucesso = "Jogo atualizado com sucesso!"
                else:
                    jogo_id = request.form['jogo_id']
                    query = "UPDATE jogos SET nome=%s, classificacao=%s, ano_lancamento=%s, genero=%s, modo_de_jogo=%s, plataforma=%s, publicadoras=%s, descricao=%s WHERE id=%s"
                    cursor.execute(query, (nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao, jogo_id))
                    mensagem_sucesso = "Jogo atualizado com sucesso!"
            else:
                # Se não houver um ID, trata-se de um novo cadastro
                nome_imagem = str("static/img/jogos/" + imagem.filename)
                imagem.save(nome_imagem)
                query = "INSERT INTO jogos (nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao, imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras, descricao, nome_imagem))
                mensagem_sucesso = "Jogo cadastrado com sucesso!"

            conexao.commit()
            return render_template('admin.html', mensagem_sucesso=mensagem_sucesso)

        elif 'excluir' in request.form:
            jogo_id = request.form['excluir']
            query1="DELETE FROM analises WHERE id_jogo = %s"
            query = "DELETE FROM jogos WHERE id=%s"
            cursor.execute(query1, (jogo_id,))
            cursor.execute(query, (jogo_id,))
            mensagem_sucesso = "Jogo excluido com sucesso"
            conexao.commit()

            return render_template('admin.html', mensagem_sucesso=mensagem_sucesso)
        
        elif 'termo_pesquisa_usuarios' in request.form:
            termo_pesquisa_usuarios = request.form['termo_pesquisa_usuarios']
            query_usuarios = "SELECT * FROM usuarios WHERE nome LIKE %s"
            cursor.execute(query_usuarios, ('%' + termo_pesquisa_usuarios + '%',))
            resultados_usuarios = cursor.fetchall()
            return render_template('admin.html', usuarios=resultados_usuarios, termo_pesquisa_usuarios=termo_pesquisa_usuarios)
        
        elif 'excluirUser' in request.form:
            user_id = request.form['excluirUser']
            query0="DELETE FROM analises WHERE email_usuario = %s"
            query = "DELETE FROM usuarios WHERE email=%s"
            cursor.execute(query0, (user_id,))
            cursor.execute(query, (user_id,))
            mensagem_sucesso = "usuario excluido com sucesso"
            conexao.commit()

            return render_template('admin.html', mensagem_sucesso=mensagem_sucesso)
        
        elif 'usuario_id' in request.form:
            email = request.form['email']
            nome = request.form['nomeUser']
            senha = request.form['senha']
            
            query = "UPDATE usuarios SET email=%s, nome=%s, senha=%s  WHERE email=%s"
            cursor.execute(query, (email, nome, senha, email))
            mensagem_sucesso = "Jogo atualizado com sucesso!"
            conexao.commit()

            return render_template('admin.html', mensagem_sucesso=mensagem_sucesso)

    # Se a requisição for GET, exibe a página principal sem resultados de pesquisa
    return render_template('admin.html', jogos=None, termo_pesquisa=None)
@app.route('/logout')
@login_required
def LogoutPage():
    logout_user()
    return redirect(url_for('LoginPage'))

if __name__ == "__main__":
    app.run(debug=True)
