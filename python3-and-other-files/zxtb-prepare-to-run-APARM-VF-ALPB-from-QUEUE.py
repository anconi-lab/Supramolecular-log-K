xtbfile='x-roda-aparm-QUEUE-list.txt'
filename='selected-geometries-queue.txt'
aparm='/home/anconi/programs/aparm/aparm-linux'


with open(xtbfile,'w') as file_object_saida, open(filename) as file_object:
    for line in file_object:
        file_object_saida.write('cp ' + line.rstrip()  + ' aparm-GEOMETRY.xyz '  + '\n')
        file_object_saida.write(aparm + '\n')
        file_object_saida.write('cp ' + 'aparm.log ' + line.rstrip() + '.aparm.log ' + '\n')
        file_object_saida.write('rm ' + 'aparm-GEOMETRY.xyz ' + '\n')
