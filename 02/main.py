client_list = []
bonus_coffee = 6
with open("test_1.txt", "r") as file:
    for line in file:
        client_list.append(line.split())

# client_list = dict(client_list)
client_dict = {key: int(value) for key, value in client_list}

for k, v in client_dict.items():
    print(k, ": ", v // bonus_coffee)

with open("max_bonus.txt", "w") as bonus_file:
    max_bonus = 0
    clients = []
    for key, values in client_dict.items():
        current_bonus =  values // bonus_coffee
        if current_bonus > max_bonus:
            max_bonus = current_bonus
            clients = [key]
        elif current_bonus == max_bonus:
            clients.append(key)

    bonus_file.write(", ".join(clients))
