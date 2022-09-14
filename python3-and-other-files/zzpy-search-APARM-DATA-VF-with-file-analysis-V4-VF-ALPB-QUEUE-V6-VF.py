import re
import csv
import os
import os.path
cwd=os.getcwd()
print(cwd)

xtbfile='zxtb-scan-APARM-DATA-ALPB-QUEUE-V6-VF.csv'
filenamelist='selected-geometries-queue.txt'
Details=['file','energy',' MSS ',' r ',' theta ',' phi ','Alpha-Euler','Beta-Euler','Gamma-Euler']


with open(xtbfile, 'w') as file_object_saida, open(filenamelist) as file_object:
    write=csv.writer(file_object_saida)
    write.writerow(Details)
    for line in file_object:
        filename=line.rstrip() + '.aparm.log' 
        file_check=os.path.isfile(cwd+'/'+filename)
#        print(file_check)
#        print(cwd+filename)
        mylines = []
        if file_check == True:
            with open (filename, 'rt') as myfile:
                for line in myfile:
                    mylines.append(line)
            for line in mylines:
                target_string=line
                result=re.search(r"CM-DIST",target_string)
                if result:
                    cm_dist=re.findall(r"[-+]?\d*\.\d+|\d+",line)
            for line in mylines:
                target_string=line
                result=re.search(r"THETA",target_string)
                if result:
                    theta=re.findall(r"[-+]?\d*\.\d+|\d+|\bNAD\b",line)
            for line in mylines:
                target_string=line
                result=re.search(r"PHI",target_string)
                if result:
                    phi=re.findall(r"[-+]?\d*\.\d+|\d+|\bNAD\b",line)
            for line in mylines:
                target_string=line
                result=re.search(r"ALPHA-EULER",target_string)
                if result:
                    alpha_euler=re.findall(r"[-+]?\d*\.\d+|\d+",line)
            for line in mylines:
                target_string=line
                result=re.search(r"BETA-EULER",target_string)
                if result:
                    beta_euler=re.findall(r"[-+]?\d*\.\d+|\d+",line)
            for line in mylines:
                target_string=line
                result=re.search(r"GAMMA-EULER",target_string)
                if result:
                    gamma_euler=re.findall(r"[-+]?\d*\.\d+|\d+",line)
            for line in mylines:
                target_string=line
                result=re.search(r"MSS",target_string)
                if result:
                    MSS=re.findall(r"\w\w\w\w\w\w",line)
                else:
                    MSS='NONE - aparm error '
            for line in mylines:
                target_string=line
                result=re.search(r"energy:",target_string)
                if result:
                    energy=re.search(r"[-+]?\d*\.\d+|d+",line)
                    energy=energy.group()
                    rows=[filename,energy,MSS,*cm_dist,*theta,*phi,*alpha_euler,*beta_euler,*gamma_euler]
                    write.writerow(rows)
        else :
            rows=[filename, ' not found ']
            write.writerow(rows)
