xtbfile='xtb-scan-gibbs-job.txt'
filename='scan-list.txt'
charge=' --chrg 0 '
opt=' --ohess '
xtb='/home/anconi/programs/xtb-6.4.1/bin/xtb '



#jobname='xTB-SCAN'


#xtbfile='xtb-scan-GIBBS-AND-ALPB-job-VERIF.sh'
#filename='scan-list.txt'
#charge=' --chrg 0 '
#opt=' --ohess '
optalpb=' --opt --alpb water '
#xtb='$EXE '


with open(xtbfile,'w') as file_object_saida, open(filename) as file_object:
#    file_object_saida.write('#!/bin/bash ' +'\n')
#    file_object_saida.write('# '+'\n')
#    file_object_saida.write('#$ -N ' + jobname +'\n')
#    file_object_saida.write('#$ -S /bin/sh' +'\n')
#    file_object_saida.write('#$ -pe mpi 24' +'\n')
#    file_object_saida.write('#$ -cwd' +'\n')
#    file_object_saida.write(' ' +'\n')
#    file_object_saida.write('EXE=/home/cleberanconi.dqi/programs/xtb-6.4.1/bin/xtb' +'\n')
#    file_object_saida.write('cd $SGE_O_WORKDIR' +'\n')
#    file_object_saida.write(' ' +'\n')
    for line in file_object:
        file_object_saida.write(xtb + line.rstrip() + charge + opt + '--namespace ' + line.rstrip() +'GIBBS'+ ' --verbose > ' + line.rstrip()+'GIBBS.log'+ '\n')
        file_object_saida.write(xtb + line.rstrip() + 'GIBBS.xtbopt.xyz' + charge + optalpb + '--namespace ' + line.rstrip() +'-ALPB-water.xyz'+ ' --verbose > ' + line.rstrip() + '-ALPB-water.log' + '\n')
                

