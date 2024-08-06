FREE_BUN = 5
clients_count = 0
clients = []

with open('client.txt', 'r', encoding='utf-8') as file:
    for line in file:
        clients.append(line.rstrip())
        clients_count += 1


def bun_counter(client):
    print(f"Привет, {client}!")


def decorator_function(func):
    def wrapper(client):
        func(client)
        global clients_count
        if clients_count % FREE_BUN == 0:
            print("Вам полагается бесплатная плюшка!")

    return wrapper


decorated_bun_counter = decorator_function(bun_counter)

while True:
    if clients:
        current_client = clients.pop(0)
        decorated_bun_counter(current_client)
    else:
        client_input = input("Введите имя клиента (или оставьте строку пустой, чтобы выйти): ")
        if client_input == '':
            break
        clients_count += 1

        decorated_bun_counter(client_input)
