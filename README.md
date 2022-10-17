# Supramolecular-log-K


For the present tutorial, we assume that the supramolecular systems consist of a host (CD) and a guest (G). The tutorial can be used to determine the binding constants (or stability constants) for the reactions:
G(aq) + CD(aq) ⇌ G@CD(aq);  
G@CD(aq): (host-guest system) in aqueous solution
OR
G(aq) + CD(aq) ⇌ G…CD (aq) ; 
G…CD (aq): (supramolecular system: simple non-bonded association of two molecules)
To compute the log K for forming a supramolecular system (G…CD) within the multi-equilibrium approach, with the GNF2-xTB method, developed by Grimme and co-workers (J. Chem. Theory Comput. 13, 1989–2009, 2017), you can use the workflow below. The python3 files and other are avaiable with this tutorial (python3-and-other-files)
 
![image](https://user-images.githubusercontent.com/86429259/190155383-56c7ebd2-f567-4a3e-8a06-5424a6d9057c.png)


Aftwer download the xTB software 
(https://xtb-docs.readthedocs.io/en/latest/setup.html#getting-the-program) 
The following steps are required (for use in a Linux distro): 

1)	Use the CREST software https://xtb-docs.readthedocs.io/en/latest/crest.html#what-is-crest (Phys. Chem. Chem. Phys., 2020, 22, 7169-7192.) to explore the conformational space for the smaller molecule (the guest), usually obtained from PubChem (https://pubchem.ncbi.nlm.nih.gov/). After running CREST, you can use the file "crest_best.xyz" which comprises the best guest geometry (the most favorable one) as the input to the UD-APARM software (ud-aparm-molecule_1.xyz). You can also select another conformer reported at crest_conformers.xyz as ud-aparm-molecule_1.xyz
2)	From an X-Ray structure, without explicit water molecules, perform a GFN2-xTB optimization of the host. Save the structure as ud-aparm-MOLECULE_2-REFERENCE.xyz
3)	Download the Linux binary file for the UD-APARM (https://github.com/anconi-lab/UD-APARM) and read the instructions (https://github.com/anconi-lab/UD-APARM/blob/main/QUICK-GUIDE-TO-UD-APARM-V3.pdf). To run the UD-APARM, you can use the input file: ud-aparm.inp (here for 252 points with a variation of r from 0 to 7 angstroms within ten steps, passage through the CD cavity, and rotation (alpha-Euler) from 0 to 300 within five steps. For testing, you can also use the files ud-aparm-molecule_1.xyz and ud-aparm-MOLECULE_2-REFERENCE.xyz available within this tutorial. In addition, running UD-APARM will generate the file scan-list.txt (take a look for a sample within this tutorial). In the file scan-list.txt, we have the list of 252 supramolecular systems obtained with UD-APARM (xyz files), each with the appropriate name, to run the GFN2-xTB software. 
Now you have to run xTB software to all the supramolecular systems described in scan-list.txt (STEP: python3 job 1 run xTB). Edit the path for the binary installation of the python software xtb-scan-GIBBS-and-ALPB--CORR-VF-LCC-UFLA3-VFLCC-VERIFICADO-LQF.py". Edit: xtb='/home/anconi/programs/xtb-6.4.1/bin/xtb ' to your xtb installation. Running the python3 software will produce a file that will run an optimization, a frequency calculation, a Gibbs evaluation, and a new optimization in implicit water (with the ALPB approach). 
python3 xtb-scan-GIBBS-and-ALPB--CORR-VF-LCC-UFLA3-VFLCC-VERIFICADO-LQF.py
Generate the file "xtb-scan-gibbs-job.txt" (with chmod ugoa+x xtb-scan-gibbs-job.txt you can run the job for obtaining Gibbs energy and ALPB energy for each supramolecular system under study. 
4)	(STEP: python3 job 2 collect data) After running the xTB (which takes several minutes or hours), you have to collect the data using the file 
"zuuu-search-imag-gibbs-elenuc-alpb-V11-VERIFICADO.py". The python3 software will collect the number of imaginary frequencies for each system (for verification), the Gibbs energy (for a given pressure and temperature), the Total Energy (vacuum) the Total ALPB energy in water. A spreadsheet with the name "zuuu-xtb-imag-gibs-elenuc-alpb-VERIF.csv" will be obtained from the python3 routine. 
5)	Now you have to run APARM software to obtain the supramolecular parameters for the characterization of each system and to verify the integrity of the supramolecular systems (in some situations, the molecules can combine along with the optimization, depending on the level of theory applied) The APARM software checks all structures. After downloading and installing the APARM binary (https://github.com/anconi-lab/APARM), you must prepare a file name for running APARM because the scan-list.txt does not comprise the name of the files after optimization in implicit solvent. Therefore, you have to copy the file "scan-list.txt" with the name: "selected-geometries.txt" and then run the python3 routine: 
"zzpy-select-geometries-ALPB-list-VF-CORR-FOR-ALL----VF.py." This python routine generates the file: 'selected-geometries-queue.txt' with all names listed in "scan-list.txt" with an additional termination: "-ALPB-water.xyz.xtbopt.xyz". The geometries employed to determine the log K corresponds to geometries optimized in implicit solvent (ALPB water). Therefore, the APARM software will run for the ALPB geometries. Now you have to prepare to run APARM for each structure listed in "selected-geometries-queue.txt"
6)	STEP: python3 job 3 run APARM. It would be best if you ran the python3 routine: 
"zxtb-prepare-to-run-APARM-VF-ALPB-from-QUEUE.py". The python3 routine will generate the file "x-roda-aparm-QUEUE-list.txt". Change to executable (chmod ugoa+x x-roda-aparm-QUEUE-list.txt" and include an APARM input (apam.inp, a file with three lines comprising the total number of atoms of the system, the number of atoms of the guest and the number of atoms of the host) within the current directory. Then, run the job that will call APARM software for each system within the "selected-geometries-queue.txt". This part takes several minutes. 
7)	Now you have to collect the data obtained from APARM. STEP: python3 job 4 (collect data from APARM) You must run the python3 routine: 
"zzpy-search-APARM-DATA-VF-with-file-analysis-V4-VF-ALPB-QUEUE-V6-VF.py" to obtain the spreadsheet: "zxtb-scan-APARM-DATA-ALPB-QUEUE-V6-VF.csv"
8)	Combine both spreadsheets to obtain the data (Gibbs energy of formation in water). Next, run the calculations for guest and host and put the data into the combined spreadsheet. Then, proceed with the spreadsheet analysis of the two .csv files obtained with the previous steps. With this part of the procedure, you must discard structures with imaginary frequencies and structures indicated as "FAILED" by the APARM software. 
9)	To exclude duplications within the supramolecular geometries, you must analyze the supramolecular parameters (from APARM). Some illustrative pictures are depicted along with the process of obtaining log K. 



![imag-check](https://user-images.githubusercontent.com/86429259/190155954-6f2562d4-f0f6-42ee-b7b0-fb4949b4408a.png)

![APARM-CHECKpng](https://user-images.githubusercontent.com/86429259/190155989-68831ee8-443a-4f21-8e29-13834feff98b.png)

![individual-molecules](https://user-images.githubusercontent.com/86429259/190156070-bf128b0e-a89e-4743-94d4-a7d38d68a05c.png)

![logK](https://user-images.githubusercontent.com/86429259/190156080-f6458cda-122c-4ab7-bd93-076bf404cde1.png)


