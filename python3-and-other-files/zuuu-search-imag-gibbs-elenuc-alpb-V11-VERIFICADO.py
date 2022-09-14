import re
import csv
import os
import os.path
cwd=os.getcwd()

xtbfile='zuuu-xtb-imag-gibs-elenuc-alpb-VERIF.csv'
filenamelist='scan-list.txt'
Details=['file',' n imaginary freq',' gibbs energy',' ele-nuc',' file ',' alpb ']
errorGibbs=111

with open(xtbfile, 'w') as file_object_saida, open(filenamelist) as file_object:
    write=csv.writer(file_object_saida)
    write.writerow(Details)
    for line in file_object:
        filename=line.rstrip() + 'GIBBS.log' 
        file_check=os.path.isfile(cwd+'/'+filename)
        filename2=line.rstrip() + '-ALPB-water.log' 
        file_check2=os.path.isfile(cwd+'/'+filename2)
        mylines = []
        mylines2 = []

        fileGibbs = ' none '
        filealpb = ' none '

        if file_check == True:
            fileGibbs = "ok"
        if file_check2 == True:
            filealpb = "ok"
#        print(fileGibbs)
        nimagin = 'n'
        gibbsenergy ='n'
        totalenergy ='n'

        if fileGibbs == "ok": 
#            print(' after if ',fileGibbs)
            with open (filename, 'rt') as myfile:

               for line in myfile:
                        mylines.append(line)
               for line in mylines:
                   target_string=line
                   result=re.search(r"# imaginary freq.",target_string)
                   if result:
                       nimagin=re.findall(r"[-+]?\d*\.\d+|\d+",line)
               for line in mylines:
                   target_string=line
                   result=re.search(r"FREE",target_string)
                   if result:
                       gibbsenergy=re.findall(r"[-+]?\d*\.\d+|\d+",line)
               for line in mylines:
                   target_string=line
                   result=re.search(r"TOTAL ENERGY",target_string)
                   if result:
                       totalenergy=re.findall(r"[-+]?\d*\.\d+|\d+",line)
               for line in mylines:
                   target_string=line
                   result=re.search(r"ERROR",target_string)
                   if result:
                      gibbsenergy = 'E'
                      totalenergy = 'E'
                      nimagin = 'E'
#            rows=[filename,*nimagin, *gibbsenergy, *totalenergy, "alpb ERROR"]
#            write.writerow(rows)
#        else : 
#                    rows=[filename,'xtb error']
#                    write.writerow(rows)
        alpbenergy = 'n'            
        if filealpb == "ok":
#            print(' file alpbp ok ',filealpb)
            with open (filename2, 'rt') as myfile2:
               for line in myfile2:
                   mylines2.append(line)
            for line in mylines2:
               target_string=line
               result=re.search(r"ENERGY",target_string)
               if result:
                   alpbenergy=re.findall(r"[-+]?\d*\.\d+|\d+",line)
            for line in mylines2:
               target_string=line
               result=re.search(r"ERROR",target_string)
               if result:
                   alpbenergy = 'E'
        
        rows=[filename,*nimagin, *gibbsenergy, *totalenergy, filename2, *alpbenergy]
        write.writerow(rows)


