from Class import *

def writer(escola : School, var : int):
    '''
    Funcão para escrever os horários da escola num ficheiro txt
    '''
    f = open(f"results/{var}_turma.txt", "w")
    g = open(f"results/{var}_profs.txt", "w")
    h = open(f"results/{var}_salas.txt", "w")

    write_to_file(f, escola.turmas)
    write_to_file(g, escola.teachers)
    write_to_file(h, escola.rooms)

    f.close()
    g.close()
    h.close()

def write_to_file(f, cenas):
    s = ''
    for cena in cenas:
        f.write('                       ' + cena.name + '\n\n')
        s = dict_to_str(cena.schedule)
        f.write(s)

def dict_to_str(schedule : dict):
    '''
    Function to tranform a schedule in a string
    '''
    s = ''
    for key in schedule.keys():
        s += key + ': '
        for hour in schedule[key]:
            if type(hour) == int:
                s += '   '
            else:
                s += hour 
            s += '|'
        s += '\n'
    s += '\n'
    return s


