from Class import *
from Generator import generator
from Recursion import recursion
from Writer import writer


def main():
    escola = generator(2,2,2,2)

    recursion(escola, '0',0,0)

"""     for turma in escola.turmas:
        for day in turma.schedule.keys():
            for hour in range(len(turma.schedule[day]) - 1):
                for subject in filter_subjects(turma):
                    if turma.schedule[day][hour] == '':
                        turma.schedule[day][hour] = subject.name
                        subject.hours -= 1
                        writer(escola, 1)
 """



def filter_subjects(turma : Turma):
    if len(turma.subjects) == 1:
        if turma.subjects[0].hours == 0:
            return []
    for i in range(len(turma.subjects) - 1):
        if turma.subjects[i].hours == 0:
            turma.subjects.pop(i)
    return turma.subjects

def turmas_keys(turmas):
    arr = []
    for turma in turmas:
        arr.append(turma.name)
    return arr

if __name__ == '__main__':
    main()
