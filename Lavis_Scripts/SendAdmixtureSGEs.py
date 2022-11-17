#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  20 22:30:01 2022

@author: Abraham
"""
#%%

import sys
import argparse
import getpass

sys.path.append("../generic_functions/")

from generic import getdata
from generic import header
from generic import bashfile
from generic import get_refs
#%%            
##########################################
ag = argparse.ArgumentParser()
ag.add_argument("-b", "--bed", required = True, help = "file with the .bed SNPs matrix") 
ag.add_argument("-d", "--dirbed", required = True, help = "directory where the .bed SNPs matrix is") 
ag.add_argument("--out", required = True, help = "Output directory")
ag.add_argument("--minS", required = True, help = "minS")
ag.add_argument("--minK", required = True, help = "minK")
ag.add_argument("--maxS", required = True, help = "maxS")
ag.add_argument("--maxK", required = True, help = "maxK")
ag.add_argument("--setname", required = True, help = "setname")


args = vars(ag.parse_args())
bed = args["bed"]
dirbed = args["dirbed"]
out = args["out"]
minS = args["minS"]
minK = args["minK"]
maxS = args["maxS"]
maxK = args["maxK"]
setname = args["setname"]

np="10"
ram="8G"

sge_dir = "/mnt/Timina/lmorales/Public/ymez/bin/SGE/10_admixture"
out_dir="/mnt/Timina/lmorales/Public/ymez/data/tmp/10_admixture"

username = getpass.getuser()
#%%
sh_out = sge_dir + "/" + username + "_admixture_K" + minK+"-"+maxK+ "_S"+minS+"-"+maxS +".sh"

#path, sample, sge, app, user, np, ram
sgs = []
for seeds in range(int(minS), int(maxS)+1):
    for ks in range(int(minK), int(maxK)+1):
        bedfile = dirbed+"/"+"$(basename "+bed+" .bed)"+"_S"+str(seeds)+"_K"+str(ks)+".bed" #ruta completa del archivo nuevo solo generado para tener un input por job
        logfile = dirbed+"/"+"$(basename "+bed+" .bed)"+"_S"+str(seeds)+"_K"+str(ks)+".log" #ruta completa del archivo nuevo solo generado para tener un input por job
        bimfile = dirbed+"/"+"$(basename "+bed+" .bed)"+"_S"+str(seeds)+"_K"+str(ks)+".bim" #ruta completa del archivo nuevo solo generado para tener un input por job
        famfile = dirbed+"/"+"$(basename "+bed+" .bed)"+"_S"+str(seeds)+"_K"+str(ks)+".fam" #ruta completa del archivo nuevo solo generado para tener un input por job
        nosexfile = dirbed+"/"+"$(basename "+bed+" .bed)"+"_S"+str(seeds)+"_K"+str(ks)+".nosex" #ruta completa del archivo nuevo solo generado para tener un input por job
        sgs.append("admixture_"+str(setname)+"_K" + str(ks) + "_S"+str(seeds) )
        file = sge_dir + "/" + "admixture_"+str(setname)+"_K" + str(ks) + "_S"+str(seeds) + ".sge"
        with open(file,'w') as sge_file:
             header(sge_dir, "Admixture"+"_K" + str(ks) + "_S"+str(seeds) , sge_file, setname, username, np, ram)
             print('module load admixture/1.3.0\n###', file =sge_file)
             print('start=$(date +%s.%N)', file = sge_file)


             print("cp "+dirbed+"/"+bed+" "+bedfile, file = sge_file )
             print("cp "+dirbed+"/"+"$(basename "+bed+" .bed)"+".log"+" "+logfile, file = sge_file )
             print("cp "+dirbed+"/"+"$(basename "+bed+" .bed)"+".bim"+" "+bimfile, file = sge_file )
             print("cp "+dirbed+"/"+"$(basename "+bed+" .bed)"+".fam"+" "+famfile, file = sge_file )
             print("cp "+dirbed+"/"+"$(basename "+bed+" .bed)"+".nosex"+" "+nosexfile, file = sge_file )
             print( "admixture -s ${RANDOM} --cv "+bedfile+" "+str(ks)+" -j4  | tee "+ out + "/log_$(basename "+bed+" .bed)_S"+str(seeds)+"_K"+str(ks)+"_LDprune.out", file = sge_file )
             print("mv "+"$(basename "+bedfile+" .bed)"+"."+str(ks)+".Q "+ out+"/"+ "$(basename "+bedfile+" .bed)"+"."+str(ks)+".Q", file = sge_file)
             print("mv "+"$(basename "+bedfile+" .bed)"+"."+str(ks)+".P "+ out+"/"+ "$(basename "+bedfile+" .bed)"+"."+str(ks)+".P", file = sge_file)
             print("rm "+bedfile, file = sge_file)
             print("rm "+logfile, file = sge_file)
             print("rm "+bimfile, file = sge_file)
             print("rm "+famfile, file = sge_file)
             print("rm "+nosexfile, file = sge_file)

             print('duration=$(echo "$(date +%s.%N) - $start" | bc)', file =sge_file)
             print('execution_time=`printf "%.2f seconds" $duration`', file = sge_file)
             print('echo "Script Execution Time: $execution_time"', file =sge_file)

bashfile(sh_out, sgs)

# Ejemplo:
# python3.7 SendAdmixtureSGEs.py --bed Matrix_LDPrune_500_10_0.35.bed --dirbed /mnt/Timina/lmorales/Public/ymez/tmp/06_genotyping/trees/SACE304 --out /mnt/Timina/lmorales/Public/ymez/tmp/06_genotyping/trees/SACE304/out --minS 1 --maxS 2 --minK 1 --maxK 2 --setname SACE304
