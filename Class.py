class Room:
    '''
    Classe para identificar salas da escola
    schedule - referência para o espaço livre
    '''
    def __init__(self, name):
        self.name = name
        self.schedule = create_schedule()   

class Teacher:
    '''
    Classe para identificar os professores da escola
    Name - Comodidade
    id - Numero do processo do professor
    schedule - Objetivo final do programa
    '''
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.schedule = create_schedule()

class Turma:
    '''
    Classe para identificar as turmas da escola
    name - string com ano e classe
    subjects - Informação com as disciplinas, horas, professores e salas disponiveis para a turma
    schdule - Objetivo final do programa
    '''
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.schedule = create_schedule()

class Subject:
    '''
    Classe que relaciona uma turma com um professor para determinada disciplina.
    rooms - salas onde é possível lecionar esta cadeira
    teacher - id do professor que leciona esta cadeira
    hours - numero de horas semanais obrigatórias 
    '''
    def __init__(self, name, rooms, teacher, hours):
        self.name = name
        self.rooms = rooms
        self.teacher = teacher
        self.hours = hours

class School:
    '''
    Classe mãe para interligar as salas, os professors e as turmas
    '''
    def __init__(self, rooms, teachers, turmas):
        self.rooms = rooms
        self.teachers = teachers
        self.turmas = turmas

def create_schedule():
    '''
    Função para criar um horário semanal vazio
    '''
    schedule = {}
    schedule['seg'] = ['']*11
    schedule['ter'] = ['']*11
    schedule['qua'] = ['']*11
    schedule['qui'] = ['']*11
    schedule['sex'] = ['']*11
    return schedule
