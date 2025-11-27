CREATE DATABASE Flashcards;
USE Flashcards;

CREATE Table Usuario(
    id_usuario int PRIMARY KEY AUTO_INCREMENT, 
    nome varchar(50), 
    email varchar(30), 
    senha varchar(20));

CREATE Table Flashcard(
    id_flashcard int PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY(id_baralho) REFERENCES Baralho(id_baralho), 
    pergunta varchar(50), 
    reposta varchar(50), 
    dificuldade varchar(15));

CREATE Table Baralho(
    id_baralho int PRIMARY KEY AUTO_INCREMENT, 
    nome varchar(50), 
    categoria varchar(50))
    ativo TINYINT DEFAULT 1;


-- chave primária composta nessa tabela
CREATE Table Estatistica(id_usuario INT, 
    id_flashcard INT, 
    id_baralho INT,
    visualizacoes INT DEFAULT 0,
    vezes_de_novo INT DEFAULT 0,
    vezes_facil INT DEFAULT 0,
    vezes_medio INT DEFAULT 0,
    vezes_dificil INT DEFAULT 0,
    ultima_revisao DATETIME DEFAULT NULL,
    ultima_resposta VARCHAR(10) NULL,
    PRIMARY KEY (id_usuario, id_flashcard, id_baralho),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_flashcard) REFERENCES Flashcard(id_flashcard),
    FOREIGN KEY (id_baralho) REFERENCES Baralho(id_baralho)
    );
