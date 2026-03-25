USE monitoramento;

CREATE TABLE IF NOT EXISTS dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME,
    temperatura FLOAT,
    umidade FLOAT
);