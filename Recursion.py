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
        for turma in range(len(school.valid_turmas())):
            subjects = school.turmas[turma].valid_subjects()
            if subjects == []:
                day = '0'
                hour = 0
            else:
                for subject in range(len(subjects)):
                    var += 1
                    '''We have a problem here'''
                    school.turmas[turma].schedule[day][hour] = school.turmas[turma].subjects[subject].name
                    school.turmas[turma].subjects[subject].hours -= 1
                    if hour == 10:
                        hour = -1
                        day = str(int(day) + 1)
                    recursion(school, day, hour + 1, var)