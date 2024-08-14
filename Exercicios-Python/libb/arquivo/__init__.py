def arquivoExiste(arq):
    try:
        a = open(arq, 'rt', encoding="utf-8")
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+, encoding="utf-8"')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt', encoding="utf-8")
    except:
        print('ERRO ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33}{dado[1]} anos')
    finally:
        a.close()
        

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at', encoding="utf-8")
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()
