class Student:
  def __init__(self, name):
    self.name = name
    
  @property
  def name(self):
    # print(f"Getting {self._name}")
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name
    print(f"Setting {name}")
    
def main():
  student = Student("Manan")
  print(student.name)
  student.name = "Jeet"
    
if __name__ == "__main__":
  main()