from Class import *
#from Generator import generator



def main():
    salas = [Room('A1'), Room('A2')]
    turmas = [Turma('11A', [Subject('MAT',['A1','A2'],'josé',2), Subject('POR',['A1','A2'],'tobias',2)]), 
    Turma('12A', [Subject('MAT',['A1','A2'],'josé',2), Subject('POR',['A1','A2'],'tobias',2)])]
    teachers = [Teacher('josé',{'MAT':4}, turmas_keys(turmas)), Teacher('tobias',{'POR':4}, turmas_keys(turmas))]
    
    escola = School(salas, teachers, turmas)

    for turma in escola.turmas:
        for day in turma.schedule.keys():
            for hour in turma.schedule[day]:
                for subject in filter_subjects(turma.subjects):
                    if type(turma.schedule[day][hour]) == int:
                        turma.schedule[day][hour] = subject                    
                        turma.subjects[subject] -= 1
    
    for turma in escola.turmas:
        print(turma.schedule)
    
def filter_subjects(subjects : dict):
    arr = subjects.copy()
    for sub in subjects.keys():
        if subjects[sub] == 0:
            arr.pop(sub)
    return arr


def turmas_keys(turmas):
    arr = []
    for turma in turmas:
        arr.append(turma.name)
    return arr

if __name__ == '__main__':
    main()


