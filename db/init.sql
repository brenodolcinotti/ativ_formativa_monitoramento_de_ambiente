CREATE DATABASE monitoramento;

USE monitoramento;

CREATE TABLE dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME,
    temperatura FLOAT,
    umidade FLOAT
);
