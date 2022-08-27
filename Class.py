class Room:
    '''
    Classe para identificar salas da escola
    schedule - referência para o espaço livre
    '''
    def __init__(self, name: str):
        self.name = name
        self.schedule = create_schedule()

    def fill_schedule(self, subject, day, hour):
        self.schedule[day][hour] = subject.name + ';' + subject.teacher.name + ':' + subject.teacher.id

    def free_check(self, day, hour):
        if self.schedule[day][hour] != '':
            return False
        return True

class Teacher:
    '''
    Classe para identificar os professores da escola
    Name - Comodidade
    id - Numero do processo do professor
    schedule - Objetivo final do programa
    '''
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.schedule = create_schedule()

    def fill_schedule(self, subject, room, day, hour):
        self.schedule[day][hour] = subject.name + ';' + str(room.name)

    def free_check(self, day, hour):
        if self.schedule[day][hour] != '':
            return False
        return True

class Subject:
    '''
    Classe que relaciona uma turma com um professor para determinada disciplina.
    rooms - salas onde é possível lecionar esta cadeira
    teacher - id do professor que leciona esta cadeira
    hours - numero de horas semanais obrigatórias
    '''
    def __init__(self, name: str, rooms, teacher: Teacher, hours: int):
        '''Verificar se o teacher é uma classe inteira ou apenas um id'''
        self.name = name
        self.rooms = rooms
        self.teacher = teacher
        self.hours = hours

class Turma:
    '''
    Classe para identificar as turmas da escola
    name - string com ano e classe
    subjects - Informação com as disciplinas, horas, professores e salas disponiveis para a turma
    schdule - Objetivo final do programa
    '''
    def __init__(self, name: str, subjects):
        self.name = name
        self.subjects = subjects
        self.schedule = create_schedule()

    def valid_subjects(self):
        arr = []
        for subject in self.subjects:
            if subject.hours != 0:
                arr.append(subject)
        return arr

class School:
    '''
    Classe mãe para interligar as salas, os professors e as turmas
    '''
    def __init__(self, rooms, teachers, turmas):
        self.rooms = rooms
        self.teachers = teachers
        self.turmas = turmas

    def is_complete(self):
        '''
        Check if all the classes have subjects fill in schedule
        '''
        for turma in self.turmas:
            if turma.valid_subjects() != []:
                return False
        return True

    def valid_turmas(self):
        arr = []
        for turma in self.turmas:
            if turma.valid_subjects() != []:
                arr.append(turma)
        return arr


def create_schedule():
    '''
    Função para criar um horário semanal vazio
    '''
    schedule = {}
    schedule['0'] = ['']*11
    schedule['1'] = ['']*11
    schedule['2'] = ['']*11
    schedule['3'] = ['']*11
    schedule['4'] = ['']*11
    return schedule
