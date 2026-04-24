# Um Arquivo é uma sequência de bytes armazenada em memória secundária.
# (Memória primeira é a RAM. A secundária serve para armazenar dados não volatéis como um HD, Pendrive).

# Para armazenar esses dados usamos arquivos como:
# Arquivo Texto = [.txt, .html, .py] (Bytes passam por codificação)
# Arquivo binário = [.exe, .mp3, .jpg] (Bytes não passam por codificação)

# O sistema de arquivos é um componente do computador que organiza os arquivos e dá meios para criar, acessar e modificar eles.
# Fornece uma visão uniforme dos arquivos, embora possam estar armazenados em diferentes dispositivos.

# As rotas saem de uma raiz, que vão para pastas, subpastas e arquivos.
# Para localizar algo pode se usar o caminho absoluto(C:\Users\User1\Desktop\teste.txt)
# E o relativo, onde você volta uma pasta (..) para acessar o caminho.

# Para acessar os arquivos em python:

open('teste.txt', 'r')

# Indica o caminho absoluto ou relativo do arquivo e o meio que ele será aberto
# r = reading mode
# w = writing mode
# a = append mode
# r+ = reading and writing
# t = text mode
# b = binary mode

# infile é uma variável que aponta para o arquivo
infile.read(n)        # Lê até n caracteres (ou bytes) do arquivo
infile.read()         # Lê todo o conteúdo restante do arquivo
infile.readline()     # Lê uma única linha do arquivo (até o \n)
infile.write()        # Escreve dados no arquivo (método genérico, precisa de argumento)
outfile.write(s)      # Escreve a string 's' no arquivo de saída
file.close()          # Fecha o arquivo, liberando recursos do sistema

# Exemplo

def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)

n_words, n_chars = readFile('teste.txt')

# Caso você precise escrever algo que não seja uma String, ele precisará ser convertido antes.