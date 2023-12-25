class Student:
  ...
  
def main():
  student = Student()
  student.name = "Raj"
  
  stud = Student()
  stud.id = 4
  
  print(stud.name) # Does not exist
  print(student.id) # Does not exist
  
if __name__ == "__main__":
  main()