from tinkoff.invest import Client
from connect import token1

#TOKEN = 'token1'

with Client(token1) as client:
    b = client.users.get_accounts()
    for a in b.accounts:
        print(a)
    d = client.orders.get_orders()
