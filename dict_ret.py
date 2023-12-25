

def main():
  student = lambda name = input("Name: "), home = input("Home: "): {"name": name, "home": home}
  print(student["name"], student["home"])

if __name__ == "__main__":
  main()  