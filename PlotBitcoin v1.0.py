import time
import requests
import matplotlib.pyplot as plt

# Inicializa a lista para armazenar os preços
prices = []

while True:
  # Faz a solicitação HTTP para obter os dados
  response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')

  # Extrai os dados da resposta
  data = response.json()

  # Obtém o preço atual
  price = data['data']['amount']
  
  # Adiciona o preço à lista
  prices.append(price)
  
  # Gera o gráfico
  plt.plot(prices)
  plt.show()
  
  # Espera um segundo antes de fazer a próxima solicitação
  time.sleep(1)
