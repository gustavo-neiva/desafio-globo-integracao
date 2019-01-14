# Projeto de integração de mídias

A ideia do projeto é criar um sistema que integre a grade televisiva com o sistema de streaming Globo Play. 

A grade televisiva é catalogada em um arquivo .txt que conterá os metadados dos programas que vão ao ar e a partir desses arquivos de texto, que serão adicionados periodicamente à um diretório específico vindos de um software que registra os dados dos programas que estão sendo televisionados. 

Desse arquivo de texto com os metadados, precisa-se selecionar os programas que tenham mais de 30 segundos de duração e coletar as informações pertinentes. Essas informações precisam ser enviadas à uma API que irá cortar os vídeos, os vídeos precisarão ser baixados e as informações pertinentes à esse video enviadas à API da Globo Play.

O principal desafio é conseguir criar um sistema de integração escalável e que não fique preso nos gargalos do tempo do corte do vídeo e do tempo do download dos arquivos de vídeo. Para tal a solução precisa ser modularizada e que possa rodar assíncronamente.

# Proposta de solução

A ideia é fazer um sistema que possa funcionar assíncronamente, onde o tempo de espera dos requests do corte e do download do vídeo não bloqueiem a continuação da observação da grade e envio de novos programas.

A solução baseia-se no padrão de filas de mensagens, onde o publisher monitora um determinado diretório à espera de novos arquivos '.txt' que serão adicionados pelo sistema que cataloga a grade televisiva. Portanto um sistema de fila com uma distribuição das tarefas permitirá o escalonamento da operação ao se subscrever novos workers para realizar o trabalho conforme o aumento da necessidade.

Utiliza a biblioteca [watchdog]('https://github.com/gorakhargosh/watchdog') para monitorar um diretório que será defindo por quem ativar o script.O  arquivo de texto é parseado e o conteúdo com uma duração maior de 30 segudos é selecionado e é enviada uma mensagem com os dados desse conteúdo ao broker que redistribuirá a mensagem para os clientes.

O broker utilizado é o RabbitMQ e o worker será o cliente que irá fazer os requests para as APIs externas e fará o trabalho de baixar e organizar os vídeos.

Ao ser parseado, o conteúdo que será cortado é adicionado à um arquivo .csv para poder ser consultado conforme a necessidade. Além disso tanto as operações de parseamento como o cliente contém logs para observar o que acontece intermanete no software.

### Principais vantagens do padrão

A principal vantagem é a possibilidade de fazer o serviço que monitora a grade televisiva continuar selecionado os vídeos de corte independentemente do trabalho de esperar o corte do video e o download do arquivo. Além disso a solução torna-se escalonável pois caso haja necessidade de aumentar o volume de requests precisa-se apenas adicionar novos workers para receber os trabalhos que estarão na fila.

Além disso o sistema é modularizado, o que facilita o desenvolvimento dos pedaços do sistema independentemente, diminuindo muito a chance de propagar bugs para outras partes do sistema.

### Principais desvantagens do padrão

A solução necessitaria de, pelo menos, três servidores atuando simultaneamente. Um que ficará responsável pelo publisher, outro para rodar o broker e outro(s) para realizar os requests. Além disso o controle das mensagens e dos callbacks precisa ser controlado e testado para se evitar erros na comunicação entre os operadores do sistema.

## Pré-requisitos

O RabbitMQ precisa estar instalado e com o servidor rodando em localhost para o broker funcionar no ambiente de desenvolvimento.

A solução foi desenvolvida utilizando a versão 3.7.2 do Pyhton

## Instalação

Basta clonar o repositório e rodar os scripts separadamente. 

Para rodar o publisher utiliza-se o comando:

```
$ python /path/repositorio/run_publisher.py /path/diretorio/observado
```

Para ativar o broker depois de ter instalado o RabbitMQ:

```
$ sudo rabbitmq-server
```

Para iniciar o worker:

```
$ python /path/repositorio/run_worker.py
```

## Testes (WIP)

Para rodar os testes utilizando todas as partes do projeto é necessário estar com um servidor do RabbitMQ operando em localhost no momento de inicialização dos testes.
```
$ sudo rabbitmq-server
```
Também precisa iniciar o publisher enviando o path do diretorio dos arquivos de texto que estão contidos na pastar tests/folder_test

```
$ python run_publisher.py path/onde/foi/baixado/tests/folder_test
$ python /path/arquivo/run_tests.py
```
Assim pode-se observar o parser funcionando e as mensagens sendo encaminhadas. O mock das API's estão bem aquém do que eu queria para fazer uma demonstração dos workers.
## TO DO

- Melhorar e aumentar os cases de testes tanto do parser quanto do client como do funcionamento do broker
- Automatizar os testes
- Definir um sistema de deploy e procurar fazê-lo de uma maneira integrada e automatizada.
- Aferir as etapas da solução e procurar otimizá-la. Talvez configurar algumas operações para funcionar em multi-threading ou então utilizar a biblioteca de operações assíncronas para aumentar a capacidade de um worker realizar requests simultâneos.
- Transformar ou integrar a solução em um web app para que um leigo possa manter, gerir, aferir e observar a operação da integração de mídias.