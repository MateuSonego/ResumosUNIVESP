Protocolos de comunicação da Internet

Toda atividade de comnicação na internet é regida por protocolos.

Para cada ação em específico existe uma reposta especifica a ser dada

Solicitação de conexão TCP > Resposta de conexão TCP >
GET http://www.example/example.pdf > "Arquivo"

Todo protocolo considera:
- O serviço a ser oferecido.
- O ambiente onde ele executa incluindo os serviços utilizados pelo protocolo.
- O vocabulário de mensagens utilizado para implementá-lo.
- O formato de cada mensagem do vocabulário.
- Os algoritmos que tentam garantir a troca de mensagens e a integridade do serviço oferecido.

---

Protocolos são padronizações que definem como se dá a comunicação e a utilização do meio físico na infraestrutura de comunicação(rede). Os protocolos consideram:
- Semântica(regras): Temporizações, controles de erros, etc.
- Sintaxe(formato): Codificações, quadro, etc.

"Um protocolo define o formato e a ordem das mensagens trocadas entre duas ou mais entidades comunicantes,
bem como as ações realizadas na transmissão e/ou recepção dessas mensagens".

---

A Internet é composta de vários tipos de redes que operam com inúmeros protocolos de comunicação, no contexto da infraestrutura de comunicação, grande parte da internet opera no modelo TCP/IP.

Estrutura de camadas:
- Aplicação (Mensagem)
- Transporte (Segmento)
- Rede (Datagrama)
- Enlance (Quadro)
- Física

IP: Atua na camada de rede(e enlance).
TCP/IP: Atua na camada de transporte.

A camada de rede tem como funções principais:
- Endereçamento
- Determinação de caminhos, rotas escolhida pelos pacotes entre a origem e destino. Algoritmos de roteamento determinam os valores para a comutação.
- Comutação(repasse), mover pacotes entre as portas de entrada e de saída dos roteadores.

Tudo que está relacionado a comunicação Host a Host está na camada de rede.

A camada de transportes tem como funções principais:
- A origem, aceitar dados da camada de aplicação e dividir eles em unidade menores em caso de necessidade,
passá-los para a camada de rede e garantir que todas essas unidade cheguem corretamente ao destino.
- Tudo deve ser feito com eficiência de forma que as camadas superiores fiquem isoladas das mudanças
na tecnologia de hardware.

Entidade de transporte é um hardware/software que executa as funções da camada de transporte (kernel do
SO, biblioteca vinculada a aplicações de rede, placa de rede, etc)

A camada de transporte liga a origem ao destino, fornecendo comunicação lógica entre os processos da
aplicação em diferentes Host

Os protocolos de transporte são executados nos sistemas finais da rede

---

UDP: User Datagram Protocol

Procolo de transporte "simplificado"

Serviço de "Melhor esforço", pois os segmentos UDP podem ser perdidos e entregues fora de ordem para a
aplicação de destino

Não existe aprensetação entre o UDP emissor e o receptor, cada segmento é tratado de forma independente dos outros

Não há estabelecimento de conexão, nem estado de conexão nem no transmissor nem no receptor, cabeçalho
reduzido

Basicamente envia os dados sem preocupação se vai chegar ou não.