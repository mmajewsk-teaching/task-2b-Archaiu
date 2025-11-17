from typing import List

class Database:
    def __init__(self, classes = []):
        self.classes = classes
    def add_class(self, new_class):
        self.classes.append(new_class)
    def return_average_points_in_class(self, name):
        for el in self.classes:
            if el.get_name() == name:
                return el.return_average_scores()
        raise ValueError()
    def return_average_frequency_in_class(self, name):
        for el in self.classes:
            if el.get_name() == name:
                return el.return_average_frequency()

    
    
class Class:
    def __init__(self, name, students = []):
        self.students = students
        self.name = name
    def add_student(self, name, points, frequency):
        self.students.append({"name": name, "points" : points, "frequency" : frequency})
    def return_class_size(self):
        return len(self.students)
    def return_average_scores(self):
        return sum(el["points"] for el in self.students) / len(self.students)
    def return_average_frequency(self):
        return sum(el["frequency"] for el in self.students) / len(self.students)
    def get_name(self):
        return self.name