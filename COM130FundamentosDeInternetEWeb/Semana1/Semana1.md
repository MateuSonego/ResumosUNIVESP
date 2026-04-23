Fundamentos de Internet e Web

---

As Redes de Computadores foram criadas com o objetivo primário de permitir que dois os mais elementos computacionais pudessem se
comunicar, compartilhar recursos(Áudio, video, imagens, acessar aplicações, operar máquinas remotamente);

As redes atuais permitem que centenas de milhares de aplicações possam trocar dados, entre pessoas, empresas e até mesmo 
dispositivos sem a intervenção humanas;

Cada um desses elementos funciona obedecendo regras para que os usuários e computadores possam se comunicar;

Devido à complexidade envolvida uma rede considera que os dados são transportados utilizando diversas camadas no processo de 
comunicação;

A internet é formada por milhões de dispositivos(sistemas finais) ou servidores que executam as aplicações, além do meio físico  e enlaces de comunicação como cabos, torres e satélites

Elas são formadas por diversos elementos que envolvem inúmeros blocos como:
- Usuários,
- Aplicações,
- Roteadores,
- Switches,
- Servidores,
- Meio físico cabeado e aéreo,
- Celulares, Tablets, desktops;

---

Para qualquer elemento computacional ser conectado a uma rede de dados é preciso:
- Uma placa de rede;
- E que essa placa esteja ligada por algum link(meio cabeado ou aéreo) a um elemento de comunicação;

É por meio da placa de rede que todos os sinais são transmitidos pelo cabo ou ar, que em sigada são interpretados tanto pelo emissor
quanto pelo receptor para que as informações possam sejam apresentadas para o usuário;

---

O elemento de comutação no contexto de uma rede local é aquele que:
- Recebe os dados em algum formato de um emissor e vai processar e comutar o mesmo, encaminhando para o receptor da informação, estando ela ou não na mesma rede do emissor;

Exemplo:
Caso um emissor X queira enviar um arquivo para o Y com ambos estando na mesma rede(rede local). O repasse de dados será simples e
feito por um Switch;
Caso eles estejam em rede separadas será preciso de um roteador para encaminhar os dados/pacotes entre eles;

---

Exemplo:
Suponha que você tenha os seguintes elementos para organizar em camadas:
- 1 palito de fósforo,
- 1 caixa de fósforo,
- 1 caixa de sapato,
- 1 caixa de papelão,
- 1 caixa de um fogão 4 bocas;

Suponha que o emissor quer enviar um palito de fósforo a um receptor, sendo a menor unidade na lista o próprio palito;

1. O emissor deve colocar o palito na caixa de fósforo,
2. A caixa de fósforo na caixa de sapato,
3. A caixa de sapato na caixa de papelão,
4. A caixa de papelão na caixa do fogão,
5. Por fim a caixa do fogão é enviada para o receptor;

O emissor encapsulou a menor unidade de informação para enviar para o receptor, quando a caixa for recebida pelo receptor, o caminho
contrário será feito

---

OSI = Open System Interconection {
    É um modelo de referência que nunca foi implementado na prática, ele possui as seguintes camadas:
    7. Aplicação,
    6. Apresentação,
    5. Sessão,
    4. Transporte,
    3. Rede,
    2. Enlace de dados,
    1. Física;
}

TCP/IP = Transmission Control Protocol/Internet Protocol {
    É o modelo padrão utilzado na comunicação na maioria das redes, sendo utilizado na prática por inúmeros elemtnos de comunicação
    em redes locais ou remotas. Possui as seguintes camadas:
    4. Aplicação {
        - Processos de rede para aplicações,
        - Representação das mensagens,
        - Formatação das mensagens;
    },
    3. Transporte {
        - Conexão ponto a ponto entre processos e aplicações que executa em hosts diferentes;
    },
    2. Internet {
        - Endereçamento lógico dos hosts,
        - Roteamento;
    },
    1. Acesso à rede {
        - Acesso ao meio físico,
        - Transmissão binária,
        - Codificação/Decodificação de sinais;
    }
}

---

Alguns exemplos de aplicações que "rodam" na internet:
- Serviços de E-mail,
- Serviços de streaming de áudio e vídeo,
- Serviços de compartilhamento de arquivos,
- Serviços de pagamento online,
- Aplicações para acesso seguro de dados;

ISPs = Internet Service Providers; Provedores de Serviços de Internet;

TCP = Transmission Control Protocol; Protocolo de Controle de Transmissões;

IP = Internet Protocol; Protocolo de Internet;

RFCs = Request For Comments;



