import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cria uma função para atualizar os dados e gerar o gráfico
def update_plot(num):
  # Faz a solicitação HTTP para obter os dados
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  
  # Obtém os dados em formato JSON
  data = response.json()
  
  # Obtém a cotação atual do bitcoin em dólares
  quote = data['bpi']['USD']['rate_float']
  
  # Adiciona a cotação à lista de cotações
  quotes.append(quote)
  
  # Atualiza o gráfico com as novas cotações
  plt.plot(quotes)

# Inicializa a lista de cotações
quotes = []

# Cria o gráfico e configura a atualização automática a cada 5 segundos
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_plot, interval=1000)

plt.show()
