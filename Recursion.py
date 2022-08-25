from Class import *
from Writer import writer

def recursion(school: School, day: str, hour: int, var: int):
    '''
    Main function to create all the schedules for the school that receive
    1 - Check if all the classes have subjects fill in schedule
    2 - Search for more schedules
    '''
    if (school.is_complete()):
        writer(school, var)
    else:
        for turma in range(len(school.turmas) - 1):
            for subject in range(len(school.turmas[turma].subjects) - 1):
                var += 1
                school.turmas[turma].schedule[day][hour] = school.turmas[turma].subjects[subject].name
                school.turmas[turma].subjects[subject].hours -= 1
                if hour == 10:
                    hour = -1
                    day = str(int(day) + 1)
                recursion(school, day, hour + 1, var)
            
def filter_subjects(turma : Turma):
    if len(turma.subjects) == 1:
        if turma.subjects[0].hours == 0:
            return []
    for i in range(len(turma.subjects) - 1):
        if turma.subjects[i].hours == 0:
            turma.subjects.pop(i)
    return turma.subjects

            
