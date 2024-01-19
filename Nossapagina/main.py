from flask import Flask , make_response, jsonify ,request,render_template
import mysql.connector


conexao= mysql.connector.connect(

    host = 'localhost',
    user='root',
    password='143786',
    database='catalogo',
)






app = Flask('Catalogo')
app.config ['JSON_SORT_KEYS']=False


@app.route('/', methods=['GET', 'POST'])
def HomePage():
    if request.method == 'POST':
        # Se o método for POST, significa que o formulário foi enviado
        cursor = conexao.cursor()

        # Obter o termo de pesquisa do formulário
        termo_pesquisa = request.form['termo_pesquisa']

        # Consultar o banco de dados para jogos que contenham o termo de pesquisa no nome
        query = "SELECT * FROM jogos WHERE nome_do_jogo LIKE %s"
        cursor.execute(query, ('%' + termo_pesquisa + '%',))
        resultados = cursor.fetchall()

        return render_template('index.html', jogos=resultados, termo_pesquisa=termo_pesquisa)

    # Se o método for GET, exibir a página principal sem resultados de pesquisa
    return render_template('index.html', jogos=None, termo_pesquisa=None)


if __name__ == "__main__":
    app.run(debug=True)