client_list = []
bonus_coffee = 6
with open("test_1.txt", "r") as file:
    for line in file:
        client_list.append(line.split())

client_list = dict(client_list)
client_dict = {key: int(value) for key, value in client_list.items()}

for k, v in client_dict.items():
    print(k, ": ", v // bonus_coffee)

with open("max_bonus.txt", "w") as bonus_file:
    for values in client_dict.values():
        max_bonus = 0
        if values > max_bonus:
            max_bonus = values // bonus_coffee
    bonus_file.write(str(max_bonus))
