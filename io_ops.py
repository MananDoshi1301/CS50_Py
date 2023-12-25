import csv

names = []

# [======================================================================]

# names = ["Harry", "Draco", "Ron", "Hermione"]

# with open("names.txt") as file:
#   for line in sorted(file):
#     print(f"Hello, {line.rstrip()}")

# [======================================================================]

# # Also prints name, home as part of csv
# with open('names.txt') as file:
#     reader = csv.reader(file)
#     for name, home in reader:        
#         names.append({"name": name, "home": home})
        
        
# for name in sorted(names, key=lambda student: student["name"]):
#     print(f"{name['name']} in {name['home']}")
    
# [======================================================================]

# # csv dict reader
# with open('names.txt') as file:
#     reader = csv.DictReader(file)
#     for row in reader:        
#         names.append({"name": row["name"], "home": row["home"]})
        
        
# for name in sorted(names, key=lambda student: student["name"]):
#     print(f"{name['name']} in {name['home']}")

# [======================================================================]

# # csv writer

# name = input("Enter name: ")
# home = input("Enter home: ")

# with open("names.txt", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# [======================================================================]

# # csv DictWriter

# name = input("Enter name: ")
# home = input("Enter home: ")

# with open("names.txt", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})