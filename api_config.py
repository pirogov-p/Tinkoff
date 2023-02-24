from openapi_client import openapi
from datetime import datetime
from pytz import timezone

from connect import token1

token = token1
client = openapi.api_client(token)

pf = client.portfolio.portfolio_get()

# Качаем все операции с 30 сентября 2016 (я один из первых клиентов Тиньков Инвестиции)
d1 = datetime(2016, 9, 30, 0, 0, 0, tzinfo=timezone('Europe/Moscow'))  # timezone нужно указывать. Иначе - ошибка
d2 = datetime.now(tz=timezone('Europe/Moscow'))  # По настоящее время
ops = client.operations.operations_get(_from=d1.isoformat(), to=d2.isoformat())

for op in ops.payload.operations: # Перебираем операции
    print(op.figi) # figi всегда берем из операции
    print(op.operation_type)   # и тип операции тоже
    if op.trades == None:      # Если биржевых сделок нет
        print('price:', op.price)       # Берем из операции цену бумаги
        print('payment:', op.payment)   # Сумму платежа
        print('quantity:', op.quantity) # И количество бумаг
    else:
        for t in op.trades:                   # А если есть сделки - то перебираем их
            print('price:', t.price)          # И берем данные из них
            print('quantity:', t.quantity)
    print('--------------')
