import datetime

def log_cash(result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'время запроса: {str(datetime.datetime.now())} \n')

def log_cash(sern):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'время запроса: {str(datetime.datetime.now())} \n')