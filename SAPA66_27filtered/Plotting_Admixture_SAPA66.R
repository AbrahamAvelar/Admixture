CVPlot <- function(archivo){
  crosvalerr<-read.table(archivo)
  plot(crosvalerr, xlab="k", ylab="CV", main=archivo)
}

archivo <- "values_CV_SAPA66_Filt500103.txt"
crosvalerr<-read.table("values_CV_SAPA66_Filt500103.txt")
plot(crosvalerr, xlab="k", ylab="CV", main=archivo)

archivo1<-"D:/Dropbox/Posdoc/Admixture/SAPA93/Filter500103/values_CV_SAPA66_Filt500103.txt"
CVPlot(archivo1)
dev.off()
archivo2<-"D:/Dropbox/Posdoc/Admixture/SAPA93/Filter2501015/values_CV_SAPA66_Filt2501015.txt"
CVPlot(archivo2)

dev.off()
ordenar=2
thisfile<-paste("D:/Dropbox/Posdoc/Admixture/SAPA93/Filter500103/Matrix_LDPrune.", "2",".Q", sep="")
thisfile<-paste("D:/Dropbox/Posdoc/Admixture/SAPA93/Filter2501015/Matrix_LDPrune2501015.", "2",".Q", sep="")
tbl<-read.table(thisfile)
ordind=order(tbl[ordenar])
SS<-read.table("SAPA66_names.csv",sep=",", header=TRUE)
par(mfrow=c(4,1), mar=c(3,4,1,2), cex.lab=1, cex.axis=0.6)
for (x in 2:5){
  thisfile<-paste("D:/Dropbox/Posdoc/Admixture/SAPA93/Filter2501015/Matrix_LDPrune2501015.", as.integer(x),".Q", sep="")
  tbl<-read.table(thisfile)
  tbl<-tbl[ordind,]
  barplot(t(as.matrix(tbl)),
          col=brewer.pal(6,"Set1"),
          ylab="Anc. Proportions", names.arg=SS[ordind,1],
          border=NA, space=0, las=2)
}
# Guardé admixture_2501015.pdf y CVPlot_SAPA66_F2501015.pdf. en el 1ero lo edité en Illustrator.
