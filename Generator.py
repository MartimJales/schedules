from random import randint, random
from re import sub
from Class import *
import random as r

#salas, stores, turmas
subjects_list = ["MAT","FQ","BIO","POR","FILO","GEO","ECO","QUI","FIS","EF","HIST","ING","GEOM","EV","ET"]
t_list = ["Joao","Andre","Joaquim","Ana","Leopoldina","Jorge","Daniela","Martim","Viegas","Beah"
,"Asdrubal","Anibal","Rosa","Mariana","Anastacia","Ursula","Marina","Luis","Pedro","Antonio","Miguel"
"Caramelo","Rodrigo","Catarina","Sara","Tatiana","Ines","Joana","Cusca","Parva","Parvo","Fucking Tourist"]
l_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def subjects_gen(subs, n_subjects, stores, salas):
    subjects = []
    for _ in range(n_subjects):
        sub_at = [] #lista de atributos da subject

        #escolher um nome da subject
        index = r.randint(0,len(subs) - 1)
        sub_at.append(subs[index]) #escolhe sub aleatória
        subs.pop(index) #remove a sub escolhida da lista de subs

        #escolher salas da subject
        rooms_list = []
        num = r.randint(1,len(salas) + 1)
        for _ in range(num):
            rooms_list.append(str(r.randint(1,len(salas))))
        rooms = [*set(rooms_list)]
        sub_at.append(rooms)

        #escolher stor da subject
        sub_at.append(stores[r.randint(0,len(stores) - 1)])
                                                         #.name
        #escolher horas de subject
        sub_at.append(r.randint(4,7))

        #criar subject
        subjects.append(Subject(sub_at[0], sub_at[1], sub_at[2], sub_at[3]))

    return subjects

def generator(n_salas, n_stores, n_turmas, n_subjects):
    salas = []; stores = []; turmas = []
    #GERAR SALAS
    for i in range(n_salas):
        salas.append(Room(str(i)))

    #GERAR STORES
    id_list = []
    for _ in range(n_stores):
        id_list.append(r.randint(1000,9000))
    ids = [*set(id_list)]

    for id in ids:
        stores.append(Teacher(t_list[r.randint(0,len(t_list)-1)], str(id)))

    #GERAR TURMAS
    for i in range(n_turmas):
        subs = subjects_list.copy()
        subjects = subjects_gen(subs, n_subjects, stores, salas)
        turmas.append(Turma(str(r.randint(7,12)) + l_list[i], subjects))

    #CRIAR ESCOLA
    school = School(salas, stores, turmas)
    return school

def print_escola(escola):
    print("\n\n")
    print("Professores: ", end='')
    print(escola.teachers[0].name+':'+str(escola.teachers[0].id))
    for stor in escola.teachers[1:]:
        print('             ' + stor.name + ':' +str(stor.id))
    print(), print("Turmas: ",end='')

    turma0 = escola.turmas[0]
    print(turma0.name+':')
    for subject in turma0.subjects:
            print("          ",end='')
            print(subject.name+'; '+subject.teacher.name+':' + subject.teacher.id + '; ' + "salas: "+str(subject.rooms) + '; horas: '+str(subject.hours))
    for turma in escola.turmas[1:]:
        print("        "+turma.name+':')
        for subject in turma.subjects:
            print("          ",end='')
            print(subject.name+'; '+subject.teacher.name+':' + subject.teacher.id + '; ' + "salas: "+str(subject.rooms) + '; horas: '+str(subject.hours))
        print()