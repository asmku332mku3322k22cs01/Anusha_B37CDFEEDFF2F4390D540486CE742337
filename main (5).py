"""
Implement a function called sort_students that takes a list of students that takes a list
of students object as input and sorts the list based on their  CGPA(Cumulative Grade Point Average)in decending order.
Each student object has the following attributes: name (strings),roll_number (string),and cgpa(float).
Test the function with different input lists of students.
"""

class student:

  def _init_(self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of CGPA 
    sorted_students = sorted(student_list,
      key=lambda student: student.cgpa,
      reverse=True)
  # syntax - lambda arg:exp'
    return sorted_students


# Example Usage:
students = [
    student("Hari", "A123", 7.8),
    student("Swetha", "A124", 8.9),
    student("Saumya", "A125", 9.1),
    student("Muthu", "A126", 9.9),
]

sorted_students = sorted_students(student)
 
# print the sorted list of students
for student in sorted_students:
      print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                               student.roll_number,

                                                                              student.cgpa))
                                                       
                                                       
                                                  


                                                       
    
  
                        
                              
  
