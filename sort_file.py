# names = ["Harry", "Draco", "Ron", "Hermione"]

with open("names.txt") as file:
  for line in sorted(file):
    print(f"Hello, {line.rstrip()}")
