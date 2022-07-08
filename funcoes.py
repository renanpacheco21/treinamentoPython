from pyodbc import connect, DatabaseError

def conectar():
    conexao = None
    try:
        conexao = connect('DSN=folhaPython', ConnectionIdleTimeout=0)
    except Exception as error:
        print(f'Erro na conexão com o banco de dados, função "conectar" {error}')
    finally:
        return {'cursor': conexao.cursor(), 'conexao': conexao}


def executar(comando):
    conexao = conectar()
    try:
        conexao['cursor'].execute(comando)
        conexao['conexao'].commit()
    except Exception as error:
        print(f'Erro na execução do comando, função "executar" {error}')
    finally:
        conexao['cursor'].close()


def consultar(comando):
    conexao = conectar()
    listaDado = []
    try:
        conexao['cursor'].execute(comando)
        resultado = conexao['cursor'].fetchall()
        for i, descricao in enumerate(resultado):
            listaDado.append({})
            for j, valor in enumerate([d[0] for d in conexao['cursor'].description]):
                listaDado[i][valor] = descricao[j]
    except Exception as error:
        print(f'Erro na consulta do comando, função "consultar" {error}')
    finally:
        conexao['cursor'].close()
        return listaDado

def permissao(comando):
    return f""" set option fire_triggers = 'off';
                {comando}
                COMMIT;
                 set option fire_triggers = 'on';"""