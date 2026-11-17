#default argument
def greeting(name="Guest"):
  print("Welcome",name)
greeting("Aadya")
greeting()

#keyword arrangement
def student_info(name,age,city):
  print(name,age,city)
student_info(age=25,name="Aadya",city="Blr")
