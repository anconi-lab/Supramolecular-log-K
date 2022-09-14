xtbfile='z-job-to-select-from-list.txt'
filename='selected-geometries.txt'
filename_list='selected-geometries-queue.txt'

contador=0

with open(xtbfile,'w') as file_object_saida, open(filename) as file_object, open(filename_list,'w') as file_object_list :
    for line in file_object:
        contador += 1
#        print(contador)
        ordem=str(contador)
        file_name_ordem= line.rstrip() + '-ALPB-water.xyz.xtbopt.xyz '  
#        print(file_name_ordem)
        file_object_list.write(file_name_ordem + '\n')
