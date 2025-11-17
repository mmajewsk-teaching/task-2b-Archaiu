# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

from database import Database, Class


def main():
    biologyClass = Class("biology class", [{"name": "Michal Tusk", "points" : 32, "frequency" : 0.65},{"name": "Marcin Zepp", "points" : 3, "frequency" : 0.21},{"name": "igor x", "points" : 54, "frequency" : 0.81}])
    database = Database([biologyClass])
    print(database.return_average_frequency_in_class("biology class"))
    print(database.return_average_points_in_class("biology class"))




if __name__ == "__main__":
    main()