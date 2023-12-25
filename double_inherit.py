class GF:
  def __init__(self, name):
    self.name = name
    
class Dad(GF):
  def __init__(self, name, bus):
    super().__init__(name)
    self.bus = bus
    
class Son(Dad):
  def __init__(self, name, bus, major):
    super().__init__(name, bus)
    self.major = major
    
  def __str__(self):
    return f"{self.name} is a {self.major} major with a {self.bus} business"
  
  @classmethod
  def getData(cls):
    name = input("Name: ")
    major = input("Major: ")
    bus = input("Business: ")
    return cls(name, bus, major)
    
    
def main():
  son = Son.getData()
  print(son)
  
if __name__ == "__main__":
  main()