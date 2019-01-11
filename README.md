# Projeto de integração de mídias

O projeto de integração foi baseado na arquitetura de um publisher que roda o parser e cria mensagens a partir dos videos que precisam ser cortados. O RabbitMQ atua como um broker para entregar as mensagens para o worker, que é quem irá fazer os requests para as APIs externas.

A ideia é fazer um sistema que possa ser escalonado, já que o tempo de corte do video e o download do mesmo bloquearia a continuidade do script, portanto um sistema de fila com uma distribuição das tarefas permitirá o escalonamento da operação ao se adicionar novos workers para operar o sistema.

## Iniciando


### Pre-requisitos

O RabbitMQ precisa estar instalado e com o servidor rodando para o broker funcionar.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
