class person:
  def display_name(self):
    print("My name is Ahmed")

class student(person):
  def display_course(self):
    print("My course is a BCA")

s =student()
s.dispaly_name()
s.display_course()
