### Quiero hacer gráficas con los outputs de admixture
#jabra
cd D://Dropbox/Posdoc/Admixture/SAPA93/Filter500103
scp javelar@dna.lavis.unam.mx:/mnt/Timina/lmorales/Public/ymez/tmp/06_genotyping/trees/SAPA66_27filtered/admixture/Filter500103/* .
grep -h CV log*.out|awk -F "=|:" '{print $2"\t"$3}' | sed 's/)//g'| sort -n > values_CV_SAPA66_Filt500103.txt

cd D://Dropbox/Posdoc/Admixture/SAPA93/Filter500103
scp javelar@dna.lavis.unam.mx:/mnt/Timina/lmorales/Public/ymez/tmp/06_genotyping/trees/SAPA66_27filtered/admixture/Filter2501015/*.
grep -h CV log*.out|awk -F "=|:" '{print $2"\t"$3}' | sed 's/)//g'| sort -n > values_CV_SAPA66_Filt2501015.txt

# La hoja con los ids: SampleSheet_SAPA93_27removed_SAPA66_forStructure.csv 

# Luego me fui al script Plotting_Admixture_SAPA66.R y de ahí salió admixture_2501015.pdf con las figuras de CV y barplots

