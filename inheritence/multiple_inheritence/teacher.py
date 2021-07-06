from inheritence.multiple_inheritence.Person import Pereson
from inheritence.multiple_inheritence import Employee

# multiple inheritence
class Teacher(Pereson, Employee):
    def teaching(self):
        return 'teaching'

ines = Teacher()
print(ines.sleep())
print(ines.teaching())
print(ines.get_fired())