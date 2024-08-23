create table tarefas (
    id INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(255),
    data_de_criacao DATETIME,
    data_de_conclusao DATETIME,
    autor VARCHAR(255),
)