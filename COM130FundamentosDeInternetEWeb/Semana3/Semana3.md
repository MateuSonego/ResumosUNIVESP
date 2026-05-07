A 'WWW' (World Wide Web)

AS ideias por trás da WWW começaram na década de 1980 no CERN na Suiça

O desejo de tornar mais fácil as pesquisas por documentos, feitas pelos cientistas, fez em 1989 um
pesquisador chamado Tim Berners-Lee iniciar um projeto para gerenciar melhor as informações trocadas
entre os pesquisadores

Berners-Lee se baseou em um sistema chamado ENQUIRE para junto com Robert Cailliau rascunhar a WWW

Em 1990 Berners-Lee usou um computador NeXTcube para escrever o primeiro servidor web e o primeiro
navegador chamado de WorldWideWeb

(O NeXTcube era um computador criado pela NeXT, empresa de Steve Jobs criada em 1985)

Em 1991 nasce a WWW, junto também surge um novo protocolo,o HTTP, já que não existiam protocolos que
atendiam às necessidades da comunidade cientifíca.
O hipertexto já era discutido desde 1960 mas Lee uniu a ideia de hipertexto e a Internet, 
como ninguém quis implementar suas ideias, ele decidiu implementar o projeto sozinho.
Neste mesmo período ele também desenvolveu um sistema de identificação global e uníco de recursos, o 
URI (Uniform Resource Identifier)

Em 1991 já haviam outros protocolos como os de serviços de e-mail, entretanto tais protocolos possuíam
limitações, para surprir algumas limitações como o acesso simples e por links, o protocolo necessitado para acessos à informações deveria atender aos seguintes requisitos:
- Incorporar a funcionalidade do FTP.
- Ser hábil para realizar buscas.
- Tenha um formato de dados automáticos para negociar a troca de informações.
- que o cliente/usuário pudesse referenciar outro servidor.

Todos os dados que "consumimos" na WWW estão armazenados em servidores, os chamados servidores Web
(como o Apache), os servidores armazem os arquivos que são requisitados pelo usuário

O usuário não consegue acessar diretamente o arquivo que deseja ler sem pedir para o servidor, nesse
caso o servidor é tanto o equipamento quanto o programa.

A aplicação web fica ligada o tempo todo, apenas esperando algúem para consumir os dados

---

Para o funcionamento básico é necessário:
- Recursos os quais serão obtidos por meio de uma URL e armazenados em servidores.
- Ao digitar uma URL no navegador desejamos acessar um recurso endereçavél:
  - Parte da URL referente ao servidor é separada e transformada em um endereço IP, por um banco de
  dados da Internet chamado DNS (Domain Name System)
  - O navegador estabelece uma conexão TCP com o servidor WEB localizado no endereço IP retornado
  - O navegador envia uma requisição HTTP ao servidor para obter o recurso indifcado pela parte restante
  da URL
  - O recurso é recebidoe interpretado pelo navegador que realiza requisições adicionais para figuras,
  arquivos de formatação e outros recursos que fazem parte da página
  - O navegador então reconstitui a página na tela do usuário.

A web se baseia fundamentalmente em três padrões:
- URL é um sistema que específica como cada página de informações recebe um "endereço" único onde possa 
ser encontrada.
- HTTP é um protocolo que especifica como o navegador e o servidor web se comunicam entre si.
- HTML é uma linguagem de marcação para codificar a informação de modo que possa ser exibida em uma 
grande quantidade de dispositivos.

Um servidor web é basicamente um programa que escuta os pedidos do navegadores ou aplicações clientes e
realiza a execução desses pedidos

O Apache é um servidor web de plataforma aberta, sendo um do mais populares. É mantido pela 
Apache Software Foundation. O Apache possui módulos que adicionam mais funções além de apenas servir o 
conteúdo, como a parte de ativação do SSL (Security Socket Layer) e recursos de balaceamento de carga
geolocalização baseada em IP, etc.

---

Para acessar os recursos disponíveis nos servidores web é preciso da ajuda de um protocolo, onde o padrão
da WWW é o HTTP, ele é um protocolo cliente-servidor que permite a obtenção de recursos tais como
documentos HTML, é um protocolo extensível da camada de aplicação do modelo TCP/IP que é encapsulado
sobre o TCP, é usado não apenas para buscar documentos de hipertexto, mas também imagens, vídeos ou 
publicar conteúdos em servidores, como nos formulários HTML.

O HTTP estabelece uma comunicação básica estabelecendo uma conexão TCP, envio da requisição do cliente
e envio dos dados pelo servidor.

Quem controla a conexão para encaminhar mensagens HTTP é a camada de transporte, ou seja, independe do 
HTTP, ele apenas requer que essa conexão seja confiável(Sem apresentar erros), por isso a base do
transporte HTTP é o TCP, não o UDP. As versões atuais se baseiam em trazer uma única conexão TCP, 
praticamente todo conteúdo de uma página, isso economiza a abertura de novas conexões TCP, garantir a
confiabilidade na entrega requer um custo computacional e de conectividade maiores, por isso o TCP é
mais lento que o UDP

o Fluxo padrão é:
- Abertura de conexão TCP
- Envio de mensagem HTTP
- Retorno da resposta do servidor
- Fechamento da conexão TCP

---

O DNS é uma sigla para o sistema de nomes de domínios, sendo um registro que contém nomes de sites e seus
respectivos endereços IP associados, basicamente converte um IP para um nome de domínio para facilitar o 
acesso.