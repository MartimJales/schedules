from Class import *
from Generator import generator
from Writer import writer


def main():
    # salas = [Room('A1'), Room('A2')]
    # turmas = [Turma('11A', [Subject('MAT',['A1','A2'],'josé',2), Subject('POR',['A1','A2'],'tobias',2)]),
    # Turma('12A', [Subject('MAT',['A1','A2'],'josé',2), Subject('POR',['A1','A2'],'tobias',2)])]
    # teachers = [Teacher('josé',{'MAT':4}, turmas_keys(turmas)), Teacher('tobias',{'POR':4}, turmas_keys(turmas))]

    escola = generator(5,5,5,7)

    for turma in escola.turmas:
        for day in turma.schedule.keys():
            for hour in range(len(turma.schedule[day]) - 1):
                for subject in filter_subjects(turma):
                    if turma.schedule[day][hour] == '':
                        turma.schedule[day][hour] = subject.name
                        subject.hours -= 1
                        writer(escola, 1)
    writer(escola, 1)




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

def fill_schedule(object, day, hour):
    object.schedule[day][hour] = ' X '
    """ recebe uma variável do tipo Teacher ou Room, um dia da semana exmp: 'seg' ou 'ter'
    e uma hour que representa um bloco no dia da semana sendo que hour = 0 refere-se a
    uma aula a começar às 8 da manhã. Esta função funciona tanto para Teacher e Room
    já que ambas têm o trabuto schedule que funciona da mesma forma """

def free_check(object, day, hour):
    if object.schedule[day][hour] == ' X ':
        return False
    return True
    """ dado um Teacher ou room, day e hour da mesma forma que a função anterior, devolve
    True ou False dependendo se o object tem o schedule livre nesse day e hour """

if __name__ == '__main__':
    main()


