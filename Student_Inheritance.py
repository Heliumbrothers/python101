class Student:
    def __init__(self, name, age, eye_colour):

        if isinstance(name, str) == True:
            self.age = age
        else:
            return ValueError('Enter a string')
        
        if isinstance(eye_colour, str) == True:
            self.eye_colour = eye_colour
        else:
            return ValueError('Enter a string')
        
        if isinstance(name, str) == True:
            self.name = name
        else:
            return ValueError('Enter a string')
        
        
    def get_name(self):
        return self.name
    
    def get_eye_colour(self):
        return self.eye_colour
    
    def get_age(self):
        return self.age


    
class JuniorSchoolStudent(Student):
    def __init__(self, name, age, eye_colour, height_in_metres, weight_in_kilograms):
        super().__init__(name, age, eye_colour)
        self.height_in_metres = height_in_metres
        self.weight_in_kilograms = weight_in_kilograms
        self.school = 'junior'
    def get_name(self):
        return self.name
    
    def get_eye_colour(self):
        return self.eye_colour
    
    def get_age(self):
        return self.age
    
    def get_height(self):
        return self.height_in_metres
    
    def get_weight(self):
        return self.weight_in_kilograms
    

    


class SeniorSchoolStudent(Student):
    def __init__(self, name, age, eye_colour, university_choice, IQ):
        super().__init__(name, age, eye_colour)
        self.university_choice = university_choice
        self.IQ = IQ
        self.school = 'senior'

    
    def get_name(self):
        return self.name
    
    def get_eye_colour(self):
        return self.eye_colour
    
    def get_age(self):
        return self.age
    
    def get_university_choice(self):
        return self.university_choice
    
    def get_IQ(self):
        return self.IQ



student_list = []

student_list.append(JuniorSchoolStudent('Bob', 9, 'Brown', 1.44, 32))
student_list.append(JuniorSchoolStudent('Tim', 7, 'Brown', 1.44, 33))
student_list.append(JuniorSchoolStudent('Gary', 8, 'Blue', 1.39, 31))
student_list.append(JuniorSchoolStudent('Sam', 9, 'Blue', 1.42, 31))
student_list.append(JuniorSchoolStudent('Tom', 9, 'Brown', 1.43, 40))
student_list.append(SeniorSchoolStudent('Joe', 13, 'Brown', 'Oxford', 165))



def print_all_junior_students_name(input_list):
    for student in input_list:
        if student.school == 'junior':
            print(student.get_name())


print_all_junior_students_name(student_list)