with open("farm.txt", "r") as file:
    sheep_count = file.readline()
    pig_count = file.readline()
    duck_count = file.readline()
count_all = int(sheep_count) * 4 + int(pig_count) * 4 + int(duck_count) * 2
print(f"Amount of all farm animals' legs: {count_all}")
