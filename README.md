# Projeto de integração de mídias

A ideia do projeto é criar um sistema que integre a grade televisiva com o sistema de streaming Globo Play. 

A grade televisiva é catalogada em um arquivo .txt que conterá os metadados dos programas que vão ao ar e a partir desses arquivos de texto, que serão adicionados periodicamente à um diretório específico vindos de um software que registra os dados dos programas que estão sendo televisionados. 

Desse arquivo de texto com os metadados, precisa-se selecionar os programas que tenham mais de 30 segundos de duração e coletar as informações pertinentes. Essas informações precisam ser enviadas à uma API que irá cortar os vídeos, os vídeos precisarão ser baixados e as informações pertinentes à esse video enviadas à API da Globo Play.

O principal desafio é conseguir criar um sistema de integração escalável e que não fique preso nos gargalos do tempo do corte do vídeo e do tempo do download dos arquivos de vídeo. Para tal a solução precisa ser modularizada e que possa rodar assíncronamente.

# Proposta de solução

A ideia é fazer um sistema que possa funcionar assíncronamente, onde o tempo de espera dos requests do corte e do download do vídeo não bloqueiem a continuação da observação da grade e envio de novos programas.

A solução baseia-se no padrão Publisher-Subscriber, onde o publisher monitora um determinado diretório à espera de novos arquivos '.txt' que serão adicionados pelo sistema que cataloga a grade televisiva. Portanto um sistema de fila com uma distribuição das tarefas permitirá o escalonamento da operação ao se subscrever novos workers para realizar o trabalho conforme o aumento da necessidade.

Utiliza a biblioteca [watchdog]('https://github.com/gorakhargosh/watchdog') para monitorar um diretório que será defindo por quem ativar o script.O  arquivo de texto é parseado e o conteúdo com uma duração maior de 30 segudos é selecionado e é enviada uma mensagem com os dados desse conteúdo ao broker que redistribuirá a mensagem para os subscriber.

O broker utilizado é o RabbitMQ e o subscriber será o cliente que irá fazer os requests para as APIs externas e fará o trabalho de baixar e organizar os vídeos.


## Iniciando


### Pre-requisitos

O RabbitMQ precisa estar instalado e com o servidor rodando para o broker funcionar.

## License


This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
