from flask import Flask, render_template, request, jsonify  # Importa módulos.
import csv #Biblioteca csv.

app = Flask(__name__) # Cria uma instância do Flask e atribue à variável app

#Espera requisição POST com dados JSON contendo a temperatura, umidade e estado os dados serão salvo em 'dados.csv'
@app.route('/registar', methods=['POST'])
#Onde recebe os dados
def registar():
    temperatura = request.json['temperatura']
    umidade = request.json['umidade']
    estado = request.json['estado']
    #Abre o arquivo CSV e escreve os dados como uma nova linha.
    with open('dados.csv', 'a', newline='') as arquivo: #'a' acrescentar mais informações
        writer = csv.writer(arquivo)
        writer.writerow([temperatura, umidade, estado])
    #Retorna uma mensagem JSON de sucesso!
    return jsonify({'mensagem': 'Dados registrados com sucesso!'}), 200

@app.route('/dashboard')
# Enviar os dados ao 'dashboard.html' e acessa a rota.
def dashboard():
    return render_template('dashboard.html')

#Esta rota espera uma requisição GET onde vai lê os dados e da a resposta em JSON
@app.route('/api/dados', methods=['GET'])
 # Abre o arquivo CSV em modo de leitura e lê os dados
def obter_dados():
    with open('dados.csv', 'r', newline='') as arquivo: #'r' de modo leitura
        reader = csv.reader(arquivo)
        dados = [{'temperatura': row[0], 'umidade': row[1], 'estado': row[2]} for row in reader if len(row) == 3] #Verifica se o comprimento da lista row é igual a 3 antes de criar o dicionário de dados
        
    # Retorna os dados como uma resposta JSON    
    return jsonify(dados)

# Executa a aplicação Flask somente quando o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)