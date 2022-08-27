from Class import *
from Generator import generator
from Writer import writer

escola = generator(5,5,5,7)

writer(escola, 1)
for teacher in escola.teachers:
	teacher.fill_schedule(escola.turmas[0].subjects[0], escola.rooms[0], '0', 4)
for room in escola.rooms:
    room.fill_schedule(escola.turmas[0].subjects[0],'0', 4)

writer(escola, 1)
