#C:\Users\Gibir\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome {}, Idade: {}'.format(registro.split(',')))
    #print('Nome {}, Idade: {}'.format())