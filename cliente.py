import requests #Biblioteca requests para enviar uma requisição POST para o servidor Flask

def enviar_dados(temperatura, umidade, estado): #Recebe o nome, email e idade como parâmetros. 
    url = 'http://localhost:5000/registar' #Definição da URL
    
    dados = {  #Onde os dados serão armazenados
        'temperatura': temperatura,
        'umidade': umidade,
        'estado': estado
    }
    
    #Requisição POST para a URL especificada, passando os dados no formato JSON. O retorno da requisição é armazenado na variável response.
    response = requests.post(url, json=dados) 
    
    #Se o retorno da requisição for 200, idinca que está funcionando e exibe a mensagem dentro do if, se não tiver exibe a mensagem do else junto com o erro.
    if response.status_code == 200: 
        print('Dados enviados com sucesso!')
    else:
        print('Erro ao enviar os dados:', response.text)


# Dados que serão enviados
enviar_dados(50.4, 12, 'R.Norte')
