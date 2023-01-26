"""
This code creates a function called 'update_plot()' which requests the current bitcoin price in dollars from an API and adds the quote to a list of quotes. It also configures a graph to update with the new quote every 5 seconds. 

It uses the 'requests' library to make the HTTP request, and the 'matplotlib.pyplot' and 'matplotlib.animation' libraries to generate the graph. 
"""

# Otimizando code
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

quotes = []

# Cria uma função para atualizar os dados e gerar o gráfico
def update_plot(num):
  # Faz a solicitação HTTP para obter os dados do json
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  
  # Obtém os dados em formato JSON
  data = response.json()
  
  # Obtém a cotação atual do bitcoin em dólares
  quote = data['bpi']['USD']['rate_float']
  
  # Adiciona a cotação à lista de cotações
  quotes.append(quote)
  
  # Atualiza o gráfico com as novas cotações
  ax.clear()
  ax.plot(quotes)

# Cria o gráfico e configura a atualização automática a cada 5 segundos
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_plot, interval=1000)

plt.show()