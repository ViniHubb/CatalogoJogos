<h1>Catalogo de Jogos</h1>
<p> Bem-vindo ao nosso site - Catalogo de Jogos! Este projeto é uma aplicação web para catalogar e analisar jogos. Antes de começar, certifique-se de ter um ambiente Python configurado e um banco de dados MySQL disponível. </p>
<h2>Configuração do Banco de Dados</h2>
1.Execute o seguinte script SQL para criar o banco de dados e tabelas necessárias:

CREATE DATABASE IF NOT EXISTS catalogo
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE catalogo;

CREATE TABLE IF NOT EXISTS jogos (
    id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL UNIQUE,
    classificacao VARCHAR(10),
    ano_lancamento SMALLINT,
    genero VARCHAR(50),
    modo_de_jogo VARCHAR(50),
    plataforma VARCHAR(255),
    publicadoras VARCHAR(100),
    descricao VARCHAR(1500),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS usuarios ( 
    email VARCHAR(60),
    senha VARCHAR(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS analises ( 
    id INT AUTO_INCREMENT,
    nota SMALLINT,
    comentario VARCHAR(500),
    id_jogo INT,
    email_usuario VARCHAR(60),
    PRIMARY KEY (id),
    FOREIGN KEY (id_jogo) REFERENCES jogos(id),
    FOREIGN KEY (email_usuario) REFERENCES usuarios(email)
);

-- Exemplo de dados
INSERT INTO jogos (nome, classificacao, ano_lancamento, genero, modo_de_jogo, plataforma, publicadoras)
VALUES 
('The Oregon Trail', 'Livre', 1974, 'Estratégia', 'Single-player', 'Minicomputador (HP 2100), Mainframe, (CDC Cyber 70/73-26), Apple II, Atari 8-Bit, Commodore 64, Steam', 'MECC'),
('Prince of Persia: The Lost Crown', '14+', 2024, 'Ação e aventura', 'Single-player', 'Nintendo Switch, PlayStation 5, PlayStation 4, Xbox One, Xbox Series X/S e PC', 'Ubisoft');

INSERT INTO usuarios (email, senha, nome)
VALUES
('joao.silva@example.com', '123456', 'João'),
('maria.fernandes@example.org', '13579', 'Maria');

INSERT INTO analises (nota, comentario, id_jogo, email_usuario)
VALUES
(5, 'Muito legal esse game cara, estou jogando a 10 dias sem parar', 1, 'joao.silva@example.com'),
(3, 'Eu gostei mais ou menos desse jogo viu, meio paradão e eu sou do rock', 1, 'maria.fernandes@example.org');


Certifique-se de ter o MySQL Connector instalado via pip install mysql-connector.


<h2>Executando o Projeto</h2>
1.Abra o seu ambiente Python no terminal do VSCode ou outro compilador.
2.Execute o seguinte comando para instalar as dependências:
    pip install flask flask-login
3.Execute o aplicativo Flask usando o seguinte comando:
   python app.py
4.Abra seu navegador e acesse http://localhost:5000

Agora você pode usar o nosso site - Catalogo de Jogos para explorar jogos, adicionar novos jogos, e muito mais! Divirta-se explorando o mundo dos games!
