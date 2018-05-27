import trello
import urllib.request
import json

"""
    Trello Board: Loja Virtual
    Link: https://trello.com/b/t0hVF51V/loja-virtual
    Não está integrado com a aplicação, somente realiza o post nos pedidos da api quando execulta manualmente esse script
"""


class TrelloApi(object):
    api = trello.TrelloApi('c381956e52fa72621677b692064051df', 'bc0d96b75ac6a07aacc2872f1f9898c3cac7981855c8b5c1dff165a98c3ce05c')

    def post_pedidos(self):
        with urllib.request.urlopen("https://api-loja-virtual.herokuapp.com/pedidos/") as url:
            pedidos = json.loads(url.read().decode())

        for p in pedidos:
            descricao = json.dumps(p, indent=4)
            self.api.cards.new(name='Pedido {}'.format(p.get('id')), idList='5b03fc922eb84b18fa9b3f00', desc='Produtos {}'.format(descricao))

    def get_status_pedido(self):
        return 'Status'

