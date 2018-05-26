import requests

#url = "https://api.trello.com/1/boards/5b03fc922eb84b18fa9b3eff"

"""
    Pegando a Board com os Dados
"""
board = "https://api.trello.com/1/boards/5b03fc922eb84b18fa9b3eff?fields=name,url&key=c381956e52fa72621677b692064051df&token=bc0d96b75ac6a07aacc2872f1f9898c3cac7981855c8b5c1dff165a98c3ce05c"

response = requests.request("GET", board)

print(response.text)

"""
    Cadastrando Card
"""

url = "https://api.trello.com/1/cards"

querystring = "http://127.0.0.1:8000/pedidos/2/"

response = requests.request("POST", url, params=querystring)

print(response.text)

import trello

api = trello.TrelloApi('c381956e52fa72621677b692064051df', 'bc0d96b75ac6a07aacc2872f1f9898c3cac7981855c8b5c1dff165a98c3ce05c')

api.boards.get_list('5b03fc922eb84b18fa9b3eff')
#api.cards.new(querystring['id'])