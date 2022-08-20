class Room:
    def __init__(self, name):
        self.name = name
        self.schedule = [[]]       

class Teacher:
    def __init__(self, name, subjects, turmas):
        self.name = name
        self.subjects = subjects
        self.turmas = turmas
        self.schedule = [[]]

class Turma:
    def __init__(self, name, subjects, teachers):
        self.name = name
        self.subjects = subjects
        self.teachers = teachers
        self.schedule = [[]]

class Subject:
    def __init__(self, name, rooms, teacher):
        self.name = name
        self.rooms = rooms
        self.teacher = teacher
        self.schedule = [[]]   
